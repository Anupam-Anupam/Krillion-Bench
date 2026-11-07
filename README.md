# Krillion Benchmark

A small browser-action harness for an LLM to play the complete Daily Dive from
**https://krillion.io/**. Browser Use Cloud hosts a fresh browser; Playwright executes
the model's actions. Browser Use's model adapters support provider APIs and compatible
endpoints. It runs as a standalone Python project with no database or job queue.

## Leaderboard UI

The static leaderboard in `index.html` follows a restrained research-table layout,
with verified score as the default ranking and the largest visual emphasis. It includes
all 100 model variants from the final-score continuation campaign, a score-versus-metric chart, search/provider/status
filters, reduced-motion/effects support, and a per-run dialog with every answer and rarity.

```sh
python3 -m http.server 8765 --bind 127.0.0.1
# Open http://127.0.0.1:8765/
```

No frontend build, framework, database, or API key is needed. The four public UI files
are `index.html`, `leaderboard.css`, `leaderboard.js`, and `leaderboard-data.json`.
Serve them alongside the bundled `krillion-*` artwork/font files at any static host, including a GitHub Pages project path. Placement badges are Krillion (1), Deep Cut (2–10), Rare (11–25), Schooler (26–50), and Plankton (51–100), fixed to global score order with model ID as the tie break. See [UI-NOTES.md](UI-NOTES.md) for behavior, accessibility, and asset credits.

**Metrics:** LLM run cost (USD), output-token cost (USD), output token count, total
elapsed time, and the game's final daily percentage. Tied scores share a rank;
question timeouts count as zero-point misses and still receive the game’s final score and rank. A run with no verified scorecard is reported separately as a run error. Charts
include completed games with usable metrics only. Cost ranks are not score ranks.

The current snapshot is the November 7 final-score continuation campaign, documented
in [CONTINUATION-REPORT.md](CONTINUATION-REPORT.md). Each model has a verified final
score; missed questions count as zero. A daily percentage is unavailable when the
game did not display it. The original TOP100 reports remain unchanged as history.

Current OpenAI-compatible runs capture numeric API usage before the adapter validates
JSON, so malformed/truncated responses can retain their reported costs. `usage.cost`
is the account charge. The output component, when present, is the provider's reported
output cost and may not sum to the account charge. Missing fields use labeled catalog
estimates where possible. Cancelled requests without usage remain partial or unavailable,
never zero. Historical TOP100 costs were estimates based on saved token usage.
No reasoning tokens are added twice. Browser hosting and credit-purchase fees are
excluded. See [OpenRouter usage accounting](https://openrouter.ai/docs/cookbook/administration/usage-accounting).

Optionally pass `runner.py --pricing-file catalog.json` to estimate fields that the
API did not return. Campaigns freeze each selected model's catalog prices and pass
the frozen manifest to the runner automatically. Run reports now contain `metrics`;
campaigns also write a public `leaderboard.json`. **Load campaign** in the UI replaces
the displayed dataset rather than mixing harness versions or daily puzzles.

To publish a new campaign snapshot:

```sh
uv run python leaderboard.py artifacts/MY_CAMPAIGN --output leaderboard-data.json
```

To rebuild the historical snapshot where private raw events and the discovery catalog
are available locally (these files are deliberately not published):

```sh
uv run python leaderboard.py artifacts/openrouter-top100-20261107 \
  --summary TOP100-SUMMARY.json --answers TOP100-ANSWERS.json \
  --catalog artifacts/openrouter-top100-discovery/catalog.json \
  --output leaderboard-data.json
```

The exporter allowlists run/answer fields and omits raw observations, network traces,
private paths, credentials, and provider response bodies. The downloadable UI JSON
contains only the exported dataset. Uploaded campaign files stay in the browser.

## Completion and failure policy

A 25-second game timeout is a missed question, not a failed game. The agent continues
through all seven rounds and the leaderboard uses the game’s actual final score,
including zero. Rejections, model inference deadlines, action timeouts, malformed
responses, output truncation, and retried provider failures remain visible in run logs.

If a terminal API error, agent step limit, or full agent runtime stops the agent,
the harness cancels outstanding inference/actions and spends up to 240 seconds
collecting the scorecard. It only uses visible navigation controls and lets unanswered
questions expire under the real timer. It does not fill answers, submit DIVE, reload
the game, swap models, or manufacture a daily percentage. These scores are marked
`scored_with_errors`, with the original diagnostic and explicit score-collection
assistance. They measure the model-and-provider run as executed.

An optional screenshot failure is logged as an artifact error and does not stop play.
An unreadable/disconnected browser or a scorecard that cannot be verified remains an
explicit run error without a ranked score. The harness cannot honestly turn missing
game evidence into a successful result. Historical aborted games must be rerun, not
relabelled using their partial points.

The current leaderboard distinguishes missed questions and score-collection recovery
in each model row and displays sanitized failure categories in its dive log.

## Quick start

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync --frozen
cp .env.example .env   # only if you do not already have .env
```

Configure `BROWSER_USE_API_KEY`, `OPENAI_API_KEY`, and `OPENAI_MODEL` in `.env`.
Set `OPENAI_BASE_URL` only when using a compatible endpoint. Credentials are loaded
only from explicitly named files; environment variables take precedence. `.env` and
run artifacts are ignored by Git.

See [VALIDATION.md](VALIDATION.md) for measured live results and known limitations.
[RECOVERY-REPORT.md](RECOVERY-REPORT.md) documents the timeout/provider fixes and
every answer in the targeted follow-up checks.

The 100-model OpenRouter campaign uses `campaign.py`. It freezes an observed ranking,
API catalog, source hashes, and settings before launching one fresh browser per model.
See [TOP100-REPORT.md](TOP100-REPORT.md) for the original historical campaign results, failure breakdown,
and every submitted answer. Machine-readable results are in
[TOP100-SUMMARY.json](TOP100-SUMMARY.json) and [TOP100-ANSWERS.json](TOP100-ANSWERS.json).

```sh
uv run runner.py smoke --env-file .env
uv run runner.py play --env-file .env
```

Change models without changing the agent:

```sh
uv run runner.py play --env-file .env --provider openai --model YOUR_MODEL
uv run runner.py play --env-file .env --provider anthropic --model YOUR_MODEL --max-output-tokens 16000
uv run runner.py play --env-file .env --provider google --model YOUR_MODEL
```

Anthropic uses `ANTHROPIC_API_KEY`; Google uses `GOOGLE_API_KEY`. Only the configured
OpenAI-compatible endpoint has been exercised in the live pilot. Structured-output
support varies by provider and model; compatibility failures remain in campaign results.

## Multi-model campaign

Export `OPENAI_API_KEY` and `OPENAI_BASE_URL=https://openrouter.ai/api/v1` in your shell.
Keep the Browser Use key in an explicit `.env` file. The ranking input has `source`,
`captured_at`, and ordered `rows` containing `id`, `directory_rank`, `name`, and
`weekly_tokens_display`; the catalog is the response from OpenRouter's public
`GET /api/v1/models`. Preserve both inputs with the campaign.

```sh
uv run campaign.py --ranking ranking.json --catalog catalog.json \
  --env-file .env --output artifacts/my-campaign --count 100 --concurrency 4
```

The selector excludes automatic routers, latest aliases, and asynchronous batch variants.
Free and paid variants remain separate by default. Use `--paid-only` to exclude `:free`
endpoints explicitly; exclusions are recorded and model IDs are never silently substituted.
Unknown IDs, duplicates, and an undersized roster fail selection. Output compatibility
fallbacks and unsuccessful attempts remain visible in the results.

The output contains a frozen `manifest.json`, atomic `state.json`, `summary.json`, combined
`REPORT.md`, and each model's normal answer reports and browser artifacts. The same command
resumes pending models without rerunning finished attempts, provided source hashes and
concurrency still match. A live/stale lock or interrupted running entry requires investigation
before resuming. Scheduling stops at a UTC date change or mismatching daily prompts. Runs
already active at detection finish and retain their actual prompt evidence. A hard outer timeout
can prevent browser cleanup; the cloud session's 15-minute lease still bounds its lifetime.

Campaigns measure this complete timed model-and-harness configuration. The current default
omits an output-token cap; model/provider output and context limits still apply. Optional
`--max-output-tokens`, `--model-retries`, and `--navigation-timeout` settings are frozen in
the campaign manifest. The published TOP100 results used the earlier 1,500-token/18-second
configuration and stop-on-failure policy; they are preserved as historical results.
Current missed questions continue to a real final scorecard; provider interruptions,
missed rounds, and run errors without verified scorecards are reported separately.
One daily puzzle per model is an exploratory comparison, not a statistically stable quality ranking.

## Output limits, API failures, and rate limits

`runner.py make_model()` uses `max_completion_tokens=None` by default for OpenRouter /
OpenAI-compatible APIs, so the parameter is absent on the wire. To set a cap deliberately:

```sh
uv run runner.py play --env-file .env --model MODEL_ID --max-output-tokens 16000
```

Omit that flag to remove the harness cap again. Google also omits its output cap by default.
The native Anthropic API requires a cap; specify one explicitly or use its OpenRouter endpoint.
Provider/model limits still exist even when the harness supplies none.

The same JSON action schema is included in the prompt and checked locally. Native structured
output is attempted first. If it is unsupported or the response is malformed/empty, the
OpenAI-compatible adapter can switch once to prompt-only JSON within the configured attempt
budget. This removes the native `response_format` parameter, not validation. The same model
must still return valid constrained actions. Reports log the compatibility change.

`--model-retries 2` permits at most two additional attempts for transient errors such as
429/503 or transport failures. Backoff respects `Retry-After`, including HTTP-date values;
all attempts still share the question's original deadline. A long cooldown carries across
rounds and is waited out before opening the next question. Authentication, insufficient
credit, and incompatible requests are diagnosed rather than retried blindly. There is no
cross-model fallback. `--model-retries 0` disables retries and compatibility reattempts.

The harness has no requests-per-minute quota to disable. OpenRouter and upstream providers
can impose their own limits, including on paid accounts. Prefer explicitly selected paid
endpoints (`campaign.py --paid-only`) over shared free pools for reliability. This reduces
exposure to free-tier restrictions but does not guarantee that 429s disappear. See
[OpenRouter limits](https://openrouter.ai/docs/api_reference/limits) and
[error handling](https://openrouter.ai/docs/api_reference/errors-and-debugging).

## What the model controls

The model starts on the initial game page and chooses answers and browser actions.
The default bounded recovery can advance stalled navigation, as described below.
Its common action schema contains:

- `click`: activate an observed game button by exact visible name. The executor uses
  keyboard Enter on the button because Krillion animates button positions.
- `fill`: type into the observed `Your answer` textbox.
- `wait`: wait one second, still charged to the active deadline.
- `done`: accepted only after seven observed rounds and the rendered final scorecard.

Observations contain an explicit phase and allowed actions, visible game controls,
the active prompt, timer, input value, rejection history, and correction feedback.
Decorative ocean text and ads are omitted so they cannot be confused with a question. No JavaScript execution, network inspection,
answer-bank access, external search, filesystem tools, or second model is exposed to
the evaluated LLM. The harness waits through previews and animations before inference.
It does not pause, reset, or extend the game's timer.

This is a **constrained browser-agent benchmark**, not unrestricted computer use.
The harness knows how to observe Krillion's UI and limits actions to game controls;
the model must choose its own answers and actions. `--vision` adds screenshots to
the same DOM observations and must be reported as a separate evaluation setting.
It is not a screenshot-only track.

## Navigation recovery and evaluation tracks

`--navigation-recovery bounded` is the default. After two model turns leave the same
non-answer navigation state unchanged, the harness may activate its single visible
BEGIN DESCENT, DESCEND, SURFACE, or results control. Each attempt goes through the
normal fresh-state/action guard. Recovery is limited to once per state and eight
attempts per run. An exhausted navigation inference timeout/API failure can also trigger
one logged recovery for that state. It never fills a textbox, submits an answer, resets
the timer, or substitutes another model. Empty transition screens have a
15-second wait limit; the whole run remains bounded too.

Use `--navigation-recovery off` for the strict navigation track. Both tracks have
phase guidance. Reports preserve the selected mode, every recovery attempt, and
whether assistance actually executed. Do not pool these tracks or mix them with
older full-page-text observations in a model ranking.

## Timing and failure contract

- The independent watchdog reads the visible countdown and uses monotonic time.
  It reserves `--margin` seconds (default 3), plus one second for integer rounding.
  Repeated or frozen timer readings cannot extend a round's deadline.
- During a question, inference and any retries share the remaining round budget; there
  is no separate 18-second cutoff. Outside questions, `--navigation-timeout` defaults
  to 60 seconds. The SDK does not retry invisibly; explicit retries are logged.
- Each action rechecks the round/phase and deadline. A stale action batch is discarded.
  Once a run stops, no new actions can execute. The game does not advance to the next
  question automatically; DESCEND is activated by the model or logged bounded recovery.
- Rejected answers may be retried within the same countdown. Rejection does not create
  a fresh budget. The input remaining open is not treated as successful submission.
- A missed question deadline cancels inference/actions for that question, waits for
  the real game timer and result, and continues through DESCEND. The game awards
  zero for NOTHING LANDED. A submission that actually landed despite a delayed browser
  acknowledgement retains its real result. No answer or score is fabricated. A stalled
  game UI or a permanent authentication/request failure can still end the run.
- Completion requires the real final scorecard, seven round entries, and the Copy
  result control. All seven round numbers must be unique and their points must sum
  to the displayed total. The model's own claim of completion is insufficient.
- Browser sessions are closed in `finally`; cloud sessions also have a 15-minute cap.
  No personal browser profile is used. All runs use 1280×800 and reduced-motion preference.

## Outputs

Each invocation writes a fresh directory under `artifacts/`:

| File | Contents |
|---|---|
| `report.md` | Every answer attempt, outcome, rarity, points, daily percentage, and recovery log |
| `report.json` | Structured report plus model-call durations, final scorecard, and evidence sources |
| `events.jsonl` | Observations, actions and their results, submissions, recoveries, model usage, timings, and sanitized failures |
| `initial.png`, `final.png` | Browser evidence when screenshots succeed |
| `final.txt` | Rendered text at the end of the run |
| `trace.zip` | Playwright trace with screenshots and DOM snapshots |

```sh
uv run playwright show-trace artifacts/RUN_DIRECTORY/trace.zip
```

Trace files can include browser network data. Keep raw artifacts private; share selected
screenshots and the summary report. Exception reports omit raw exception strings because
SDK exceptions can contain authenticated browser URLs. Model diagnostics retain scrubbed,
bounded messages, HTTP/provider codes, provider name, rate-limit source, and Retry-After
when available; they omit credentials, raw headers, and arbitrary response objects. Failed screenshot/trace collection
is best effort and does not replace the run's actual outcome.

The daily percentage is parsed from **BETTER THAN X% OF TODAY’S PLAYERS**, only with
a verified final scorecard. It is not score divided by 700. Missing or partial-game
percentiles remain unavailable. Rarity comes from the displayed result; a labeled
points-to-category mapping is available when only scorecard evidence survives.
Every attempted submission remains in order, including rejected answers, game
corrections requiring confirmation, and unconfirmed attempts. Rarity is attached to
an attempt only when its text matches the accepted game result. Ambiguous attempts
remain unconfirmed. Submissions are registered before awaiting the remote keypress;
if that action fails, the attempt remains visible without claiming game acceptance.

Backfill saved runs without overwriting their original `report.json`:

```sh
uv run python reporting.py artifacts/RUN_DIRECTORY
```

This creates `report.enriched.json` and `report.enriched.md` using the saved result
text, final text, and event observations. See [OPENROUTER-REPORT.md](OPENROUTER-REPORT.md)
for all six original runs and the separately labeled Scout regression run.

## Reliability checks

Run in this order:

1. **Startup:** `uv run runner.py smoke --env-file .env` checks cloud connection and
   the actual initial BEGIN DESCENT control.
2. **Submission without an LLM:** supply a JSON mapping of exact visible prompts to
   known accepted answers. These controls are never loaded by `play`.
3. **Full model game:** `uv run runner.py play --env-file .env` measures actual
   inference plus observation and browser-action latency.
4. **Repeat:** use fresh sessions and inspect all failures, not just successful games.

The included control file is specific to the November 7, 2026 Daily Dive and will fail
closed when a different prompt appears:

```sh
uv run runner.py baseline --env-file .env \
  --answers-file tests/control-answers-2026-11-07.json
```

Unit tests cover deadline boundaries, frozen timers, stale actions, premature completion,
and invalid actions. Real Chromium integration tests exercise seven-round completion
and rejection followed by a successful retry within the original budget:

```sh
uv run playwright install chromium
uv run pytest -q
```

To use an existing Chrome installation for tests:

```sh
KRILLION_TEST_CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' uv run pytest -q
```

Local browser mode uses the same player and deadline logic:

```sh
uv run runner.py play --browser local --env-file .env --headed \
  --executable '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
```

## Why this implementation

The first pilot used Browser Use's general-purpose `Agent`. A model call took about
1.3 seconds, but page processing stalled during the first timed round. The watchdog
stopped that run. The final implementation retains managed browsers and model adapters
while using a small explicit action loop; it does not run the general-purpose Agent.
This follows the supported [Browser Use Cloud infrastructure path](https://docs.browser-use.com/cloud/quickstart),
which exposes managed browsers over CDP for direct Playwright control.

The pilot is an engineering check on one day's seven questions, not evidence of an
overall model ranking or a statistical uptime guarantee. Pin model versions/settings,
use matched questions across models, and report failed and timed-out runs in the denominator.
Krillion's curated accepted answers and game-awarded scores are authoritative for this
benchmark; a plausible rejected answer is recorded as a rejection, not independently graded.

## Data storage

The site is static: GitHub Pages serves `leaderboard-data.json` from this repository.
There is no application database. Published campaign manifests, sanitized reports,
and answer logs are versioned in Git alongside the code. The leaderboard download
exports the currently loaded public dataset; loading a file is local to the page.

Private runtime artifacts are written below the directory passed to `--output`
(default: `artifacts/`). These include event logs, screenshots, final page text,
model observations, usage records, and cloud session identifiers. `artifacts/` and
`.env` are ignored by Git. A checkout or output directory under `/tmp` is temporary
storage; preserve it in a durable private location before cleanup. Browser Use also
hosts cloud recordings; their retention is separate from this repository and has
not been verified. Do not rely on cloud recording retention as the only archive.
