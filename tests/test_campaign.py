import asyncio
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from campaign import run_campaign, select_models, summarize


def test_selection_excludes_routers_aliases_batch_but_keeps_free_variant():
    ids = ["~org/latest", "openrouter/auto", "org/a:batch", "org/a:free", "org/a"]
    ranking = {"rows": [{"id": model} for model in ids]}
    catalog = {"data": [{"id": model, "architecture": {"output_modalities": ["text"]}} for model in ids]}
    selected, excluded = select_models(ranking, catalog, 2)
    assert [r["id"] for r in selected] == ["org/a:free", "org/a"]
    assert len(excluded) == 3


def test_missing_model_and_short_roster_fail_instead_of_silent_replacement():
    with pytest.raises(ValueError, match="missing"):
        select_models({"rows": [{"id": "org/a"}]}, {"data": []}, 1)
    with pytest.raises(ValueError, match="Only 0"):
        select_models({"rows": []}, {"data": []}, 100)


def test_partial_report_never_receives_final_score_or_percentile():
    report = {"status": "deadline_exceeded", "final_score": "100", "daily_percentile": 99,
              "rounds": [{"round": "1/7", "prompt": "A color", "points": 100, "submissions": []}],
              "model_call_durations_s": [1, 3]}
    result = summarize({"model": "org/a"}, report, [])
    assert result["score"] is None
    assert result["daily_percentile"] is None
    assert result["partial_points"] == 100
    assert result["median_model_latency_s"] == 2


async def test_campaign_bounds_concurrency_and_resume_does_not_retry_failures(tmp_path, monkeypatch):
    models = [f"org/model-{n}" for n in range(3)]
    ranking = tmp_path / "ranking.json"
    catalog = tmp_path / "catalog.json"
    ranking.write_text(json.dumps({"source": "https://example.test/models", "captured_at": "fixture",
                                  "rows": [{"id": m} for m in models]}))
    catalog.write_text(json.dumps({"data": [{"id": m, "architecture": {"output_modalities": ["text"]}} for m in models]}))
    active = peak = calls = 0

    async def launch(*command, **kwargs):
        nonlocal active, peak, calls
        active += 1
        peak = max(peak, active)
        calls += 1
        output = Path(command[command.index("--output") + 1])
        output.mkdir()
        model = command[command.index("--model") + 1]
        report = {"status": "failed", "model": model, "error_type": "ProviderError",
                  "scorecard_verified": False, "daily_percentile": None,
                  "navigation_recovery": "bounded", "rounds": [], "recoveries": []}
        (output / "report.json").write_text(json.dumps(report))

        class Process:
            pid = 123
            returncode = 1

            async def wait(self):
                nonlocal active
                await asyncio.sleep(0.01)
                active -= 1
                return 1

        return Process()

    monkeypatch.setattr(asyncio, "create_subprocess_exec", launch)
    args = SimpleNamespace(output=tmp_path / "run", ranking=ranking, catalog=catalog,
                           env_file=tmp_path / ".env", count=3, concurrency=2)
    assert await run_campaign(args) == 0
    assert calls == 3 and peak == 2
    assert await run_campaign(args) == 0
    assert calls == 3
    summary = json.loads((args.output / "summary.json").read_text())
    assert summary["finished"] == 3 and summary["verified_complete"] == 0
    assert summary["statuses"] == {"failed": 3}
    assert not (args.output / ".campaign.lock").exists()
