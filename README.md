<div align="center">

<img src="web/assets/images/krillion-krillion.png" width="96" alt="Krillion shrimp">

# Krillion Bench

### A deep dive into language models under pressure

[**Dive into the leaderboard →**](https://krillionbench.com/)

<img src="web/assets/images/krillion-plankton.png" width="40" alt="Plankton">
<img src="web/assets/images/krillion-schooler.png" width="40" alt="Schooler">
<img src="web/assets/images/krillion-rare.png" width="40" alt="Rare">
<img src="web/assets/images/krillion-deepcut.png" width="40" alt="Deep Cut">
<img src="web/assets/images/krillion-krillion.png" width="40" alt="Krillion">

</div>

---

Krillion Bench compares 100 language models playing [Krillion](https://krillion.io/), a game of seven timed questions. Models use a browser to submit answers, and rarer accepted answers earn more points. The benchmark measures how well models play under real time pressure.

## Explore the website

- **Live updates:** newly verified scorecards automatically refresh the website’s metrics and reports, usually within a minute.
- **Average:** compare average scores, daily placement, inference costs, output tokens, and time across tested days.
- **Daily:** choose a tested date on the calendar and open a model’s report to see its questions, answers, and points.
- **Graph:** compare average score against cost, tokens, time, or daily placement.
- **Filters:** search models and browse providers or open and closed models. “Show more” reveals one complete ranking tier at a time.

## The top of the ocean

From the website’s published snapshot of **2,379 clean verified games**, updated November 10, 2026. Scores are rounded to whole numbers; ranking uses the underlying averages.

| Rank | Tier | Model | Average score / 700 | Average daily percentile |
| ---: | :---: | --- | ---: | ---: |
| 1 | <img src="web/assets/images/krillion-krillion.png" width="28" alt="Krillion" title="Krillion"> | openai/gpt-6-sol | 558 | 99.53% |
| 2 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | openai/gpt-5.6-sol | 544 | 99.24% |
| 3 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | openai/gpt-6-astra | 534 | 98.95% |
| 4 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | particle-ai/particle-1 | 527 | 98.81% |
| 5 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | deepseek/deepseek-v4.1-flash-1017 | 525 | 98.71% |
| 6 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | google/gemini-3.6-flash | 524 | 98.94% |
| 7 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | openai/gpt-6-luna-pro | 523 | 98.76% |
| 8 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | deepseek/deepseek-v4.1-flash | 514 | 97.68% |
| 9 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | moonshotai/kimi-k3.1-pro | 511 | 98.18% |
| 10 | <img src="web/assets/images/krillion-deepcut.png" width="28" alt="Deep Cut" title="Deep Cut"> | openai/gpt-5.6-terra | 510 | 98.57% |
| 11 | <img src="web/assets/images/krillion-rare.png" width="28" alt="Rare" title="Rare"> | anthropic/claude-opus-5 | 502 | 97.12% |
| 12 | <img src="web/assets/images/krillion-rare.png" width="28" alt="Rare" title="Rare"> | openai/gpt-6-luna | 502 | 98.33% |
| 13 | <img src="web/assets/images/krillion-rare.png" width="28" alt="Rare" title="Rare"> | openai/gpt-5.6-luna-pro | 501 | 97.56% |
| 14 | <img src="web/assets/images/krillion-rare.png" width="28" alt="Rare" title="Rare"> | google/gemini-3-flash-preview | 499 | 97.70% |
| 15 | <img src="web/assets/images/krillion-rare.png" width="28" alt="Rare" title="Rare"> | google/gemini-3.7-flash | 497 | 97.69% |

<p align="center">
<img src="web/assets/images/krillion-krillion.png" width="24" alt=""> <strong>Krillion</strong> #1 &nbsp; · &nbsp;
<img src="web/assets/images/krillion-deepcut.png" width="24" alt=""> <strong>Deep Cut</strong> #2–10 &nbsp; · &nbsp;
<img src="web/assets/images/krillion-rare.png" width="24" alt=""> <strong>Rare</strong> #11–25<br>
<img src="web/assets/images/krillion-schooler.png" width="24" alt=""> <strong>Schooler</strong> #26–50 &nbsp; · &nbsp;
<img src="web/assets/images/krillion-plankton.png" width="24" alt=""> <strong>Plankton</strong> #51–100
</p>

The daily percentile is Krillion’s “better than” comparison at the time each game was captured, averaged across available days. It is not the model’s percentile within this leaderboard. Date coverage still varies while remaining runs finish; missing results are excluded rather than counted as zero.

## How results are checked

Only clean, verified seven-round scorecards enter these results. Real zero scores count. Raw browser traces stay private; Daily reports expose sanitized gameplay summaries. This is a benchmark of timed game performance, not a general intelligence ranking.

## Documentation

- [Technical setup and harness guide](docs/HARNESS-GUIDE.md)
- [Repository layout](docs/REPOSITORY-LAYOUT.md)
- [Validation notes](docs/VALIDATION.md)

Independent evaluation. Krillion’s game, artwork, and font belong to their respective creators.
