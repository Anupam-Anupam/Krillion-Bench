import json
from types import SimpleNamespace

import httpx
import pytest
from browser_use.llm.messages import SystemMessage

from metrics import aggregate, clean_usage, estimate, usage_hook
from leaderboard import export_campaign
from player import Turn
from runner import Recorder, TimedModel, make_model


def test_cost_estimate_accounts_for_cache_and_does_not_double_reasoning():
    usage = clean_usage({'prompt_tokens':100, 'completion_tokens':20,
                         'prompt_tokens_details':{'cached_tokens':40},
                         'completion_tokens_details':{'reasoning_tokens':15}})
    total, output = estimate(usage, {'prompt':'.01','completion':'.02','input_cache_read':'.001'})
    assert total == pytest.approx(1.04) and output == pytest.approx(.4)
    assert estimate(usage, {'prompt':'.01','completion':'.02'})[0] is None


def test_missing_calls_are_partial_and_zero_is_not_missing():
    events=[{'event':'model_call','duration_s':2}, {'event':'model_call','duration_s':3},
            {'event':'model_usage','usage':{'input_tokens':10,'output_tokens':2,'cost_usd':0,'output_cost_usd':0}}]
    m=aggregate(events)
    assert m['run_cost_usd']==0 and m['cost_basis']=='partial_reported'
    assert not m['usage_complete'] and m['output_tokens']==2
    assert aggregate([])['run_cost_usd'] is None


def test_wire_usage_preferred_over_duplicate_parsed_output():
    events=[{'event':'model_call','duration_s':1},{'event':'model_usage','usage':{'output_tokens':8,'cost_usd':.02}},
            {'event':'model_output','usage':{'completion_tokens':8}}]
    m=aggregate(events)
    assert m['output_tokens']==8 and m['cost_basis']=='reported'
    assert m['run_cost_usd']==.02 and m['usage_complete']


async def test_wire_capture_retains_cost_for_invalid_actions_without_secrets(tmp_path,monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY','fake-key')
    monkeypatch.setenv('OPENAI_BASE_URL','https://example.test/v1')
    async def handle(request):
        return httpx.Response(200,json={'id':'gen-private','object':'chat.completion','created':0,'model':'test',
            'choices':[{'index':0,'finish_reason':'stop','message':{'role':'assistant','content':'not valid json'}}],
            'usage':{'prompt_tokens':100,'completion_tokens':5,'total_tokens':105,'cost':.003,
                     'cost_details':{'upstream_inference_completions_cost':.001},'secret':'must not persist'}})
    record=Recorder(tmp_path/'run')
    model=make_model(SimpleNamespace(provider='openai',model='org/model',max_output_tokens=None,reasoning='low'))
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle),event_hooks={'response':[usage_hook(record)]}) as client:
        model.http_client=client
        with pytest.raises(Exception):
            await TimedModel(model,record).ainvoke([SystemMessage(content='test')],output_format=Turn)
    text=(record.output/'events.jsonl').read_text()
    assert 'must not persist' not in text and 'gen-private' not in text
    m=aggregate([json.loads(l) for l in text.splitlines()])
    assert m['run_cost_usd']==.003 and m['output_cost_usd']==.001 and m['usage_complete']


def test_export_drops_private_fields_and_never_ranks_partial_score():
    summary={'updated_at':'fixture','runs':[{'model':'org/a','rank':1,'status':'failed','score':300,
               'daily_percentile':99,'scorecard_verified':False,'private':'secret'}]}
    manifest={'models':[{'id':'org/a'}],'utc_date':'2026-11-07','settings':{}}
    report={'org/a':{'trace':'secret','rounds':[{'prompt':'test','result_text':'private','submissions':[]}]}}
    result=export_campaign(summary,manifest,report)
    assert result['runs'][0]['score'] is None and result['runs'][0]['daily_percentile'] is None
    assert 'secret' not in json.dumps(result) and 'result_text' not in json.dumps(result)


def test_estimate_applies_context_tier_per_call():
    price={'prompt':'.01','completion':'.02','overrides':[{'min_prompt_tokens':100,'prompt':'.03','completion':'.04'}]}
    assert estimate({'input_tokens':100,'output_tokens':5},price)==(3.2,.2)
    assert estimate({'input_tokens':50,'output_tokens':5},price)==(.6,.1)
