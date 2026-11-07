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
OpenAI-compatible endpoint has been exercised in the live pilot. Provider/model
support for structured output must be validated before a model joins the benchmark.

## What the model controls

The model starts on the initial game page and chooses every start, next-round,
answer-entry, submit, and final-results action. Its common action schema contains:

- `click`: activate an observed game button by exact visible name. The executor uses
  keyboard Enter on the button because Krillion animates button positions.
- `fill`: type into the observed `Your answer` textbox.
- `wait`: wait one second, still charged to the active deadline.
- `done`: accepted only after seven observed rounds and the rendered final scorecard.

Observations contain rendered text, visible controls, the current prompt, the visible
timer, and the current input value. No JavaScript execution, network inspection,
answer-bank access, external search, filesystem tools, or second model is exposed to
the evaluated LLM. The harness waits through previews and animations before inference.
It does not pause, reset, or extend the game's timer.

This is a **constrained browser-agent benchmark**, not unrestricted computer use.
The harness knows how to observe Krillion's UI and limits actions to game controls;
the model must choose its own answers and actions. `--vision` adds screenshots to
the same DOM observations and must be reported as a separate evaluation setting.
It is not a screenshot-only track.

## Timing and failure contract

- The independent watchdog reads the visible countdown and uses monotonic time.
  It reserves `--margin` seconds (default 3), plus one second for integer rounding.
  Repeated or frozen timer readings cannot extend a round's deadline.
- Each model call is bounded by the smaller of 18 seconds and the remaining budget.
  Retries and cross-model fallback are disabled in the adapters.
- Each action rechecks the round/phase and deadline. A stale action batch is discarded.
  Once a run stops, no new actions can execute. The game does not advance to the next
  question automatically; the model must activate DESCEND.
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
| `report.json` | Status, model, per-round submissions/results, model-call durations, final scorecard |
| `events.jsonl` | Observations, actions, model responses/usage, timings, and sanitized failure locations |
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
