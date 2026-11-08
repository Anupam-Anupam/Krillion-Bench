"""Private, immutable GCS checkpoints with readable date/model object names.

This backend is opt-in. Creating a store does not switch an existing campaign.
Credentials must be explicitly supplied from the dedicated personal project.
"""
import asyncio
import gzip
import hashlib
import json
import re
from datetime import date
from urllib.parse import quote

from private_storage import PrivateGitHubStore, encode_document


class ReportLayout:
    def __init__(self, model_ids):
        ids = list(model_ids)
        if (not ids or len(ids) != len(set(ids))
                or not all(isinstance(m, str) and '/' in m
                           and all(m.split('/', 1)) for m in ids)):
            raise ValueError('Use unique, exact provider/model IDs')
        self.models = {hashlib.sha256(m.encode()).hexdigest()[:24]: m for m in ids}
        if len(self.models) != len(ids):
            raise ValueError('Model identifier collision')

    @staticmethod
    def model_folder(model):
        provider, name = model.split('/', 1)
        # Percent encoding preserves free suffixes and any embedded slashes uniquely.
        return quote(provider, safe='') + '/' + quote(name, safe='')

    def describe(self, path):
        PrivateGitHubStore._path(path)
        if not path.endswith('.json.gz') or '/' not in path:
            raise ValueError('Expected a campaign JSON checkpoint')
        campaign, relative = path.split('/', 1)
        match = re.fullmatch(r'(runs|startup-retries)/(\d{4}-\d{2}-\d{2})/([a-f0-9]{24})(?:/(attempt-[1-3]))?\.json\.gz', relative)
        if not match:
            if relative.startswith(('runs/', 'startup-retries/')):
                raise ValueError('Invalid run checkpoint name')
            return 'campaigns/' + path, {'campaign': campaign}
        kind, day, digest, retry = match.groups()
        if (kind == 'runs') != (retry is None):
            raise ValueError('Invalid attempt path')
        date.fromisoformat(day)
        if digest not in self.models:
            raise ValueError('Report model is absent from the campaign roster')
        model = self.models[digest]
        attempt = retry or 'initial'
        name = f'campaigns/{campaign}/games/{day}/models/{self.model_folder(model)}/attempts/{attempt}/report.json.gz'
        return name, {'campaign': campaign, 'game_date': day, 'model': model, 'attempt': attempt}

    def catalog(self):
        return {'schema_version': 1, 'layout': 'campaigns/<campaign>/games/<YYYY-MM-DD>/models/<provider>/<model>/attempts/<attempt>/report.json.gz',
                'models': [{'model': m, 'folder': self.model_folder(m), 'legacy_id': h}
                           for h, m in sorted(self.models.items(), key=lambda item: item[1])]}


class PrivateGCSStore:
    def __init__(self, bucket, project, project_number, layout, *, credentials_file=None, client=None):
        from google.cloud import storage
        from google.oauth2 import service_account
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{1,61}[a-z0-9]', bucket):
            raise ValueError('Invalid bucket name')
        if client is None:
            if not credentials_file:
                raise ValueError('An explicit bucket-scoped service-account credential is required')
            credentials = service_account.Credentials.from_service_account_file(
                credentials_file, scopes=['https://www.googleapis.com/auth/devstorage.read_write'])
            if (credentials.project_id != project or
                    not credentials.service_account_email.endswith('@' + project + '.iam.gserviceaccount.com')):
                raise ValueError('Credential does not belong to the dedicated personal project')
            client = storage.Client(project=project, credentials=credentials)
        self.storage_client = client
        self.bucket = client.bucket(bucket)
        self.bucket_name = bucket
        self.project = project
        self.project_number = str(project_number)
        self.layout = layout
        self.lock = asyncio.Lock()

    def _verify(self):
        self.bucket.reload(timeout=30)
        iam = self.bucket.iam_configuration
        if (str(self.bucket.project_number) != self.project_number
                or iam.public_access_prevention != 'enforced'
                or not iam.uniform_bucket_level_access_enabled):
            raise RuntimeError('Reports require the expected project and enforced private uniform access')

    async def verify(self):
        async with self.lock:
            await asyncio.to_thread(self._verify)

    def _read(self, path):
        from google.api_core.exceptions import NotFound
        name, identity = self.layout.describe(path)
        blob = self.bucket.blob(name)
        try:
            blob.reload(timeout=30)
        except NotFound:
            return None
        metadata = blob.metadata or {}
        content = blob.download_as_bytes(if_generation_match=blob.generation, raw_download=True,
                                         checksum='crc32c', timeout=60)
        if (metadata.get('logical_path') != path
                or any(metadata.get(k) != v for k, v in identity.items())
                or metadata.get('sha256') != hashlib.sha256(content).hexdigest()):
            raise RuntimeError('Private checkpoint identity or checksum mismatch')
        document = json.loads(gzip.decompress(content))
        self._validate_document(identity, document)
        return document

    async def read(self, path):
        async with self.lock:
            await asyncio.to_thread(self._verify)
            return await asyncio.to_thread(self._read, path)

    @staticmethod
    def _validate_document(identity, document):
        if not isinstance(document, dict):
            raise ValueError('Checkpoint must be a JSON object')
        if 'model' in identity and (document.get('model') != identity['model']
                                  or document.get('game_date') != identity['game_date']):
            raise ValueError('Report model/date does not match its object path')

    def _put(self, path, document):
        from google.api_core.exceptions import GoogleAPICallError
        from google.cloud.storage.retry import DEFAULT_RETRY_IF_GENERATION_SPECIFIED
        self._verify()
        name, identity = self.layout.describe(path)
        self._validate_document(identity, document)
        content = encode_document(document)
        digest = hashlib.sha256(content).hexdigest()
        blob = self.bucket.blob(name)
        blob.metadata = {**identity, 'logical_path': path, 'sha256': digest}
        try:
            blob.upload_from_string(content, content_type='application/gzip', if_generation_match=0,
                                    checksum='crc32c', timeout=60,
                                    retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED)
        except GoogleAPICallError:
            # A lost acknowledgement or an identical repeated put must never overwrite.
            existing = self._read(path)
            if existing is None:
                raise RuntimeError('Private GCS upload unconfirmed') from None
            if encode_document(existing) != content:
                raise RuntimeError('Immutable report path already contains different data') from None
            return digest
        # Confirm durable bytes and identity, not just the upload response.
        if encode_document(self._read(path)) != content:
            raise RuntimeError('Private GCS upload readback mismatch')
        return digest

    async def put(self, path, document):
        async with self.lock:
            return await asyncio.to_thread(self._put, path, document)

    def _paths(self):
        self._verify()
        result = set()
        # SDK iterator follows all pages; only checkpoint objects enter resume state.
        for blob in self.storage_client.list_blobs(self.bucket, prefix='campaigns/', timeout=60):
            path = (blob.metadata or {}).get('logical_path')
            if path is None:
                raise RuntimeError('Unindexed object in campaign checkpoint namespace')
            if self.layout.describe(path)[0] != blob.name:
                raise RuntimeError('Checkpoint index does not match object name')
            result.add(path)
        return result

    async def paths(self):
        async with self.lock:
            return await asyncio.to_thread(self._paths)

    async def close(self):
        async with self.lock:
            await asyncio.to_thread(self.storage_client.close)


class ReadThroughStore:
    """Read frozen historical GitHub checkpoints; write new checkpoints only to GCS."""
    def __init__(self, destination, legacy):
        self.destination, self.legacy = destination, legacy
        # Public aggregate progress keeps its separate GitHub status endpoint.
        self.client = legacy.client
        self.legacy_paths = None

    async def verify(self):
        await self.destination.verify()
        await self.legacy.verify()
        if self.legacy_paths is None:
            self.legacy_paths = await self.legacy.paths()

    async def paths(self):
        if self.legacy_paths is None:
            await self.verify()
        return self.legacy_paths | await self.destination.paths()

    async def read(self, path):
        if self.legacy_paths is None:
            await self.verify()
        old = await self.legacy.read(path) if path in self.legacy_paths else None
        new = await self.destination.read(path)
        if old is not None and new is not None and encode_document(old) != encode_document(new):
            raise RuntimeError('Conflicting historical and GCS checkpoints')
        return new if new is not None else old

    async def put(self, path, document):
        if self.legacy_paths is None:
            await self.verify()
        if path in self.legacy_paths:
            previous = await self.legacy.read(path)
            if previous is None or encode_document(previous) != encode_document(document):
                raise RuntimeError('Historical checkpoint cannot be replaced')
            return hashlib.sha256(encode_document(previous)).hexdigest()
        return await self.destination.put(path, document)

    async def prepare_campaign(self, manifest):
        """Freeze the historical inventory before any new game starts.

        Existing results stay at their original remote destination. The private
        catalog and original manifest also make the new bucket understandable on
        its own, without putting any trajectories into a local checkout.
        """
        await self.verify()
        campaign = manifest['campaign']
        cutover = dict(schema_version=1, campaign=campaign,
                       legacy_repo=self.legacy.repo,
                       legacy_paths=sorted(self.legacy_paths),
                       destination=dict(bucket=self.destination.bucket_name,
                                        project=self.destination.project,
                                        project_number=self.destination.project_number),
                       policy='read historical GitHub checkpoints; create new reports only in GCS')
        path = campaign + '/storage-cutover.json.gz'
        previous = await self.destination.read(path)
        if previous is not None and previous != cutover:
            raise RuntimeError('Frozen historical inventory or GCS destination changed')
        await self.destination.put(path, cutover)
        await self.destination.put(campaign + '/manifest.json.gz', manifest)
        catalog = self.destination.layout.catalog()
        catalog.update(campaign=campaign, games=manifest['games'], legacy_repo=self.legacy.repo,
                       historical_checkpoints=cutover['legacy_paths'])
        await self.destination.put(campaign + '/catalog.json.gz', catalog)

    async def close(self):
        try:
            await self.destination.close()
        finally:
            await self.legacy.close()
