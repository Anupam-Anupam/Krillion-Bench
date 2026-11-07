# Krillion Benchmark

A small browser-action harness for an LLM to play the complete Daily Dive from
**https://krillion.io/**. Browser Use Cloud hosts a fresh browser; Playwright executes
the model's actions. Browser Use's model adapters support provider APIs and compatible
endpoints. It runs as a standalone Python project with no database or job queue.

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

The 100-model OpenRouter campaign uses `campaign.py`. It freezes an observed ranking,
API catalog, source hashes, and settings before launching one fresh browser per model.
See [TOP100-REPORT.md](TOP100-REPORT.md) for the campaign results, failure breakdown,
and every submitted answer. Machine-readable results are in
[TOP100-SUMMARY.json](TOP100-SUMMARY.json) and [TOP100-ANSWERS.json](TOP100-ANSWERS.json).

```sh
uv run runner.py smoke --env-file .env
uv run runner.py play --env-file .env
```

Change models without changing the agent:

```sh
uv run runner.py play --env-file .env --provider openai --model YOUR_MODEL
uv run runner.py play --env-file .env --provider anthropic --model YOUR_MODEL
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
Free and paid variants remain separate. Unknown IDs, duplicates, and an undersized roster
fail selection. Unsupported structured-output models are attempted and retained as failures;
they are not silently removed from the denominator or replaced.

The output contains a frozen `manifest.json`, atomic `state.json`, `summary.json`, combined
`REPORT.md`, and each model's normal answer reports and browser artifacts. The same command
resumes pending models without rerunning finished attempts, provided source hashes and
concurrency still match. A live/stale lock or interrupted running entry requires investigation
before resuming. Scheduling stops at a UTC date change or mismatching daily prompts. Runs
already active at detection finish and retain their actual prompt evidence. A hard outer timeout
can prevent browser cleanup; the cloud session's 15-minute lease still bounds its lifetime.

Campaigns measure this complete timed model-and-harness configuration. A reasoning model may
consume its 1,500-token budget before emitting actions. Schema incompatibility, provider errors,
timeouts, and navigation failures are meaningful separate failure modes, not zero game scores.
One daily puzzle per model is an exploratory comparison, not a statistically stable quality ranking.

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
attempts per run. It never fills a textbox, submits an answer, resets the timer,
retries model calls, or substitutes another model. Empty transition screens have a
15-second wait limit; the whole run remains bounded too.

Use `--navigation-recovery off` for the strict navigation track. Both tracks have
phase guidance. Reports preserve the selected mode, every recovery attempt, and
whether assistance actually executed. Do not pool these tracks or mix them with
older full-page-text observations in a model ranking.

## Timing and failure contract

- The independent watchdog reads the visible countdown and uses monotonic time.
  It reserves `--margin` seconds (default 3), plus one second for integer rounding.
  Repeated or frozen timer readings cannot extend a round's deadline.
- Each model call is bounded by the smaller of 18 seconds and the remaining budget.
  Retries and cross-model fallback are disabled in the adapters.
- Each action rechecks the round/phase and deadline. A stale action batch is discarded.
  Once a run stops, no new actions can execute. The game does not advance to the next
  question automatically; DESCEND is activated by the model or logged bounded recovery.
- Rejected answers may be retried within the same countdown. Rejection does not create
  a fresh budget. The input remaining open is not treated as successful submission.
- A missed harness deadline stops the run and produces a nonzero exit code. It does
  not silently skip the question, substitute another model, or fabricate an answer.
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
SDK exceptions can contain authenticated browser URLs. Failed screenshot/trace collection
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
