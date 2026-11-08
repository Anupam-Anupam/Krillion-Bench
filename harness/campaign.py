"""Run a frozen model roster against Krillion, with resumable, bounded concurrency."""

import argparse
import asyncio
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys

from reporting import cell, markdown
from leaderboard import export_campaign


SOURCES = ("runner.py", "player.py", "deadline.py", "reporting.py", "model_policy.py", "metrics.py", "leaderboard.py", "campaign.py", "uv.lock")


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path, value):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, indent=2) + "\n")
    temp.replace(path)


def select_models(ranking, catalog, count, paid_only=False):
    by_id = {m["id"]: m for m in catalog["data"]}
    selected, excluded, seen = [], [], set()
    for row in ranking["rows"]:
        model = row["id"]
        if model in seen:
            raise ValueError(f"Duplicate ranked model: {model}")
        seen.add(model)
        reason = ("latest alias" if model.startswith("~") else
                  "automatic router" if model.startswith("openrouter/") else
                  "free endpoint excluded by paid-only selection" if paid_only and model.endswith(':free') else
                  "asynchronous batch variant" if model.endswith(":batch") else None)
        if reason:
            excluded.append({**row, "reason": reason})
            continue
        if model not in by_id:
            raise ValueError(f"Ranked model missing from frozen API catalog: {model}")
        meta = by_id[model]
        if "text" not in meta["architecture"]["output_modalities"]:
            raise ValueError(f"Non-text model in text ranking: {model}")
        selected.append({**row, "rank": len(selected) + 1,
                         "canonical_slug": meta.get("canonical_slug"),
                         "pricing": meta.get("pricing", {}),
                         "supported_parameters": meta.get("supported_parameters", [])})
        if len(selected) == count:
            return selected, excluded
    raise ValueError(f"Only {len(selected)} eligible models; requested {count}")


def source_hashes(root):
    # Preserve logical manifest keys while the dependency lock stays at repo root.
    paths = {name: root / name for name in SOURCES}
    if not paths['uv.lock'].is_file():
        paths['uv.lock'] = root.parent / 'uv.lock'
    return {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in paths.items()}


def summarize(row, report, events):
    verified = report.get("scorecard_verified", False)
    durations = report.get("model_call_durations_s", [])
    rounds = report.get("rounds", [])
    return {**row, "status": report.get("status", "missing_report"),
            "error_type": report.get("error_type"), "metrics": report.get("metrics"), "scorecard_verified": verified,
            "score": int(report["final_score"]) if verified else None,
            "partial_points": sum(r.get("points", 0) or 0 for r in rounds),
            "daily_percentile": report.get("daily_percentile") if verified else None,
            "rounds_observed": len(rounds),
            "rounds_scored": sum(r.get("points") is not None for r in rounds),
            "submissions": sum(len(r.get("submissions", [])) for r in rounds),
            "model_calls": len(durations),
            "median_model_latency_s": statistics.median(durations) if durations else None,
            "max_model_latency_s": max(durations) if durations else None,
            "navigation_recoveries": len(report.get("recoveries", [])),
            "missed_rounds": sum(r.get("round_outcome") == "missed" for r in rounds),
            "model_issues": report.get("model_issues", []),
            "prompts": {r["round"]: r["prompt"] for r in rounds},
            "browser_ready": any(e["event"] == "browser_ready" for e in events)}


def update_reports(output, manifest, state):
    ordered = sorted(state["runs"].values(), key=lambda r: r["rank"])
    finished = [r for r in ordered if r["status"] != "running"]
    verified = [r for r in finished if r.get("scorecard_verified")]
    counts = dict(Counter(r["status"] for r in finished))
    atomic_json(output / "summary.json", {"updated_at": utcnow(), "planned": len(manifest["models"]),
                "finished": len(finished), "verified_complete": len(verified), "statuses": counts,
                "stop_reason": state.get("stop_reason"), "runs": ordered})
    public_reports = {}
    for row in finished:
        path = output / row['directory'] / 'report.json'
        if path.exists():
            public_reports[row['model']] = json.loads(path.read_text())
    public_summary = dict(updated_at=utcnow(), runs=finished)
    atomic_json(output / 'leaderboard.json', export_campaign(public_summary, manifest, public_reports))
    lines = ["# OpenRouter top 100: Krillion campaign", "",
             f"Finished: **{len(finished)}/{len(manifest['models'])}**. Verified full games: **{len(verified)}**.", "",
             "Selection: active text model variants in OpenRouter’s **Top Weekly** directory order, "
             "excluding latest aliases, automatic routers, and asynchronous batch variants. "
             + ("Free endpoints are excluded by paid-only selection. " if manifest.get('paid_only') else "Free and paid variants are separate entries. ")
             + "This is usage selection, not a quality ranking.", "",
             f"[OpenRouter source]({manifest['ranking_source']}); captured {manifest['ranking_captured_at']}. "
             "Ranking attribution: OpenRouter, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "
             "Directory token counts are a live seven-day window and differ from the rankings page’s completed-day buckets.", "",
             "One fresh Browser Use Cloud browser per model; DOM observations; bounded navigation recovery; "
             "25-second game clock; inference uses remaining round time; 3-second safety margin plus timer rounding; "
             f"output-token request cap: {manifest['settings'].get('max_output_tokens')}; "
             f"same-model transient retries: {manifest['settings'].get('model_retries', 2)}; "
             "requested low reasoning; schema-validated actions. Missed questions continue to the game's actual "
             "scorecard. No answer fallback or replacement of failed entries.", "",
             f"Concurrency: {manifest['concurrency']}. Frozen harness hashes and roster: `manifest.json`. "
             "The daily percentage is the game’s live ‘better than’ comparison, not score divided by 700. "
             "Percentiles may drift as other people play. Partial scores are not ranked with completed games.", "",
             "| Usage rank | Model | Status | Score /700 | Partial points | Daily % | Rounds scored | Calls | Median call s | Recovery attempts |",
             "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in ordered:
        values = [r["rank"], r["model"], r["status"], r.get("score"),
                  r.get("partial_points") if not r.get("scorecard_verified") else None,
                  r.get("daily_percentile"), r.get("rounds_scored"), r.get("model_calls"),
                  round(r["median_model_latency_s"], 3) if r.get("median_model_latency_s") is not None else None,
                  r.get("navigation_recoveries")]
        lines.append("| " + " | ".join(map(cell, values)) + " |")
    if state.get("stop_reason"):
        lines += ["", f"Scheduling stopped: {cell(state['stop_reason'])}."]
    for r in finished:
        report_path = output / r["directory"] / "report.json"
        if report_path.exists():
            report = json.loads(report_path.read_text())
            lines += ["", "---", "", markdown(report)]
        else:
            lines += ["", f"## {cell(r['model'])}", "", f"No runner report: {cell(r['status'])}."]
    (output / "REPORT.md").write_text("\n".join(lines) + "\n")


async def run_campaign(args):
    root = Path(__file__).resolve().parent
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    lock = output / ".campaign.lock"
    # A stale lock needs explicit investigation; never silently double-submit runs.
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    try:
        manifest_path = output / "manifest.json"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())
            if manifest["source_sha256"] != source_hashes(root):
                raise ValueError("Harness changed since freeze; create a new campaign")
            if args.concurrency != manifest["concurrency"]:
                raise ValueError("Concurrency changed since freeze")
            if manifest.get('paid_only', False) != getattr(args, 'paid_only', False):
                raise ValueError('Paid-only selection changed since freeze')
            for key, default in (("max_output_tokens", None), ("model_retries", 2), ("navigation_timeout", 60)):
                if manifest['settings'].get(key) != getattr(args, key, default):
                    raise ValueError(f"{key} changed since freeze")
        else:
            ranking = json.loads(args.ranking.read_text())
            models, excluded = select_models(ranking, json.loads(args.catalog.read_text()), args.count,
                                              getattr(args, 'paid_only', False))
            manifest = {"created_at": utcnow(), "utc_date": utcnow()[:10], "models": models,
                        "excluded": excluded, "source_sha256": source_hashes(root),
                        "ranking_source": ranking["source"], "ranking_captured_at": ranking["captured_at"],
                        "concurrency": args.concurrency, "outer_timeout_s": 900,
                        "paid_only": getattr(args, 'paid_only', False),
                        "settings": {"provider": "openai", "browser": "cloud", "vision": False,
                                     "navigation_recovery": "bounded", "reasoning": "low",
                                     "max_output_tokens": getattr(args, 'max_output_tokens', None),
                                     "model_retries": getattr(args, 'model_retries', 2),
                                     "navigation_timeout": getattr(args, 'navigation_timeout', 60),
                                     "round_timeout_policy": "continue",
                                     "terminal_failure_policy": "collect_actual_scorecard_without_answers",
                                     "scorecard_collection_timeout_s": 240,
                                     "max_steps": 50, "run_timeout_s": 600, "margin_s": 3}}
            atomic_json(manifest_path, manifest)
        state_path = output / "state.json"
        state = json.loads(state_path.read_text()) if state_path.exists() else {"runs": {}, "reference_prompts": {}}
        for r in state["runs"].values():
            if r["status"] == "running":
                raise ValueError("Interrupted attempt present; inspect its process and report before resuming")
        queue = asyncio.Queue()
        for model in manifest["models"]:
            if model["id"] not in state["runs"]:
                queue.put_nowait(model)

        def save():
            atomic_json(state_path, state)
            update_reports(output, manifest, state)

        async def worker():
            while not queue.empty() and not state.get("stop_reason"):
                if utcnow()[:10] != manifest["utc_date"]:
                    state["stop_reason"] = "UTC date changed; avoid mixing daily puzzles"
                    save()
                    break
                model = queue.get_nowait()
                model_id = model["id"]
                directory = f"{model['rank']:03d}-" + model_id.replace("/", "--").replace(":", "-")
                row = {"rank": model["rank"], "model": model_id, "directory": directory,
                       "started_at": utcnow(), "status": "running"}
                state["runs"][model_id] = row
                save()
                print(f"START {model['rank']:03d} {model_id}", flush=True)
                command = [sys.executable, str(root / "runner.py"), "play", "--env-file", str(args.env_file.resolve()),
                           "--provider", "openai", "--model", model_id, "--navigation-recovery", "bounded",
                           "--output", str(output / directory)]
                command += ['--pricing-file', str(manifest_path), '--model-retries', str(manifest['settings']['model_retries']),
                            '--navigation-timeout', str(manifest['settings']['navigation_timeout'])]
                if manifest['settings']['max_output_tokens'] is not None:
                    command += ['--max-output-tokens', str(manifest['settings']['max_output_tokens'])]
                proc = None
                try:
                    with (output / (directory + ".log")).open("w") as log:
                        proc = await asyncio.create_subprocess_exec(*command, cwd=root, stdout=log, stderr=log)
                        row["pid"] = proc.pid
                        save()
                        try:
                            await asyncio.wait_for(proc.wait(), manifest["outer_timeout_s"])
                        except TimeoutError:
                            proc.kill()
                            await proc.wait()
                            row["status"] = "outer_timeout"
                    report_path = output / directory / "report.json"
                    if report_path.exists():
                        report = json.loads(report_path.read_text())
                        events_path = output / directory / "events.jsonl"
                        events = [json.loads(x) for x in events_path.read_text().splitlines()] if events_path.exists() else []
                        row = summarize(row, report, events)
                    elif row["status"] == "running":
                        row["status"] = "runner_exited_without_report"
                    row["exit_code"] = proc.returncode
                except asyncio.CancelledError:
                    if proc and proc.returncode is None:
                        proc.terminate()
                        await proc.wait()
                    row["status"] = "interrupted"
                    raise
                except Exception as exc:
                    row.update(status="orchestrator_error", error_type=type(exc).__name__)
                finally:
                    row["ended_at"] = utcnow()
                    state["runs"][model_id] = row
                    for label, prompt in row.get("prompts", {}).items():
                        previous = state["reference_prompts"].setdefault(label, prompt)
                        if previous != prompt:
                            state["stop_reason"] = "Daily prompt mismatch detected"
                    save()
                    print(f"END {model['rank']:03d} {model_id}: {row['status']} score={row.get('score')} daily={row.get('daily_percentile')}", flush=True)
                    queue.task_done()
        save()
        await asyncio.gather(*(worker() for _ in range(args.concurrency)))
        return 0 if not state.get("stop_reason") else 2
    finally:
        lock.unlink()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ranking", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--env-file", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--max-output-tokens", type=int, default=None)
    parser.add_argument("--model-retries", type=int, default=2)
    parser.add_argument("--navigation-timeout", type=float, default=60)
    parser.add_argument("--paid-only", action="store_true", help="Exclude :free endpoints and record roster exclusions")
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 8 or args.count < 1:
        parser.error("Concurrency must be 1–8 and count must be positive")
    if args.max_output_tokens is not None and args.max_output_tokens < 1:
        parser.error('Output-token cap must be positive or omitted')
    if not 0 <= args.model_retries <= 10 or not 1 <= args.navigation_timeout <= 120:
        parser.error('Retries must be 0–10 and navigation timeout must be 1–120 seconds')
    if not os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENAI_BASE_URL") != "https://openrouter.ai/api/v1":
        parser.error("Set OPENAI_API_KEY and OPENAI_BASE_URL for OpenRouter in the environment")
    raise SystemExit(asyncio.run(run_campaign(args)))
