# Validation — November 7, 2026

This is a working pilot, not a proven uptime guarantee. Tests used the live Daily
Dive starting at https://krillion.io/. Every cloud run used a fresh managed browser.
Model runs used `groq:openai/gpt-oss-120b` through the configured OpenAI-compatible
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

The final automated suite passed **25 tests in 4.74 seconds**, including real
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

Only one configured model endpoint has been exercised live. Anthropic and Google
adapters are implemented but unverified. Vision input is also unverified. This
measures constrained DOM browser actions, not general desktop or screenshot-only
computer use. The benchmark stops an unsuccessful run rather than continuing with
an automatically skipped question; failures must stay in the denominator.

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
