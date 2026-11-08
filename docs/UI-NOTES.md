# Krillion ocean leaderboard

The static leaderboard uses Krillion's pixel ocean artwork, VT323 type, cyan/pink accents, and rarity sprites. Normal page scrolling translates a fixed 4,800px ocean scene from surface to trench. The depth HUD shows **page exploration progress**, not a model's score or game depth. No framework, tracking, game scripts, or external runtime asset requests are needed.

The hero omits the summary stats, and there is no visible tier legend. The results table shows the first five matching models by default, with a Show all / Show fewer button. Sorting and filters apply to the whole snapshot before the five-row preview; charts and downloads always retain all matching / all exported models respectively. Loading a campaign resets the table to five rows. The # column header sorts by overall rank, best first on the initial click and reversed on the next; shared ranks retain the model-ID tie break.

## Placement badges

Completed models are ordered by verified score descending, then model ID ascending for ties. Badge placement is computed once per imported snapshot, independent of table sorting, provider filtering, or search:

| Overall position | Icon |
| --- | --- |
| 1 | Krillion |
| 2–10 | Deep Cut |
| 11–25 | Rare |
| 26–50 | Schooler |
| 51–100 | Plankton |

The score rank column continues to share ranks for tied scores. Badge placement uses the deterministic tie break so the five groups contain exactly 1, 9, 15, 25, and 50 models in the current campaign. Run errors and positions beyond 100 have no placement badge. Badges are benchmark placements, not a model's individual answer rarity.

Score progress bars and daily percentages use the game’s default rarity palette for each placement: Krillion gold `#ffd166`, Deep Cut purple `#9d7bff`, Rare red `#ff5252`, Schooler cyan `#4de3ff`, and Plankton slate `#8fa3c4`. Bar fills use a translucent gradient with a solid tier-colored edge so score numerals remain readable. Colors follow the global badge through sorting and filtering.

## Accessibility and behavior

- `prefers-reduced-motion` freezes the ocean and disables ambient animation and smooth scrolling. The header's effects button offers a persistent manual reduced-effects mode.
- Decorative scenery is hidden from accessibility APIs. Badges have descriptive alternative text and tooltips.
- On small screens, the table scrolls horizontally; model and score appear first. The depth readout moves into a narrow bottom bar.
- Sorting, search, provider/status filters, metric charts, per-round answer reports, campaign import, and JSON export are retained.
- No benchmark results or harness behavior changed in this redesign.

## Visual asset credits

Ocean artwork and rarity sprites originate from [Krillion](https://krillion.io/), retrieved November 7, 2026 and used for this independent benchmark's requested game-matching presentation. These third-party assets remain the property of their respective owners; this project's code license does not relicense them.

| Local file | Original source |
| --- | --- |
| `web/assets/images/krillion-bg-sky.webp` | https://krillion.io/gen/optimized/v1/bg-sky.webp |
| `web/assets/images/krillion-bg-top.webp` | https://krillion.io/gen/optimized/v1/bg-top.webp |
| `web/assets/images/krillion-bg-mid.webp` | https://krillion.io/gen/optimized/v1/bg-mid.webp |
| `web/assets/images/krillion-bg-trench.webp` | https://krillion.io/gen/optimized/v1/bg-trench.webp |
| `web/assets/images/krillion-krillion.png` | https://krillion.io/tiers/krillion.png |
| `web/assets/images/krillion-deepcut.png` | https://krillion.io/tiers/deepcut.png |
| `web/assets/images/krillion-rare.png` | https://krillion.io/tiers/rare.png |
| `web/assets/images/krillion-schooler.png` | https://krillion.io/tiers/schooler.png |
| `web/assets/images/krillion-plankton.png` | https://krillion.io/tiers/plankton.png |

`web/assets/fonts/krillion-vt323.woff2` is the VT323 font served by Krillion, copyright Peter Hull, licensed under SIL OFL 1.1. See `web/assets/fonts/KRILLION-FONT-LICENSE.txt` and the [Google Fonts source](https://github.com/google/fonts/tree/main/ofl/vt323).

## Validation — November 7, 2026

- Browser verified all 100 badge images load and tier counts are 1 / 9 / 15 / 25 / 50, including boundary positions.
- Cost sorting and provider/search filtering preserve each model's global badge. Daily placement chart plots 99 available values; cost chart plots 47 complete cost records.
- Desktop and 390px phone layouts checked visually. Phone page width remains 390px with the full model/score columns visible; other metrics scroll within the table.
- Seven-round answer report, close control, campaign import, and JSON download verified. Effects setting survives reload; ocean depth reaches 7,000m at the bottom. No browser errors or warnings observed.
- `node --check leaderboard.js` and `git diff --check` pass. The benchmark dataset remains byte-for-byte unchanged (SHA-256 `bc02aba0ef8a736a6ac65e3b84ee36234665a76e538dc5e43fba47d9cbd57fc7`).

### Compact leaderboard follow-up

Browser verification confirmed the default five rows expand to 100 and collapse to five; the chart still includes all 47 complete cost records. Search finds a model outside the preview, and the expansion button disappears for five or fewer matching results. The # header sorts shared ranks ascending and descending in both preview and full-list modes, including keyboard activation. No browser errors were observed.

### Tier metric colors follow-up

Browser computed-style checks confirmed matching score-bar edges and daily percentages across all five tiers (1 / 9 / 15 / 25 / 50 rows). Rank sorting and search preserve the global placement color, and the compact five-row view remains intact. The stylesheet URL is versioned to invalidate cached styling.

### Tier glow follow-up

Daily percentages use the same `0 0 9px` tier-colored text shadow as Krillion’s passed depth labels (`.ds-tierline.passed .tag`). Score fills adapt that halo to their leading edge, with a softer bloom around the fill. The glow is static; Reduce ocean effects removes these metric shadows.

Only the first-place row receives a gold background highlight and soft halo, with gold model/rank text and icon glow. Other rows retain their usual background and their own tier-colored metrics. Reduced effects also removes the winner’s shadows.

### Simplified chart labels

Removed the Run errors filter tab, completion/error/ranking summary, campaign label beside the snapshot date, and plotted-run count. The snapshot date and About these metrics link remain. Provider legend labels use the same Krillion pixel font as the rest of the chart. Chart eligibility, underlying results, and error diagnostics are unchanged.

### Aggregate score intervals

Archive-mean datasets render a 95% bootstrap confidence whisker under each score bar, with matching tier color and pixel-font interval bounds. Mean scores use one decimal and daily percentages use two. Aggregate dialogs show per-metric sample counts and intervals without individual answers. Single-day snapshots retain their original presentation and have no fabricated interval. Synthetic aggregate data is used only for local UI validation.
