# Private 75-game campaign

Target: the existing 100 model IDs, each playing the same 75 archived daily puzzles,
from **November 6 back through August 24, 2026**. This is 7,500 verified games.
The prior single-day results remain public until the complete panel is available.

## Storage

Private destination: `Anupam-Anupam/Krillion-Bench-Private-Runs` on GitHub.
`private_storage.py` checks that this personal repository is private and writable.
Reports and event logs are compressed in memory and uploaded through the GitHub
Contents API. The uploader checks Git blob checksums and refuses overwrites.
It serializes writes and honors service rate limits. No Git checkout of reports is
needed. Credentials are neither included in reports nor written into either repo.

The archive runner uses `MemoryRecorder`, disables cloud recordings, and skips
local screenshots, Playwright tracing, final-page dumps, and JSON/Markdown reports.
Only numeric aggregate exports may be written locally. Synthetic test fixtures are
not model trajectories. A process crash before an upload is acknowledged can lose
an in-memory run; local recovery files are deliberately unavailable. An unverified
run is saved privately and pauses scheduling for diagnosis instead of being scored
as zero or silently retried until it wins.

## Prerequisites and pilot

1. Restore the purchased Krillion Unlimited entitlement in the dedicated Browser
   Use cloud profile. Complete Google login or the normal purchase-link restoration
   yourself. Do not upload personal Chrome/Gmail profiles or broad cookie jars.
2. Verify archive navigation and independent replay in fresh profile-based sessions.
   Account-level saved results must not be mistaken for a new model's score.
3. Record the actual archive URLs and visible date/dive labels from the calendar.
   The game manifest is a JSON array with `date`, `url`, and `visible_label`, in
   descending date order. No URL format is guessed. There must be 75 unique entries.
4. Authenticate `gh` as Anupam-Anupam, or set `KRILLION_GITHUB_TOKEN` with access to
   the private repository. Set `BROWSER_USE_API_KEY`, `OPENAI_API_KEY`,
   `OPENAI_BASE_URL=https://openrouter.ai/api/v1`, and `KRILLION_PROFILE_ID` in the
   runner environment. Existing provider credential files may be passed explicitly
   with `--env-file`; the profile ID is an environment variable.
5. Run a two-game pilot, then inspect both private reports and confirm independent
   play, matching prompts, full scorecards, timing, and percentile availability.

```sh
python archive_campaign.py --games archive-games.json --limit 2
# Once the pilot is verified, resume the exact frozen configuration:
python archive_campaign.py --games archive-games.json
```

The roster comes from `leaderboard-data.json`; original model IDs, including free
variants, are preserved. The initial OpenRouter catalog freezes prices. Missing
model IDs stop preparation. A private manifest freezes source hashes, settings,
dates, and concurrency. Changing those requires a separate campaign, never mixing
results. Each new browser must show its expected archive label and exact URL before
model inference starts. A SHA-256 fingerprint of the seven visible prompts must
match other models on the same date.

Default concurrency is four; raise it only after measuring the pilot and checking
browser/provider capacity. The game deadline and all existing same-model retry and
final-score recovery rules remain unchanged. Completed remote checkpoints are
resumed without replay. The orchestrator emits progress counts, never answer logs.

## Aggregation and public presentation

The exporter requires exactly one verified scorecard per model/date pair, including
genuine zero scores after seven missed questions. Missing scorecards, duplicate
results, and unbalanced model panels block publication. There is no best-of-reruns
selection.

Score is the arithmetic mean across all 75 games. Averages of cost, output cost,
tokens, elapsed time, and daily percentile carry their own sample counts. Missing
values and partial bills are excluded from that metric's mean, never imputed as
zero. Reported charges and catalog estimates retain their provenance. Historical
percentiles are included only if actually displayed by the game.

Score whiskers show a 95% percentile-bootstrap confidence interval over game dates:
10,000 resamples, deterministic seed 20261107, the same resampled date indices for
each model. They describe variation across archived puzzles, not repeated model
trials on one puzzle, and overlapping intervals are not a significance test.

The public export contains only model identifiers, numeric aggregates, sample counts,
uncertainty metadata, and configuration. It contains no prompts, submitted answers,
events, or individual trajectories. Aggregate dialogs show metric coverage and
intervals. The existing pixel font, tier colors, and gold winner highlight apply to
the error bars. The website only displays error bars when real aggregate data is
loaded; it does not fabricate intervals for the existing single-day snapshot.

## Current validation status

Private repository creation and direct in-memory upload/readback are verified.
Unit tests cover no local report writes, private-only uploads, immutable checkpoints,
complete-panel aggregation, missing metric handling, and reproducible intervals.
The aggregate UI is checked with clearly synthetic test data. Archived live-game
replay and the paid 7,500-game campaign remain pending entitlement restoration and
the pilot; no archive scores have been claimed or published.
