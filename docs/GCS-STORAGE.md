# Private Google Cloud Storage

## Provisioned resources

- Owner: the user’s personal Google account; no organization or work account.
- Project: `krillion-bench-20261107` (number `819743372056`), no organization.
- Bucket: `krillion-runs-20261107-83e52a`.
- Region: `us-east1`; Standard storage, uniform bucket access, public access
  prevention enforced, Google-managed encryption, seven-day soft delete.

Status: the bucket and dedicated `krillion-runner` service account exist. The
three bucket-only roles below are saved. Credential creation was approved and
Google reported its JSON download; the local download has not yet been confirmed,
so the credential smoke test and live cutover remain pending.
The current ten-worker campaign still writes to its private GitHub repository.
The new backend is wired into the campaign CLI but is opt-in.

## Readable report layout

```text
campaigns/
  archive-75-20261106-v3/
    manifest.json.gz
    catalog.json.gz
    execution-revisions/<revision-id>.json.gz
    games/2026-11-06/models/openai/<exact-model-name>/
      attempts/initial/report.json.gz
      attempts/attempt-1/report.json.gz
```

Every report preserves its exact `model`, `game_date`, execution revision, capture
timestamp, prompt fingerprint, complete report, and ordered events. Custom object
metadata also carries campaign/date/model/attempt, the original logical checkpoint
path, and a SHA-256 checksum. Model names are percent-encoded reversibly, so paid
and `:free` variants cannot collide. `catalog.json.gz` maps original model IDs to
folders and legacy identifiers. Retry attempts are distinct immutable objects;
a missed question or zero score never earns a best-of rerun.

To find a report, select the campaign, then the puzzle's calendar date (not the
worker's execution date), then its provider and exact model name. `initial` is the
first attempt; `attempt-1` through `attempt-3` preserve only permitted startup
retries. The report records execution time separately. For example, the initial
`openai/example:free` report for November 6 lives at:

```text
campaigns/archive-75-20261106-v3/games/2026-11-06/models/openai/example%3Afree/attempts/initial/report.json.gz
```

`ReportLayout.catalog()` prepares the model index. The complete campaign manifest
remains the authoritative roster, calendar, settings, and price snapshot.

## Authentication and write contract

Install the optional official SDK with `uv sync --extra gcs --frozen` in a separate
new environment. Use an explicit service-account credential file belonging to this
personal project, outside the repository. Never load work ADC implicitly.
The intended runner permissions are bucket-scoped Storage Object Creator, Storage
Object Viewer, and Storage Legacy Bucket Reader. These allow create/read/list and
bucket-metadata verification, without overwrite/delete or IAM administration.
The user explicitly approved this bucket-only credential. The credential file must
be confirmed locally before attempting the smoke test.

The backend rechecks project number and privacy, compresses JSON in memory, uses
`if_generation_match=0` to prevent overwrites, verifies CRC32C and SHA-256, and
checks uploaded bytes by reading them back. A lost acknowledgement is reconciled
against identical stored content. Conflicts and unconfirmed writes stop work.
No new trajectories, credentials, or private indexes belong in Git or local
artifact directories. The local filesystem is used only for the explicitly
configured credential, never as a trajectory sink.

## Cutover plan — do not switch the running process yet

1. Confirm the approved credential file is available; verify a synthetic in-memory
   upload/read/list and refusal to overwrite. Do not use a real game as a test.
2. The CLI wiring and exact source-hash migration are prepared and tested against
   the real frozen manifest. The isolated continuation is
   `/private/tmp/Krillion-Bench-gcs`; all ten existing gameplay/shared modules are
   unchanged. Its new adapter and dependency lock are pinned. Public numeric
   progress keeps its existing separate GitHub status branch. Do not bypass source
   hashes or pull reorganized main into the running process.
3. Gracefully drain all ten workers; verify every report uploaded and the old
   coordinator exited. Freeze the legacy path inventory and destination identity.
4. The GCS startup path uploads an immutable catalog, original manifest, and
   cutover record containing the historical checkpoint inventory and destination.
   A changed historical inventory is rejected on subsequent restarts. Resume exactly the remaining
   model/day pairs with ten rolling workers. `ReadThroughStore` reads old GitHub
   checkpoints and writes only new ones to GCS; it never silently falls back to
   GitHub writes. Duplicate checkpoints with conflicting content fail closed.
5. Update monitoring to read both stores and retain the original all-7,500 balanced
   completion gate. Keep previous GitHub data and all real scores unchanged.
6. Publish only the final numeric aggregate to `web/data/leaderboard-data.json`.

References: [GCS preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions),
[private access](https://docs.cloud.google.com/storage/docs/public-access-prevention),
[bucket roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Credential smoke test

Run from the organized checkout after placing the approved JSON credential outside
Git with owner-only file permissions:

```sh
.venv/bin/python harness/gcs_smoke.py \
  --bucket krillion-runs-20261107-83e52a \
  --project krillion-bench-20261107 --project-number 819743372056 \
  --credentials "$HOME/.config/krillion-bench/runner.json"
```

This creates a small synthetic object under `campaigns/storage-smoke/`. It checks
create/read/list, privacy, allowed and forbidden IAM permissions, checksums,
idempotency, and conflict refusal. It never starts a game or saves a trajectory
locally. Synthetic checkpoints remain separate from scored campaign reports.

## Activation flags

Only after a successful smoke test and clean drain, add these flags to the
existing campaign command in the isolated continuation checkout:

```sh
--storage gcs --gcs-bucket krillion-runs-20261107-83e52a \
--gcs-project krillion-bench-20261107 --gcs-project-number 819743372056 \
--gcs-credentials "$HOME/.config/krillion-bench/runner.json" \
--accept-gcs-migration --accept-five-word-prompt --concurrency 10
```

Keep the original campaign ID, calendar, roster, profile, pricing and deadline
settings. Supply a clear `--execution-revision-reason` documenting this storage-only
cutover. The historical private repository remains the source for older reports;
only newly executed reports go into GCS. Neither the catalog nor the cutover record
belongs on the public website.

## Runtime parity for this continuation

The prepared continuation uses the same Python 3.13.12 interpreter as the live
campaign. Installed distributions were compared before cutover preparation.
The live environment already has `pyobjc-core==13.0` and
`pyobjc-framework-cocoa==13.0`, while the historical lock pins 12.1. The separate
continuation environment explicitly retains the observed 13.0 versions. All
existing installed distribution versions match the active runtime; the only
additions are the four GCS packages. Do not run a generic sync on this frozen
continuation without repeating this parity check.
