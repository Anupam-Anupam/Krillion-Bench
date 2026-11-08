# Repository layout and publication

The repository root is the working directory for all README commands. Python
scripts live in `harness/`; their sibling imports work when invoked as
`uv run python harness/runner.py ...`. Pytest adds `harness/` to its import path.
Dependency configuration and the lockfile stay at the root. Campaign manifests
retain their logical source names, including `uv.lock`.

## Website

GitHub Pages serves `main` at `/`. Keep `index.html` at the root and deploy the
whole tree: it loads `web/leaderboard.js`, `web/leaderboard.css`, and
`web/data/leaderboard-data.json`. Artwork is under `web/assets/images/`; the font
and its existing license are under `web/assets/fonts/`.

Preview from the root with `python3 -m http.server 8765 --bind 127.0.0.1`.
The site URL, section anchors, styling, and leaderboard values are unchanged.

## Historical records

- `history/top100/`: original 100-model report, answers, ranking, summary, manifest.
- `history/openrouter/`: original six-model report and manifest.
- `history/continuation/`: final-score continuation report and manifest.
- `history/recovery/`: targeted recovery report.
- `docs/VALIDATION.md`: accumulated validation notes.
- `data/archive-games.json`: observed archive URLs and labels.

All existing files were retained. Historical commands and source hashes describe
the layouts and versions in use when those runs happened. Relative documentation
links have been updated; historical JSON, artwork, and font contents are unchanged.
New archive trajectories still go directly from RAM to the private reports repo;
this organization does not add a local or public report sink.

## Active campaign: keep its frozen checkout

The ongoing `archive-75-20261106-v3` campaign runs from the separate checkout
`/private/tmp/Krillion-Bench-9pnucipl` at `583a4b6`. Leave that checkout, its paths,
and its ten-worker coordinator untouched. Do not pull this reorganization into
it, restart it from the organized checkout, or relax its source-hash checks.
Use that original source/layout for any necessary continuation or final export.
The five-word system prompt and automatic correction acceptance remain unchanged.

Progress is independent of the main branch layout: the active coordinator writes
`campaign-progress.json` on the public `campaign-status` branch. Its URL stays
unchanged. Local progress contains aggregate counts only.

Only after all 7,500 model/day pairs are verified, validate the complete balanced
aggregate export and its 95% confidence intervals. In a separate publication
checkout of the latest public `main`, copy that numeric aggregate export to
`web/data/leaderboard-data.json`. Preserve `protocol_note` and metric coverage,
commit as Anupam, push to the personal repository, and verify the live site.
Never copy private reports or replace historical manifests/results during this
publication. Existing single-day values remain until the complete panel is ready.
