"""Verify bucket-scoped credentials using synthetic in-memory data only."""
import argparse
import asyncio
from pathlib import Path
import uuid

from gcs_storage import PrivateGCSStore, ReportLayout


async def smoke(args):
    store = PrivateGCSStore(args.bucket, args.project, args.project_number,
                            ReportLayout(['test/synthetic']), credentials_file=args.credentials)
    try:
        await store.verify()
        required = {'storage.buckets.get', 'storage.objects.create',
                    'storage.objects.get', 'storage.objects.list'}
        forbidden = {'storage.objects.delete', 'storage.objects.update',
                     'storage.buckets.setIamPolicy', 'storage.buckets.delete'}
        granted = set(await asyncio.to_thread(store.bucket.test_iam_permissions,
                                              sorted(required | forbidden), timeout=30))
        if not required <= granted or forbidden & granted:
            raise RuntimeError('Runner permissions differ from the approved bucket-only contract')
        path = f'storage-smoke/{uuid.uuid4().hex}.json.gz'
        document = {'synthetic': True, 'purpose': 'verify private storage without running a game'}
        digest = await store.put(path, document)
        assert await store.read(path) == document
        assert path in await store.paths()
        assert await store.put(path, document) == digest
        try:
            await store.put(path, {**document, 'changed': True})
        except RuntimeError as exc:
            if 'different data' not in str(exc):
                raise
        else:
            raise RuntimeError('Immutable upload accepted conflicting content')
        print('PASS: private bucket, scoped permissions, create/read/list, checksum, idempotency, conflict rejection.')
        print('Synthetic checkpoint: gs://' + args.bucket + '/' + store.layout.describe(path)[0])
    finally:
        await store.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--project-number', required=True)
    parser.add_argument('--credentials', type=Path, required=True)
    args = parser.parse_args()
    asyncio.run(smoke(args))
