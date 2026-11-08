import hashlib
from unittest.mock import AsyncMock

import pytest
import archive_campaign as campaign
from private_storage import encode_document


def saved(category='credit_or_budget', score='0'):
    return {'model':'test/model','game_date':'2026-11-02','report':{
        'scorecard_verified':True,'final_score':score,'model_issues':[{'category':category}]}}


async def test_exact_infrastructure_failure_can_supersede_verified_zero():
    manifest={'campaign':'archive-test'}
    path=campaign.report_path(manifest,'test/model','2026-11-02')
    original=saved()
    recovery={path:hashlib.sha256(encode_document(original)).hexdigest()}
    store=AsyncMock();store.read.return_value=original
    result,retry,previous=await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',infrastructure_recovery=recovery)
    assert result is None and previous==path and retry.endswith('/attempt-1.json.gz')
    store.put.assert_not_called()


async def test_clean_zero_and_model_mistakes_remain_terminal():
    manifest={'campaign':'archive-test'}
    path=campaign.report_path(manifest,'test/model','2026-11-02')
    original=saved('invalid_model_output')
    recovery={path:hashlib.sha256(encode_document(original)).hexdigest()}
    store=AsyncMock();store.read.return_value=original
    result,chosen,previous=await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',infrastructure_recovery=recovery)
    assert result==original and chosen==path and previous is None


async def test_recovery_counts_only_clean_latest_attempt():
    manifest={'campaign':'archive-test'}
    path=campaign.report_path(manifest,'test/model','2026-11-02')
    retry=path.replace('/runs/','/startup-retries/').removesuffix('.json.gz')+'/attempt-1.json.gz'
    original=saved();clean=saved('invalid_model_output','100')
    recovery={path:hashlib.sha256(encode_document(original)).hexdigest()}
    store=AsyncMock();store.read.side_effect=[original,clean]
    result,chosen,previous=await campaign.load_checkpoint(store,{path,retry},manifest,'test/model','2026-11-02',infrastructure_recovery=recovery)
    assert result==clean and chosen==retry and previous is None


def test_generic_or_cross_campaign_replay_authorization_rejected():
    with pytest.raises(ValueError):
        campaign.infrastructure_recovery_paths({'campaign':'archive-test','authorization':'retry anything','reports':[]},'archive-test')


def test_unavailable_and_server_failure_detected_without_reclassifying_game_timeout():
    row=saved('invalid_request')
    row['report']['model_issues'][0]['message']='model is no longer available on OpenRouter'
    assert campaign.infrastructure_affected(row)
    row=saved('provider_error');row['report']['model_issues'][0]['http_status']=503
    assert campaign.infrastructure_affected(row)
    assert not campaign.infrastructure_affected(saved('inference_deadline'))


def receipt_fixture():
    manifest={'campaign':'archive-test'}
    path=campaign.report_path(manifest,'test/model','2026-11-02')
    retry=path.replace('/runs/','/startup-retries/').removesuffix('.json.gz')+'/attempt-1.json.gz'
    authpath='archive-test/infrastructure-recoveries/test.json.gz'
    old=saved();new=saved('invalid_model_output','100');new['report']['rounds']=[{} for _ in range(7)]
    new.update(retry_of=path,infrastructure_recovery=authpath)
    digest=hashlib.sha256(encode_document(old)).hexdigest()
    rp='archive-test/superseded-reports/'+hashlib.sha256(path.encode()).hexdigest()+'.json.gz'
    receipt=dict(campaign='archive-test',authorization='user_requested_affected_report_cleanup',path=path,sha256=digest,model='test/model',game_date='2026-11-02',replacement_path=retry,replacement_sha256=hashlib.sha256(encode_document(new)).hexdigest(),recovery_kind='infrastructure_recovery',recovery_path=authpath)
    auth=dict(campaign='archive-test',authorization='user_requested_infrastructure_failure_retries',reports=[dict(path=path,sha256=digest)])
    return manifest,path,retry,rp,receipt,new,auth,authpath


async def test_deleted_original_resumes_only_verified_clean_replacement():
    manifest,path,retry,rp,receipt,new,auth,ap=receipt_fixture()
    docs={retry:new,rp:receipt,ap:auth};store=AsyncMock();store.read.side_effect=lambda p: docs.get(p)
    supersessions=await campaign.load_supersessions(store,set(docs),'archive-test',{}, {path:receipt['sha256']})
    result,chosen,previous=await campaign.load_checkpoint(store,set(docs),manifest,'test/model','2026-11-02',supersessions=supersessions)
    assert result==new and chosen==retry and previous is None


@pytest.mark.parametrize('damage',['checksum','missing','failure','identity','authorization','provenance'])
async def test_cleanup_receipt_fails_closed(damage):
    manifest,path,retry,rp,receipt,new,auth,ap=receipt_fixture()
    docs={retry:new,rp:receipt,ap:auth};store=AsyncMock();store.read.side_effect=lambda p: docs.get(p)
    if damage=='checksum':receipt['replacement_sha256']='0'*64
    elif damage=='missing':docs.pop(retry)
    elif damage=='failure':new['report']['model_issues']=[dict(category='rate_limit')]
    elif damage=='identity':receipt['game_date']='2026-11-03'
    elif damage=='authorization':auth['authorization']='anything'
    else:new['retry_of']='different'
    with pytest.raises(ValueError):
        await campaign.load_supersessions(store,set(docs),'archive-test',{}, {path:receipt['sha256']})


async def test_unreceipted_gap_still_rejected():
    manifest,path,retry,rp,receipt,new,auth,ap=receipt_fixture()
    store=AsyncMock();store.read.return_value=new
    with pytest.raises(ValueError,match='gap'):
        await campaign.load_checkpoint(store,{retry},manifest,'test/model','2026-11-02')
