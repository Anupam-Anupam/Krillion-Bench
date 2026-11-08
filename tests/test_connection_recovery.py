import hashlib
from copy import deepcopy
from unittest.mock import AsyncMock

import httpx
import pytest
import archive_campaign as campaign
from private_storage import encode_document


def fixture():
    manifest={'campaign':'archive-test'}
    path=campaign.report_path(manifest,'test/model','2026-11-02')
    saved={'model':'test/model','game_date':'2026-11-02','report':{'scorecard_verified':False,'rounds':[{'prompt':'already started'}],'error_type':'ConnectError'},'events':[]}
    digest=hashlib.sha256(encode_document(saved)).hexdigest()
    doc={'campaign':'archive-test','authorization':'user_requested_connection_drop_retries','reports':[{'path':path,'sha256':digest}]}
    return manifest,path,saved,doc


async def test_exact_authorized_network_failure_retries_without_replacing_original():
    manifest,path,saved,doc=fixture()
    store=AsyncMock();store.read.return_value=saved
    with pytest.raises(ValueError,match='diagnosis'):
        await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02')
    recovery=campaign.connection_recovery_paths(doc,'archive-test')
    result,retry,previous=await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',recovery)
    assert result is None and previous==path and retry.endswith('/attempt-1.json.gz')
    store.put.assert_not_called()
    saved['events'].append({'event':'changed'})
    with pytest.raises(ValueError,match='diagnosis'):
        await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',recovery)


async def test_verified_zero_is_terminal_even_if_allowlisted():
    manifest,path,saved,doc=fixture()
    saved['report'].update(scorecard_verified=True,final_score='0')
    doc['reports'][0]['sha256']=hashlib.sha256(encode_document(saved)).hexdigest()
    store=AsyncMock();store.read.return_value=saved
    result,chosen,previous=await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',campaign.connection_recovery_paths(doc,'archive-test'))
    assert result==saved and chosen==path and previous is None


@pytest.mark.parametrize('fault',['campaign','authorization','hash','duplicate','cross_campaign'])
def test_invalid_recovery_manifest_rejected(fault):
    _,_,_,doc=fixture()
    if fault=='campaign':doc['campaign']='wrong'
    if fault=='authorization':doc['authorization']='generic retry'
    if fault=='hash':doc['reports'][0]['sha256']='bad'
    if fault=='duplicate':doc['reports'].append(deepcopy(doc['reports'][0]))
    if fault=='cross_campaign':doc['reports'][0]['path']='another/runs/x.json.gz'
    with pytest.raises(ValueError):campaign.connection_recovery_paths(doc,'archive-test')


async def test_non_network_error_does_not_gain_retry():
    manifest,path,saved,doc=fixture()
    saved['report']['error_type']='ValueError'
    doc['reports'][0]['sha256']=hashlib.sha256(encode_document(saved)).hexdigest()
    store=AsyncMock();store.read.return_value=saved
    with pytest.raises(ValueError,match='diagnosis'):
        await campaign.load_checkpoint(store,{path},manifest,'test/model','2026-11-02',campaign.connection_recovery_paths(doc,'archive-test'))


async def test_connection_timeout_is_an_authorized_network_retry():
    manifest,path,saved,doc=fixture()
    saved['report']['error_type']='ConnectTimeout'
    doc['reports'][0]['sha256']=hashlib.sha256(encode_document(saved)).hexdigest()
    store=AsyncMock();store.read.return_value=saved
    result,retry,previous=await campaign.load_checkpoint(
        store,{path},manifest,'test/model','2026-11-02',campaign.connection_recovery_paths(doc,'archive-test'))
    assert result is None and previous==path and retry.endswith('/attempt-1.json.gz')


async def test_upload_waits_in_same_slot_retries_identical_report(monkeypatch):
    store=AsyncMock();saved={'private':'test-only'}
    store.put.side_effect=[httpx.ConnectError('offline'),httpx.ReadTimeout('offline'),'ack']
    sleep=AsyncMock();monkeypatch.setattr(campaign.asyncio,'sleep',sleep)
    assert await campaign.persist_checkpoint(store,'path',saved)=='ack'
    assert store.put.await_count==3
    assert all(call.args==('path',saved) for call in store.put.await_args_list)
    assert [call.args[0] for call in sleep.await_args_list]==[10,20]


async def test_integrity_conflict_still_stops(monkeypatch):
    store=AsyncMock();store.put.side_effect=RuntimeError('Immutable conflict')
    sleep=AsyncMock();monkeypatch.setattr(campaign.asyncio,'sleep',sleep)
    with pytest.raises(RuntimeError,match='Immutable conflict'):
        await campaign.persist_checkpoint(store,'path',{})
    assert store.put.await_count==1
    sleep.assert_not_called()
