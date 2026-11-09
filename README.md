# Krillion Bench

**[Explore the leaderboard → krillionbench.com](https://krillionbench.com/)**

Krillion Bench compares 100 language models playing [Krillion](https://krillion.io/), a game of seven timed questions. Models use a browser to submit answers, and rarer accepted answers earn more points. The benchmark measures how well models play under real time pressure.

## Explore the website

- **Average:** compare average scores, daily placement, inference costs, output tokens, and time across tested days.
- **Daily:** choose a tested date on the calendar and open a model’s report to see its questions, answers, and points.
- **Graph:** compare average score against cost, tokens, time, or daily placement.
- **Filters:** search models and browse providers or open and closed models. “Show more” reveals one complete ranking tier at a time.

## Top 15

From the website’s published snapshot of **2,140 clean verified games**, updated November 8, 2026. Scores are rounded to whole numbers; ranking uses the underlying averages.

| Rank | Model | Average score / 700 | Average daily percentile |
| ---: | --- | ---: | ---: |
| 1 | openai/gpt-6-sol | 558 | 99.55% |
| 2 | openai/gpt-5.6-sol | 542 | 99.20% |
| 3 | openai/gpt-6-astra | 532 | 98.91% |
| 4 | particle-ai/particle-1 | 527 | 98.84% |
| 5 | deepseek/deepseek-v4.1-flash-1017 | 525 | 98.70% |
| 6 | google/gemini-3.6-flash | 522 | 98.90% |
| 7 | openai/gpt-6-luna-pro | 518 | 98.67% |
| 8 | deepseek/deepseek-v4.1-flash | 518 | 97.70% |
| 9 | moonshotai/kimi-k3.1-pro | 512 | 98.18% |
| 10 | openai/gpt-5.6-terra | 509 | 98.58% |
| 11 | openai/gpt-6-luna | 502 | 98.36% |
| 12 | anthropic/claude-opus-5 | 498 | 96.91% |
| 13 | google/gemini-3-flash-preview | 497 | 97.56% |
| 14 | openai/gpt-5.6-luna-pro | 497 | 97.39% |
| 15 | z-ai/glm-5.2 | 497 | 97.57% |

The daily percentile is Krillion’s “better than” comparison at the time each game was captured, averaged across available days. It is not the model’s percentile within this leaderboard. Date coverage still varies while remaining runs finish; missing results are excluded rather than counted as zero.

## How results are checked

Only clean, verified seven-round scorecards enter these results. Real zero scores count. Raw browser traces stay private; Daily reports expose sanitized gameplay summaries. This is a benchmark of timed game performance, not a general intelligence ranking.

## Documentation

- [Technical setup and harness guide](docs/HARNESS-GUIDE.md)
- [Repository layout](docs/REPOSITORY-LAYOUT.md)
- [Validation notes](docs/VALIDATION.md)

Independent evaluation. Krillion’s game, artwork, and font belong to their respective creators.
