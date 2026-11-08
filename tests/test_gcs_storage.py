import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

pytest.importorskip('google.cloud.storage')
from google.api_core.exceptions import NotFound, PreconditionFailed, ServiceUnavailable
from gcs_storage import PrivateGCSStore, ReadThroughStore, ReportLayout
from private_storage import encode_document

MODEL = 'openai/example:free'
HASH = hashlib.sha256(MODEL.encode()).hexdigest()[:24]
PATH = f'archive-v3/runs/2026-11-06/{HASH}.json.gz'
REPORT = {'model': MODEL, 'game_date': '2026-11-06', 'report': {'scorecard_verified': True, 'final_score': '0'}}


class Blob:
    def __init__(self, bucket, name):
        self.bucket, self.name, self.metadata, self.generation = bucket, name, None, None

    def reload(self, **kwargs):
        if self.name not in self.bucket.objects:
            raise NotFound('missing')
        _, self.metadata = self.bucket.objects[self.name]
        self.generation = 1

    def upload_from_string(self, content, **kwargs):
        assert kwargs['if_generation_match'] == 0
        assert kwargs['checksum'] == 'crc32c'
        if self.name in self.bucket.objects:
            raise PreconditionFailed('exists')
        self.bucket.objects[self.name] = content, dict(self.metadata)
        if self.bucket.lose_ack:
            raise ServiceUnavailable('ack lost')

    def download_as_bytes(self, **kwargs):
        assert kwargs['if_generation_match'] == self.generation
        assert kwargs['raw_download'] is True and kwargs['checksum'] == 'crc32c'
        return self.bucket.objects[self.name][0]


class Client:
    def __init__(self):
        self.objects, self.lose_ack = {}, False
        self.project_number = '123'
        self.iam_configuration = SimpleNamespace(public_access_prevention='enforced', uniform_bucket_level_access_enabled=True)

    def bucket(self, name):
        return self

    def reload(self, **kwargs):
        pass

    def blob(self, name):
        return Blob(self, name)

    def list_blobs(self, bucket, **kwargs):
        assert kwargs['prefix'] == 'campaigns/'
        for name in self.objects:
            blob = self.blob(name)
            blob.reload()
            yield blob

    def close(self):
        pass


def make_store():
    client = Client()
    store = PrivateGCSStore('test-bucket', 'personal-project', '123', ReportLayout([MODEL]), client=client)
    return store, client


def test_names_expose_day_model_and_attempt_without_collisions():
    layout = ReportLayout([MODEL, 'openai/example-free'])
    name, identity = layout.describe(PATH)
    assert name == 'campaigns/archive-v3/games/2026-11-06/models/openai/example%3Afree/attempts/initial/report.json.gz'
    retry = f'archive-v3/startup-retries/2026-11-06/{HASH}/attempt-2.json.gz'
    assert '/attempts/attempt-2/' in layout.describe(retry)[0]
    assert identity['model'] == MODEL
    assert len({r['folder'] for r in layout.catalog()['models']}) == 2
    with pytest.raises(ValueError):
        layout.describe('../secret.json.gz')


async def test_immutable_roundtrip_and_index_never_write_trajectories_locally(monkeypatch):
    store, client = make_store()
    def forbidden(*args, **kwargs):
        raise AssertionError('Local trajectory write')
    monkeypatch.setattr(Path, 'write_bytes', forbidden)
    monkeypatch.setattr(Path, 'write_text', forbidden)
    first = await store.put(PATH, REPORT)
    assert await store.put(PATH, REPORT) == first
    assert await store.read(PATH) == REPORT
    assert await store.paths() == {PATH}
    assert len(client.objects) == 1
    with pytest.raises(RuntimeError, match='different data'):
        await store.put(PATH, {**REPORT, 'changed': True})


async def test_lost_ack_reconciles_by_verified_content():
    store, client = make_store()
    client.lose_ack = True
    assert await store.put(PATH, REPORT) == hashlib.sha256(encode_document(REPORT)).hexdigest()
    assert len(client.objects) == 1


@pytest.mark.parametrize('invalid', ['project', 'public', 'uniform'])
async def test_wrong_project_or_weakened_privacy_blocks_writes(invalid):
    store, client = make_store()
    if invalid == 'project': client.project_number = '999'
    if invalid == 'public': client.iam_configuration.public_access_prevention = 'inherited'
    if invalid == 'uniform': client.iam_configuration.uniform_bucket_level_access_enabled = False
    with pytest.raises(RuntimeError, match='expected project'):
        await store.put(PATH, REPORT)
    assert not client.objects


async def test_checksum_corruption_and_wrong_report_identity_fail_closed():
    store, client = make_store()
    with pytest.raises(ValueError, match='model/date'):
        await store.put(PATH, {**REPORT, 'game_date': '2026-11-05'})
    await store.put(PATH, REPORT)
    name = store.layout.describe(PATH)[0]
    content, metadata = client.objects[name]
    client.objects[name] = content + b'corrupt', metadata
    with pytest.raises(RuntimeError, match='checksum'):
        await store.read(PATH)


async def test_split_storage_retains_old_results_and_never_falls_back_to_github_writes():
    legacy, destination = AsyncMock(), AsyncMock()
    legacy.paths.return_value = {PATH}
    legacy.read.return_value = REPORT
    destination.read.return_value = None
    destination.paths.return_value = {'archive-v3/new.json.gz'}
    store = ReadThroughStore(destination, legacy)
    assert await store.read(PATH) == REPORT
    await store.put(PATH, REPORT)
    destination.put.assert_not_called()
    assert await store.paths() == {PATH, 'archive-v3/new.json.gz'}
    destination.put.side_effect = RuntimeError('GCS unavailable')
    with pytest.raises(RuntimeError, match='GCS unavailable'):
        await store.put('archive-v3/new.json.gz', {'new': True})
    legacy.put.assert_not_called()
    destination.read.return_value = {**REPORT, 'changed': True}
    with pytest.raises(RuntimeError, match='Conflicting'):
        await store.read(PATH)


def test_entire_campaign_calendar_and_roster_have_distinct_report_locations():
    root = Path(__file__).resolve().parents[1]
    models = [r['model'] for r in json.loads((root / 'web/data/leaderboard-data.json').read_text())['runs']]
    games = json.loads((root / 'data/archive-games.json').read_text())
    layout = ReportLayout(models)
    locations = set()
    for model in models:
        digest = hashlib.sha256(model.encode()).hexdigest()[:24]
        for game in games:
            day = game['date']
            paths = [f'archive-v3/runs/{day}/{digest}.json.gz'] + [
                f'archive-v3/startup-retries/{day}/{digest}/attempt-{i}.json.gz'
                for i in range(1, 4)]
            for path in paths:
                name, identity = layout.describe(path)
                assert identity['model'] == model and identity['game_date'] == day
                assert name not in locations
                locations.add(name)
    assert len(models) == 100 and len(games) == 75
    assert len(locations) == 30_000


@pytest.mark.parametrize('invalid', [
    PATH.replace('2026-11-06', '2026-02-30'),
    PATH.replace(HASH, '0' * 24),
    PATH.replace('/runs/', '/startup-retries/'),
])
def test_invalid_date_model_or_attempt_is_rejected(invalid):
    with pytest.raises(ValueError):
        ReportLayout([MODEL]).describe(invalid)


async def test_mislabelled_metadata_and_unindexed_objects_are_rejected():
    store, client = make_store()
    await store.put(PATH, REPORT)
    name = store.layout.describe(PATH)[0]
    content, metadata = client.objects[name]
    client.objects[name] = content, {**metadata, 'model': 'other/model'}
    with pytest.raises(RuntimeError, match='identity'):
        await store.read(PATH)
    client.objects[name] = content, {}
    with pytest.raises(RuntimeError, match='Unindexed'):
        await store.paths()


async def test_cutover_catalog_retains_calendar_roster_and_historical_locations():
    destination, client = make_store()
    legacy = AsyncMock()
    legacy.repo = 'Anupam-Anupam/private-example'
    legacy.paths.return_value = {PATH, 'archive-v3/manifest.json.gz'}
    manifest = dict(campaign='archive-v3', games=[{'date': '2026-11-06', 'url': 'https://krillion.io/test-only'}])
    store = ReadThroughStore(destination, legacy)
    await store.prepare_campaign(manifest)
    await store.prepare_campaign(manifest)  # Idempotent restart, no new checkpoint copies.
    catalog = await destination.read('archive-v3/catalog.json.gz')
    assert catalog['games'] == manifest['games']
    assert catalog['models'][0]['model'] == MODEL
    assert catalog['historical_checkpoints'] == sorted(legacy.paths.return_value)
    assert len(client.objects) == 3
    legacy.put.assert_not_called()
    # A later coordinator must detect new writes to the historical repository.
    legacy.paths.return_value = legacy.paths.return_value | {'archive-v3/added.json.gz'}
    restarted = ReadThroughStore(destination, legacy)
    with pytest.raises(RuntimeError, match='Frozen historical inventory'):
        await restarted.prepare_campaign(manifest)
