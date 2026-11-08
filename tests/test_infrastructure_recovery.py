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
