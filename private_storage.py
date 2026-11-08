"""In-memory trajectory capture and immutable uploads to a personal private repo."""
import asyncio
import base64
import gzip
import hashlib
import json
import os
import re
import subprocess
import time

import httpx


class MemoryRecorder:
    persist_artifacts = False

    def __init__(self, run_id):
        self.run_id = run_id
        self.start = time.monotonic()
        self.model_latencies = []
        self.events = []
        self.final_text = ''

    def event(self, kind, **data):
        self.events.append(dict(elapsed_s=round(time.monotonic() - self.start, 4),
                                event=kind, **data))


def github_token():
    token = os.environ.get('KRILLION_GITHUB_TOKEN')
    if not token:
        result = subprocess.run(['gh', 'auth', 'token', '--hostname', 'github.com',
                                 '--user', 'Anupam-Anupam'], capture_output=True, text=True)
        token = result.stdout.strip() if result.returncode == 0 else ''
    if not token:
        raise RuntimeError('Authenticate Anupam-Anupam with gh auth login first')
    return token


def encode_document(document):
    raw = json.dumps(document, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > 900_000:
        raise ValueError('Report exceeds the private storage object size limit')
    return packed


def blob_sha(content):
    return hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()


class PrivateGitHubStore:
    """No checkout or temporary report files. Upload failures stop new work."""

    def __init__(self, repo, token, *, client=None, write_interval=9.0):
        if not re.fullmatch(r'Anupam-Anupam/[A-Za-z0-9_.-]+', repo):
            raise ValueError('Only the explicitly authorized personal owner is supported')
        self.repo = repo
        self.client = client or httpx.AsyncClient(
            base_url='https://api.github.com', timeout=60,
            headers={'Authorization': 'Bearer ' + token,
                     'Accept': 'application/vnd.github+json'})
        self.write_interval = write_interval
        self.lock = asyncio.Lock()
        self.last_write = 0.0
        self.verified = False

    async def close(self):
        await self.client.aclose()

    @staticmethod
    def retry_delay(response):
        if response is None:
            return None
        retry = response.headers.get('retry-after')
        if retry and retry.isdigit():
            return max(1, int(retry))
        if response.headers.get('x-ratelimit-remaining') == '0':
            reset = response.headers.get('x-ratelimit-reset', '')
            if reset.isdigit():
                return max(1, int(reset) - time.time() + 1)
        return None

    async def get(self, url, **kwargs):
        for attempt in range(6):
            response = await self.client.get(url, **kwargs)
            delay = self.retry_delay(response)
            if response.status_code not in (403, 429) or delay is None:
                return response
            # Pause at the service's reset time; never evade an external quota.
            while delay > 0:
                await asyncio.sleep(min(delay, 60))
                delay -= 60
        raise RuntimeError('GitHub read quota remains unavailable')

    async def verify(self):
        response = await self.get('/repos/' + self.repo)
        if response.status_code != 200:
            raise RuntimeError(f'Private repository access failed (HTTP {response.status_code})')
        meta = response.json()
        if (meta.get('private') is not True or meta.get('full_name') != self.repo
                or not meta.get('permissions', {}).get('push')):
            raise RuntimeError('Reports require a private personal repository with write access')
        self.verified = True

    @staticmethod
    def _path(path):
        if not re.fullmatch(r'[A-Za-z0-9_./-]+', path) or '..' in path or path.startswith('/'):
            raise ValueError('Invalid remote report path')
        return path

    async def read(self, path):
        self._path(path)
        if not self.verified:
            await self.verify()
        response = await self.get(f'/repos/{self.repo}/contents/{path}')
        if response.status_code == 404:
            return None
        if response.status_code != 200:
            raise RuntimeError(f'Private report read failed (HTTP {response.status_code})')
        body = response.json()
        if body.get('encoding') != 'base64':
            raise RuntimeError('Unexpected private report representation')
        content = base64.b64decode(body['content'])
        if blob_sha(content) != body['sha']:
            raise RuntimeError('Private report checksum mismatch')
        return json.loads(gzip.decompress(content))

    async def paths(self):
        if not self.verified:
            await self.verify()
        response = await self.get(f'/repos/{self.repo}/git/trees/main', params={'recursive': '1'})
        if response.status_code != 200 or response.json().get('truncated'):
            raise RuntimeError('Cannot enumerate private checkpoints completely')
        return {entry['path'] for entry in response.json()['tree'] if entry['type'] == 'blob'}

    async def put(self, path, document):
        self._path(path)
        content = encode_document(document)
        expected = blob_sha(content)
        async with self.lock:
            # Recheck privacy before every write; never silently upload to a public repo.
            await self.verify()
            for attempt in range(5):
                await asyncio.sleep(max(0, self.last_write + self.write_interval - time.monotonic()))
                self.last_write = time.monotonic()
                try:
                    response = await self.client.put(f'/repos/{self.repo}/contents/{path}', json={
                        'message': 'Store private benchmark checkpoint',
                        'content': base64.b64encode(content).decode(),
                        'author': {'name': 'Anupam Chettimada',
                                   'email': '92892810+Anupam-Anupam@users.noreply.github.com'}})
                except httpx.TransportError:
                    response = None
                if response is not None and response.status_code == 201:
                    if response.json().get('content', {}).get('sha') != expected:
                        raise RuntimeError('Upload acknowledgement checksum mismatch')
                    return expected
                if response is None or response.status_code in (409, 422):
                    # A lost acknowledgement may have committed successfully. Never overwrite.
                    existing = await self.read(path)
                    if existing is not None:
                        if encode_document(existing) == content:
                            return expected
                        raise RuntimeError('Immutable report path already contains different data')
                if response is not None and response.status_code not in (403, 429, 500, 502, 503, 504, 409, 422):
                    raise RuntimeError(f'Private upload failed (HTTP {response.status_code})')
                delay = self.retry_delay(response)
                if response is not None and response.status_code in (401, 403) and delay is None:
                    raise RuntimeError('GitHub authorization or quota requires attention')
                wait = max(2 ** attempt, delay or 0)
                while wait > 0:
                    await asyncio.sleep(min(wait, 60))
                    wait -= 60
            raise RuntimeError('Private upload unconfirmed; reports remain only in process memory')
