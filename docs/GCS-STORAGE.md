# Private Google Cloud Storage

## Provisioned resources

- Owner: the user’s personal Google account; no organization or work account.
- Project: `krillion-bench-20261107` (number `819743372056`), no organization.
- Bucket: `krillion-runs-20261107-83e52a`.
- Region: `us-east1`; Standard storage, uniform bucket access, public access
  prevention enforced, Google-managed encryption, seven-day soft delete.

Status: the bucket and dedicated `krillion-runner` service account are configured
with the three bucket-only roles below. The approved JSON credential is stored
outside Git with owner-only permissions. The live synthetic test passed private
bucket verification, create/read/list, checksum validation, identical-write
reconciliation, conflict refusal, and absence of overwrite/delete/IAM permissions.

The original coordinator drained cleanly at **228 verified games** on
2026-11-08 UTC (November 7 in Toronto), exited with code 0, and remains retired.
The isolated continuation has started with GCS enabled and has uploaded the
immutable original manifest, catalog, and historical-inventory cutover record.
Startup verified all 228 historical games and resumed the remaining 7,272 with
ten rolling workers. Five new game reports were observed in GCS during activation;
three independent readbacks verified checksums, exact model/date identity, all seven
rounds, and final scorecards. Replacement browser sessions started immediately
after completed uploads. All new reports go to GCS. The subsequent historical
backfill copied and verified all 228 accepted earlier reports into the same bucket;
the original reports remain in private GitHub.

## Readable report layout

```text
campaigns/
  archive-75-20261106-v3/
    manifest.json.gz
    catalog.json.gz
    storage-cutover.json.gz
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
The user explicitly approved this bucket-only credential. The saved credential
was validated against the expected project and service account before the
successful smoke test; its directory is mode 0700 and file mode 0600.

The backend rechecks project number and privacy, compresses JSON in memory, uses
`if_generation_match=0` to prevent overwrites, verifies CRC32C and SHA-256, and
checks uploaded bytes by reading them back. A lost acknowledgement is reconciled
against identical stored content. Conflicts and unconfirmed writes stop work.
No new trajectories, credentials, or private indexes belong in Git or local
artifact directories. The local filesystem is used only for the explicitly
configured credential, never as a trajectory sink.

## Cutover procedure and restart contract

1. The approved credential and synthetic in-memory upload/read/list/immutability
   test are verified. The test did not start a game.
2. The CLI wiring and exact source-hash migration are prepared and tested against
   the real frozen manifest. The isolated continuation is
   `/private/tmp/Krillion-Bench-gcs`; all ten existing gameplay/shared modules are
   unchanged. Its new adapter and dependency lock are pinned. Public numeric
   progress keeps its existing separate GitHub status branch. Do not bypass source
   hashes or pull reorganized main into the running process.
3. The original coordinator drained and exited with 228 verified reports. Leave
   its stop sentinel in place; never restart it alongside the GCS continuation.
   The legacy path inventory and destination identity are frozen in GCS.
4. The GCS startup path uploads an immutable catalog, original manifest, and
   cutover record containing the historical checkpoint inventory and destination.
   A changed historical inventory is rejected on subsequent restarts. Resume exactly the remaining
   model/day pairs with ten rolling workers. `ReadThroughStore` reads old GitHub
   checkpoints and writes only new ones to GCS; it never silently falls back to
   GitHub writes. Duplicate checkpoints with conflicting content fail closed.
5. Monitoring now targets the isolated GCS runtime and reads both stores. It
   retains the original all-7,500 balanced completion gate. Previous GitHub data
   and all real scores remain unchanged. Numeric progress is refreshed periodically;
   reports are acknowledged before each worker starts its next game.
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
cutover. The historical private repository retains the originals of older reports; those
accepted reports are now also copied into GCS. Newly executed reports go only to GCS. Neither the catalog nor the cutover record
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

## Historical report backfill

Completed November 7, 2026 (Toronto): **228 accepted reports** copied with full
content/checksum readback verification. The operation covered 234 objects: the
already-present original manifest, three execution revisions, protocol lineage,
228 reports, and the completion audit. Earlier discarded campaigns and health
diagnostic reports were not imported. The ten-worker campaign remained running.

`harness/backfill_gcs.py` copies the accepted campaign's historical reports into
exactly the same date/provider/model/attempt folders used by new workers. It does
not start games or change the coordinator. Run from the organized repository with
the GCS-enabled environment:

```sh
/private/tmp/Krillion-Bench-gcs/.venv/bin/python harness/backfill_gcs.py \
  --bucket krillion-runs-20261107-83e52a \
  --project krillion-bench-20261107 --project-number 819743372056 \
  --credentials "$HOME/.config/krillion-bench/runner.json" \
  --expected-count 228 --apply
```

Omit `--apply` for read-only validation. The tool checks the cutover's frozen source
inventory and destination, identical original manifests, accepted attempt history,
seven-round verified scorecards, score bounds, and per-date prompt fingerprints.
It preserves valid zero scores, question timeouts, and pre-amendment reports
exactly. Earlier discarded campaigns and diagnostic runs are excluded. If the
historical inventory contains rejected predecessors or unmatched attempts, it
stops for an explicit provenance-copy policy instead of creating incomplete chains.

All source validation and destination conflict checks happen before writing. Each
immutable upload is read back and compared to the source; identical existing
objects are reused. Reads and transfers stay in memory. GitHub originals are
retained unchanged. Shared logical checkpoint paths are deduplicated by the live
reader, so copying a report never changes its score or counts it twice.

The original execution revisions and protocol lineage accompany the reports.
After all objects verify, the tool writes the private completion audit:

```text
campaigns/archive-75-20261106-v3/migrations/github-backfill-v1.json.gz
```

This immutable audit records the source repository, cutover digest, report count,
and each logical path, readable object name, and SHA-256. The original catalog and
cutover record remain unchanged as historical evidence. The running continuation
still reads/checks both stores; retain GitHub access and its frozen inventory even
after the copies are complete.
