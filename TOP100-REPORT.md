# OpenRouter top 100: Krillion campaign

Finished: **100/100**. Verified full games: **45**.

## Campaign results

All **100 model variants** were attempted once. **45** reached verified seven-round scorecards; **55** did not. **642 submitted answer attempts** are preserved below, including rejections and spelling confirmations.

| Model | Score /700 | Better than today’s players |
|---|---:|---:|
| moonshotai/kimi-k3.1-pro | 445 | 97% |
| openai/gpt-6-astra | 420 | 95% |
| openai/gpt-6-sol | 420 | 95% |
| x-ai/grok-4.7 | 420 | 95% |
| openai/gpt-6.1-terra | 415 | 94% |
| google/gemini-3.6-flash | 390 | 90% |
| meta/muse-spark-1.3-contributor | 385 | 88% |
| openai/gpt-5.6-luna-pro | 385 | 88% |
| z-ai/glm-5.3-flash | 370 | 86% |
| openai/gpt-6-luna | 365 | 85% |

### Failures and recovery

| Failure mode | Runs | Interpretation |
|---|---:|---|
| DeadlineExceeded | 17 | The round watchdog exhausted the safe action budget within the game's 25-second clock. |
| ModelOutputTruncatedError | 17 | The 1,500-token completion budget ended before usable actions were returned. Reasoning can consume this budget. |
| ModelProviderError | 5 | The model adapter reported a provider error; sanitized logs do not establish its underlying cause. |
| ModelRateLimitError | 1 | The model adapter reported rate limiting. |
| TimeoutError | 15 | An inference or action timeout expired; see the stage breakdown below. |

Timeout stages from saved stack frames: action_execution: 3, model_call: 12. Model calls have an 18-second cap or the remaining round budget. Browser actions have their own cap bounded by that same round budget; an action timeout is not automatically an inference failure or a browser outage.

A fatal model or deadline error stops the entire run. Later questions are **unattempted**, not additional failed rounds. Partial points remain visible but are never presented as a final score or daily percentage.

Answer-attempt outcomes: accepted: 453, confirmation_required: 50, rejected: 136, unconfirmed: 3. Rejected answers and correction confirmations can recover within the original countdown; neither automatically means a failed game.

| Prompt | Rejected attempts |
|---|---:|
| Name a song released in 2025 or 2026 with over 10 million Spotify streams. | 120 |
| Name a country bigger than the UK but smaller than Egypt, by area. | 13 |
| Name a red sauce, dip or condiment. | 1 |
| Name a cardio exercise. | 1 |
| Name a food with a filling inside. | 1 |

| State at fatal failure | Runs |
|---|---:|
| answering / PROMPT 5 OF 7 | 26 |
| start / SURFACE | 8 |
| answering / PROMPT 1 OF 7 | 6 |
| answering / PROMPT 3 OF 7 | 4 |
| answering / PROMPT 4 OF 7 | 4 |
| between_rounds / PROMPT 3 OF 7 | 3 |
| between_rounds / PROMPT 2 OF 7 | 2 |
| answering / PROMPT 2 OF 7 | 1 |
| between_rounds / PROMPT 6 OF 7 | 1 |

Browser readiness was observed in 100/100 attempts. Bounded navigation recovery logged 35 attempts across 18 runs. It only advances visible navigation controls and never chooses an answer.

Read these as results for this timed harness configuration, not a general intelligence ranking. Models that fail the deadline or exhaust the output budget have no final score or percentile. There is one run per variant on one daily puzzle; free and paid endpoints are separate variants. No failed run was retried or replaced.

Follow-up evaluation should separately test a larger output budget, deterministic navigation, and continuing after a missed round with an explicit zero/missed result. Those changes would define a new configuration; none was introduced during this campaign.

Selection: active text model variants in OpenRouter’s **Top Weekly** directory order, excluding latest aliases, automatic routers, and asynchronous batch variants. Free and paid variants are separate entries. This is usage selection, not a quality ranking.

[OpenRouter source](https://openrouter.ai/models?fmt=cards&output_modalities=text&order=top-weekly); captured 2026-11-07T20:28:00.407Z. Ranking attribution: OpenRouter, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Directory token counts are a live seven-day window and differ from the rankings page’s completed-day buckets.

One fresh Browser Use Cloud browser per model; DOM observations; bounded navigation recovery; 25-second game clock; 18-second maximum model call; 3-second safety margin plus timer rounding; 1,500 maximum output tokens; requested low reasoning; schema-validated actions; no model retries, answer fallback, or replacement of failed entries. Unsupported provider settings remain recorded failures.

Concurrency: 4. Frozen harness hashes and roster: [TOP100-MANIFEST.json](TOP100-MANIFEST.json). The daily percentage is the game’s live ‘better than’ comparison, not score divided by 700. Percentiles may drift as other people play. Partial scores are not ranked with completed games.

| Usage rank | Model | Status | Score /700 | Partial points | Daily % | Rounds scored | Calls | Median call s | Recovery attempts |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | deepseek/deepseek-v4.1-flash-1017 | agent_finished | 280 | — | 52.0 | 7 | 16 | 0.764 | 0 |
| 2 | deepseek/deepseek-v4.1-flash | failed | — | 0 | — | 0 | 2 | 3.258 | 0 |
| 3 | z-ai/glm-5.3-flash | agent_finished | 370 | — | 86.0 | 7 | 18 | 0.946 | 0 |
| 4 | tencent/hy4 | failed | — | 0 | — | 0 | 1 | 17.042 | 0 |
| 5 | openai/gpt-6-luna | agent_finished | 365 | — | 85.0 | 7 | 20 | 1.741 | 0 |
| 6 | stepfun/step-5-preview | agent_finished | 295 | — | 57.0 | 7 | 16 | 2.268 | 0 |
| 7 | anthropic/claude-opus-5.5 | agent_finished | 355 | — | 80.0 | 7 | 15 | 2.208 | 0 |
| 8 | minimax/minimax-m3.1-flash | failed | — | 80 | — | 4 | 10 | 0.565 | 0 |
| 9 | tencent/hy4-preview | failed | — | 0 | — | 0 | 2 | 12.116 | 0 |
| 10 | openai/gpt-6.1-sol | agent_finished | 355 | — | 80.0 | 7 | 15 | 1.536 | 0 |
| 11 | openai/gpt-5.6-luna | agent_finished | 340 | — | 78.0 | 7 | 16 | 1.61 | 0 |
| 12 | moonshotai/kimi-k3.1-pro | agent_finished | 445 | — | 97.0 | 7 | 17 | 1.565 | 0 |
| 13 | z-ai/glm-5.3 | agent_finished | 340 | — | 78.0 | 7 | 21 | 1.231 | 0 |
| 14 | deepseek/deepseek-v4-flash-0731 | agent_finished | 295 | — | 57.0 | 7 | 16 | 1.023 | 0 |
| 15 | nvidia/nemotron-3-ultra-550b-a55b:free | failed | — | 90 | — | 3 | 8 | 3.532 | 0 |
| 16 | stealth/crouton-alpha | failed | — | 90 | — | 2 | 5 | 5.099 | 0 |
| 17 | nvidia/nemotron-3.5-super-vl:free | failed | — | 180 | — | 4 | 12 | 1.599 | 1 |
| 18 | tencent/hy3 | deadline_exceeded | — | 205 | — | 3 | 10 | 4.932 | 0 |
| 19 | meta/muse-spark-1.3-contributor | agent_finished | 385 | — | 88.0 | 7 | 15 | 3.987 | 0 |
| 20 | anthropic/claude-haiku-5.5 | agent_finished | 335 | — | 76.0 | 7 | 16 | 0.915 | 0 |
| 21 | xiaomi/mimo-v2.6-flash | failed | — | 0 | — | 0 | 1 | 15.991 | 0 |
| 22 | deepseek/deepseek-v4-flash | deadline_exceeded | — | 60 | — | 4 | 12 | 2.91 | 0 |
| 23 | anthropic/claude-sonnet-5.5 | agent_finished | 250 | — | 38.0 | 7 | 16 | 1.565 | 0 |
| 24 | moonshotai/kimi-k3 | agent_finished | 300 | — | 60.0 | 7 | 17 | 1.311 | 0 |
| 25 | google/gemini-3.8-flash | agent_finished | 300 | — | 60.0 | 7 | 15 | 3.506 | 0 |
| 26 | upstage/solar-mini4 | deadline_exceeded | — | 0 | — | 0 | 7 | 1.789 | 1 |
| 27 | google/gemini-4-argon | agent_finished | 355 | — | 80.0 | 7 | 18 | 3.5 | 2 |
| 28 | nvidia/nemotron-3.5-lightning:free | failed | — | 0 | — | 0 | 1 | 10.477 | 0 |
| 29 | xiaomi/mimo-v2.6-pro | failed | — | 235 | — | 4 | 11 | 3.324 | 0 |
| 30 | openai/gpt-6.1-terra | agent_finished | 415 | — | 94.0 | 7 | 17 | 1.623 | 0 |
| 31 | z-ai/glm-5.2 | agent_finished | 270 | — | 46.0 | 7 | 16 | 0.85 | 0 |
| 32 | nvidia/nemotron-3.5-super-vl | agent_finished | 280 | — | 52.0 | 7 | 23 | 1.486 | 4 |
| 33 | deepseek/deepseek-v4-pro-0813 | failed | — | 120 | — | 4 | 14 | 0.867 | 1 |
| 34 | qwen/qwen3.8-flash | failed | — | 240 | — | 4 | 11 | 7.342 | 0 |
| 35 | dots-studio/dots-3-note-preview:free | failed | — | 100 | — | 4 | 11 | 3.398 | 0 |
| 36 | qwen/qwen3.8-27b | agent_finished | 300 | — | 60.0 | 7 | 16 | 1.89 | 0 |
| 37 | minimax/minimax-m3 | agent_finished | 130 | — | 3.0 | 7 | 22 | 0.45 | 1 |
| 38 | google/gemini-3-flash-preview | failed | — | 210 | — | 4 | 15 | 1.025 | 0 |
| 39 | openai/gpt-6-luna-pro | deadline_exceeded | — | 265 | — | 4 | 13 | 4.015 | 0 |
| 40 | deepseek/deepseek-v4-pro | failed | — | 80 | — | 4 | 11 | 3.823 | 0 |
| 41 | google/gemini-3.1-flash-lite | agent_finished | 270 | — | 46.0 | 7 | 22 | 0.91 | 0 |
| 42 | anthropic/claude-sonnet-5 | agent_finished | 275 | — | 50.0 | 7 | 15 | 1.407 | 0 |
| 43 | google/gemma-4-31b-it | deadline_exceeded | — | 120 | — | 4 | 24 | 0.917 | 5 |
| 44 | qwen/qwen3.7-flash | deadline_exceeded | — | 40 | — | 2 | 7 | 3.42 | 0 |
| 45 | upstage/solar-pro4 | deadline_exceeded | — | 130 | — | 4 | 18 | 1.586 | 1 |
| 46 | google/gemma-4-26b-a4b-it | deadline_exceeded | — | 80 | — | 4 | 23 | 0.634 | 0 |
| 47 | google/gemini-3.7-flash | agent_finished | 330 | — | 73.0 | 7 | 17 | 2.605 | 0 |
| 48 | openai/gpt-6-astra | agent_finished | 420 | — | 95.0 | 7 | 16 | 2.403 | 0 |
| 49 | openai/gpt-oss-120b | deadline_exceeded | — | 180 | — | 4 | 17 | 1.055 | 0 |
| 50 | stepfun/step-3.7-flash | failed | — | 40 | — | 2 | 7 | 6.024 | 1 |
| 51 | openai/gpt-5.6-sol | agent_finished | 360 | — | 83.0 | 7 | 16 | 1.93 | 0 |
| 52 | mistralai/mistral-nemo | deadline_exceeded | — | 130 | — | 4 | 13 | 3.846 | 0 |
| 53 | google/gemini-2.5-flash-lite | failed | — | 0 | — | 0 | 1 | 3.146 | 0 |
| 54 | deepseek/deepseek-v3.2 | deadline_exceeded | — | 60 | — | 4 | 17 | 1.677 | 0 |
| 55 | anthropic/claude-fable-5.1 | agent_finished | 355 | — | 80.0 | 7 | 15 | 3.16 | 0 |
| 56 | qwen/qwen3.6-35b-a3b | failed | — | 30 | — | 1 | 5 | 3.611 | 1 |
| 57 | google/gemini-2.5-flash | failed | — | 60 | — | 2 | 6 | 0.614 | 0 |
| 58 | google/gemini-3.5-flash-lite | agent_finished | 220 | — | 25.0 | 7 | 21 | 0.897 | 1 |
| 59 | openai/gpt-6-sol | agent_finished | 420 | — | 95.0 | 7 | 15 | 1.415 | 0 |
| 60 | x-ai/grok-4.7 | agent_finished | 420 | — | 95.0 | 7 | 15 | 2.957 | 0 |
| 61 | anthropic/claude-opus-5 | agent_finished | 275 | — | 50.0 | 7 | 16 | 1.617 | 0 |
| 62 | openai/gpt-4o-mini | failed | — | 100 | — | 4 | 23 | 0.804 | 3 |
| 63 | anthropic/claude-sonnet-4.6 | failed | — | 120 | — | 5 | 17 | 1.496 | 0 |
| 64 | cohere/north-mini-code:free | failed | — | 0 | — | 0 | 1 | 2.535 | 0 |
| 65 | anthropic/claude-opus-4.8 | agent_finished | 200 | — | 18.0 | 7 | 18 | 1.483 | 0 |
| 66 | openai/gpt-5.6-terra | agent_finished | 325 | — | 70.0 | 7 | 16 | 1.306 | 0 |
| 67 | qwen/qwen3.8-max-0902 | failed | — | 90 | — | 3 | 8 | 10.367 | 0 |
| 68 | openai/gpt-oss-20b | failed | — | 50 | — | 3 | 8 | 1.808 | 0 |
| 69 | anthropic/claude-sonnet-4.5 | deadline_exceeded | — | 120 | — | 4 | 17 | 1.635 | 0 |
| 70 | anthropic/claude-haiku-4.5 | deadline_exceeded | — | 120 | — | 4 | 22 | 1.044 | 2 |
| 71 | mistralai/mistral-large-4-0 | agent_finished | 270 | — | 46.0 | 7 | 15 | 3.891 | 0 |
| 72 | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | failed | — | 0 | — | 0 | 2 | 8.118 | 0 |
| 73 | moonshotai/kimi-k2.6 | failed | — | 0 | — | 0 | 2 | 10.033 | 0 |
| 74 | particle-ai/particle-1 | agent_finished | 355 | — | 80.0 | 7 | 15 | 0.682 | 0 |
| 75 | qwen/qwen3.5-9b | failed | — | 30 | — | 1 | 4 | 4.93 | 1 |
| 76 | meta/muse-spark-open | agent_finished | 355 | — | 80.0 | 7 | 17 | 1.659 | 0 |
| 77 | inclusionai/ling-3.0-flash | failed | — | 0 | — | 0 | 1 | 18.001 | 0 |
| 78 | meta/muse-spark-1.3 | failed | — | 205 | — | 4 | 11 | 3.375 | 0 |
| 79 | z-ai/glm-5.3-flashx | agent_finished | 280 | — | 52.0 | 7 | 16 | 1.874 | 0 |
| 80 | xingchen-agi/xing4.0-29b-a4b:free | failed | — | 0 | — | 0 | 1 | 0.647 | 0 |
| 81 | meta/muse-wonder | agent_finished | 335 | — | 76.0 | 7 | 15 | 3.161 | 0 |
| 82 | google/gemini-3.6-flash | agent_finished | 390 | — | 90.0 | 7 | 18 | 1.837 | 0 |
| 83 | google/gemini-3.1-flash-lite-preview | agent_finished | 270 | — | 47.0 | 7 | 23 | 0.849 | 1 |
| 84 | anthropic/claude-opus-4.6 | agent_finished | 300 | — | 60.0 | 7 | 21 | 2.546 | 0 |
| 85 | reflection/beam-1.0-501b-a23b | agent_finished | 305 | — | 63.0 | 7 | 16 | 0.921 | 0 |
| 86 | google/gemini-3.1-pro-preview | deadline_exceeded | — | 150 | — | 4 | 11 | 4.943 | 0 |
| 87 | openai/gpt-5-mini | failed | — | 60 | — | 1 | 4 | 2.431 | 1 |
| 88 | openai/gpt-4.1-mini | deadline_exceeded | — | 135 | — | 4 | 24 | 1.273 | 4 |
| 89 | openai/gpt-5.4-nano | deadline_exceeded | — | 100 | — | 4 | 18 | 1.674 | 4 |
| 90 | openai/gpt-5.6-luna-pro | agent_finished | 385 | — | 88.0 | 7 | 15 | 3.208 | 0 |
| 91 | openai/gpt-5.4-mini | agent_finished | 270 | — | 47.0 | 7 | 18 | 1.357 | 0 |
| 92 | recursive/flint-v1.0:free | failed | — | 180 | — | 4 | 14 | 2.915 | 0 |
| 93 | x-ai/grok-4.5 | failed | — | 60 | — | 2 | 6 | 5.077 | 0 |
| 94 | inception/mercury-3 | failed | — | 0 | — | 0 | 3 | 1.027 | 0 |
| 95 | qwen/qwen3.7-plus | failed | — | 150 | — | 4 | 10 | 5.533 | 0 |
| 96 | openai/gpt-5.4 | agent_finished | 335 | — | 76.0 | 7 | 16 | 1.517 | 0 |
| 97 | deepseek/deepseek-v4-flash-vision-exp | failed | — | 70 | — | 2 | 5 | 1.184 | 0 |
| 98 | qwen/qwen3-235b-a22b-2507 | deadline_exceeded | — | 175 | — | 4 | 18 | 1.654 | 0 |
| 99 | inclusionai/ling-3.1-flash | failed | — | 0 | — | 0 | 1 | 0.205 | 0 |
| 100 | x-ai/grok-4.6 | failed | — | 90 | — | 2 | 6 | 8.225 | 0 |

---

# Krillion run: deepseek/deepseek-v4.1-flash-1017

Status: **agent_finished**. Score: **280/700**.

Final daily percentage: **better than 52% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 24 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Uzbekistan | accepted | Rare | 60 | 24 |

Round result: Uzbekistan · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | burpees | confirmation_required → Burpee | — | — | 24 |
| 2 | Burpee | accepted | Schooler | 30 | 20 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Golden | accepted | Plankton | 10 | 23 |

Round result: Golden · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | romesco | accepted | Rare | 60 | 24 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 24 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: deepseek/deepseek-v4.1-flash

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: z-ai/glm-5.3-flash

Status: **agent_finished**. Score: **370/700**.

Final daily percentage: **better than 86% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Vol-au-vent | accepted | Deep Cut | 85 | 22 |

Round result: Vol-au-vent · Deep Cut · 85 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 23 |

Round result: Metalocalypse · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Paraguay | accepted | Rare | 60 | 23 |

Round result: Paraguay · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 24 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild by Sabrina Carpenter | confirmation_required → Manchild | — | — | 20 |
| 2 | Manchild | accepted | Plankton | 10 | 17 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bomba | confirmation_required → Bomba calabrese | — | — | 24 |
| 2 | Bomba calabrese | accepted | Deep Cut | 85 | 22 |

Round result: Bomba calabrese · Deep Cut · 85 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 24 |

Round result: Booking.com · Plankton · 10 points (source: displayed_result).


---

# Krillion run: tencent/hy4

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.


---

# Krillion run: openai/gpt-6-luna

Status: **agent_finished**. Score: **365/700**.

Final daily percentage: **better than 85% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | arancini | accepted | Rare | 60 | 22 |

Round result: Arancini · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |

Round result: The Shivering Truth · Deep Cut · 85 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 21 |

Round result: Ecuador · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burpees | confirmation_required → Burpee | — | — | 21 |
| 2 | Burpee | accepted | Schooler | 30 | 16 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild by Sabrina Carpenter | confirmation_required → Manchild | — | — | 22 |
| 2 | Manchild by Sabrina Carpenter | confirmation_required → Manchild | — | — | 17 |
| 3 | Manchild by Sabrina Carpenter | confirmation_required → Manchild | — | — | 14 |
| 4 | Manchild by Sabrina Carpenter | confirmation_required → Manchild | — | — | 11 |
| 5 | Manchild | accepted | Plankton | 10 | 8 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 22 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Viator | accepted | Rare | 60 | 22 |

Round result: Viator · Rare · 60 points (source: displayed_result).


---

# Krillion run: stepfun/step-5-preview

Status: **agent_finished**. Score: **295/700**.

Final daily percentage: **better than 57% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | cannoli | accepted | Schooler | 30 | 19 |

Round result: Cannoli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 20 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Côte d&#x27;Ivoire | confirmation_required → Ivory Coast | — | — | 21 |
| 2 | Ivory Coast | accepted | Deep Cut | 85 | 17 |

Round result: Ivory Coast · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Kickboxing | accepted | Schooler | 30 | 23 |

Round result: Kickboxing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Nuevayol | accepted | Schooler | 30 | 16 |

Round result: NUEVAYoL · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 21 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 22 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: anthropic/claude-opus-5.5

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 22 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Primal | accepted | Rare | 60 | 23 |

Round result: Primal · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 21 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 22 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sapphire | accepted | Schooler | 30 | 18 |

Round result: Sapphire · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: minimax/minimax-m3.1-flash

Status: **failed**. Score: **80 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | sandwich | accepted | Schooler | 30 | 24 |

Round result: Sandwich · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 24 |

Round result: France · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Running | accepted | Plankton | 10 | 24 |

Round result: Running · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: tencent/hy4-preview

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: openai/gpt-6.1-sol

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 23 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 21 |

Round result: Burkina Faso · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 22 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sports car | accepted | Schooler | 30 | 23 |

Round result: Sports Car · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 20 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: openai/gpt-5.6-luna

Status: **agent_finished**. Score: **340/700**.

Final daily percentage: **better than 78% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pupusa | accepted | Rare | 60 | 22 |

Round result: Pupusa · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Oblongs | accepted | Rare | 60 | 22 |

Round result: The Oblongs · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 21 |

Round result: Ecuador · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stair climbing | accepted | Schooler | 30 | 22 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | DtMF | accepted | Plankton | 10 | 21 |

Round result: DtMF · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | salsa macha | accepted | Rare | 60 | 22 |

Round result: Salsa macha · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 22 |

Round result: Hipcamp · Rare · 60 points (source: displayed_result).


---

# Krillion run: moonshotai/kimi-k3.1-pro

Status: **agent_finished**. Score: **445/700**.

Final daily percentage: **better than 97% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | piroshki | confirmation_required → Pirozhki | — | — | 23 |
| 2 | Pirozhki | accepted | Rare | 60 | 20 |

Round result: Pirozhki · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 23 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 23 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Snowshoeing | accepted | Rare | 60 | 22 |

Round result: Snowshoeing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Illegal by PinkPantheress | confirmation_required → Illegal | — | — | 21 |
| 2 | Illegal | accepted | Rare | 60 | 19 |

Round result: Illegal · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: z-ai/glm-5.3

Status: **agent_finished**. Score: **340/700**.

Final daily percentage: **better than 78% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | stromboli | accepted | Rare | 60 | 21 |

Round result: Stromboli · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Duckman | confirmation_required → Duckman: Private Dick/Family Man | — | — | 22 |
| 2 | Duckman: Private Dick/Family Man | accepted | Rare | 60 | 19 |

Round result: Duckman: Private Dick/Family Man · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Botswana | accepted | Rare | 60 | 23 |

Round result: Botswana · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | mountain climbers | confirmation_required → Mountain climber | — | — | 23 |
| 2 | Burpees | confirmation_required → Burpee | — | — | 21 |
| 3 | Burpee | accepted | Schooler | 30 | 8 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 24 |
| 2 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 23 |
| 3 | Ordinary | accepted | Plankton | 10 | 20 |

Round result: Ordinary · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |

Round result: Ajvar · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 24 |

Round result: Hostelworld · Rare · 60 points (source: displayed_result).


---

# Krillion run: deepseek/deepseek-v4-flash-0731

Status: **agent_finished**. Score: **295/700**.

Final daily percentage: **better than 57% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | ravioli | accepted | Schooler | 30 | 23 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 22 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 22 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jumping jacks | accepted | Schooler | 30 | 24 |

Round result: Jumping jacks · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | TV Off | rejected | — | — | 23 |
| 2 | Sports Car | accepted | Schooler | 30 | 20 |

Round result: Sports Car · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sambal Oelek | accepted | Rare | 60 | 23 |

Round result: Sambal oelek · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Kayak | accepted | Schooler | 30 | 24 |

Round result: Kayak · Schooler · 30 points (source: displayed_result).


---

# Krillion run: nvidia/nemotron-3-ultra-550b-a55b:free

Status: **failed**. Score: **90 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 20 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 21 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: stealth/crouton-alpha

Status: **failed**. Score: **90 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 22 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tuca &amp; Bertie | accepted | Rare | 60 | 18 |

Round result: Tuca &amp; Bertie · Rare · 60 points (source: displayed_result).


---

# Krillion run: nvidia/nemotron-3.5-super-vl:free

Status: **failed**. Score: **180 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | cannoli | accepted | Schooler | 30 | 23 |

Round result: Cannoli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 20 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zimbabwe | accepted | Rare | 60 | 13 |

Round result: Zimbabwe · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 21 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

## Navigation recovery log

- 75.55s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: tencent/hy3

Status: **deadline_exceeded**. Score: **205 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 19 |

Round result: Knish · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Superjail! | accepted | Rare | 60 | 9 |

Round result: Superjail! · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 12 |

Round result: Burkina Faso · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | speed skaters | confirmation_required → Skaters | — | — | 13 |


---

# Krillion run: meta/muse-spark-1.3-contributor

Status: **agent_finished**. Score: **385/700**.

Final daily percentage: **better than 88% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 20 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 21 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 20 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 20 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Your Idol | accepted | Schooler | 30 | 18 |

Round result: Your Idol · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 18 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hopper | accepted | Rare | 60 | 19 |

Round result: Hopper · Rare · 60 points (source: displayed_result).


---

# Krillion run: anthropic/claude-haiku-5.5

Status: **agent_finished**. Score: **335/700**.

Final daily percentage: **better than 76% of today’s players**.

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
| 1 | Undone | accepted | Deep Cut | 85 | 24 |

Round result: Undone · Deep Cut · 85 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Myanmar | accepted | Rare | 60 | 23 |

Round result: Myanmar · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing machine | confirmation_required → Rowing | — | — | 24 |
| 2 | Jump rope | accepted | Schooler | 30 | 22 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Golden | accepted | Plankton | 10 | 24 |

Round result: Golden · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sambal oelek | accepted | Rare | 60 | 23 |

Round result: Sambal oelek · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tripadvisor | accepted | Rare | 60 | 24 |

Round result: Tripadvisor · Rare · 60 points (source: displayed_result).


---

# Krillion run: xiaomi/mimo-v2.6-flash

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.


---

# Krillion run: deepseek/deepseek-v4-flash

Status: **deadline_exceeded**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 21 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 20 |

Round result: South Park · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 22 |

Round result: France · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jumping rope | confirmation_required → Jump rope | — | — | 22 |
| 2 | Jump rope | accepted | Schooler | 30 | 16 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stargazing | rejected | — | — | 13 |


---

# Krillion run: anthropic/claude-sonnet-5.5

Status: **agent_finished**. Score: **250/700**.

Final daily percentage: **better than 38% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cannoli | accepted | Schooler | 30 | 23 |

Round result: Cannoli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ghana | rejected | — | — | 23 |
| 2 | Uzbekistan | accepted | Rare | 60 | 19 |

Round result: Uzbekistan · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 23 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild | accepted | Plankton | 10 | 22 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sambal oelek | accepted | Rare | 60 | 23 |

Round result: Sambal oelek · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Kayak | accepted | Schooler | 30 | 23 |

Round result: Kayak · Schooler · 30 points (source: displayed_result).


---

# Krillion run: moonshotai/kimi-k3

Status: **agent_finished**. Score: **300/700**.

Final daily percentage: **better than 60% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 23 |

Round result: Knish · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Invincible | accepted | Schooler | 30 | 21 |

Round result: Invincible · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 23 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burpees | confirmation_required → Burpee | — | — | 24 |
| 2 | Burpee | accepted | Schooler | 30 | 22 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Anxiety by Doechii | confirmation_required → Anxiety | — | — | 21 |
| 2 | Anxiety | accepted | Schooler | 30 | 19 |

Round result: Anxiety · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hopper | accepted | Rare | 60 | 23 |

Round result: Hopper · Rare · 60 points (source: displayed_result).


---

# Krillion run: google/gemini-3.8-flash

Status: **agent_finished**. Score: **300/700**.

Final daily percentage: **better than 60% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 19 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Botswana | accepted | Rare | 60 | 19 |

Round result: Botswana · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 21 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cry for Me | accepted | Schooler | 30 | 9 |

Round result: Cry For Me · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Kayak | accepted | Schooler | 30 | 20 |

Round result: Kayak · Schooler · 30 points (source: displayed_result).


---

# Krillion run: upstage/solar-mini4

Status: **deadline_exceeded**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumplings | confirmation_required → Dumpling | — | — | 23 |
| 2 | dumplings | confirmation_required → Dumpling | — | — | 12 |
| 3 | dumplings | confirmation_required → Dumpling | — | — | 7 |

## Navigation recovery log

- 12.21s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: google/gemini-4-argon

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 2.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Daria | accepted | Rare | 60 | 21 |

Round result: Daria · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 21 |

Round result: Gabon · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | elliptical | accepted | Schooler | 30 | 21 |

Round result: Elliptical · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sports car | accepted | Schooler | 30 | 21 |

Round result: Sports Car · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 21 |

Round result: Resy · Rare · 60 points (source: displayed_result).

## Navigation recovery log

- 68.05s: DESCEND ▼ — ok (two turns without navigation progress).
- 93.42s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: nvidia/nemotron-3.5-lightning:free

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.


---

# Krillion run: xiaomi/mimo-v2.6-pro

Status: **failed**. Score: **235 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 20 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 21 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |

Round result: Gabon · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 22 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Golden by HUNTR/X | confirmation_required → Golden | — | — | 13 |
| 2 | Golden | unconfirmed | — | — | 5 |


---

# Krillion run: openai/gpt-6.1-terra

Status: **agent_finished**. Score: **415/700**.

Final daily percentage: **better than 94% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Oblongs | accepted | Rare | 60 | 23 |

Round result: The Oblongs · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Botswana | accepted | Rare | 60 | 23 |

Round result: Botswana · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cross-country skiing | accepted | Rare | 60 | 21 |

Round result: Cross-country skiing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Garden of Eden by Lady Gaga | confirmation_required → Garden of Eden | — | — | 23 |
| 2 | Garden of Eden | accepted | Rare | 60 | 20 |

Round result: Garden of Eden · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 23 |

Round result: Tock · Deep Cut · 85 points (source: displayed_result).


---

# Krillion run: z-ai/glm-5.2

Status: **agent_finished**. Score: **270/700**.

Final daily percentage: **better than 46% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | ravioli | accepted | Schooler | 30 | 24 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 24 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 24 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Jumping rope | confirmation_required → Jump rope | — | — | 24 |
| 2 | Jump rope | accepted | Schooler | 30 | 21 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra | accepted | Schooler | 30 | 22 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: nvidia/nemotron-3.5-super-vl

Status: **agent_finished**. Score: **280/700**.

Final daily percentage: **better than 52% of today’s players**.

Navigation recovery: bounded; successful assistance: 4.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | King of the Hill | accepted | Schooler | 30 | 22 |

Round result: King of the Hill · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Nigeria | accepted | Rare | 60 | 22 |

Round result: Nigeria · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jumping rope | confirmation_required → Jump rope | — | — | 23 |
| 2 | Jump rope | accepted | Schooler | 30 | 20 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ordinary | accepted | Plankton | 10 | 22 |

Round result: Ordinary · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Agoda | accepted | Rare | 60 | 23 |

Round result: Agoda · Rare · 60 points (source: displayed_result).

## Navigation recovery log

- 24.07s: DESCEND ▼ — ok (two turns without navigation progress).
- 40.14s: DESCEND ▼ — ok (two turns without navigation progress).
- 85.65s: DESCEND ▼ — ok (two turns without navigation progress).
- 112.76s: SURFACE ▲ — ok (two turns without navigation progress).


---

# Krillion run: deepseek/deepseek-v4-pro-0813

Status: **failed**. Score: **120 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 22 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 24 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 24 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jumping rope | confirmation_required → Jump rope | — | — | 23 |
| 2 | Jump rope | accepted | Schooler | 30 | 20 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 24 |

## Navigation recovery log

- 20.38s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: qwen/qwen3.8-flash

Status: **failed**. Score: **240 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | momo | accepted | Rare | 60 | 15 |

Round result: Momo · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Primal | accepted | Rare | 60 | 15 |

Round result: Primal · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 18 |

Round result: Ecuador · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 22 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: dots-studio/dots-3-note-preview:free

Status: **failed**. Score: **100 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 20 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 22 |

Round result: South Park · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sweden | accepted | Schooler | 30 | 12 |

Round result: Sweden · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jump rope | accepted | Schooler | 30 | 18 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: qwen/qwen3.8-27b

Status: **agent_finished**. Score: **300/700**.

Final daily percentage: **better than 60% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | ravioli | accepted | Schooler | 30 | 22 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 18 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 21 |

Round result: Namibia · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jump rope | accepted | Schooler | 30 | 21 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Luther | rejected | — | — | 19 |
| 2 | Anxiety | accepted | Schooler | 30 | 13 |

Round result: Anxiety · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 22 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: minimax/minimax-m3

Status: **agent_finished**. Score: **130/700**.

Final daily percentage: **better than 3% of today’s players**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 24 |

Round result: Rick and Morty · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 24 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Jumping jacks | accepted | Schooler | 30 | 24 |

Round result: Jumping jacks · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 24 |
| 2 | Espresso | rejected | — | — | 22 |
| 3 | Die With A Smile | rejected | — | — | 21 |
| 4 | Birds of a Feather | rejected | — | — | 19 |
| 5 | Luther | rejected | — | — | 18 |
| 6 | Ordinary | accepted | Plankton | 10 | 16 |

Round result: Ordinary · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Chimichurri | rejected | — | — | 24 |
| 2 | Sriracha | accepted | Plankton | 10 | 23 |

Round result: Sriracha · Plankton · 10 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 23 |

Round result: Booking.com · Plankton · 10 points (source: displayed_result).

## Navigation recovery log

- 26.41s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: google/gemini-3-flash-preview

Status: **failed**. Score: **210 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Spanakopita | accepted | Rare | 60 | 23 |

Round result: Spanakopita · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 23 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Paraguay | accepted | Rare | 60 | 23 |

Round result: Paraguay · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burpees | confirmation_required → Burpee | — | — | 24 |
| 2 | Burpee | accepted | Schooler | 30 | 22 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | F1 Trillion | rejected | — | — | 24 |
| 2 | After Hours | rejected | — | — | 21 |
| 3 | Squid Game Main Theme | rejected | — | — | 18 |
| 4 | Bed Chem | rejected | — | — | 7 |
| 5 | Daylight | unconfirmed | — | — | 5 |


---

# Krillion run: openai/gpt-6-luna-pro

Status: **deadline_exceeded**. Score: **265 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 19 |

Round result: Knish · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 21 |

Round result: The Shivering Truth · Deep Cut · 85 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 19 |

Round result: Ecuador · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 19 |

Round result: Aqua jogging · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 20 |
| 2 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 15 |
| 3 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 9 |


---

# Krillion run: deepseek/deepseek-v4-pro

Status: **failed**. Score: **80 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 18 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 21 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 18 |

Round result: France · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | kickboxing | accepted | Schooler | 30 | 18 |

Round result: Kickboxing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: google/gemini-3.1-flash-lite

Status: **agent_finished**. Score: **270/700**.

Final daily percentage: **better than 46% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 23 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Elliptical | accepted | Schooler | 30 | 23 |

Round result: Elliptical · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Espresso | rejected | — | — | 24 |
| 2 | Taste | rejected | — | — | 22 |
| 3 | Die With A Smile | rejected | — | — | 20 |
| 4 | Good Luck, Babe! | rejected | — | — | 17 |
| 5 | APT. | rejected | — | — | 15 |
| 6 | Stargazing | rejected | — | — | 12 |
| 7 | Beautiful Things | accepted | Rare | 60 | 10 |

Round result: Beautiful Things · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 24 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: anthropic/claude-sonnet-5

Status: **agent_finished**. Score: **275/700**.

Final daily percentage: **better than 50% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bojack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 18 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 24 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Messy | accepted | Rare | 60 | 23 |

Round result: Messy · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sriracha | accepted | Plankton | 10 | 23 |

Round result: Sriracha · Plankton · 10 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 23 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: google/gemma-4-31b-it

Status: **deadline_exceeded**. Score: **120 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 5.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bojack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Norway | accepted | Schooler | 30 | 24 |

Round result: Norway · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Jump rope | accepted | Schooler | 30 | 24 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | none | rejected | — | — | 24 |
| 2 | Not Applicable | rejected | — | — | 22 |
| 3 | Impossible | rejected | — | — | 19 |
| 4 | Unknown | rejected | — | — | 17 |
| 5 | N/A | rejected | — | — | 15 |
| 6 | I cannot answer this | rejected | — | — | 13 |
| 7 | None | rejected | — | — | 11 |
| 8 | Not Available | rejected | — | — | 8 |
| 9 |  nonexistent | unconfirmed | — | — | 6 |

## Navigation recovery log

- 13.57s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).
- 25.86s: DESCEND ▼ — ok (two turns without navigation progress).
- 39.53s: DESCEND ▼ — ok (two turns without navigation progress).
- 50.53s: DESCEND ▼ — ok (two turns without navigation progress).
- 63.60s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: qwen/qwen3.7-flash

Status: **deadline_exceeded**. Score: **40 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 12 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Big Mouth | accepted | Schooler | 30 | 21 |

Round result: Big Mouth · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | China | rejected | — | — | 12 |


---

# Krillion run: upstage/solar-pro4

Status: **deadline_exceeded**. Score: **130 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pie | accepted | Plankton | 10 | 22 |

Round result: Pie · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Beavis and Butt-Head | accepted | Schooler | 30 | 23 |

Round result: Beavis and Butt-Head · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tunisia | rejected | — | — | 22 |
| 2 | Iraq | accepted | Schooler | 30 | 18 |

Round result: Iraq · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | shadow boxing | accepted | Rare | 60 | 22 |

Round result: Shadow boxing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile | rejected | — | — | 23 |
| 2 | Espresso | rejected | — | — | 19 |
| 3 | Birds of a Feather | rejected | — | — | 16 |
| 4 | Lovin On Me | rejected | — | — | 13 |
| 5 | Yes, And? | rejected | — | — | 10 |
| 6 | Not Like Us | rejected | — | — | 6 |

## Navigation recovery log

- 14.26s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: google/gemma-4-26b-a4b-it

Status: **deadline_exceeded**. Score: **80 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Dumpling | accepted | Plankton | 10 | 24 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 24 |

Round result: South Park · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Greece | rejected | — | — | 24 |
| 2 | Japan | accepted | Schooler | 30 | 22 |

Round result: Japan · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Elliptical | accepted | Schooler | 30 | 24 |

Round result: Elliptical · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 24 |
| 2 | Die With A Smile | rejected | — | — | 22 |
| 3 | Birds of a Feather | rejected | — | — | 20 |
| 4 | Starboy | rejected | — | — | 19 |
| 5 | Espresso | rejected | — | — | 17 |
| 6 | Flowers | rejected | — | — | 15 |
| 7 | Million Dollar Baby | rejected | — | — | 13 |
| 8 | Who | rejected | — | — | 11 |
| 9 | APT. | rejected | — | — | 10 |
| 10 | New Woman | rejected | — | — | 7 |
| 11 | Supernova | rejected | — | — | 6 |


---

# Krillion run: google/gemini-3.7-flash

Status: **agent_finished**. Score: **330/700**.

Final daily percentage: **better than 73% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 21 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Paraguay | accepted | Rare | 60 | 21 |

Round result: Paraguay · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | burpees | confirmation_required → Burpee | — | — | 21 |
| 2 | Burpee | accepted | Schooler | 30 | 17 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Open Hearts | accepted | Rare | 60 | 12 |

Round result: Open Hearts · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 22 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 22 |

Round result: Hostelworld · Rare · 60 points (source: displayed_result).


---

# Krillion run: openai/gpt-6-astra

Status: **agent_finished**. Score: **420/700**.

Final daily percentage: **better than 95% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | khachapuri | accepted | Rare | 60 | 22 |

Round result: Khachapuri · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Mauritania | rejected | — | — | 22 |
| 2 | Namibia | accepted | Rare | 60 | 18 |

Round result: Namibia · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | cross-country skiing | accepted | Rare | 60 | 22 |

Round result: Cross-country skiing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | twilight zone | accepted | Rare | 60 | 20 |

Round result: Twilight zone · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 21 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 20 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: openai/gpt-oss-120b

Status: **deadline_exceeded**. Score: **180 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bojack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Afghanistan | accepted | Rare | 60 | 21 |

Round result: Afghanistan · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | staircase sprint | rejected | — | — | 22 |
| 2 | battle rope slams | confirmation_required → Battle ropes | — | — | 20 |
| 3 | Battle ropes | accepted | Rare | 60 | 17 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Neon Dreams | rejected | — | — | 20 |
| 2 | Eternal Summer | rejected | — | — | 15 |
| 3 | Starlight Voyage | rejected | — | — | 13 |
| 4 | Solar Pulse | rejected | — | — | 10 |
| 5 | Midnight Echoes | rejected | — | — | 6 |


---

# Krillion run: stepfun/step-3.7-flash

Status: **failed**. Score: **40 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | calzone | accepted | Schooler | 30 | 12 |

Round result: Calzone · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 18 |

Round result: Rick and Morty · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

## Navigation recovery log

- 16.34s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: openai/gpt-5.6-sol

Status: **agent_finished**. Score: **360/700**.

Final daily percentage: **better than 83% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 22 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Duckman | confirmation_required → Duckman: Private Dick/Family Man | — | — | 22 |
| 2 | Duckman: Private Dick/Family Man | accepted | Rare | 60 | 19 |

Round result: Duckman: Private Dick/Family Man · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 22 |

Round result: Namibia · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cross-country skiing | accepted | Rare | 60 | 22 |

Round result: Cross-country skiing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sports car | accepted | Schooler | 30 | 21 |

Round result: Sports Car · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 21 |

Round result: Ajvar · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booksy | accepted | Rare | 60 | 22 |

Round result: Booksy · Rare · 60 points (source: displayed_result).


---

# Krillion run: mistralai/mistral-nemo

Status: **deadline_exceeded**. Score: **130 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ravioli | accepted | Schooler | 30 | 18 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 19 |

Round result: South Park · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 18 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hula hooping | accepted | Rare | 60 | 17 |

Round result: Hula hooping · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Glitter in the Air | rejected | — | — | 18 |
| 2 | Starboy | rejected | — | — | 12 |
| 3 | Leave the Door Open | rejected | — | — | 5 |


---

# Krillion run: google/gemini-2.5-flash-lite

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.


---

# Krillion run: deepseek/deepseek-v3.2

Status: **deadline_exceeded**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 22 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 23 |

Round result: South Park · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 23 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cycling | accepted | Plankton | 10 | 23 |

Round result: Cycling · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Blame | rejected | — | — | 23 |
| 2 | Houdini | rejected | — | — | 20 |
| 3 | Is It Over Now | rejected | — | — | 17 |
| 4 | Fortnight | rejected | — | — | 14 |
| 5 | Espresso | rejected | — | — | 12 |
| 6 | Die With A Smile | rejected | — | — | 9 |
| 7 | GUTS | rejected | — | — | 6 |


---

# Krillion run: anthropic/claude-fable-5.1

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 21 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Mozambique | accepted | Deep Cut | 85 | 22 |

Round result: Mozambique · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 21 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Azizam | accepted | Schooler | 30 | 17 |

Round result: Azizam · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 21 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: qwen/qwen3.6-35b-a3b

Status: **failed**. Score: **30 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 13 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

## Navigation recovery log

- 13.39s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: google/gemini-2.5-flash

Status: **failed**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 24 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).


---

# Krillion run: google/gemini-3.5-flash-lite

Status: **agent_finished**. Score: **220/700**.

Final daily percentage: **better than 25% of today’s players**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romania | rejected | — | — | 23 |
| 2 | Italy | accepted | Schooler | 30 | 21 |

Round result: Italy · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 24 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 24 |
| 2 | Taste | rejected | — | — | 22 |
| 3 | The Emptiness Machine | rejected | — | — | 20 |
| 4 | Disease | rejected | — | — | 18 |
| 5 | Golden | accepted | Plankton | 10 | 16 |

Round result: Golden · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 24 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).

## Navigation recovery log

- 92.00s: SURFACE ▲ — ok (two turns without navigation progress).


---

# Krillion run: openai/gpt-6-sol

Status: **agent_finished**. Score: **420/700**.

Final daily percentage: **better than 95% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 21 |

Round result: Knish · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 22 |

Round result: Metalocalypse · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 22 |

Round result: Namibia · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Cross-country skiing | accepted | Rare | 60 | 22 |

Round result: Cross-country skiing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Headphones On | accepted | Rare | 60 | 21 |

Round result: Headphones On · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 22 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 22 |

Round result: Hostelworld · Rare · 60 points (source: displayed_result).


---

# Krillion run: x-ai/grok-4.7

Status: **agent_finished**. Score: **420/700**.

Final daily percentage: **better than 95% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 18 |

Round result: Khinkali · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 12 |

Round result: Metalocalypse · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 9 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 19 |

Round result: Battle ropes · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild | accepted | Plankton | 10 | 15 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | romesco | accepted | Rare | 60 | 18 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 11 |

Round result: Tock · Deep Cut · 85 points (source: displayed_result).


---

# Krillion run: anthropic/claude-opus-5

Status: **agent_finished**. Score: **275/700**.

Final daily percentage: **better than 50% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 22 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 23 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. follow-up — &quot;Luther&quot; by Kendrick Lamar and SZA | rejected | — | — | 23 |
| 2 | Ordinary | accepted | Plankton | 10 | 20 |

Round result: Ordinary · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 23 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: openai/gpt-4o-mini

Status: **failed**. Score: **100 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 3.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bhaji | rejected | — | — | 23 |
| 2 | Dumpling | accepted | Plankton | 10 | 19 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bojack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Portugal | rejected | — | — | 24 |
| 2 | Malawi | rejected | — | — | 20 |
| 3 | Cuba | rejected | — | — | 17 |
| 4 | Japan | accepted | Schooler | 30 | 13 |

Round result: Japan · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zumba | accepted | Schooler | 30 | 24 |

Round result: Zumba · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Song Title Example | rejected | — | — | 24 |
| 2 | Imaginary Song 2026 | rejected | — | — | 21 |
| 3 | Unreleased Anthem 2026 | rejected | — | — | 17 |
| 4 | Future Echoes | rejected | — | — | 14 |
| 5 | Lost in the Echo | rejected | — | — | 10 |
| 6 | Echoes of Tomorrow | rejected | — | — | 6 |

## Navigation recovery log

- 29.10s: DESCEND ▼ — ok (two turns without navigation progress).
- 61.59s: DESCEND ▼ — ok (two turns without navigation progress).
- 73.15s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: anthropic/claude-sonnet-4.6

Status: **failed**. Score: **120 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelProviderError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 22 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Germany | accepted | Plankton | 10 | 23 |

Round result: Germany · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | cycling | accepted | Plankton | 10 | 24 |

Round result: Cycling · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile | rejected | — | — | 22 |
| 2 | APT | rejected | — | — | 19 |
| 3 | Luther | rejected | — | — | 17 |
| 4 | Beautiful Things | accepted | Rare | 60 | 14 |

Round result: Beautiful Things · Rare · 60 points (source: displayed_result).


---

# Krillion run: cohere/north-mini-code:free

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelProviderError.


---

# Krillion run: anthropic/claude-opus-4.8

Status: **agent_finished**. Score: **200/700**.

Final daily percentage: **better than 18% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zimbabwe | accepted | Rare | 60 | 23 |

Round result: Zimbabwe · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 23 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. by Rosé and Bruno Mars | rejected | — | — | 23 |
| 2 | DtMF by Bad Bunny | confirmation_required → DtMF | — | — | 19 |
| 3 | DtMF by Bad Bunny | confirmation_required → DtMF | — | — | 16 |
| 4 | DtMF | accepted | Plankton | 10 | 11 |

Round result: DtMF · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sriracha | accepted | Plankton | 10 | 24 |

Round result: Sriracha · Plankton · 10 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 23 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: openai/gpt-5.6-terra

Status: **agent_finished**. Score: **325/700**.

Final daily percentage: **better than 70% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 22 |

Round result: The Maxx · Deep Cut · 85 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Italy | accepted | Schooler | 30 | 23 |

Round result: Italy · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | stair climbing | accepted | Schooler | 30 | 22 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra | accepted | Schooler | 30 | 23 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 22 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: qwen/qwen3.8-max-0902

Status: **failed**. Score: **90 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | calzone | accepted | Schooler | 30 | 15 |

Round result: Calzone · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 14 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 8 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: openai/gpt-oss-20b

Status: **failed**. Score: **50 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelProviderError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 23 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Simpsons | accepted | Plankton | 10 | 20 |

Round result: The Simpsons · Plankton · 10 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Spain | accepted | Plankton | 10 | 23 |

Round result: Spain · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: anthropic/claude-sonnet-4.5

Status: **deadline_exceeded**. Score: **120 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | ravioli | accepted | Schooler | 30 | 23 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pakistan | accepted | Schooler | 30 | 23 |

Round result: Pakistan · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 23 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 23 |
| 2 | Die With A Smile | rejected | — | — | 20 |
| 3 | Espresso | rejected | — | — | 17 |
| 4 | Birds of a Feather | rejected | — | — | 14 |
| 5 | Lose Control | rejected | — | — | 11 |
| 6 | Good Luck, Babe! | rejected | — | — | 8 |
| 7 | Austin | rejected | — | — | 6 |


---

# Krillion run: anthropic/claude-haiku-4.5

Status: **deadline_exceeded**. Score: **120 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 2.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 24 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 24 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Libya | rejected | — | — | 24 |
| 2 | Tunisia | rejected | — | — | 21 |
| 3 | Morocco | accepted | Schooler | 30 | 19 |

Round result: Morocco · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 24 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Espresso | rejected | — | — | 23 |
| 2 | Flowers | rejected | — | — | 21 |
| 3 | Cruel Summer | rejected | — | — | 18 |
| 4 | Vampire | rejected | — | — | 16 |
| 5 | Espresso | rejected | — | — | 14 |
| 6 | Starboy | rejected | — | — | 11 |
| 7 | Blinding Lights | rejected | — | — | 9 |
| 8 | One Dance | rejected | — | — | 7 |

## Navigation recovery log

- 24.51s: DESCEND ▼ — ok (two turns without navigation progress).
- 52.12s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: mistralai/mistral-large-4-0

Status: **agent_finished**. Score: **270/700**.

Final daily percentage: **better than 46% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 11 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 20 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 17 |

Round result: Namibia · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | kickboxing | accepted | Schooler | 30 | 22 |

Round result: Kickboxing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra | accepted | Schooler | 30 | 21 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 18 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: moonshotai/kimi-k2.6

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: particle-ai/particle-1

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 24 |

Round result: Burkina Faso · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | shadow boxing | accepted | Rare | 60 | 24 |

Round result: Shadow boxing · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Anxiety | accepted | Schooler | 30 | 24 |

Round result: Anxiety · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 24 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: qwen/qwen3.5-9b

Status: **failed**. Score: **30 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 20 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## Navigation recovery log

- 16.62s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: meta/muse-spark-open

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 22 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 23 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 22 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Mountain climbers | confirmation_required → Mountain climber | — | — | 22 |
| 2 | Mountain climber | accepted | Schooler | 30 | 18 |

Round result: Mountain climber · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra by Lady Gaga | confirmation_required → Abracadabra | — | — | 22 |
| 2 | Abracadabra | accepted | Schooler | 30 | 17 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 16 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zocdoc | accepted | Rare | 60 | 17 |

Round result: Zocdoc · Rare · 60 points (source: displayed_result).


---

# Krillion run: inclusionai/ling-3.0-flash

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.


---

# Krillion run: meta/muse-spark-1.3

Status: **failed**. Score: **205 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 17 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 19 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 20 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stairmaster | confirmation_required → Stair climbing | — | — | 21 |
| 2 | Stair climbing | accepted | Schooler | 30 | 10 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: z-ai/glm-5.3-flashx

Status: **agent_finished**. Score: **280/700**.

Final daily percentage: **better than 52% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | cannoli | accepted | Schooler | 30 | 22 |

Round result: Cannoli · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Aqua Teen Hunger Force | accepted | Rare | 60 | 21 |

Round result: Aqua Teen Hunger Force · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 22 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 23 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 21 |
| 2 | Ordinary | accepted | Plankton | 10 | 17 |

Round result: Ordinary · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |

Round result: Ajvar · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: xingchen-agi/xing4.0-29b-a4b:free

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelRateLimitError.


---

# Krillion run: meta/muse-wonder

Status: **agent_finished**. Score: **335/700**.

Final daily percentage: **better than 76% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 22 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Tuca &amp; Bertie | accepted | Rare | 60 | 18 |

Round result: Tuca &amp; Bertie · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 21 |

Round result: Burkina Faso · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stair climbing | accepted | Schooler | 30 | 20 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | DtMF | accepted | Plankton | 10 | 21 |

Round result: DtMF · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 19 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hopper | accepted | Rare | 60 | 20 |

Round result: Hopper · Rare · 60 points (source: displayed_result).


---

# Krillion run: google/gemini-3.6-flash

Status: **agent_finished**. Score: **390/700**.

Final daily percentage: **better than 90% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 20 |

Round result: Ecuador · Rare · 60 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Plyometrics | accepted | Rare | 60 | 22 |

Round result: Plyometrics · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Open Hearts | accepted | Rare | 60 | 14 |

Round result: Open Hearts · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 22 |

Round result: Romesco · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Agoda | accepted | Rare | 60 | 22 |

Round result: Agoda · Rare · 60 points (source: displayed_result).


---

# Krillion run: google/gemini-3.1-flash-lite-preview

Status: **agent_finished**. Score: **270/700**.

Final daily percentage: **better than 47% of today’s players**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 24 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 23 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Elliptical | accepted | Schooler | 30 | 24 |

Round result: Elliptical · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile | rejected | — | — | 24 |
| 2 | Taste | rejected | — | — | 22 |
| 3 | Good Luck, Babe! | rejected | — | — | 20 |
| 4 | Espresso | rejected | — | — | 18 |
| 5 | Get It Goin | rejected | — | — | 16 |
| 6 | Illusion | rejected | — | — | 14 |
| 7 | The Emptiness Machine | rejected | — | — | 12 |
| 8 | Beautiful Things | accepted | Rare | 60 | 10 |

Round result: Beautiful Things · Rare · 60 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 24 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).

## Navigation recovery log

- 93.78s: SURFACE ▲ — ok (two turns without navigation progress).


---

# Krillion run: anthropic/claude-opus-4.6

Status: **agent_finished**. Score: **300/700**.

Final daily percentage: **better than 60% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | calzone | accepted | Schooler | 30 | 22 |

Round result: Calzone · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Daria | accepted | Rare | 60 | 21 |

Round result: Daria · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Romania | rejected | — | — | 22 |
| 2 | Poland | accepted | Schooler | 30 | 18 |

Round result: Poland · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | burpees | confirmation_required → Burpee | — | — | 22 |
| 2 | Burpee | accepted | Schooler | 30 | 19 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 22 |
| 2 | Luther | rejected | — | — | 19 |
| 3 | Die With A Smile | rejected | — | — | 15 |
| 4 | Birds of a Feather | rejected | — | — | 11 |
| 5 | Abracadabra | accepted | Schooler | 30 | 7 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gochujang | accepted | Rare | 60 | 22 |

Round result: Gochujang · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turo | accepted | Rare | 60 | 22 |

Round result: Turo · Rare · 60 points (source: displayed_result).


---

# Krillion run: reflection/beam-1.0-501b-a23b

Status: **agent_finished**. Score: **305/700**.

Final daily percentage: **better than 63% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Oman | accepted | Deep Cut | 85 | 23 |

Round result: Oman · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | mountain climbers | confirmation_required → Mountain climber | — | — | 23 |
| 2 | Mountain climber | accepted | Schooler | 30 | 20 |

Round result: Mountain climber · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Fate of Ophelia | accepted | Plankton | 10 | 18 |

Round result: The Fate of Ophelia · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | arrabbiata | accepted | Rare | 60 | 24 |

Round result: Arrabbiata · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Hopper | accepted | Rare | 60 | 24 |

Round result: Hopper · Rare · 60 points (source: displayed_result).


---

# Krillion run: google/gemini-3.1-pro-preview

Status: **deadline_exceeded**. Score: **150 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 18 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 19 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 17 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 20 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Texas Hold &#x27;Em | rejected | — | — | 15 |


---

# Krillion run: openai/gpt-5-mini

Status: **failed**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 1.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | kolache | accepted | Rare | 60 | 22 |

Round result: Kolache · Rare · 60 points (source: displayed_result).

## Navigation recovery log

- 14.21s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).


---

# Krillion run: openai/gpt-4.1-mini

Status: **deadline_exceeded**. Score: **135 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 4.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Dumpling | accepted | Plankton | 10 | 23 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 24 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 23 |

Round result: Gabon · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | running | accepted | Plankton | 10 | 24 |

Round result: Running · Plankton · 10 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Flowers by Miley Cyrus | rejected | — | — | 24 |
| 2 | Anti-Hero by Taylor Swift | rejected | — | — | 21 |
| 3 | Calm Down by Rema &amp; Selena Gomez | rejected | — | — | 19 |
| 4 | Vampire by Olivia Rodrigo | rejected | — | — | 16 |
| 5 | Cupid by FIFTY FIFTY | rejected | — | — | 15 |
| 6 | Kill Bill by SZA | rejected | — | — | 12 |
| 7 | Flowers by Miley Cyrus | rejected | — | — | 10 |
| 8 | As It Was by Harry Styles | rejected | — | — | 8 |
| 9 | Die For You by The Weeknd and Ariana Grande | rejected | — | — | 6 |

## Navigation recovery log

- 11.07s: ▼ BEGIN DESCENT ▼ — ok (two turns without navigation progress).
- 24.85s: DESCEND ▼ — ok (two turns without navigation progress).
- 37.09s: DESCEND ▼ — ok (two turns without navigation progress).
- 50.57s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: openai/gpt-5.4-nano

Status: **deadline_exceeded**. Score: **100 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 4.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 22 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 21 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 21 |

Round result: France · Plankton · 10 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stair climber | confirmation_required → Stair climbing | — | — | 22 |
| 2 | Stair climbing | accepted | Schooler | 30 | 17 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sabrina Carpenter – “Nonsense” | rejected | — | — | 18 |
| 2 | Sabrina Carpenter – “Please Please Please” | rejected | — | — | 12 |
| 3 | Kendrick Lamar – “TV Off” (2025) | rejected | — | — | 7 |

## Navigation recovery log

- 25.69s: DESCEND ▼ — ok (two turns without navigation progress).
- 40.88s: DESCEND ▼ — ok (two turns without navigation progress).
- 56.04s: DESCEND ▼ — ok (two turns without navigation progress).
- 74.52s: DESCEND ▼ — ok (two turns without navigation progress).


---

# Krillion run: openai/gpt-5.6-luna-pro

Status: **agent_finished**. Score: **385/700**.

Final daily percentage: **better than 88% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jiaozi | accepted | Rare | 60 | 20 |

Round result: Jiaozi · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 20 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 19 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Stair climbing | accepted | Schooler | 30 | 20 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Baile Inolvidable | accepted | Schooler | 30 | 17 |

Round result: Baile Inolvidable · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Salsa macha | accepted | Rare | 60 | 21 |

Round result: Salsa macha · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booksy | accepted | Rare | 60 | 21 |

Round result: Booksy · Rare · 60 points (source: displayed_result).


---

# Krillion run: openai/gpt-5.4-mini

Status: **agent_finished**. Score: **270/700**.

Final daily percentage: **better than 47% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | xiao long bao | confirmation_required → Xiaolongbao | — | — | 22 |
| 2 | Xiaolongbao | accepted | Rare | 60 | 18 |

Round result: Xiaolongbao · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 22 |

Round result: Archer · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 22 |

Round result: Madagascar · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | burpees | confirmation_required → Burpee | — | — | 22 |
| 2 | Burpee | accepted | Schooler | 30 | 19 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Azizam by Ed Sheeran | confirmation_required → Azizam | — | — | 21 |
| 2 | Azizam | accepted | Schooler | 30 | 18 |

Round result: Azizam · Schooler · 30 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 22 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 21 |

Round result: OpenTable · Schooler · 30 points (source: displayed_result).


---

# Krillion run: recursive/flint-v1.0:free

Status: **failed**. Score: **180 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | samosa | accepted | Schooler | 30 | 21 |

Round result: Samosa · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Critic | accepted | Rare | 60 | 17 |

Round result: The Critic · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 18 |

Round result: Turkey · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 21 |

Round result: Aqua jogging · Rare · 60 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | I Had Some Help | rejected | — | — | 19 |


---

# Krillion run: x-ai/grok-4.5

Status: **failed**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 18 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 17 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: inception/mercury-3

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelOutputTruncatedError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | baozi | confirmation_required → Bao | — | — | 24 |


---

# Krillion run: qwen/qwen3.7-plus

Status: **failed**. Score: **150 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 14 |

Round result: Knish · Rare · 60 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 13 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Italy | accepted | Schooler | 30 | 12 |

Round result: Italy · Schooler · 30 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | rowing | accepted | Schooler | 30 | 19 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |


---

# Krillion run: openai/gpt-5.4

Status: **agent_finished**. Score: **335/700**.

Final daily percentage: **better than 76% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 21 |

Round result: Gabon · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Burpees | confirmation_required → Burpee | — | — | 22 |
| 2 | Burpee | accepted | Schooler | 30 | 19 |

Round result: Burpee · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild | accepted | Plankton | 10 | 21 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

## PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 22 |

Round result: Muhammara · Rare · 60 points (source: displayed_result).

## PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


---

# Krillion run: deepseek/deepseek-v4-flash-vision-exp

Status: **failed**. Score: **70 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelProviderError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 24 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 19 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).


---

# Krillion run: qwen/qwen3-235b-a22b-2507

Status: **deadline_exceeded**. Score: **175 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 22 |

Round result: Empanada · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 22 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Mongolia | rejected | — | — | 24 |
| 2 | Zambia | accepted | Deep Cut | 85 | 21 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

## PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jumping jacks | accepted | Schooler | 30 | 23 |

Round result: Jumping jacks · Schooler · 30 points (source: displayed_result).

## PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Flowers | rejected | — | — | 22 |
| 2 | As It Was | rejected | — | — | 19 |
| 3 | Blinding Lights | rejected | — | — | 15 |
| 4 | Anti-Hero | rejected | — | — | 13 |
| 5 | Padam Padam | rejected | — | — | 10 |
| 6 | Flowers | rejected | — | — | 6 |


---

# Krillion run: inclusionai/ling-3.1-flash

Status: **failed**. Score: **0 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: ModelProviderError.


---

# Krillion run: x-ai/grok-4.6

Status: **failed**. Score: **90 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

## PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 13 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

## PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 9 |

Round result: Metalocalypse · Rare · 60 points (source: displayed_result).

## PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

