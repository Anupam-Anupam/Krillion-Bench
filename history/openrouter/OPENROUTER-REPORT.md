# OpenRouter Krillion run reports — November 7, 2026

Six original live browser games, followed by two separately labeled engineering checks. Every submitted answer appears below, including corrections and rejections. A daily percentage means the game’s “better than X% of today’s players,” captured at the end of that run. Failed runs have no final percentage.

| Original model | Outcome | Accepted rounds | Score | Daily percentage |
|---|---|---:|---:|---:|
| anthropic/claude-haiku-5.5 | agent_finished | 7/7 | 365 | 85% |
| deepseek/deepseek-v4.1-flash | agent_finished | 7/7 | 440 | 96% |
| google/gemini-4-argon | agent_finished | 7/7 | 355 | 80% |
| meta-llama/llama-4-maverick | agent_finished | 7/7 | 305 | 63% |
| meta-llama/llama-4-scout | failed | 2/7 | 20 partial | unavailable |
| openai/gpt-6.1-terra | agent_finished | 7/7 | 355 | 80% |

## Method and provenance

The original campaign used the unchanged published harness at e3a7d96, Browser Use Cloud with fresh sessions, OpenRouter, DOM-only observations, requested low reasoning, 1,500 output tokens, an 18-second inference cap, and concurrency two. One game per model, with the same daily prompts. No whole-run retries or replacement results. This is a small engineering sample, not a model ranking.

Reports are backfilled from saved submissions, displayed result text, model observations, and final scorecards. Pre-press action events establish attempt order when remote keypress completion and observation timestamps overlap. Rarity labels come from displayed results; any category derived from points is labeled as such. The original raw reports and timing values remain unchanged. Source hashes and settings are recorded in OPENROUTER-MANIFEST.json. Raw browser traces and credentials are not published.

Original Scout failure: after two accepted answers, the model repeatedly tried filling a nonexistent textbox between rounds, using ocean scenery as answers. The final model call timed out; question three never opened.

## Follow-up checks with phase guidance and bounded navigation recovery

| Model | Outcome | Accepted rounds | Score | Daily percentage | Recoveries used |
|---|---|---:|---:|---:|---:|
| meta-llama/llama-4-scout | deadline_exceeded | 4/7 | 60 partial | unavailable | 0 |
| anthropic/claude-haiku-5.5 | agent_finished | 7/7 | 310 | 66% | 0 |

Scout navigated past its former stall without fallback, then missed the round-five harness deadline after eight rejected song submissions. The final filled text was blocked from submission at the deadline and is not counted as an extra submitted answer. This is still a failed run, retained separately from the original. Haiku completed all seven rounds, exercising both correction feedback and a rejected-answer retry. Neither follow-up used navigation assistance. The actual fallback is verified by automated replay in real Chrome, including Scout-style wrong fills between rounds two and three.

The Scout follow-up preceded the event timestamp correction; its per-submission elapsed_s fields remain round-relative, while the later version writes event elapsed_s as run-relative and round_elapsed_s separately. The Haiku run used corrected event timestamps. A subsequent diagnostic-only change logs exceptions from recovery attempts; it and the eight-recovery cap passed regression tests. These follow-ups use different observation guidance from the original campaign and must not replace or be pooled with it.

## Original run details

### Krillion run: anthropic/claude-haiku-5.5

Status: **agent_finished**. Score: **365/700**.

Final daily percentage: **better than 85% of today’s players**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pastizzi | accepted | Deep Cut | 85 | 22 |

Round result: Pastizzi · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Moral Orel | accepted | Rare | 60 | 23 |

Round result: Moral Orel · Rare · 60 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Papua New Guinea | accepted | Rare | 60 | 21 |

Round result: Papua New Guinea · Rare · 60 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing machine | confirmation_required → Rowing | — | — | 23 |
| 2 | Rowing | accepted | Schooler | 30 | 20 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Manchild | accepted | Plankton | 10 | 22 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sambal oelek | accepted | Rare | 60 | 23 |

Round result: Sambal oelek · Rare · 60 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 23 |

Round result: Resy · Rare · 60 points (source: displayed_result).


### Krillion run: deepseek/deepseek-v4.1-flash

Status: **agent_finished**. Score: **440/700**.

Final daily percentage: **better than 96% of today’s players**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | knish | accepted | Rare | 60 | 17 |

Round result: Knish · Rare · 60 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Shivering Truth | accepted | Deep Cut | 85 | 23 |

Round result: The Shivering Truth · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 18 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | shadowboxing | confirmation_required → Shadow boxing | — | — | 23 |
| 2 | Shadow boxing | accepted | Rare | 60 | 21 |

Round result: Shadow boxing · Rare · 60 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Anxiety | accepted | Schooler | 30 | 18 |

Round result: Anxiety · Schooler · 30 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 21 |

Round result: Resy · Rare · 60 points (source: displayed_result).


### Krillion run: google/gemini-4-argon

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 21 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | The Venture Bros. | accepted | Rare | 60 | 16 |

Round result: The Venture Bros. · Rare · 60 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Turkmenistan | accepted | Deep Cut | 85 | 20 |

Round result: Turkmenistan · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | stairmaster | confirmation_required → Stair climbing | — | — | 21 |
| 2 | Stair climbing | accepted | Schooler | 30 | 16 |

Round result: Stair climbing · Schooler · 30 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra | accepted | Schooler | 30 | 9 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 21 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 21 |

Round result: Resy · Rare · 60 points (source: displayed_result).


### Krillion run: meta-llama/llama-4-maverick

Status: **agent_finished**. Score: **305/700**.

Final daily percentage: **better than 63% of today’s players**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Ravioli | accepted | Schooler | 30 | 21 |

Round result: Ravioli · Schooler · 30 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | BoJack Horseman | accepted | Schooler | 30 | 23 |

Round result: BoJack Horseman · Schooler · 30 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bulgaria | rejected | — | — | 24 |
| 2 | Lithuania | rejected | — | — | 21 |
| 3 | Bulgaria | rejected | — | — | 18 |
| 4 | Lithuania | rejected | — | — | 15 |
| 5 | Burkina Faso | accepted | Deep Cut | 85 | 13 |

Round result: Burkina Faso · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Jumping jacks | accepted | Schooler | 30 | 24 |

Round result: Jumping jacks · Schooler · 30 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Greedy with Envy | rejected | — | — | 24 |
| 2 | Lovin on Me | rejected | — | — | 19 |
| 3 | Espresso | rejected | — | — | 17 |
| 4 | Lovin on Me | rejected | — | — | 13 |
| 5 | Greedy | accepted | Rare | 60 | 11 |

Round result: Greedy · Rare · 60 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 24 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Booking.com | accepted | Plankton | 10 | 23 |

Round result: Booking.com · Plankton · 10 points (source: displayed_result).


### Krillion run: meta-llama/llama-4-scout

Status: **failed**. Score: **20 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: TimeoutError.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 23 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 22 |

Round result: Rick and Morty · Plankton · 10 points (source: displayed_result).


### Krillion run: openai/gpt-6.1-terra

Status: **agent_finished**. Score: **355/700**.

Final daily percentage: **better than 80% of today’s players**.

Navigation recovery: off (historical); successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | pierogi | accepted | Schooler | 30 | 23 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Home Movies | accepted | Rare | 60 | 23 |

Round result: Home Movies · Rare · 60 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Gabon | accepted | Deep Cut | 85 | 22 |

Round result: Gabon · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing | accepted | Schooler | 30 | 22 |

Round result: Rowing · Schooler · 30 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Abracadabra by Lady Gaga | confirmation_required → Abracadabra | — | — | 23 |
| 2 | Abracadabra | accepted | Schooler | 30 | 22 |

Round result: Abracadabra · Schooler · 30 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Harissa | accepted | Rare | 60 | 23 |

Round result: Harissa · Rare · 60 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 22 |

Round result: Resy · Rare · 60 points (source: displayed_result).


## Follow-up run details

### Krillion run: meta-llama/llama-4-scout

Status: **deadline_exceeded**. Score: **60 partial points**.

Final daily percentage: **unavailable (no verified final percentile)**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

Failure: DeadlineExceeded.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | dumpling | accepted | Plankton | 10 | 22 |

Round result: Dumpling · Plankton · 10 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rick and Morty | accepted | Plankton | 10 | 24 |

Round result: Rick and Morty · Plankton · 10 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Bolivia | rejected | — | — | 22 |
| 2 | Chile | accepted | Schooler | 30 | 20 |

Round result: Chile · Schooler · 30 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | jogging | accepted | Plankton | 10 | 24 |

Round result: Jogging · Plankton · 10 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Vampire | rejected | — | — | 24 |
| 2 | Lose Control | rejected | — | — | 21 |
| 3 | Tutti | rejected | — | — | 19 |
| 4 | Rich Flex | rejected | — | — | 16 |
| 5 | Lose Control | rejected | — | — | 14 |
| 6 | Flowers | rejected | — | — | 11 |
| 7 | Tutti | rejected | — | — | 9 |
| 8 | vroma | rejected | — | — | 7 |


### Krillion run: anthropic/claude-haiku-5.5

Status: **agent_finished**. Score: **310/700**.

Final daily percentage: **better than 66% of today’s players**.

Navigation recovery: bounded; successful assistance: 0.

Rarity is the game’s category, not an invented per-answer percentage. Rejected or unconfirmed attempts have no rarity. The daily percentage is the live game’s population comparison at capture time, not score ÷ 700.

#### PROMPT 1 OF 7: Name a food with a filling inside.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Pierogi | accepted | Schooler | 30 | 24 |

Round result: Pierogi · Schooler · 30 points (source: displayed_result).

#### PROMPT 2 OF 7: Name an animated TV show that isn&#x27;t meant for kids (no anime).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Undone | accepted | Deep Cut | 85 | 23 |

Round result: Undone · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 3 OF 7: Name a country bigger than the UK but smaller than Egypt, by area.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Zambia | accepted | Deep Cut | 85 | 21 |

Round result: Zambia · Deep Cut · 85 points (source: displayed_result).

#### PROMPT 4 OF 7: Name a cardio exercise.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Rowing machine | confirmation_required → Rowing | — | — | 24 |
| 2 | Jump rope | accepted | Schooler | 30 | 22 |

Round result: Jump rope · Schooler · 30 points (source: displayed_result).

#### PROMPT 5 OF 7: Name a song released in 2025 or 2026 with over 10 million Spotify streams.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Golden Hour Echo | rejected | — | — | 24 |
| 2 | Manchild | accepted | Plankton | 10 | 20 |

Round result: Manchild · Plankton · 10 points (source: displayed_result).

#### PROMPT 6 OF 7: Name a red sauce, dip or condiment.

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Sriracha | accepted | Plankton | 10 | 24 |

Round result: Sriracha · Plankton · 10 points (source: displayed_result).

#### PROMPT 7 OF 7: Name an app or website where you book things (like Expedia for travel).

| Attempt | Submitted answer | Outcome | Rarity | Points | Timer at submission |
|---:|---|---|---|---:|---:|
| 1 | Resy | accepted | Rare | 60 | 24 |

Round result: Resy · Rare · 60 points (source: displayed_result).

