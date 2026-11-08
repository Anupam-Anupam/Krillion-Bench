import copy
import hashlib
import json
from pathlib import Path

import pytest
from archive_campaign import report_path
from backfill_gcs import backfill, digest
from gcs_storage import ReadThroughStore, ReportLayout

CAMPAIGN = 'archive-75-20261106-v3'
MODEL = 'example/model:free'
DAY = '2026-11-06'


class Store:
    def __init__(self, documents):
        self.documents = copy.deepcopy(documents)
        self.writes = []
        self.repo = 'Anupam-Anupam/Krillion-Bench-Private-Runs'
        self.bucket_name, self.project, self.project_number = 'private-bucket', 'personal', '123'
        self.layout = ReportLayout([MODEL])
        self.client = None

    async def verify(self):
        pass

    async def paths(self):
        return set(self.documents)

    async def read(self, path):
        return copy.deepcopy(self.documents.get(path))

    async def put(self, path, document):
        if path in self.documents and self.documents[path] != document:
            raise RuntimeError('Immutable conflict')
        self.writes.append(path)
        self.documents[path] = copy.deepcopy(document)
        return digest(document)


def stores():
    manifest = dict(campaign=CAMPAIGN, games=[{'date': DAY}], models=[{'id': MODEL}])
    path = report_path(manifest, MODEL, DAY)
    prompts = [f'Prompt {n}' for n in range(7)]
    saved = dict(model=MODEL, game_date=DAY,
        prompt_fingerprint=hashlib.sha256(json.dumps(prompts, ensure_ascii=False).encode()).hexdigest(),
        report=dict(scorecard_verified=True, final_score='0', rounds=[{'prompt': p} for p in prompts],
                    inference_interruptions=[{'reason': 'round_inference_deadline'}]), events=[])
    manifest_path = CAMPAIGN+'/manifest.json.gz'
    old = Store({manifest_path: manifest, path: saved,
                 CAMPAIGN+'/execution-revisions/old.json.gz': {'reason': 'original protocol'},
                 'discarded-v2/runs/report.json.gz': {'excluded': True}})
    new = Store({manifest_path: manifest})
    new.documents[CAMPAIGN+'/storage-cutover.json.gz'] = dict(campaign=CAMPAIGN, legacy_repo=old.repo,
        legacy_paths=sorted(old.documents), destination=dict(bucket=new.bucket_name, project=new.project, project_number=new.project_number))
    return old, new, path


async def test_preserves_zero_timeout_pre_amendment_report_and_provenance_without_local_writes(monkeypatch):
    old, new, path = stores()
    original = copy.deepcopy(old.documents)
    def forbidden(*args, **kwargs):
        raise AssertionError('No private local files')
    monkeypatch.setattr(Path, 'write_text', forbidden)
    monkeypatch.setattr(Path, 'write_bytes', forbidden)
    result = await backfill(old, new, CAMPAIGN, 1, apply=True)
    assert result['reports'] == 1
    assert new.documents[path] == original[path]
    assert old.documents == original and old.writes == []
    assert not any(p.startswith('discarded') for p in new.documents)
    assert new.writes[-1] == CAMPAIGN+'/migrations/github-backfill-v1.json.gz'
    assert CAMPAIGN+'/execution-revisions/old.json.gz' in new.documents
    # Shared paths are a set, so an identical copy never adds a second scored run.
    combined = ReadThroughStore(new, old)
    assert await combined.read(path) == original[path]
    assert sum(p == path for p in await combined.paths()) == 1
    writes = list(new.writes)
    repeated = await backfill(old, new, CAMPAIGN, 1, apply=True)
    assert repeated['already_present'] == repeated['objects']
    assert new.writes == writes


async def test_dry_run_never_writes():
    old, new, _ = stores()
    result = await backfill(old, new, CAMPAIGN, 1)
    assert result['applied'] is False and new.writes == old.writes == []


@pytest.mark.parametrize('fault', ['count', 'conflict', 'fingerprint', 'unverified', 'inventory', 'destination', 'rounds'])
async def test_preflight_failure_prevents_all_writes(fault):
    old, new, path = stores()
    expected = 1
    if fault == 'count': expected = 2
    if fault == 'conflict': new.documents[path] = {'changed': True}
    if fault == 'fingerprint': old.documents[path]['prompt_fingerprint'] = 'wrong'
    if fault == 'unverified': old.documents[path]['report']['scorecard_verified'] = False
    if fault == 'inventory': old.documents['unexpected.json.gz'] = {}
    if fault == 'destination': new.project = 'wrong'
    if fault == 'rounds': old.documents[path]['report']['rounds'].pop()
    with pytest.raises(ValueError):
        await backfill(old, new, CAMPAIGN, expected, apply=True)
    assert new.writes == [] and old.writes == []


async def test_mid_upload_failure_resumes_identically_without_touching_new_live_reports():
    old, new, path = stores()
    live_path = CAMPAIGN+'/runs/2026-11-05/live.json.gz'
    new.documents[live_path] = {'live': True}
    put = new.put
    async def fail_on_report(p, document):
        if p == path:
            raise RuntimeError('Upload unavailable')
        return await put(p, document)
    new.put = fail_on_report
    with pytest.raises(RuntimeError, match='Upload unavailable'):
        await backfill(old, new, CAMPAIGN, 1, apply=True)
    assert CAMPAIGN+'/migrations/github-backfill-v1.json.gz' not in new.documents
    new.put = put
    await backfill(old, new, CAMPAIGN, 1, apply=True)
    assert new.documents[live_path] == {'live': True}
    assert new.documents[path] == old.documents[path]
