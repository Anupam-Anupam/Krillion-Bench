# Krillion: final-score continuation campaign

Date: **2026-11-07**. Finished **100/100** models; **100 verified final scorecards**, **0 run errors without a score**.

The same 100-model roster was rerun under one frozen harness version. There were **884 submitted attempts**, **136 zero-point questions across 57 runs**, and **0 navigation-only scorecard recoveries**. Missed questions count toward the actual final score, including zero.

## Method and provenance

Each model received a fresh Browser Use Cloud browser at the initial Krillion website and the same daily questions. The game retains its 25-second timer. Inference uses the remaining round budget with a 3-second action margin and timer-rounding allowance. There is no harness output-token cap. Same-model transient retries and schema-compatibility fallback remain bounded by the current deadline. Concurrency was 8; the agent limit was 600 seconds, with up to 240 seconds of scorecard collection after terminal failure. No replacement model or fallback answer was used.

Question timeouts continue to later rounds. After terminal model/provider failure, outstanding calls are cancelled and the harness only advances visible navigation controls; unanswered questions expire naturally. Such scores retain their failure diagnostics and are marked as recovered. Browser failures without verifiable game evidence cannot be assigned a final score.

The prior pilot launched 12 models: 8 verified games and 4 startup screenshot failures. That pilot was stopped, the optional screenshot was made nonfatal, and this entire campaign was started separately. Pilot results are excluded from this leaderboard. Historical TOP100 files remain unchanged.

[Frozen roster, settings and source hashes](CONTINUATION-MANIFEST.json) · [Public data, metrics and all answers](leaderboard-data.json) · [Historical report](TOP100-REPORT.md).

Original usage-ranking capture: 2026-11-07T20:28:00.407Z; [OpenRouter source](https://openrouter.ai/models?fmt=cards&output_modalities=text&order=top-weekly). Ranking attribution: OpenRouter, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The roster includes free and paid endpoints separately and is a usage selection, not a quality ranking.

The daily percentage is the live game’s “better than today’s players” result, not score divided by 700. It can drift during the campaign. Costs exclude browser hosting. API-reported account charges and provider output components have separate provenance; cancelled calls without usage leave partial cost/token totals, never an assumed zero. This is one run per model on one daily puzzle, not a general model-quality ranking.

## Audit

All 884 logged submissions matched the reports. Each verified game has seven round entries summing to its displayed score and a parsed daily percentage whenever the game displayed one. Daily percentages were captured for 99 games. DeepSeek V4 Flash scored 300, but its saved final page and DOM trace did not contain a daily percentage; that field remains unavailable. Nonaccepted attempts have no attributed rarity. Navigation-only score collection submitted no answers. Source hashes still match the frozen manifest. No optional artifact errors were recorded.

Answer outcomes: {'accepted': 543, 'confirmation_required': 92, 'rejected': 238, 'unconfirmed': 11}. Inference interruptions: {'round_inference_deadline': 122, 'navigation_inference_timeout': 22, 'provider_error': 11, 'rate_limit': 9}. Diagnostic event counts (retries may repeat a cause): {'provider_error': 36, 'rate_limit': 30, 'invalid_request': 2}.

## Results

| Model | Final score /700 | Daily % | Missed questions | Scorecard recovery |
|---|---:|---:|---:|---|
| moonshotai/kimi-k3.1-pro | 570 | 99.79 | 0 | no |
| openai/gpt-5-mini | 545 | 99.63 | 0 | no |
| openai/gpt-5.6-sol | 545 | 99.63 | 0 | no |
| deepseek/deepseek-v4-flash-0731 | 535 | 99.58 | 0 | no |
| deepseek/deepseek-v4.1-flash-1017 | 520 | 99.0 | 0 | no |
| openai/gpt-6-sol | 520 | 99.0 | 0 | no |
| xiaomi/mimo-v2.6-pro | 515 | 99.0 | 0 | no |
| moonshotai/kimi-k3 | 495 | 99.0 | 0 | no |
| openai/gpt-5.6-terra | 495 | 99.0 | 0 | no |
| openai/gpt-6-luna-pro | 495 | 99.0 | 0 | no |
| openai/gpt-6.1-sol | 495 | 99.0 | 0 | no |
| openai/gpt-6.1-terra | 495 | 99.0 | 0 | no |
| deepseek/deepseek-v4.1-flash | 490 | 99.0 | 0 | no |
| google/gemini-3.5-flash-lite | 490 | 99.0 | 0 | no |
| particle-ai/particle-1 | 490 | 99.0 | 0 | no |
| google/gemini-3.6-flash | 470 | 98.0 | 0 | no |
| meta/muse-spark-1.3 | 470 | 98.0 | 0 | no |
| openai/gpt-6-astra | 470 | 98.0 | 0 | no |
| deepseek/deepseek-v4-flash-vision-exp | 465 | 98.0 | 0 | no |
| openai/gpt-5.6-luna-pro | 465 | 98.0 | 0 | no |
| openai/gpt-6-luna | 465 | 98.0 | 0 | no |
| inception/mercury-3 | 460 | 97.0 | 1 | no |
| google/gemini-3.1-pro-preview | 445 | 97.0 | 0 | no |
| meta/muse-wonder | 445 | 97.0 | 0 | no |
| z-ai/glm-5.3-flashx | 445 | 97.0 | 0 | no |
| anthropic/claude-sonnet-5 | 440 | 96.0 | 0 | no |
| minimax/minimax-m3 | 440 | 96.0 | 0 | no |
| openai/gpt-5.4 | 440 | 96.0 | 0 | no |
| openai/gpt-5.6-luna | 440 | 96.0 | 0 | no |
| recursive/flint-v1.0:free | 435 | 95.0 | 1 | no |
| x-ai/grok-4.5 | 435 | 95.0 | 1 | no |
| anthropic/claude-haiku-5.5 | 420 | 95.0 | 0 | no |
| anthropic/claude-opus-4.6 | 415 | 94.0 | 0 | no |
| google/gemini-3.7-flash | 415 | 94.0 | 0 | no |
| google/gemini-4-argon | 415 | 94.0 | 0 | no |
| meta/muse-spark-1.3-contributor | 415 | 94.0 | 0 | no |
| anthropic/claude-opus-5 | 410 | 93.0 | 0 | no |
| openai/gpt-oss-120b | 410 | 93.0 | 1 | no |
| stepfun/step-5-preview | 405 | 92.0 | 1 | no |
| z-ai/glm-5.3-flash | 405 | 92.0 | 1 | no |
| nvidia/nemotron-3.5-super-vl | 395 | 91.0 | 0 | no |
| z-ai/glm-5.2 | 390 | 90.0 | 0 | no |
| anthropic/claude-fable-5.1 | 385 | 89.0 | 0 | no |
| anthropic/claude-opus-5.5 | 385 | 89.0 | 0 | no |
| anthropic/claude-sonnet-5.5 | 385 | 89.0 | 0 | no |
| deepseek/deepseek-v4-pro-0813 | 385 | 89.0 | 1 | no |
| google/gemini-3-flash-preview | 385 | 89.0 | 1 | no |
| google/gemini-3.8-flash | 385 | 89.0 | 1 | no |
| meta/muse-spark-open | 385 | 89.0 | 1 | no |
| qwen/qwen3-235b-a22b-2507 | 385 | 89.0 | 1 | no |
| google/gemini-2.5-flash | 380 | 87.0 | 1 | no |
| z-ai/glm-5.3 | 380 | 87.0 | 0 | no |
| inclusionai/ling-3.1-flash | 375 | 86.0 | 2 | no |
| google/gemma-4-26b-a4b-it | 360 | 83.0 | 1 | no |
| nvidia/nemotron-3.5-super-vl:free | 360 | 83.0 | 1 | no |
| xiaomi/mimo-v2.6-flash | 360 | 83.0 | 0 | no |
| anthropic/claude-sonnet-4.5 | 355 | 81.0 | 1 | no |
| deepseek/deepseek-v4-pro | 355 | 80.0 | 1 | no |
| google/gemini-3.1-flash-lite-preview | 355 | 81.0 | 1 | no |
| inclusionai/ling-3.0-flash | 350 | 79.0 | 2 | no |
| qwen/qwen3.8-27b | 350 | 79.0 | 2 | no |
| qwen/qwen3.8-flash | 350 | 79.0 | 2 | no |
| qwen/qwen3.8-max-0902 | 350 | 79.0 | 2 | no |
| openai/gpt-5.4-mini | 340 | 78.0 | 0 | no |
| tencent/hy3 | 340 | 78.0 | 3 | no |
| minimax/minimax-m3.1-flash | 335 | 76.0 | 1 | no |
| google/gemini-3.1-flash-lite | 330 | 73.0 | 1 | no |
| anthropic/claude-opus-4.8 | 325 | 70.0 | 1 | no |
| deepseek/deepseek-v3.2 | 325 | 70.0 | 2 | no |
| nvidia/nemotron-3.5-lightning:free | 325 | 70.0 | 1 | no |
| cohere/north-mini-code:free | 315 | 68.0 | 3 | no |
| openai/gpt-4o-mini | 305 | 64.0 | 1 | no |
| deepseek/deepseek-v4-flash | 300 | — | 2 | no |
| openai/gpt-4.1-mini | 295 | 58.0 | 1 | no |
| openai/gpt-5.4-nano | 295 | 58.0 | 1 | no |
| stepfun/step-3.7-flash | 295 | 58.0 | 2 | no |
| reflection/beam-1.0-501b-a23b | 290 | 57.0 | 3 | no |
| anthropic/claude-sonnet-4.6 | 275 | 50.0 | 1 | no |
| google/gemma-4-31b-it | 270 | 47.0 | 2 | no |
| dots-studio/dots-3-note-preview:free | 265 | 45.0 | 2 | no |
| x-ai/grok-4.7 | 265 | 45.0 | 3 | no |
| openai/gpt-oss-20b | 260 | 43.0 | 3 | no |
| upstage/solar-pro4 | 245 | 36.0 | 2 | no |
| anthropic/claude-haiku-4.5 | 235 | 32.0 | 2 | no |
| google/gemini-2.5-flash-lite | 230 | 30.0 | 0 | no |
| moonshotai/kimi-k2.6 | 230 | 30.0 | 4 | no |
| qwen/qwen3.6-35b-a3b | 230 | 30.0 | 4 | no |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 205 | 21.0 | 4 | no |
| nvidia/nemotron-3-ultra-550b-a55b:free | 205 | 21.0 | 4 | no |
| mistralai/mistral-nemo | 180 | 12.0 | 3 | no |
| upstage/solar-mini4 | 170 | 10.0 | 1 | no |
| mistralai/mistral-large-4-0 | 155 | 8.0 | 4 | no |
| qwen/qwen3.7-flash | 90 | 1.0 | 5 | no |
| qwen/qwen3.7-plus | 85 | 1.0 | 6 | no |
| qwen/qwen3.5-9b | 60 | 0.0 | 6 | no |
| x-ai/grok-4.6 | 60 | 0.0 | 6 | no |
| xingchen-agi/xing4.0-29b-a4b:free | 30 | 0.0 | 4 | no |
| stealth/crouton-alpha | 0 | 0.0 | 7 | no |
| tencent/hy4 | 0 | 0.0 | 7 | no |
| tencent/hy4-preview | 0 | 0.0 | 7 | no |

---

## deepseek/deepseek-v4.1-flash-1017

Status: agent_finished. Final score: 520/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Supplì.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | supplì | accepted | Deep Cut | 85 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 11 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | rucking | accepted | Rare | 60 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Sally, When The Wine Runs Out.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sally, When the Wine Runs Out by ROLE MODEL | confirmation_required → Sally, When The Wine Runs Out | — | — | 21 |
| 2 | Sally, When The Wine Runs Out | accepted | Rare | 60 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Campspot.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Campspot | accepted | Deep Cut | 85 | 23 |

---

## deepseek/deepseek-v4.1-flash

Status: agent_finished. Final score: 490/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kroppkaka.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kroppkaka | accepted | Deep Cut | 85 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · VersaClimber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | VersaClimber | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · The Subway.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Eusexua | rejected | — | — | 22 |
| 2 | Nice to Meet You | rejected | — | — | 11 |
| 3 | The Subway | accepted | Schooler | 30 | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Peerspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peerspace | accepted | Deep Cut | 85 | 22 |

---

## z-ai/glm-5.3-flash

Status: agent_finished. Final score: 405/700. Daily placement: 92.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Tim Tam.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tim Tam | accepted | Rare | 60 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Double unders | confirmation_required → Jump rope | — | — | 23 |
| 2 | Double unders | confirmation_required → Jump rope | — | — | 21 |
| 3 | Jump rope | accepted | Schooler | 30 | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile | rejected | — | — | 24 |
| 2 | Retrograde Drift | rejected | — | — | 17 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Peerspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peerspace | accepted | Deep Cut | 85 | 24 |

---

## tencent/hy4

Status: agent_finished. Final score: 0/700. Daily placement: 0.0%. Missed questions: 7. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- DIVE COMPLETE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## openai/gpt-6-luna

Status: agent_finished. Final score: 465/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Bánh pía.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Bánh pía | accepted | Deep Cut | 85 | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Madagascar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Kangoo Jumps.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kangoo Jumps | accepted | Deep Cut | 85 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · The Giver.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Giver | accepted | Rare | 60 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Salsa macha.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Salsa macha | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 21 |

---

## stepfun/step-5-preview

Status: agent_finished. Final score: 405/700. Daily placement: 92.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Pastizzi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pastizz | confirmation_required → Pastizzi | — | — | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Republic of the Congo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Republic of the Congo | accepted | Deep Cut | 85 | 17 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Rowing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Indoor rowing | confirmation_required → Rowing | — | — | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Blue Valentine.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Blue Valentine by NMIXX | confirmation_required → Blue Valentine | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Isot biber salçası | rejected | — | — | 19 |
| 2 | Ajvar | accepted | Rare | 60 | 15 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · FareHarbor.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | FareHarbor | accepted | Deep Cut | 85 | 23 |

---

## anthropic/claude-opus-5.5

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Pelmeni.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pelmeni | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Home Movies.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Home Movies | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Burpee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Burpees | confirmation_required → Burpee | — | — | 23 |
| 2 | Burpee | accepted | Schooler | 30 | 17 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Folded.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Folded | accepted | Schooler | 30 | 16 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 23 |

---

## minimax/minimax-m3.1-flash

Status: agent_finished. Final score: 335/700. Daily placement: 76.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Pączki.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pączek | confirmation_required → Pączki | — | — | 24 |
| 2 | pączek | confirmation_required → Pączki | — | — | 21 |
| 3 | pączek | confirmation_required → Pączki | — | — | 18 |
| 4 | pączek | confirmation_required → Pączki | — | — | 15 |
| 5 | pączek | confirmation_required → Pączki | — | — | 11 |
| 6 | Pączek | confirmation_required → Pączki | — | — | 9 |
| 7 | Pączek | confirmation_required → Pączki | — | — | 6 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Zły chłopcy | rejected | — | — | 24 |
| 2 | Moral Orel | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 10 points · Plankton · France.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile | rejected | — | — | 24 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Doubanjiang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Doubanjiang | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · FareHarbor.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tixster | rejected | — | — | 22 |
| 2 | FareHarbor | accepted | Deep Cut | 85 | 20 |

---

## tencent/hy4-preview

Status: agent_finished. Final score: 0/700. Daily placement: 0.0%. Missed questions: 7. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## openai/gpt-6.1-sol

Status: agent_finished. Final score: 495/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Xavier: Renegade Angel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Xavier: Renegade Angel | accepted | Rare | 60 | 20 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 17 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Cross-country skiing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Cross-country skiing | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Killah.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Killah | accepted | Deep Cut | 85 | 22 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Tock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 21 |

---

## openai/gpt-5.6-luna

Status: agent_finished. Final score: 440/700. Daily placement: 96.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Ecuador.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Kangoo Jumps.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kangoo Jumps | accepted | Deep Cut | 85 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Nokia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nokia | accepted | Schooler | 30 | 21 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · BookMyShow.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | BookMyShow | accepted | Rare | 60 | 21 |

---

## moonshotai/kimi-k3.1-pro

Status: agent_finished. Final score: 570/700. Daily placement: 99.79%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kubdari.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kubdari | accepted | Deep Cut | 85 | 16 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Seal jacks.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Seal jacks | accepted | Deep Cut | 85 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Taxes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Taxes by Geese | confirmation_required → Taxes | — | — | 14 |
| 2 | Taxes | accepted | Deep Cut | 85 | 10 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Tock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 20 |

---

## z-ai/glm-5.3

Status: agent_finished. Final score: 380/700. Daily placement: 87.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kroppkaka.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khachapuri adjarian | rejected | — | — | 24 |
| 2 | khanom krok | rejected | — | — | 20 |
| 3 | kroppkakor | confirmation_required → Kroppkaka | — | — | 10 |
| 4 | Kroppkaka | accepted | Deep Cut | 85 | 8 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · Smiling Friends.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Smiling Friends | accepted | Schooler | 30 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | skipping rope | confirmation_required → Jump rope | — | — | 24 |
| 2 | Jump rope | accepted | Schooler | 30 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Sports Car.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | that&#x27;s so true - Abby Roberts | rejected | — | — | 23 |
| 2 | Juna - Clairo | rejected | — | — | 17 |
| 3 | Sports car - Tate McRae | confirmation_required → Sports Car | — | — | 15 |
| 4 | Sports Car | accepted | Schooler | 30 | 12 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Rome2Rio.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rome2rio | accepted | Rare | 60 | 24 |

---

## deepseek/deepseek-v4-flash-0731

Status: agent_finished. Final score: 535/700. Daily placement: 99.58%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Drinky Crow Show.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Drinky Crow Show | accepted | Deep Cut | 85 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 16 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · SkiErg.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | SkiErg sprints | confirmation_required → SkiErg | — | — | 22 |
| 2 | SkiErg | accepted | Rare | 60 | 10 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Killah.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Killah | accepted | Deep Cut | 85 | 17 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 100 points · One In A Krillion · Sniffspot.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sniffspot | accepted | One In A Krillion | 100 | 5 |

---

## nvidia/nemotron-3-ultra-550b-a55b:free

Status: agent_finished. Final score: 205/700. Daily placement: 21.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 15 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · SkiErg.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ski ergometer | confirmation_required → SkiErg | — | — | 23 |
| 2 | SkiErg | accepted | Rare | 60 | 11 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Peerspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peerspace | accepted | Deep Cut | 85 | 12 |

---

## stealth/crouton-alpha

Status: agent_finished. Final score: 0/700. Daily placement: 0.0%. Missed questions: 7. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 2 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 2 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 2 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 2 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 2 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · rate_limit · 429 · Stealth · ModelRateLimitError
- PROMPT 5 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · rate_limit · 429 · Stealth · ModelRateLimitError
- PROMPT 7 OF 7 · rate_limit · 429 · Stealth · ModelRateLimitError
- PROMPT 7 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · provider_error · 502 · Stealth · ModelProviderError
- DIVE COMPLETE · provider_error · 502 · Stealth · ModelProviderError
- DIVE COMPLETE · provider_error · 502 · Stealth · ModelProviderError
- DIVE COMPLETE · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 2 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 3 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 4 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 5 OF 7 · rate_limit · rate_limit · 429 · Stealth · ModelRateLimitError
- PROMPT 5 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 6 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- PROMPT 7 OF 7 · provider_error · provider_error · 502 · Stealth · ModelProviderError
- DIVE COMPLETE · provider_error · provider_error · 502 · Stealth · ModelProviderError

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## nvidia/nemotron-3.5-super-vl:free

Status: agent_finished. Final score: 360/700. Daily placement: 83.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Manti.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | manti | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 14 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Papua New Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Papua New Guinea | accepted | Rare | 60 | 15 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rucking | accepted | Rare | 60 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · HotelTonight.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | HotelTonight | accepted | Rare | 60 | 18 |

---

## tencent/hy3

Status: agent_finished. Final score: 340/700. Daily placement: 78.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Lukhmi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | lukhmi | accepted | Deep Cut | 85 | 5 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · Assy McGee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Assy McGee | accepted | Deep Cut | 85 | 13 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Slackline jumping jacks | rejected | — | — | 15 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Pindjur.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pindjur | accepted | Deep Cut | 85 | 17 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Campspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Campspace | accepted | Deep Cut | 85 | 5 |

---

## meta/muse-spark-1.3-contributor

Status: agent_finished. Final score: 415/700. Daily placement: 94.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Bierock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Bierock | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Mission Hill.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mission Hill | accepted | Rare | 60 | 17 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 14 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Zumba.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | zumba | accepted | Schooler | 30 | 16 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Bara Bada Bastu.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Espresso Macchiato | rejected | — | — | 16 |
| 2 | Bara Bada Bastu | accepted | Rare | 60 | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 15 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Omio.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Omio | accepted | Rare | 60 | 16 |

---

## anthropic/claude-haiku-5.5

Status: agent_finished. Final score: 420/700. Daily placement: 95.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Gujiya.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gujiya | accepted | Deep Cut | 85 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Home Movies.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kaput Krunch Mesoscopic Harbor Dispatch | rejected | — | — | 21 |
| 2 | Home Movies | accepted | Rare | 60 | 17 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kayaking on glacial meltwater | rejected | — | — | 22 |
| 2 | Aqua jogging | accepted | Rare | 60 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Ordinary.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ordinary | accepted | Plankton | 10 | 21 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hostelworld.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Bookaroo | rejected | — | — | 23 |
| 2 | Hostelworld | accepted | Rare | 60 | 18 |

---

## xiaomi/mimo-v2.6-flash

Status: agent_finished. Final score: 360/700. Daily placement: 83.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Khuushuur.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khuushuur | accepted | Deep Cut | 85 | 16 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Xavier: Renegade Angel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Xavier: Renegade Angel | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 8 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Burpee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Burpee | accepted | Schooler | 30 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Manchild.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Manchild | accepted | Plankton | 10 | 21 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 30 points · Schooler · OpenTable.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 23 |

---

## deepseek/deepseek-v4-flash

Status: agent_finished. Final score: 300/700. Daily placement: —%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khachapuri.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khachapuri | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 16 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | trampoline rebounding | rejected | — | — | 15 |
| 2 | battle rope waves | confirmation_required → Battle ropes | — | — | 9 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 17 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Turo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turo | accepted | Rare | 60 | 13 |

---

## anthropic/claude-sonnet-5.5

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Pastel de nata.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pastéis de nata | confirmation_required → Pastel de nata | — | — | 21 |
| 2 | Pastel de nata | accepted | Rare | 60 | 16 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Stair climbing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Stair climbing | accepted | Schooler | 30 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Just Keep Watching.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ordinary Fog | rejected | — | — | 22 |
| 2 | Just Keep Watching | accepted | Schooler | 30 | 16 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Romesco.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tripcase | rejected | — | — | 23 |
| 2 | Hipcamp | accepted | Rare | 60 | 19 |

---

## moonshotai/kimi-k3

Status: agent_finished. Final score: 495/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kreplach.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kreplach | accepted | Deep Cut | 85 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Central African Republic.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Central African Republic | accepted | Deep Cut | 85 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Man I Need.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Man I Need | accepted | Plankton | 10 | 20 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Pilpelchuma.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pilpelchuma | accepted | Deep Cut | 85 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · DesignMyNight.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | DesignMyNight | accepted | Deep Cut | 85 | 16 |

---

## google/gemini-3.8-flash

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knish.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 17 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Duckman: Private Dick/Family Man.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Duckman | confirmation_required → Duckman: Private Dick/Family Man | — | — | 20 |
| 2 | Duckman: Private Dick/Family Man | accepted | Rare | 60 | 15 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 6 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Nordic walking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nordic walking | accepted | Rare | 60 | 17 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hostelworld.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 19 |

---

## upstage/solar-mini4

Status: agent_finished. Final score: 170/700. Daily placement: 10.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Bananas Foster | rejected | — | — | 23 |
| 2 | Bananas Foster | unconfirmed | — | — | 20 |
| 3 | Curry | rejected | — | — | 17 |
| 4 | Tiramisu | rejected | — | — | 13 |
| 5 | Tiramisu | unconfirmed | — | — | 11 |
| 6 | Pierogi | accepted | Schooler | 30 | 7 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 10 points · Plankton · The Simpsons.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Murder, She Wrote | rejected | — | — | 24 |
| 2 | The Simpsons | accepted | Plankton | 10 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Turkey.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkey | accepted | Schooler | 30 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Burpee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | burpees | confirmation_required → Burpee | — | — | 22 |
| 2 | burpees | confirmation_required → Burpee | — | — | 19 |
| 3 | burpees | confirmation_required → Burpee | — | — | 15 |
| 4 | burpees | confirmation_required → Burpee | — | — | 9 |
| 5 | burpees | confirmation_required → Burpee | — | — | 6 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Houdini | rejected | — | — | 23 |
| 2 | Miracle | rejected | — | — | 16 |
| 3 | Midnight City | rejected | — | — | 14 |
| 4 | Marilyn Monroe | rejected | — | — | 12 |
| 5 | Do I Do | rejected | — | — | 10 |
| 6 | Pillow Talk | rejected | — | — | 7 |
| 7 | Midnight City | rejected | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 10 points · Plankton · Sriracha.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sriracha | accepted | Plankton | 10 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Klook.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klook | accepted | Rare | 60 | 23 |

---

## google/gemini-4-argon

Status: agent_finished. Final score: 415/700. Daily placement: 94.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Pirozhki.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pirozhki | accepted | Rare | 60 | 20 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Mission Hill.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mission Hill | accepted | Rare | 60 | 20 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Burkina Faso.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Mountain climber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mountain climbers | confirmation_required → Mountain climber | — | — | 20 |
| 2 | Mountain climber | accepted | Schooler | 30 | 16 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Baptized In Fear.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Baptized in Fear | accepted | Rare | 60 | 19 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Mindbody.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mindbody | accepted | Rare | 60 | 21 |

---

## nvidia/nemotron-3.5-lightning:free

Status: agent_finished. Final score: 325/700. Daily placement: 70.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- SURFACE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Empanada.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 20 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Italy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Italy | accepted | Schooler | 30 | 17 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Inline skating.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | inline skating | accepted | Rare | 60 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Luna - Neon Nights (2025) | rejected | — | — | 20 |
| 2 | Mitski - My Love Mine All Mine (2025) | rejected | — | — | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Gochujang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peri-peri sauce | confirmation_required → Peri-peri | — | — | 21 |
| 2 | gochujang | accepted | Rare | 60 | 12 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Rail Europe.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rail Europe | accepted | Deep Cut | 85 | 19 |

---

## xiaomi/mimo-v2.6-pro

Status: agent_finished. Final score: 515/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Karelian pasty.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Karelian pasty | accepted | Deep Cut | 85 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Drinky Crow Show.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Drinky Crow Show | accepted | Deep Cut | 85 | 15 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Fartlek.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | fartlek | accepted | Deep Cut | 85 | 17 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · How It&#x27;s Done.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mr. Electric Blue - Saja Boys | rejected | — | — | 20 |
| 2 | How It&#x27;s Done - HUNTR/X | confirmation_required → How It&#x27;s Done | — | — | 13 |
| 3 | How It&#x27;s Done | accepted | Schooler | 30 | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Romesco.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · FareHarbor.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | FareHarbor | accepted | Deep Cut | 85 | 16 |

---

## openai/gpt-6.1-terra

Status: agent_finished. Final score: 495/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

Diagnostics:
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Cross-country skiing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · What Was That.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | What Was That by Lorde | unconfirmed | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Pitchup.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pitchup | accepted | Deep Cut | 85 | 21 |

---

## z-ai/glm-5.2

Status: agent_finished. Final score: 390/700. Daily placement: 90.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Tangyuan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | tangyuan | accepted | Rare | 60 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Frisky Dingo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Frisky Dingo | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Tanzania.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tanzania | accepted | Rare | 60 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Kettlebell swing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kettlebell swings | confirmation_required → Kettlebell swing | — | — | 23 |
| 2 | Kettlebell swing | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Gnarly.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | GNARLY by KATSEYE | confirmation_required → Gnarly | — | — | 18 |
| 2 | GNARLY by KATSEYE | confirmation_required → Gnarly | — | — | 15 |
| 3 | Gnarly | accepted | Schooler | 30 | 13 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

---

## nvidia/nemotron-3.5-super-vl

Status: agent_finished. Final score: 395/700. Daily placement: 91.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · VersaClimber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | VersaClimber | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Ordinary.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ordinary | accepted | Plankton | 10 | 17 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Klook.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klook | accepted | Rare | 60 | 23 |

---

## deepseek/deepseek-v4-pro-0813

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Syrniki | rejected | — | — | 23 |
| 2 | Khinkali | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 14 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | aqua jogging | accepted | Rare | 60 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 18 |

---

## qwen/qwen3.8-flash

Status: agent_finished. Final score: 350/700. Daily placement: 79.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 16 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Space Ghost Coast to Coast.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Space Ghost Coast to Coast | accepted | Rare | 60 | 18 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · SkiErg.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ski erg intervals | confirmation_required → SkiErg | — | — | 17 |
| 2 | SkiErg | accepted | Rare | 60 | 12 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Giggster.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Giggster | accepted | Deep Cut | 85 | 16 |

---

## dots-studio/dots-3-note-preview:free

Status: agent_finished. Final score: 265/700. Daily placement: 45.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Stuffed squash blossoms.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Stuffed zucchini blossoms | confirmation_required → Stuffed squash blossoms | — | — | 14 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Primal.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Primal | accepted | Rare | 60 | 17 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Finland.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Finland | accepted | Schooler | 30 | 10 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 10 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 30 points · Schooler · OpenTable.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 18 |

---

## qwen/qwen3.8-27b

Status: agent_finished. Final score: 350/700. Daily placement: 79.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Durian-filled cannoli | rejected | — | — | 20 |
| 2 | mushroom-stuffed morel | rejected | — | — | 13 |
| 3 | foie gras-stuffed oyster | rejected | — | — | 10 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Harvey Birdman, Attorney at Law.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harvey Birdman: Attorney at Law | unconfirmed | — | — | 16 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Papua New Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Papua New Guinea | accepted | Rare | 60 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rucking | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Lose Control | rejected | — | — | 22 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Rouille.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rouille | accepted | Deep Cut | 85 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Giggster.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Giggster | accepted | Deep Cut | 85 | 18 |

---

## minimax/minimax-m3

Status: agent_finished. Final score: 440/700. Daily placement: 96.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Jiaozi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jiaozi | accepted | Rare | 60 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · Archer.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Ivory Coast.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Côte d&#x27;Ivoire | confirmation_required → Ivory Coast | — | — | 24 |
| 2 | Ivory Coast | accepted | Deep Cut | 85 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Gimme Dat.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gimme Dat | accepted | Deep Cut | 85 | 24 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ponzu | rejected | — | — | 24 |
| 2 | Harissa | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Omio.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Omio | accepted | Rare | 60 | 24 |

---

## google/gemini-3-flash-preview

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Duckman | confirmation_required → Duckman: Private Dick/Family Man | — | — | 24 |
| 2 | Moral Orel | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Central African Republic.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Central African Republic | accepted | Deep Cut | 85 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Nordic walking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nordic walking | accepted | Rare | 60 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Houdini | rejected | — | — | 24 |
| 2 | Texas Hold &#x27;Em | rejected | — | — | 21 |
| 3 | Sailor Song | rejected | — | — | 19 |
| 4 | Squid Game | rejected | — | — | 17 |
| 5 | Hiss | rejected | — | — | 15 |
| 6 | Apple | rejected | — | — | 12 |
| 7 | The Emptiness Machine | rejected | — | — | 10 |
| 8 | APT. | rejected | — | — | 7 |
| 9 | Who | unconfirmed | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

---

## openai/gpt-6-luna-pro

Status: agent_finished. Final score: 495/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kibinai.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kibinai | accepted | Deep Cut | 85 | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · The Giver.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Giver by Chappell Roan | confirmation_required → The Giver | — | — | 13 |
| 2 | The Giver by Chappell Roan | confirmation_required → The Giver | — | — | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 19 |

---

## deepseek/deepseek-v4-pro

Status: agent_finished. Final score: 355/700. Daily placement: 80.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 16 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rebounding.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | rebounding | accepted | Rare | 60 | 15 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · ExtraL.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ExtraL | accepted | Rare | 60 | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Gochujang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | gochujang | accepted | Rare | 60 | 16 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hostelworld.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 17 |

---

## google/gemini-3.1-flash-lite

Status: agent_finished. Final score: 330/700. Daily placement: 73.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Oblongs.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Oblongs | accepted | Rare | 60 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Myanmar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Myanmar | accepted | Rare | 60 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jump rope | accepted | Schooler | 30 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile (Live at Las Vegas) | rejected | — | — | 24 |
| 2 | Espresso (Live from Coachella) | rejected | — | — | 22 |
| 3 | Good Luck, Babe! (Live from London) | rejected | — | — | 19 |
| 4 | The Emptiness Machine (Live at Wembley) | rejected | — | — | 17 |
| 5 | Taste (Live from Madison Square Garden) | rejected | — | — | 15 |
| 6 | Stargazer (Live from Paris) | rejected | — | — | 12 |
| 7 | APT. (Live from Seoul) | rejected | — | — | 10 |
| 8 | Solita (Live at the Grammy Museum) | rejected | — | — | 7 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · GetYourGuide.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | GetYourGuide | accepted | Rare | 60 | 23 |

---

## anthropic/claude-sonnet-5

Status: agent_finished. Final score: 440/700. Daily placement: 96.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Superjail!.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Superjail! | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Race walking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jumping rope with double-unders | rejected | — | — | 22 |
| 2 | Race walking | accepted | Rare | 60 | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Undressed.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Messy by Lola Young | rejected | — | — | 23 |
| 2 | Undressed by sombr | confirmation_required → Undressed | — | — | 20 |
| 3 | Undressed by sombr | confirmation_required → Undressed | — | — | 18 |
| 4 | Undressed | accepted | Schooler | 30 | 15 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · ResortPass.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ResortPass | accepted | Deep Cut | 85 | 23 |

---

## google/gemma-4-31b-it

Status: agent_finished. Final score: 270/700. Daily placement: 47.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros | unconfirmed | — | — | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Namibia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Sprinting.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kappaswimming | confirmation_required → Swimming | — | — | 22 |
| 2 | Sprinting | accepted | Schooler | 30 | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | None | rejected | — | — | 24 |
| 2 | Since it is currently 2024, no such song exists. | rejected | — | — | 22 |
| 3 | Unknown | rejected | — | — | 20 |
| 4 | None | rejected | — | — | 17 |
| 5 | N/A | rejected | — | — | 15 |
| 6 | The Impossible Dream | rejected | — | — | 13 |
| 7 | None | rejected | — | — | 11 |
| 8 | Future Echoes | rejected | — | — | 9 |
| 9 | Stardust Horizon | rejected | — | — | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Gochujang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gochujang | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Turo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turo | accepted | Rare | 60 | 24 |

---

## qwen/qwen3.7-flash

Status: agent_finished. Final score: 90/700. Daily placement: 1.0%. Missed questions: 5. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Metalocalypse.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 6 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 30 points · Schooler · Kayak.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | KAYAK | accepted | Schooler | 30 | 5 |

---

## upstage/solar-pro4

Status: agent_finished. Final score: 245/700. Daily placement: 36.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Samosa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | samosa | accepted | Schooler | 30 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 10 points · Plankton · South Park.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | South Park | accepted | Plankton | 10 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Niger | rejected | — | — | 23 |
| 2 | Niger | unconfirmed | — | — | 21 |
| 3 | Argentina | rejected | — | — | 19 |
| 4 | Iran | rejected | — | — | 16 |
| 5 | Niger | rejected | — | — | 13 |
| 6 | Mali | rejected | — | — | 9 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | aquajogging | confirmation_required → Aqua jogging | — | — | 23 |
| 2 | Aqua jogging | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | A Bar Song (Tipsy) | rejected | — | — | 23 |
| 2 | Espresso | rejected | — | — | 20 |
| 3 | Birds of a Feather | rejected | — | — | 17 |
| 4 | Beautiful as the Sun | rejected | — | — | 15 |
| 5 | Water (Taloi Havini Reimagining remix) | rejected | — | — | 12 |
| 6 | Stick Season | rejected | — | — | 10 |
| 7 | Not Like Us | rejected | — | — | 7 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Sambal.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | jnana | rejected | — | — | 24 |
| 2 | Ají amarillo paste | rejected | — | — | 21 |
| 3 | sambal | accepted | Rare | 60 | 19 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · TheFork.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Corporette | rejected | — | — | 23 |
| 2 | Bookatable | confirmation_required → TheFork | — | — | 21 |
| 3 | TheFork | accepted | Deep Cut | 85 | 18 |

---

## google/gemma-4-26b-a4b-it

Status: agent_finished. Final score: 360/700. Daily placement: 83.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- DIVE COMPLETE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Baklava.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Baklava | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Yemen.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Libya | rejected | — | — | 24 |
| 2 | Greece | rejected | — | — | 22 |
| 3 | Yemen | accepted | Deep Cut | 85 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Step aerobics.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Elliptical training | confirmation_required → Elliptical | — | — | 23 |
| 2 | Burpees | confirmation_required → Burpee | — | — | 21 |
| 3 | Kettlebell swings | confirmation_required → Kettlebell swing | — | — | 19 |
| 4 | Elliptical training | confirmation_required → Elliptical | — | — | 17 |
| 5 | Burpees | confirmation_required → Burpee | — | — | 14 |
| 6 | Step aerobics | accepted | Rare | 60 | 12 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | None | rejected | — | — | 24 |
| 2 | No such song exists | rejected | — | — | 20 |
| 3 | Houdini by Dua Lipa | rejected | — | — | 18 |
| 4 | APT. by ROSÉ &amp; Bruno Mars | rejected | — | — | 16 |
| 5 | Disease by Lady Gaga | rejected | — | — | 13 |
| 6 | Die With A Smile by Lady Gaga and Bruno Mars | rejected | — | — | 11 |
| 7 | Espresso by Sabrina Carpenter | rejected | — | — | 8 |
| 8 | Apple by Charli xcx | rejected | — | — | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 10 points · Plankton · Booking.com.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 24 |

---

## google/gemini-3.7-flash

Status: agent_finished. Final score: 415/700. Daily placement: 94.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knish.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Knish | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Mission Hill.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mission Hill | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Shadow boxing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | shadowboxing | confirmation_required → Shadow boxing | — | — | 21 |
| 2 | Shadow boxing | accepted | Rare | 60 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Sports Car.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sports car | accepted | Schooler | 30 | 11 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 21 |

---

## openai/gpt-6-astra

Status: agent_finished. Final score: 470/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Mission Hill.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mission Hill | accepted | Rare | 60 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rebounding.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rebounding | accepted | Rare | 60 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Shadow Of A Man.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Shadow of a Man | accepted | Deep Cut | 85 | 19 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 19 |

---

## openai/gpt-oss-120b

Status: agent_finished. Final score: 410/700. Daily placement: 93.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Mochi ice cream.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mochi ice cream | accepted | Rare | 60 | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Yemen.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Yemen | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Battle rope slams | confirmation_required → Battle ropes | — | — | 23 |
| 2 | Battle ropes | accepted | Rare | 60 | 13 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Midnight Echoes by Luna Vale | rejected | — | — | 22 |
| 2 | Solar Flare by Aurora Nova | rejected | — | — | 19 |
| 3 | Neon Horizons by Echo Drift | rejected | — | — | 16 |
| 4 | Starlight Pulse by Luna Reverie | rejected | — | — | 13 |
| 5 | Silicon Dreams by Chrono Pulse | rejected | — | — | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 21 |

---

## stepfun/step-3.7-flash

Status: agent_finished. Final score: 295/700. Daily placement: 58.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · Assy McGee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Assy McGee | accepted | Deep Cut | 85 | 17 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Finland.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Finland | accepted | Schooler | 30 | 6 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 9 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 13 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Skiplagged.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Skiplagged | accepted | Rare | 60 | 14 |

---

## openai/gpt-5.6-sol

Status: agent_finished. Final score: 545/700. Daily placement: 99.63%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Klepon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klepon | accepted | Deep Cut | 85 | 20 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · VersaClimber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | VersaClimber | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Dum, Dumb, and Dumber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | All the Way by BigXthaPlug and Bailey Zimmerman | rejected | — | — | 21 |
| 2 | Dum, Dumb, and Dumber by Lil Baby, Young Thug and Future | confirmation_required → Dum, Dumb, and Dumber | — | — | 16 |
| 3 | Dum, Dumb, and Dumber | accepted | Deep Cut | 85 | 14 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Dockwa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Dockwa | accepted | Deep Cut | 85 | 21 |

---

## mistralai/mistral-nemo

Status: agent_finished. Final score: 180/700. Daily placement: 12.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Strawberry Pop-Tart | confirmation_required → Pop-Tart | — | — | 19 |
| 2 | Churro with chili-caramel filling | rejected | — | — | 14 |
| 3 | Raspberry and cream-filled donut | rejected | — | — | 11 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · Archer.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Ren &amp; Stimpy Show | rejected | — | — | 23 |
| 2 | Invader Zim | rejected | — | — | 19 |
| 3 | Archer | accepted | Schooler | 30 | 15 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Switzerland | rejected | — | — | 23 |
| 2 | Liechtenstein | rejected | — | — | 15 |
| 3 | San Marino | rejected | — | — | 8 |
| 4 | Malta | rejected | — | — | 5 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · High knees.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | High Knees | accepted | Schooler | 30 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Glitter in Reverse by Bad Bunny | rejected | — | — | 19 |
| 2 | La Diabla by Rosalía | rejected | — | — | 16 |
| 3 | La Diabla by Rosalía | unconfirmed | — | — | 9 |
| 4 | Heart of Glass by St. Vincent | rejected | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Gochujang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sriracha Mayo | rejected | — | — | 22 |
| 2 | Gochujang | accepted | Rare | 60 | 12 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Eventbrite.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tickettailor | confirmation_required → Ticket Tailor | — | — | 17 |
| 2 | Eventbrite | accepted | Rare | 60 | 8 |

---

## google/gemini-2.5-flash-lite

Status: agent_finished. Final score: 230/700. Daily placement: 30.0%. Missed questions: 0. Scorecard recovery: False.

Diagnostics:
- SURFACE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- DIVE COMPLETE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Empanada.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Empanada | accepted | Schooler | 30 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 10 points · Plankton · Rick and Morty.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Poland.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Poland | accepted | Schooler | 30 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jumping jacks.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jumping Jacks | accepted | Schooler | 30 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Beautiful Things.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | A Bar Song | rejected | — | — | 24 |
| 2 | Already Dead | rejected | — | — | 21 |
| 3 | Beautiful Things | accepted | Rare | 60 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 10 points · Plankton · Marinara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Marinara | accepted | Plankton | 10 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · SeatGeek.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Etsy | rejected | — | — | 24 |
| 2 | AllTrails | rejected | — | — | 22 |
| 3 | SeatGeek | accepted | Rare | 60 | 17 |

---

## deepseek/deepseek-v3.2

Status: agent_finished. Final score: 325/700. Daily placement: 70.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khachapuri (Georgian cheese-filled bread) | rejected | — | — | 22 |
| 2 | Baozi (Chinese steamed bun with meat filling) | rejected | — | — | 19 |
| 3 | Pirozhki (Russian stuffed pastry) | rejected | — | — | 15 |
| 4 | Ravioli (Italian pasta with filling) | rejected | — | — | 12 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Critic.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Critic | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Paraguay.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Paraguay | accepted | Rare | 60 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Underwater hockey.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Underwater hockey | accepted | Deep Cut | 85 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kukushka by Molchat Doma 2025 | rejected | — | — | 23 |
| 2 | Unison by Bicep 2026 | rejected | — | — | 19 |
| 3 | Plankton by The Comet Is Coming 2025 | rejected | — | — | 15 |
| 4 | Razor&#x27;s Edge by IDLES 2025 | rejected | — | — | 11 |
| 5 | Fission Dream by Black Country, New Road 2025 | rejected | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Fermented shrimp paste (Bagoong) | rejected | — | — | 22 |
| 2 | Harissa | accepted | Rare | 60 | 19 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Klook.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klook | accepted | Rare | 60 | 23 |

---

## anthropic/claude-fable-5.1

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 14 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Rowing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Perfumito Nuevo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Perfumito Nuevo | accepted | Rare | 60 | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hostelworld.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 21 |

---

## qwen/qwen3.6-35b-a3b

Status: agent_finished. Final score: 230/700. Daily placement: 30.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Bombolone.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | bomboloni | confirmation_required → Bombolone | — | — | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Aqua Teen Hunger Force.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua Teen Hunger Force | accepted | Rare | 60 | 8 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Fartlek.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Fartlek | accepted | Deep Cut | 85 | 19 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## google/gemini-2.5-flash

Status: agent_finished. Final score: 380/700. Daily placement: 87.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- DIVE COMPLETE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kishka.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kishka | accepted | Deep Cut | 85 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Metalocalypse.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Metalocalypse | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · New Zealand.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | New Zealand | accepted | Rare | 60 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | jump rope | accepted | Schooler | 30 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | I will not let you go | rejected | — | — | 24 |
| 2 | I can&#x27;t imagine a future without you | rejected | — | — | 22 |
| 3 | I will love you always | rejected | — | — | 20 |
| 4 | Future Nostalgia (The Moonlight Edition) | rejected | — | — | 18 |
| 5 | Something About Us | rejected | — | — | 16 |
| 6 | I can&#x27;t believe it&#x27;s not butter | rejected | — | — | 14 |
| 7 | The Sound of Silence (Simon &amp; Garfunkel, 2026 Remaster) | rejected | — | — | 12 |
| 8 | I can&#x27;t imagine a future without you | rejected | — | — | 10 |
| 9 | I will never let you go | rejected | — | — | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Sambal oelek.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sambal Oelek | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Setmore.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | HoppyCopy | rejected | — | — | 24 |
| 2 | Setmore | accepted | Deep Cut | 85 | 21 |

---

## google/gemini-3.5-flash-lite

Status: agent_finished. Final score: 490/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Xtacles.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Head Hunters | rejected | — | — | 23 |
| 2 | The Xtacles | accepted | Deep Cut | 85 | 20 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Zambia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Uganda | rejected | — | — | 23 |
| 2 | Zambia | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aquajogging | confirmation_required → Aqua jogging | — | — | 24 |
| 2 | Aqua jogging | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Chroma Drift.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Lumina | rejected | — | — | 24 |
| 2 | Vapor Trails | rejected | — | — | 21 |
| 3 | Starlight Echoes | rejected | — | — | 18 |
| 4 | Neon Abyss | rejected | — | — | 16 |
| 5 | Chrono Drift | confirmation_required → Chroma Drift | — | — | 13 |
| 6 | Chroma Drift | accepted | Deep Cut | 85 | 11 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · ASAP Tickets.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Asaptickets | confirmation_required → ASAP Tickets | — | — | 24 |
| 2 | ASAP Tickets | accepted | Deep Cut | 85 | 21 |

---

## openai/gpt-6-sol

Status: agent_finished. Final score: 520/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Klepon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klepon | accepted | Deep Cut | 85 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Drinky Crow Show.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Drinky Crow Show | accepted | Deep Cut | 85 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · The Beast.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Beast by Lady Gaga | confirmation_required → The Beast | — | — | 21 |
| 2 | The Beast | accepted | Deep Cut | 85 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 22 |

---

## x-ai/grok-4.7

Status: agent_finished. Final score: 265/700. Daily placement: 45.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 17 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Xavier: Renegade Angel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Xavier: Renegade Angel | accepted | Rare | 60 | 5 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · VersaClimber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | VersaClimber | accepted | Rare | 60 | 16 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Swimply.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Swimply | accepted | Deep Cut | 85 | 15 |

---

## anthropic/claude-opus-5

Status: agent_finished. Final score: 410/700. Daily placement: 93.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khachapuri.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khachapuri | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Central African Republic.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Central African Republic | accepted | Deep Cut | 85 | 16 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Stair climbing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nordic skiing on a SkiErg | rejected | — | — | 23 |
| 2 | rope jumping | confirmation_required → Jump rope | — | — | 19 |
| 3 | Stair climbing | accepted | Schooler | 30 | 10 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Anxiety.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Anxiety by Doechii | confirmation_required → Anxiety | — | — | 22 |
| 2 | Anxiety | accepted | Schooler | 30 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Ajika.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajika | accepted | Deep Cut | 85 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

---

## openai/gpt-4o-mini

Status: agent_finished. Final score: 305/700. Daily placement: 64.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Ravioli.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pork bun | confirmation_required → Bao | — | — | 23 |
| 2 | Ravioli | accepted | Schooler | 30 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 10 points · Plankton · Rick and Morty.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Malaysia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Iceland | rejected | — | — | 24 |
| 2 | Portugal | rejected | — | — | 21 |
| 3 | Malaysia | accepted | Rare | 60 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | AI Anthem | rejected | — | — | 23 |
| 2 | Techno Dreams | rejected | — | — | 20 |
| 3 | Ecstasy Peaks | rejected | — | — | 18 |
| 4 | Euphoria Rising | rejected | — | — | 15 |
| 5 | Rhythm of Tomorrow | rejected | — | — | 12 |
| 6 | Future Soundscape | rejected | — | — | 9 |
| 7 | Melodic Reflections | unconfirmed | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Campspot.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Campspot | accepted | Deep Cut | 85 | 24 |

---

## anthropic/claude-sonnet-4.6

Status: agent_finished. Final score: 275/700. Daily placement: 50.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 24 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Burpee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Burpee | accepted | Schooler | 30 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Manchmal (Luciano &amp; Capital Bra) | rejected | — | — | 22 |
| 2 | Luther (Kendrick Lamar &amp; SZA) | rejected | — | — | 19 |
| 3 | Timeless (The Weeknd &amp; Playboi Carti) | rejected | — | — | 16 |
| 4 | Die With A Smile (Lady Gaga &amp; Bruno Mars) | rejected | — | — | 13 |
| 5 | Apt. (Rose &amp; Bruno Mars) | rejected | — | — | 9 |
| 6 | Now and Then (Beatles) | rejected | — | — | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 10 points · Plankton · Sriracha.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sriracha | accepted | Plankton | 10 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Klook.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klook | accepted | Rare | 60 | 23 |

---

## cohere/north-mini-code:free

Status: agent_finished. Final score: 315/700. Daily placement: 68.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Maultaschen.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Maultaschen | accepted | Deep Cut | 85 | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Beetroot ketchup.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | beet ketchup | confirmation_required → Beetroot ketchup | — | — | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Peerspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peerspace | accepted | Deep Cut | 85 | 12 |

---

## anthropic/claude-opus-4.8

Status: agent_finished. Final score: 325/700. Daily placement: 70.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jump rope double-unders | rejected | — | — | 22 |
| 2 | Jumping jacks burpees mountain climbers | rejected | — | — | 19 |
| 3 | Jacobs ladder climber machine | rejected | — | — | 15 |
| 4 | VersaClimber interval sprints | rejected | — | — | 12 |
| 5 | SkiErg tabata intervals | rejected | — | — | 8 |
| 6 | Jacobs ladder sprints reverse | rejected | — | — | 5 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Nokia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Anxiety by Doechii | confirmation_required → Anxiety | — | — | 22 |
| 2 | Messy by Lola Young | rejected | — | — | 19 |
| 3 | Taste by Sabrina Carpenter | rejected | — | — | 16 |
| 4 | Anxiety by Doechii | confirmation_required → Anxiety | — | — | 12 |
| 5 | Nokia by Drake | confirmation_required → Nokia | — | — | 8 |
| 6 | Nokia | accepted | Schooler | 30 | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ajvar | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

---

## openai/gpt-5.6-terra

Status: agent_finished. Final score: 495/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · What Was That.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | What Was That | accepted | Rare | 60 | 21 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Splacer.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Splacer | accepted | Deep Cut | 85 | 21 |

---

## qwen/qwen3.8-max-0902

Status: agent_finished. Final score: 350/700. Daily placement: 79.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Xiaolongbao.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | xiaolongbao | accepted | Rare | 60 | 15 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Brothers Grunt.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Brothers Grunt | accepted | Deep Cut | 85 | 9 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Battle ropes | accepted | Rare | 60 | 13 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 13 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Tock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 13 |

---

## openai/gpt-oss-20b

Status: agent_finished. Final score: 260/700. Daily placement: 43.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mochi with azuki bean paste | rejected | — | — | 23 |
| 2 | Bánh khọt with shrimp filling | rejected | — | — | 19 |
| 3 | Karelian pasties with fish filling | rejected | — | — | 16 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 30 points · Schooler · Madagascar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Madagascar | accepted | Schooler | 30 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Plyometric box jumps | confirmation_required → Box jump | — | — | 24 |
| 2 | Weighted jump rope with ankle straps | rejected | — | — | 20 |
| 3 | Double-unders with a weighted belt | rejected | — | — | 13 |
| 4 | Sled shuffles | rejected | — | — | 8 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Stargaze Elixir by The Midnight Lurkers (2025) | rejected | — | — | 18 |
| 2 | Nebula Threads by Royal Nothing (2026) | rejected | — | — | 12 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Salsa de chile de árbol.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Salsa de chile de árbol | accepted | Deep Cut | 85 | 18 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Couchsurfing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Couchsurfing | accepted | Deep Cut | 85 | 24 |

---

## anthropic/claude-sonnet-4.5

Status: agent_finished. Final score: 355/700. Daily placement: 81.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Namibia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Namibia | accepted | Rare | 60 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | aqua jogging | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | APT. | rejected | — | — | 23 |
| 2 | Die With A Smile | rejected | — | — | 17 |
| 3 | Sailor Song | rejected | — | — | 12 |
| 4 | Timeless | rejected | — | — | 8 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Romesco.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Romesco | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Setmore.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Setmore | accepted | Deep Cut | 85 | 22 |

---

## anthropic/claude-haiku-4.5

Status: agent_finished. Final score: 235/700. Daily placement: 32.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Pierogi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · BoJack Horseman.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Libya | rejected | — | — | 23 |
| 2 | Tunisia | rejected | — | — | 20 |
| 3 | Mauritania | rejected | — | — | 16 |
| 4 | Algeria | rejected | — | — | 13 |
| 5 | Mali | rejected | — | — | 9 |
| 6 | Sudan | rejected | — | — | 6 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Burpee.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rowing machine | confirmation_required → Rowing | — | — | 24 |
| 2 | Ergometer | confirmation_required → Rowing | — | — | 21 |
| 3 | Burpee | accepted | Schooler | 30 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Espresso by Sabrina Carpenter | rejected | — | — | 21 |
| 2 | Greedy by Tyla | rejected | — | — | 19 |
| 3 | Snap by Rosa Linn | rejected | — | — | 16 |
| 4 | Flowers by Miley Cyrus | rejected | — | — | 14 |
| 5 | Love Grows by Eddie Vedder | rejected | — | — | 10 |
| 6 | Beautiful Things by Benson Boone | rejected | — | — | 8 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Tkemali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Adjika | confirmation_required → Ajika | — | — | 23 |
| 2 | Tkemali | accepted | Deep Cut | 85 | 20 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Viator.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Viator | accepted | Rare | 60 | 22 |

---

## mistralai/mistral-large-4-0

Status: agent_finished. Final score: 155/700. Daily placement: 8.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Xavier: Renegade Angel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Xavier: Renegade Angel | accepted | Rare | 60 | 17 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Golden.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sodium Lights by The Prismatics | rejected | — | — | 19 |
| 2 | Golden by Huntrix | confirmation_required → Golden | — | — | 10 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Ajika.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Adjika | confirmation_required → Ajika | — | — | 11 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free

Status: agent_finished. Final score: 205/700. Daily placement: 21.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- SURFACE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Börek.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | burek | confirmation_required → Börek | — | — | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Peerspace.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Peerspace | accepted | Deep Cut | 85 | 14 |

---

## moonshotai/kimi-k2.6

Status: agent_finished. Final score: 230/700. Daily placement: 30.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Drinky Crow Show.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Drinky Crow Show | accepted | Deep Cut | 85 | 5 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 5 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## particle-ai/particle-1

Status: agent_finished. Final score: 490/700. Daily placement: 99.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kueh tutu.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kueh tutu | accepted | Deep Cut | 85 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · VersaClimber.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | VersaClimber | accepted | Rare | 60 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · The Subway.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Love Me Not by Ravyn Lenae | rejected | — | — | 21 |
| 2 | The Subway by Chappell Roan | confirmation_required → The Subway | — | — | 18 |
| 3 | The Subway | accepted | Schooler | 30 | 14 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Campspot.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Campspot | accepted | Deep Cut | 85 | 23 |

---

## qwen/qwen3.5-9b

Status: agent_finished. Final score: 60/700. Daily placement: 0.0%. Missed questions: 6. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 18 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Song That Aint Released Yet | rejected | — | — | 20 |
| 2 | Aperture Resonance - Code Clouds (2025) | rejected | — | — | 14 |
| 3 | Moonlight Echoes - Nebula Drift | rejected | — | — | 10 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Argentinian lesso brasquero | rejected | — | — | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## meta/muse-spark-open

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Xavier: Renegade Angel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Xavier: Renegade Angel | accepted | Rare | 60 | 18 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Burkina Faso.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Burkina Faso | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Nordic walking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nordic walking | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sleep Token - Emergence | confirmation_required → Emergence | — | — | 21 |
| 2 | Ghost - Satanized | rejected | — | — | 11 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Fresha.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Fresha | accepted | Rare | 60 | 20 |

---

## inclusionai/ling-3.0-flash

Status: agent_finished. Final score: 350/700. Daily placement: 79.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- PROMPT 2 OF 7 · invalid_request · 400 · Novita · ModelProviderError
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · Lucy: The Daughter of the Devil.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Lucy, the Daughter of the Devil | unconfirmed | — | — | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Oman.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Oman | accepted | Deep Cut | 85 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rucking | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | A Bar Song (Tipsy) by Shaboozey | rejected | — | — | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Klook.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Klook | accepted | Rare | 60 | 19 |

---

## meta/muse-spark-1.3

Status: agent_finished. Final score: 470/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Maultaschen.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Maultaschen | accepted | Deep Cut | 85 | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 13 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 14 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | aquajogging | confirmation_required → Aqua jogging | — | — | 15 |
| 2 | Aqua jogging | accepted | Rare | 60 | 8 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Emergence.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Emergence by Sleep Token | confirmation_required → Emergence | — | — | 7 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 17 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hostelworld.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hostelworld | accepted | Rare | 60 | 13 |

---

## z-ai/glm-5.3-flashx

Status: agent_finished. Final score: 445/700. Daily placement: 97.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kreplach.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Kreplach | accepted | Deep Cut | 85 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Frisky Dingo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Frisky Dingo | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Botswana.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Botswana | accepted | Rare | 60 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rucking | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Vanish Into You.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Vanish Into You by Lady Gaga | confirmation_required → Vanish Into You | — | — | 17 |
| 2 | Vanish Into You | accepted | Rare | 60 | 13 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 22 |

---

## xingchen-agi/xing4.0-29b-a4b:free

Status: agent_finished. Final score: 30/700. Daily placement: 0.0%. Missed questions: 4. Scorecard recovery: False.

Diagnostics:
- SURFACE · rate_limit · 429 · Phala · ModelRateLimitError
- SURFACE · rate_limit · 429 · Phala · ModelRateLimitError
- SURFACE · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 3 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 3 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 3 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 4 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 4 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 4 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 5 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 5 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 5 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 5 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 6 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 6 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 6 OF 7 · rate_limit · 429 · Phala · ModelRateLimitError
- SURFACE · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 1 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 2 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 3 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 4 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 5 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError
- PROMPT 6 OF 7 · rate_limit · rate_limit · 429 · Phala · ModelRateLimitError

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Strawberry | rejected | — | — | 18 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 10 points · Plankton · France.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | France | accepted | Plankton | 10 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 10 points · Plankton · Cycling.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | cycling | accepted | Plankton | 10 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 10 points · Plankton · Expedia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Expedia | accepted | Plankton | 10 | 24 |

---

## meta/muse-wonder

Status: agent_finished. Final score: 445/700. Daily placement: 97.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 20 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Tuca &amp; Bertie.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tuca &amp; Bertie | accepted | Rare | 60 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | mountain climbers | confirmation_required → Mountain climber | — | — | 18 |
| 2 | battle ropes | accepted | Rare | 60 | 10 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · House Tour.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | House Tour | accepted | Rare | 60 | 15 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 19 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Momondo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Momondo | accepted | Rare | 60 | 17 |

---

## google/gemini-3.6-flash

Status: agent_finished. Final score: 470/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Pastizzi.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | pastizz | confirmation_required → Pastizzi | — | — | 22 |
| 2 | Pastizzi | accepted | Deep Cut | 85 | 17 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 19 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · SkiErg.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | SkiErg | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Open Hearts.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Open Hearts | accepted | Rare | 60 | 9 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · GetYourGuide.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | GetYourGuide | accepted | Rare | 60 | 22 |

---

## google/gemini-3.1-flash-lite-preview

Status: agent_finished. Final score: 355/700. Daily placement: 81.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Khinkali | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Oblongs.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Oblongs | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Oman.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Oman | accepted | Deep Cut | 85 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Jump rope | accepted | Schooler | 30 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Die With A Smile (Live in Las Vegas) | rejected | — | — | 24 |
| 2 | Espresso (Remix) | rejected | — | — | 22 |
| 3 | APT. | rejected | — | — | 20 |
| 4 | Taste | rejected | — | — | 18 |
| 5 | Good Luck, Babe! | rejected | — | — | 16 |
| 6 | Saviour | rejected | — | — | 13 |
| 7 | The Emptiness Machine | rejected | — | — | 11 |
| 8 | Heart on My Sleeve | rejected | — | — | 9 |
| 9 | Beautiful Things (Live) | rejected | — | — | 7 |
| 10 | Get It Goin&#x27; | rejected | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 24 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · GetYourGuide.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | GetYourGuide | accepted | Rare | 60 | 24 |

---

## anthropic/claude-opus-4.6

Status: agent_finished. Final score: 415/700. Daily placement: 94.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knish.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Knish | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Brickleberry.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Brickleberry | accepted | Rare | 60 | 23 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Abracadabra.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Noid by Yeat | rejected | — | — | 23 |
| 2 | Lyfestyle by Yeat ft. Lil Wayne | rejected | — | — | 20 |
| 3 | Abracadabra by Lady Gaga | confirmation_required → Abracadabra | — | — | 17 |
| 4 | Abracadabra | accepted | Schooler | 30 | 15 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

---

## reflection/beam-1.0-501b-a23b

Status: agent_finished. Final score: 290/700. Daily placement: 57.0%. Missed questions: 3. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Scavengers Reign.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Scavengers Reign | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · South Sudan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | South Sudan | accepted | Rare | 60 | 15 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 85 points · Deep Cut · Llajwa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Llajua | confirmation_required → Llajwa | — | — | 20 |
| 2 | Llajwa | accepted | Deep Cut | 85 | 16 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · TrustedHousesitters.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | TrustedHousesitters | accepted | Deep Cut | 85 | 16 |

---

## google/gemini-3.1-pro-preview

Status: agent_finished. Final score: 445/700. Daily placement: 97.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knish.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Knish | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Frisky Dingo.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Frisky Dingo | accepted | Rare | 60 | 18 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Shadow boxing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Shadowboxing | confirmation_required → Shadow boxing | — | — | 20 |
| 2 | Shadow boxing | accepted | Rare | 60 | 14 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 60 points · Rare · Wake Me Up.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Wake Me Up | accepted | Rare | 60 | 15 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Hipcamp.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hipcamp | accepted | Rare | 60 | 19 |

---

## openai/gpt-5-mini

Status: agent_finished. Final score: 545/700. Daily placement: 99.63%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Cepelinai.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kroppkakor | confirmation_required → Kroppkaka | — | — | 19 |
| 2 | kroppkakor | confirmation_required → Kroppkaka | — | — | 15 |
| 3 | kroppkakor | confirmation_required → Kroppkaka | — | — | 11 |
| 4 | Cepelinai | accepted | Deep Cut | 85 | 7 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · 12 oz. Mouse.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | 12 oz. Mouse | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · New Zealand.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | New Zealand | accepted | Rare | 60 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Skijoring.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Skijoring | accepted | Deep Cut | 85 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · Neon Ride.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Glass Orchard | rejected | — | — | 20 |
| 2 | Moonlit Kelp | rejected | — | — | 17 |
| 3 | Wormlight Canticle | rejected | — | — | 13 |
| 4 | Neon Tides | confirmation_required → Neon Ride | — | — | 10 |
| 5 | Neon Ride | accepted | Deep Cut | 85 | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Boatsetter.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Boatsetter | accepted | Deep Cut | 85 | 21 |

---

## openai/gpt-4.1-mini

Status: agent_finished. Final score: 295/700. Daily placement: 58.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- SURFACE · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · navigation_inference_timeout · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Empanada.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | empanada | accepted | Schooler | 30 | 24 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · Archer.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 24 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Hungary | rejected | — | — | 23 |
| 2 | Gabon | accepted | Deep Cut | 85 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 30 points · Schooler · Jump rope.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | jump rope | accepted | Schooler | 30 | 24 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Future Nostalgia | rejected | — | — | 24 |
| 2 | Echoes of Tomorrow | rejected | — | — | 22 |
| 3 | Solar Winds | rejected | — | — | 20 |
| 4 | Neon Drifters | rejected | — | — | 17 |
| 5 | Quantum Groove | rejected | — | — | 15 |
| 6 | Stellar Drift | rejected | — | — | 12 |
| 7 | Celestial Voyage | rejected | — | — | 10 |
| 8 | Midnight Reverie | rejected | — | — | 8 |
| 9 | Lunar Mirage | rejected | — | — | 5 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Zocdoc.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Snagajob | rejected | — | — | 24 |
| 2 | Zocdoc | accepted | Rare | 60 | 20 |

---

## openai/gpt-5.4-nano

Status: agent_finished. Final score: 295/700. Daily placement: 58.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 30 points · Schooler · Gyoza.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gyoza | accepted | Schooler | 30 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 30 points · Schooler · Archer.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Archer | accepted | Schooler | 30 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Mozambique.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mozambique | accepted | Deep Cut | 85 | 22 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Cross-country skiing.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Cross-country skiing | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Taylor Swift – Fresh Air (2026) | rejected | — | — | 22 |
| 2 | The Weeknd – Wake Me Up (2026) | rejected | — | — | 18 |
| 3 | Olivia Rodrigo – Lost Memory (2025) | rejected | — | — | 14 |
| 4 | Chappell Roan  Red Wine (2025) | rejected | — | — | 11 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Harissa.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | harissa | accepted | Rare | 60 | 23 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 30 points · Schooler · OpenTable.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 23 |

---

## openai/gpt-5.6-luna-pro

Status: agent_finished. Final score: 465/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Modak.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | modak | accepted | Deep Cut | 85 | 17 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 20 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Guinea.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Guinea | accepted | Deep Cut | 85 | 18 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Rucking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Rucking | accepted | Rare | 60 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Daisies.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Daisies | accepted | Schooler | 30 | 18 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 21 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Booksy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Booksy | accepted | Rare | 60 | 20 |

---

## openai/gpt-5.4-mini

Status: agent_finished. Final score: 340/700. Daily placement: 78.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Xiaolongbao.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | xiao long bao | confirmation_required → Xiaolongbao | — | — | 22 |
| 2 | Xiaolongbao | accepted | Rare | 60 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 60 points · Rare · Ecuador.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ecuador | accepted | Rare | 60 | 21 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 10 points · Plankton · Ordinary.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | back to friends by sombr | rejected | — | — | 21 |
| 2 | Ordinary by Alex Warren | confirmation_required → Ordinary | — | — | 17 |
| 3 | Ordinary | accepted | Plankton | 10 | 13 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | ajvar | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 30 points · Schooler · OpenTable.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | OpenTable | accepted | Schooler | 30 | 21 |

---

## recursive/flint-v1.0:free

Status: agent_finished. Final score: 435/700. Daily placement: 95.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Manti.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkish manti | confirmation_required → Manti | — | — | 21 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Maxx.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Maxx | accepted | Deep Cut | 85 | 21 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Ivory Coast.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ivory Coast | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Aqua jogging | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Birds of a Feather | rejected | — | — | 15 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Gochujang.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Belacan | rejected | — | — | 18 |
| 2 | Gochujang | accepted | Rare | 60 | 13 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Mozio.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mozio | accepted | Deep Cut | 85 | 19 |

---

## x-ai/grok-4.5

Status: agent_finished. Final score: 435/700. Daily placement: 95.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Xiaolongbao.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | xiaolongbao | accepted | Rare | 60 | 11 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · 12 oz. Mouse.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | 12 oz. Mouse | accepted | Deep Cut | 85 | 13 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 5 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · SkiErg.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | SkiErg | accepted | Rare | 60 | 6 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 16 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Tock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 15 |

---

## inception/mercury-3

Status: agent_finished. Final score: 460/700. Daily placement: 97.0%. Missed questions: 1. Scorecard recovery: False.

Diagnostics:
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Khinkali.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | khinkali | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Life &amp; Times of Tim.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Life &amp; Times of Tim | accepted | Deep Cut | 85 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Turkmenistan.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 15 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Nordic walking.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Nordic walking | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 85 points · Deep Cut · LoveDrug.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | LoveDrug | accepted | Deep Cut | 85 | 7 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Giggster.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Giggster | accepted | Deep Cut | 85 | 19 |

---

## qwen/qwen3.7-plus

Status: agent_finished. Final score: 85/700. Daily placement: 1.0%. Missed questions: 6. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 6 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 85 points · Deep Cut · Skijoring.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Skijoring | accepted | Deep Cut | 85 | 20 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## openai/gpt-5.4

Status: agent_finished. Final score: 440/700. Daily placement: 96.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knish.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 20 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · Moral Orel.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 20 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Aqua jogging.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | aquajogging | confirmation_required → Aqua jogging | — | — | 21 |
| 2 | Aqua jogging | accepted | Rare | 60 | 18 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Sports Car.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Sports car | accepted | Schooler | 30 | 20 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ajvar | accepted | Rare | 60 | 22 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · Tock.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Tock | accepted | Deep Cut | 85 | 21 |

---

## deepseek/deepseek-v4-flash-vision-exp

Status: agent_finished. Final score: 465/700. Daily placement: 98.0%. Missed questions: 0. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Coxinha.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | coxinha | accepted | Rare | 60 | 22 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 14 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 23 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 22 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 30 points · Schooler · Like Jennie.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Like Jennie | accepted | Schooler | 30 | 8 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Romesco.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | romesco | accepted | Rare | 60 | 17 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 85 points · Deep Cut · FareHarbor.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | FareHarbor | accepted | Deep Cut | 85 | 20 |

---

## qwen/qwen3-235b-a22b-2507

Status: agent_finished. Final score: 385/700. Daily placement: 89.0%. Missed questions: 1. Scorecard recovery: False.

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 60 points · Rare · Knafeh.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | knafeh | accepted | Rare | 60 | 23 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 60 points · Rare · The Venture Bros..

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros | unconfirmed | — | — | 22 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Zambia.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Mongolia | rejected | — | — | 23 |
| 2 | Zambia | accepted | Deep Cut | 85 | 19 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Capoeira.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Capoeira | accepted | Rare | 60 | 23 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Labyrinth of the Golden Toad by Sussman Lawrence | rejected | — | — | 20 |
| 2 | Infinite Sleep by The Krolg | rejected | — | — | 17 |
| 3 | Echoes of Tomorrow by Null Entity | rejected | — | — | 15 |
| 4 | Whispers in Static by Vexed Data | rejected | — | — | 11 |
| 5 | Neon Eclipse by Data Panacea | rejected | — | — | 6 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Ajvar.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Ssamjang | rejected | — | — | 20 |
| 2 | Ajvar | accepted | Rare | 60 | 16 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 60 points · Rare · Resy.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

---

## inclusionai/ling-3.1-flash

Status: agent_finished. Final score: 375/700. Daily placement: 86.0%. Missed questions: 2. Scorecard recovery: False.

Diagnostics:
- SURFACE · invalid_request · 400 · Novita · ModelProviderError
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 85 points · Deep Cut · Kreplach.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | kreplach | accepted | Deep Cut | 85 | 19 |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 85 points · Deep Cut · The Shivering Truth.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 18 |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 85 points · Deep Cut · Gabon.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 10 |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 60 points · Rare · Battle ropes.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | battle ropes | accepted | Rare | 60 | 21 |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Velvet Static by NOVA KLINE | rejected | — | — | 15 |
| 2 | Fractured Light by Elowen Vale | rejected | — | — | 10 |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | Muhammara | accepted | Rare | 60 | 19 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |

---

## x-ai/grok-4.6

Status: agent_finished. Final score: 60/700. Daily placement: 0.0%. Missed questions: 6. Scorecard recovery: False.

Diagnostics:
- PROMPT 1 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 2 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 3 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 4 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 5 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout
- PROMPT 7 OF 7 · inference_deadline · round_inference_deadline · ModelResponseTimeout

### PROMPT 1 OF 7: Name a food with a filling inside.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 4 OF 7: Name a cardio exercise.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

Result: 60 points · Rare · Muhammara.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| 1 | muhammara | accepted | Rare | 60 | 7 |
### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

Result: 0 points · — · —.

| Attempt | Submitted answer | Outcome | Rarity | Points | Clock |
|---:|---|---|---|---:|---:|
| — | No recorded submission | — | — | — | — |
