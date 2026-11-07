# Validation — November 7, 2026

This is a working pilot, not a proven uptime guarantee. Tests used the live Daily
Dive starting at https://krillion.io/. Every cloud run used a fresh managed browser.
The initial pilot model runs used `groq:openai/gpt-oss-120b` through the configured OpenAI-compatible
endpoint, requested low reasoning, and DOM observations without screenshots.
Control answers were available only to the scripted baseline.

## Sequential checks

| Check | Evidence | Result |
|---|---|---|
| Local browser startup | `artifacts/local-smoke-1` | Passed |
| Cloud browser startup | `artifacts/cloud-smoke-1` | Passed |
| Real controls with fixed answers | `artifacts/cloud-baseline-5` | 7/7 accepted; verified 205 points |
| Slim-loop model pilot | `artifacts/cloud-model-3` | 7/7 accepted; screenshot confirms 440 points |
| Direct-connection model repeat | `artifacts/cloud-model-4` | Failed in round 5 after repeated rejected song titles |
| Final model repeat | `artifacts/cloud-model-5` | Deadline guard stopped round 5 after five rejected submissions; four accepted rounds |
| Strengthened verifier control | `artifacts/cloud-baseline-6` | 7/7 accepted, 205 points; verifier rejected uppercase COPY RESULT |
| Final corrected control | `artifacts/cloud-baseline-7` | Passed: 7/7 accepted, unique round entries and total of 205 verified |

The control run's longest observed question-to-form-close time was **4.85 seconds**.
The final corrected control run's longest was **4.79 seconds**. It exercised the
shipped code, including disabled-input and uppercase-scorecard guards.
The successful model pilot's longest was **12.53 seconds**, with model-call median
**1.72 seconds** and nearest-rank p95 **2.84 seconds**. This includes retried game
answers when measuring each round, but inference latency is measured separately.
Times start at the first observation of the active form and include network/browser
overhead; they are not measurements from an internal game clock. Form closure alone
is not treated as acceptance: the result and final scorecard are also checked.

`cloud-model-3` predates the final direct connection and stronger scoreboard verifier.
Its report did not parse the final total; 440 is supported by its final screenshot
and seven recorded point values. It must not be presented as a final-version pass.

The final model repeat had 20 calls: median **1.13 seconds**, nearest-rank p95
**2.03 seconds**. Its first four rounds were accepted in at most **5.12 seconds**
from first observation; repeated rejected answers exhausted round 5's budget.
The three slim-loop model pilots completed one full game out of three, across
evolving implementations. This is not a stable-version success-rate estimate, and
the two failures are not excluded. No live completion claim is made for the final
model configuration.

The initial release suite passed **25 tests in 4.74 seconds**, including real
Chromium integration tests. It checks complete seven-round flow, rejected-answer
recovery, temporarily disabled input, deadline enforcement, stale actions, allowed
controls, premature completion, duplicate scorecard rounds, and mismatched totals.

## Failures retained and corrected

- The general Browser Use Agent stalled processing the page during the first timed
  round (`cloud-model-1`). Replaced it with the small action loop while retaining
  Browser Use's cloud browser and model adapters.
- Early baseline runs and `cloud-model-2` exposed continuously animated buttons.
  Waiting for click stability timed out, and forced coordinate clicks could miss.
  Model click actions now activate the exact observed button with keyboard Enter.
- `cloud-baseline-4` accepted every answer but failed final verification because the
  round entries use HTML `title`, not `aria-label`. Corrected the observed selector;
  `cloud-baseline-5` passed.
- `cloud-model-4` made fast calls (median 1.17 seconds, p95 1.95 seconds) but exhausted
  its round budget after seven rejected song answers. It remains a failed benchmark
  attempt. Round-budget expiry during inference now has a specific deadline status
  instead of the earlier generic TimeoutError classification.
- Added guards for duplicate scorecard rounds, mismatched totals, and a temporarily
  disabled input resetting the deadline. Disabled visible input remains in the
  timed phase; browser action waits still consume the same budget.
- `cloud-baseline-6` exposed a case mismatch in the strengthened completion verifier:
  CSS renders the button as COPY RESULT while its accessible name is Copy result.
  Verification now compares that control case-insensitively. The Chromium test uses
  the same CSS transformation, and the baseline briefly waits for score animation.

Raw evidence is retained in ignored `artifacts/` directories: event logs, final
screenshots, rendered text, and Playwright traces. The portable source archive
excludes raw traces and credentials.

## Limits and next benchmark gate

The initial pilot used one configured endpoint; six additional models have now been
exercised through OpenRouter (see the campaign below). Direct Anthropic and Google
adapters are implemented but unverified. Vision input is also unverified. This
measures constrained DOM browser actions, not general desktop or screenshot-only
computer use. The initial pilot and historical top-100 campaign stopped an unsuccessful run.
The revised harness below continues missed questions to an observed final scorecard;
all interruptions and incomplete runs still remain in the results.

Do not rank models from this one day's questions or cherry-pick a successful retry.
Before publishing rankings, freeze the harness and model settings, run matched
questions across models over multiple days, and separately report completion rate,
game score, answer rejections, deadline failures, infrastructure failures, and latency.
Current prompts and selectors are coupled to the observed game UI and will fail
closed if that UI changes incompatibly.

## Release hygiene

The release contains only this standalone project. Credentials, local environments,
raw browser traces, and unrelated workspace files are excluded. Git ignores `.env`,
`.venv`, and artifacts; the local credential file has mode 600.


## OpenRouter campaign and report/recovery validation

All six original models played the actual game through Browser Use Cloud and the
published OpenAI-compatible adapter: GPT 6.1 Terra, Claude Haiku 5.5, Gemini 4 Argon,
DeepSeek V4.1 Flash, Llama 4 Maverick, and Llama 4 Scout. Five completed; Scout
stalled between rounds 2 and 3. No source changes were made during that campaign.
[OPENROUTER-REPORT.md](OPENROUTER-REPORT.md) contains every submitted answer, its
outcome and rarity, verified final totals, daily percentages, and separate follow-up
runs. Historic reports are derived from retained UI evidence; their original raw
reports and timing data are preserved.

The revised suite passes **44 tests**, including real Chromium tests. Added checks
cover result-vs-legend parsing, percentiles requiring verified scorecards, corrections
requiring confirmation, repeated rejected answers, uncertain keypresses, pre/post
remote submission timestamp races, Markdown escaping, and labeled scorecard rarity
fallbacks. Recovery tests replay Scout's invalid textbox fills and repeated waits,
verify the exact next-round control is activated, and prove no answer is supplied.
Strict mode, stale phases, ambiguous navigation, one-recovery-per-state limits, and
unchanged question deadlines are also checked.

In the live Scout regression, phase guidance got it beyond the old navigation stall
without assistance. It accepted four answers for **60 partial points**, then the
round-5 deadline stopped it after eight rejected song submissions. It has no final
daily percentage and remains a failed run. This validates navigation improvement in
one run; it does not establish overall Scout reliability or repair answer knowledge.

The Scout check preceded a reporting-only correction that gives submission events
separate run-relative and round-relative timestamps. Its gameplay and raw evidence
are retained. The Haiku follow-up uses the corrected submission timestamps. A later diagnostic-only
change ensures failed recovery attempts are logged too; its exception path and the
eight-recovery run limit are covered by the automated suite.

The Haiku report regression completed **7/7 rounds, 310/700 points**, with **66%**
shown by the game as its final daily percentage. It exercised correction feedback
and a rejected-answer retry. No navigation recovery was needed. Its final screenshot,
seven unique scorecard entries, and sum of points agree. This repeat is listed
separately from the original Haiku run (365 points, 85%).

## Frozen 100-model OpenRouter campaign

The November 7 campaign ran from 20:29:52 to 21:08:25 UTC with four concurrent
fresh Browser Use Cloud sessions. All 100 selected model variants were attempted
exactly once: **45 verified complete games and 55 incomplete runs**. Browser readiness
was observed for all 100. There was no daily-prompt mismatch or scheduling stop.
The frozen roster, settings, source hashes, and ranking provenance are in
[TOP100-MANIFEST.json](TOP100-MANIFEST.json) and [TOP100-RANKING.json](TOP100-RANKING.json).

Final audit matched all **642 submission events** to report entries: 453 accepted,
136 rejected, 50 requiring correction confirmation, and 3 unconfirmed. All completed
games had seven round entries whose points sum to the displayed total and a parsed
daily percentage. Every incomplete run had no final daily percentage; every
nonaccepted attempt had no attributed rarity. Source hashes matched the frozen
manifest after the campaign. Navigation recovery logged 35 attempts across 18 runs.

Failures were 17 output truncations, 17 round-deadline expiries, 15 timeouts,
5 provider errors, and 1 rate limit. Stack-frame review separates the timeouts into
12 model calls and 3 actions (two DIVE submissions and one wait near the deadline).
Provider error types are retained, but sanitized logs do not establish their
underlying HTTP/provider cause. The song question accounted for 120 of 136 rejected
attempts and 26 runs' fatal failures. A fatal error ends the run: later rounds are
unattempted, not additional failed answers. No failed run was retried or replaced.

The full prelaunch suite passed **47 tests in 7.25 seconds**, including four real
Chromium tests. A subsequent campaign concurrency/resume test brought the current
suite to 48 distinct tests; the four campaign tests passed together in 0.05 seconds.
They cover roster exclusions, catalog validation, incomplete-score handling,
bounded concurrency, and resume without retrying completed failures. Gameplay code
and settings were unchanged during the campaign.

[TOP100-REPORT.md](TOP100-REPORT.md) contains every answer, rarity, final daily
percentage, failure breakdown, and the completed-game results. Structured exports
are [TOP100-SUMMARY.json](TOP100-SUMMARY.json) and
[TOP100-ANSWERS.json](TOP100-ANSWERS.json). These are exploratory results on one
daily puzzle under this configuration; they are not a general model-quality ranking.
The live game's daily percentages can drift during the campaign. Raw traces and
credentials remain excluded from publication.

## Continuation and provider compatibility follow-up

The revised harness omits the OpenRouter output-token cap by default, replaces the
18-second inference cutoff with the remaining round budget, and continues after
missed questions to a verified final scorecard. The game clock and safety margin
remain unchanged. Same-model retries and a logged prompt-JSON compatibility fallback
are bounded by the original deadline; provider diagnostics retain sanitized causes.

The final suite passed **60 tests in 9.04 seconds**, including six real Chromium
tests. Five targeted live games completed: a deliberately missed scripted control,
Cohere North Mini, GPT-OSS20B, an intermediate Ling run, and a final-version Ling run.
Final Ling recovered from Novita's HTTP 400 structured-output rejection, missed one
question, and reached **250 points / better than 38%** with seven verified rounds.

[RECOVERY-REPORT.md](RECOVERY-REPORT.md) records the version boundaries, source hashes,
provider diagnosis limitations, all answers/rarities, and final daily percentages.
All scorecards, point totals, submission counts, and zero-point rarity handling were
audited; live-regression gameplay source hashes matched the pre-run snapshot. The newer
GitHub niche-answer prompt wording was merged afterward and the full suite rerun;
the live scores predate that wording-only merge. The old 100-model
results were not rerun or rewritten.
