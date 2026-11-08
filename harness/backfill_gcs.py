"""Copy accepted historical reports to GCS, in memory, without changing the runner."""
import argparse
import asyncio
import hashlib
import json

from archive_campaign import load_checkpoint
from gcs_storage import PrivateGCSStore, ReportLayout
from private_storage import PrivateGitHubStore, encode_document, github_token


def digest(document):
    return hashlib.sha256(encode_document(document)).hexdigest()


async def backfill(legacy, destination, campaign, expected_count, *, apply=False, progress=lambda **data: None):
    await legacy.verify()
    await destination.verify()
    cutover = await destination.read(campaign + '/storage-cutover.json.gz')
    identity = dict(bucket=destination.bucket_name, project=destination.project,
                    project_number=destination.project_number)
    if not cutover or cutover.get('campaign') != campaign or cutover.get('legacy_repo') != legacy.repo or cutover.get('destination') != identity:
        raise ValueError('Cutover source or destination mismatch')
    frozen = set(cutover['legacy_paths'])
    if await legacy.paths() != frozen:
        raise ValueError('Historical inventory changed after cutover')
    manifest_path = campaign + '/manifest.json.gz'
    manifest = await legacy.read(manifest_path)
    if not manifest or manifest.get('campaign') != campaign or manifest != await destination.read(manifest_path):
        raise ValueError('Original campaign manifests differ')
    report_paths = {p for p in frozen if p.startswith((campaign+'/runs/', campaign+'/startup-retries/'))}
    accepted, fingerprints = {}, {}
    for game in manifest['games']:
        for model in manifest['models']:
            saved, path, _ = await load_checkpoint(legacy, frozen, manifest, model['id'], game['date'])
            if saved is None:
                continue
            report = saved['report']
            if len(report.get('rounds', [])) != 7 or report.get('scorecard_verified') is not True:
                raise ValueError('Historical report lacks a verified seven-round scorecard')
            score = report.get('final_score')
            if isinstance(score, bool) or not str(score).isdigit() or not 0 <= int(score) <= 700:
                raise ValueError('Historical report has an invalid final score')
            fingerprint = hashlib.sha256(json.dumps([r['prompt'] for r in report['rounds']], ensure_ascii=False).encode()).hexdigest()
            if fingerprint != saved.get('prompt_fingerprint') or fingerprints.setdefault(game['date'], fingerprint) != fingerprint:
                raise ValueError('Historical puzzle fingerprint mismatch')
            accepted[path] = saved
            if len(accepted) % 25 == 0:
                progress(stage='validated', reports=len(accepted))
    if len(accepted) != expected_count:
        raise ValueError(f'Expected {expected_count} accepted reports, found {len(accepted)}')
    # This backfill must not create an incomplete retry chain in the destination.
    # A campaign with rejected predecessors needs an explicit provenance-copy policy.
    if set(accepted) != report_paths:
        raise ValueError('Historical report inventory contains rejected or unmatched attempts; review before copying')
    documents = {manifest_path: manifest}
    for path in sorted(frozen):
        if path.startswith(campaign+'/execution-revisions/') or path == campaign+'/protocol-lineage.json.gz':
            document = await legacy.read(path)
            if not document:
                raise ValueError('Missing historical provenance document')
            documents[path] = document
    documents.update(accepted)
    audit = dict(schema_version=1, campaign=campaign, source_repo=legacy.repo,
                 destination=identity, cutover_sha256=digest(cutover),
                 policy='Identical copies of accepted historical reports; preserve originals, scores, and execution provenance; no reruns.',
                 report_count=len(accepted),
                 documents=[dict(logical_path=p, object=destination.layout.describe(p)[0], sha256=digest(d))
                            for p, d in sorted(documents.items())])
    audit_path = campaign+'/migrations/github-backfill-v1.json.gz'
    documents[audit_path] = audit
    # Complete source validation and conflict preflight before any write.
    already_present = set()
    for i, (path, document) in enumerate(documents.items(), 1):
        existing = await destination.read(path)
        if existing is not None:
            if encode_document(existing) != encode_document(document):
                raise ValueError('Destination conflicts with historical source: ' + path)
            already_present.add(path)
        if i % 25 == 0:
            progress(stage='preflight', objects=i, total=len(documents))
    if await legacy.paths() != frozen:
        raise ValueError('Historical inventory changed during validation')
    result = dict(reports=len(accepted), objects=len(documents), already_present=len(already_present), applied=apply)
    if not apply:
        return result
    # Audit is inserted last, only after all referenced objects have verified readback.
    for i, (path, document) in enumerate(documents.items(), 1):
        if path not in already_present:
            acknowledged = await destination.put(path, document)
            if acknowledged != digest(document):
                raise RuntimeError('Upload acknowledgement digest mismatch')
        if encode_document(await destination.read(path)) != encode_document(document):
            raise RuntimeError('Backfill readback differs from original')
        if i % 25 == 0:
            progress(stage='copied_and_verified', objects=i, total=len(documents))
    result['audit_object'] = destination.layout.describe(audit_path)[0]
    return result


async def main(args):
    legacy = PrivateGitHubStore(args.repo, github_token())
    destination = None
    try:
        manifest = await legacy.read(args.campaign+'/manifest.json.gz')
        if not manifest:
            raise ValueError('Historical campaign not found')
        destination = PrivateGCSStore(args.bucket, args.project, args.project_number,
            ReportLayout(m['id'] for m in manifest['models']), credentials_file=args.credentials)
        result = await backfill(legacy, destination, args.campaign, args.expected_count,
            apply=args.apply, progress=lambda **data: print(json.dumps(data), flush=True))
        print(json.dumps(result), flush=True)
    finally:
        await legacy.close()
        if destination is not None:
            await destination.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default='Anupam-Anupam/Krillion-Bench-Private-Runs')
    parser.add_argument('--campaign', default='archive-75-20261106-v3')
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--project-number', required=True)
    parser.add_argument('--credentials', required=True)
    parser.add_argument('--expected-count', type=int, required=True)
    parser.add_argument('--apply', action='store_true', help='Copy after full validation; default is read-only')
    asyncio.run(main(parser.parse_args()))
