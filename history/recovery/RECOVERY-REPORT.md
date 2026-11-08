# Timeout recovery and provider compatibility validation

Validated November 7, 2026. These are targeted follow-up checks, **not a rerun of the
100-model campaign**. Historical TOP100 results remain unchanged.

## The six failure modes

1. **Output truncation:** the old 1,500-token request cap was imposed by this harness.
   OpenRouter/OpenAI-compatible requests now omit it by default. Configure it with
   `--max-output-tokens N` in either runner.py or campaign.py; omit the flag for no
   harness cap. Provider/model limits remain. Native Anthropic requires an explicit cap.
2. **Round deadline:** previously this aborted the game. Now the harness stops answering
   that question, observes the real expired-round result, and continues through the
   visible controls. Krillion displays NOTHING LANDED and awards zero. The report
   retains that miss and the actual final score/daily percentage. Permanent API errors,
   a stalled game, or whole-run limits can still leave a game incomplete.
3. **Inference timeouts:** 12 of the historical 15 TimeoutErrors happened during model
   calls. The old 18-second cutoff was ours, not evidence that a model stopped itself.
   Now calls and retries share the question's remaining clock budget. The unchanged
   safety reserve is 3 seconds plus 1 second for integer-timer rounding. Elapsed time
   alone cannot distinguish reasoning, provider queueing, or network delay.
4. **Action timeouts:** the other three occurred during two DIVE actions and one wait
   near the deadline. These were executor/deadline interruptions, not proof of a browser
   outage. Recovery observes whether a submission actually landed before continuing;
   a delayed acknowledgement must not turn an accepted answer into a miss or duplicate it.
5. **Provider errors:** new diagnostics preserve sanitized HTTP status, provider name,
   provider explanation, error category, limit source, and Retry-After when available.
   Compatible adapters can switch once from native structured output to prompt-only
   JSON, using the same model and the same locally validated action schema. Transient
   errors have at most two additional attempts by default (`--model-retries 2`), all
   bounded by the original question deadline. No second model chooses answers.
6. **Rate limits:** there is no harness requests-per-minute quota. Upstream limits cannot
   be disabled here. New campaigns can use `--paid-only` to explicitly exclude :free
   variants, with exclusions recorded; IDs are never silently replaced. Same-model
   backoff honors Retry-After and carries cooldown across rounds, waiting before the
   next question starts. This mitigates throttling without promising it cannot recur.

Outside questions, inference has a configurable `--navigation-timeout 60`. Bounded
navigation recovery remains logged and never fills answers or resets the game clock.
See [README.md](../../README.md) for commands and the complete timing contract.

## Provider diagnoses

The original five provider-error logs did not preserve sufficient underlying details
for retrospective root-cause proof. Fresh diagnostic requests replayed saved observations
without playing games. These establish current behavior, not certain historical causes:

| Model | Fresh evidence |
|---|---|
| anthropic/claude-sonnet-4.6 | Returned schema-valid actions; original failure not reproduced. |
| openai/gpt-oss-20b | Returned schema-valid actions; also completed a fresh live game below. |
| deepseek/deepseek-v4-flash-vision-exp | Returned schema-valid actions; original failure not reproduced. |
| cohere/north-mini-code:free | Some requests returned plain commands or empty content instead of valid JSON. A later live game completed. |
| inclusionai/ling-3.1-flash | Novita returned HTTP 400: structured outputs unsupported. The final live run recovered via prompt JSON. |
| xingchen-agi/xing4.0-29b-a4b:free | Intermittent success and HTTP 429 from Phala, identifying upstream_provider_shared_pool throttling. |

The observed Xing error was not an exhausted account free-request quota. Paid account
status alone does not remove a shared free-provider pool's restrictions. References:
[OpenRouter limits](https://openrouter.ai/docs/api_reference/limits) and
[error diagnostics](https://openrouter.ai/docs/api_reference/errors-and-debugging).

## Live checks and version boundaries

All five runs below reached verified seven-round scorecards. Daily percentage means
"better than X% of today's players" at capture time, not score divided by 700.

| Version / check | Score /700 | Daily percentage | Missed rounds |
|---|---:|---:|---:|
| Intermediate: scripted timeout control | 175 | 12% | 1 |
| Intermediate: cohere/north-mini-code:free | 120 | 2% | 2 |
| Intermediate: openai/gpt-oss-20b | 295 | 57% | 0 |
| Intermediate: inclusionai/ling-3.1-flash | 150 | 6% | 4 |
| Final: inclusionai/ling-3.1-flash | 250 | 38% | 1 |

The scripted control deliberately withheld the first answer until after the deadline,
then used six predefined control answers. It validates recovery, not LLM capability.
Cohere missed round 3 at the action deadline and round 5 at the inference deadline.
The first Ling run exposed ambiguous schema-wrapper instructions: it emitted extra
name/arguments fields, producing 11 model issues. The final version puts the actual
JSON schema directly in the common prompt and explicitly forbids those wrappers.
The four intermediate checks predate that prompt cleanup and a recovery-logging refactor.
Do not present them as runs of byte-identical final source.

The final Ling run recorded one provider issue (Novita HTTP 400) and one same-model
prompt-JSON switch at the initial page. No further model/API issues were recorded.
It missed round 5 at the inference deadline, then completed rounds 6 and 7 and the
final scorecard. One successful run does not prove universal provider compatibility.

## Validation

The final full suite passed **60 tests in 9.04 seconds**, including six real Chromium
checks, after merging the niche-answer wording. An initial rerun omitted the configured
Chrome path and had six setup errors; rerunning with the documented
KRILLION_TEST_CHROME setting passed. Coverage includes inference cancellation followed by a real zero and final
score, a submission accepted before its delayed acknowledgement, stale-action guards,
provider diagnostics/redaction, cap omission on the wire, schema fallback, bounded
retries, Retry-After without extending question time, paid-only selection, and reporting.

An independent artifact audit verified seven unique scoreboard entries per live run,
round-point sums equal to final totals, submission-event/report counts, no answer or
rarity fabricated for zero-point rounds, and no rarity assigned to nonaccepted attempts.
Live-regression source hashes matched the pre-run snapshot after the game.
Before publication, the newer GitHub commit 3f2a9da was discovered and its two-line
niche-answer objective was preserved in the common prompt. The live runs therefore
precede that final wording merge; no gameplay logic changed during the merge.
Raw traces, credentials, authenticated browser URLs, and private account details are
excluded. Every recorded submission and rarity from the five checks follows below.

## Source snapshots

Hashes identify the gameplay source used in each check; the earlier snapshot also
includes other files frozen by the regression driver.

### Intermediate

```json
{
  "runner.py": "6b638b763f2ab74d304731eb2442bea518724cfb3711bfcd2810f84c616f329a",
  "player.py": "796a17f39f7280ddbe1d34f7dcb3201c122641e7d05f3a610b2a9233c4ce6d7b",
  "reporting.py": "3a806aa9af76f7bd7a4572c86c6157131cc007b532813c6cc9511628ec12f05e",
  "model_policy.py": "ac6a12b046aac96748cdf0d8c4e33b0a4163c663c7bb6d05282047e26ee422bb"
}
```

### Final live regression (before merging the niche-answer wording)

```json
{
  "runner.py": "72acd9d32697fb719b828fb0b6b3441b22f450ca5f5bf430e15d0285e6e61e26",
  "player.py": "ec014a252cd8d19531eb184d676fd04f5ad493449512872e364fffc6b0ada4a8",
  "deadline.py": "11b1ccde407205c18883d2cc35b6e2d7b648134be4b3db08afe05f1290e1c369",
  "reporting.py": "3a806aa9af76f7bd7a4572c86c6157131cc007b532813c6cc9511628ec12f05e",
  "model_policy.py": "ac6a12b046aac96748cdf0d8c4e33b0a4163c663c7bb6d05282047e26ee422bb"
}
```


---

## Intermediate scripted control

# Krillion run: scripted-timeout-control

Status: **agent_finished**. Score: **175/700**.

Final daily percentage: **better than 12% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: round_inference_deadline.

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 25 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 25 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | running | accepted | Plankton | 10 | 25 |

Round result: Running · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra | accepted | Schooler | 30 | 25 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | ketchup | accepted | Plankton | 10 | 25 |

Round result: Ketchup · Plankton · 10 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 25 |

Round result: Booking.com · Plankton · 10 points (source: displayed_result).


---

## Intermediate Cohere

# Krillion run: cohere/north-mini-code:free

Status: **agent_finished**. Score: **120/700**.

Final daily percentage: **better than 2% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Calzone | accepted | Schooler | 30 | 22 |

Round result: Calzone · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Family Guy | accepted | Plankton | 10 | 18 |

Round result: Family Guy · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: round_action_deadline.

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Running | accepted | Plankton | 10 | 22 |

Round result: Running · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: round_inference_deadline.

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | gochujang | accepted | Rare | 60 | 19 |

Round result: Gochujang · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 21 |

Round result: Booking.com · Plankton · 10 points (source: displayed_result).


---

## Intermediate GPT-OSS

# Krillion run: openai/gpt-oss-20b

Status: **agent_finished**. Score: **295/700**.

Final daily percentage: **better than 57% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 23 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Poland | accepted | Schooler | 30 | 24 |

Round result: Poland · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Plyometric jump squats | rejected | — | — | 24 |
| 2 | Bear crawl | accepted | Rare | 60 | 22 |

Round result: Bear crawl · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Siren | rejected | — | — | 22 |
| 2 | Horizon | rejected | — | — | 17 |
| 3 | Echoes | accepted | Deep Cut | 85 | 12 |

Round result: Echoes · Deep Cut · 85 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Salsa de chipotle | confirmation_required → Chipotle salsa | — | — | 23 |
| 2 | Barbecue sauce | confirmation_required → BBQ sauce | — | — | 18 |
| 3 | BBQ sauce | accepted | Schooler | 30 | 12 |

Round result: BBQ sauce · Schooler · 30 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Kayak | accepted | Schooler | 30 | 24 |

Round result: Kayak · Schooler · 30 points (source: displayed_result).


---

## Intermediate Ling

# Krillion run: inclusionai/ling-3.1-flash

Status: **agent_finished**. Score: **150/700**.

Final daily percentage: **better than 6% of today’s players**.

Navigation recovery: bounded; successful assistance: 7.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: invalid_model_output.

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: invalid_model_output.

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Paraguay | accepted | Rare | 60 | 13 |

Round result: Paraguay · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 14 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: round_inference_deadline.

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 17 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: invalid_model_output.

## Navigation recovery log

- 10.43s: ▼ BEGIN DESCENT ▼ — ok (invalid_model_output).
- 41.94s: DESCEND ▼ — ok (invalid_model_output).
- 73.39s: DESCEND ▼ — ok (invalid_model_output).
- 96.68s: DESCEND ▼ — ok (invalid_model_output).
- 117.10s: DESCEND ▼ — ok (invalid_model_output).
- 148.53s: DESCEND ▼ — ok (invalid_model_output).
- 168.45s: DESCEND ▼ — ok (invalid_model_output).

## Model/API diagnostics

| Round | Category | HTTP status | Provider | Detail |
|---|---|---:|---|---|
| SURFACE | invalid_request | 400 | Novita | {&quot;code&quot;:400,&quot;reason&quot;:&quot;INVALID_REQUEST_BODY&quot;,&quot;message&quot;:&quot;model features structured outputs not support&quot;,&quot;metadata&quot;:{}} |
| SURFACE | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |
| PROMPT 1 OF 7 | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |
| PROMPT 2 OF 7 | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |
| PROMPT 2 OF 7 | invalid_model_output | — | — | 3 validation errors for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] arguments   Extra inputs are not permitted [type=extra_forbidden, input_value={&#x27;actions&#x27;: [{&#x27;kind&#x27;: &#x27;fi...&#x27;: &#x27;DIVE&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}, input_type=dict]     For further information visit [url] actions   Field required [type=missing, input_value={&#x27;name&#x27;: &#x27;agent_output&#x27;, ...: &#x27;DIVE&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}}, input_type=dict]     For further information visit [url] |
| PROMPT 3 OF 7 | invalid_model_output | — | — | 3 validation errors for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] arguments   Extra inputs are not permitted [type=extra_forbidden, input_value={&#x27;actions&#x27;: [{&#x27;kind&#x27;: &#x27;cl...CEND ▼&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}, input_type=dict]     For further information visit [url] actions   Field required [type=missing, input_value={&#x27;name&#x27;: &#x27;agent_output&#x27;, ...END ▼&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}}, input_type=dict]     For further information visit [url] |
| PROMPT 4 OF 7 | invalid_model_output | — | — | 3 validation errors for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] content   Extra inputs are not permitted [type=extra_forbidden, input_value={&#x27;actions&#x27;: [{&#x27;kind&#x27;: &#x27;cl...CEND ▼&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}, input_type=dict]     For further information visit [url] actions   Field required [type=missing, input_value={&#x27;name&#x27;: &#x27;agent_output&#x27;, ...END ▼&#x27;, &#x27;text&#x27;: &#x27;&#x27;}]}}, input_type=dict]     For further information visit [url] |
| PROMPT 5 OF 7 | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |
| PROMPT 6 OF 7 | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |
| PROMPT 7 OF 7 | invalid_model_output | — | — | 2 validation errors for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] schema   Extra inputs are not permitted [type=extra_forbidden, input_value={&#x27;type&#x27;: &#x27;object&#x27;, &#x27;prope...ionalProperties&#x27;: False}, input_type=dict]     For further information visit [url] |
| PROMPT 7 OF 7 | invalid_model_output | — | — | 1 validation error for Turn name   Extra inputs are not permitted [type=extra_forbidden, input_value=&#x27;agent_output&#x27;, input_type=str]     For further information visit [url] |

## Output compatibility changes

- SURFACE: prompt_json; same model and validated action schema retained (invalid_request).


---

## Final Ling

# Krillion run: inclusionai/ling-3.1-flash

Status: **agent_finished**. Score: **250/700**.

Final daily percentage: **better than 38% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 19 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | F Is for Family | accepted | Rare | 60 | 14 |

Round result: F Is for Family · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Spain | accepted | Plankton | 10 | 17 |

Round result: Spain · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 22 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

Round result: — · — · 0 points (source: verified_scorecard_timeout).

Round missed: the game awarded 0 points. Continued to the next round.

Round interruptions: round_inference_deadline.

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 18 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).

## Model/API diagnostics

| Round | Category | HTTP status | Provider | Detail |
|---|---|---:|---|---|
| SURFACE | invalid_request | 400 | Novita | {&quot;code&quot;:400,&quot;reason&quot;:&quot;INVALID_REQUEST_BODY&quot;,&quot;message&quot;:&quot;model features structured outputs not support&quot;,&quot;metadata&quot;:{}} |

## Output compatibility changes

- SURFACE: prompt_json; same model and validated action schema retained (invalid_request).

