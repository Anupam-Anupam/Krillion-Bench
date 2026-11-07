"""Browser Use plays Krillion through the visible UI; no game API or answer bank."""

import argparse
import asyncio
from contextlib import asynccontextmanager, suppress
from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import time
import traceback

# Set before importing Browser Use. Benchmark traces stay in the chosen output folder.
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["BROWSER_USE_CLOUD_SYNC"] = "false"
os.environ["BROWSER_USE_LOGGING_LEVEL"] = "result"

from browser_use import ChatAnthropic, ChatGoogle, ChatOpenAI
from browser_use_sdk.v4 import AsyncBrowserUse
from dotenv import dotenv_values
from playwright.async_api import async_playwright

from deadline import DeadlineExceeded, RoundDeadline
from reporting import correction, read_events, rejection, result_details, write_report
from model_policy import error_details


# These selectors were observed on the live UI. Read rendered state only.
READ_STATE = """() => {
  const visible = el => !!el && !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
  const text = selector => [...document.querySelectorAll(selector)].filter(visible).map(e => e.innerText.trim()).filter(Boolean).at(-1) || '';
  const input = document.querySelector('input[aria-label="Your answer"]');
  const body = document.body.innerText;
  const buttons = [...document.querySelectorAll('button')].filter(visible).map(e => e.innerText.trim());
  return {prompt: text('.prompt'), round_label: text('.ds-prompt-count'),
    timer: text('.ds-time-digits'), answering: visible(input),
    input_enabled: visible(input) && !input.disabled,
    answer: visible(input) ? input.value : '', buttons, text: body,
    results: [...document.querySelectorAll('[title^="Round "]')].filter(visible).map(e => e.getAttribute('title')),
    score: (body.match(/SCORE\\s*\\n\\s*(\\d+)/) || [])[1] || null};
}"""


@dataclass
class State:
    prompt: str
    round_label: str
    timer: str
    answering: bool
    answer: str
    buttons: list[str]
    text: str
    score: str | None
    results: list[str] = field(default_factory=list)
    input_enabled: bool = True

    @property
    def key(self):
        return f"{self.round_label}|{self.prompt}"


class Recorder:
    def __init__(self, output):
        self.output = output
        output.mkdir(parents=True, exist_ok=False)
        self.start = time.monotonic()
        self.model_latencies = []

    def event(self, kind, **data):
        with (self.output / "events.jsonl").open("a") as stream:
            stream.write(json.dumps({"elapsed_s": round(time.monotonic() - self.start, 4), "event": kind, **data}) + "\n")


class Observer:
    def __init__(self, page, record, margin=3):
        self.page, self.record = page, record
        self.deadline = RoundDeadline(margin=margin)
        self.rounds = {}
        self.current = None
        self.last_state = None
        self.lock = asyncio.Lock()
        self.blocked = False

    async def read(self):
        async with self.lock:
            # Timestamp before the browser call: remote latency never grants extra time.
            now = time.monotonic()
            state = State(**await asyncio.wait_for(self.page.evaluate(READ_STATE), 5))
            self.last_state = state
            if state.answering:
                if not state.prompt or not state.timer.isdigit():
                    raise RuntimeError("Timed form changed; cannot safely determine deadline")
                if state.key not in self.rounds:
                    self.rounds[state.key] = {"prompt": state.prompt, "round": state.round_label,
                                              "observed_at": now, "initial_timer": int(state.timer)}
                    self.record.event("round_open", **self.rounds[state.key])
                self.current = state.key
                self.deadline.observe(state.key, int(state.timer), now)
                row = self.rounds[state.key]
                rejected = rejection(state.text)
                submissions = row.get("submissions", [])
                if submissions and not state.input_enabled:
                    submissions[-1]["saw_pending"] = True
                if (rejected is not None and submissions and state.input_enabled
                        and (rejected != submissions[-1].get("feedback_at_submit")
                             or submissions[-1].get("saw_pending"))
                        and submissions[-1]["answer"].casefold() == rejected.casefold()
                        and submissions[-1].get("outcome") == "unconfirmed"):
                    submissions[-1].update(outcome="rejected", evidence="visible_no_echo")
                    self.record.event("answer_rejected", round=row["round"], answer=rejected)
                corrected = correction(state.text)
                if (corrected and submissions and submissions[-1].get("outcome") == "unconfirmed"
                        and submissions[-1]["answer"].casefold() == corrected["answer"].casefold()):
                    submissions[-1].update(outcome="confirmation_required", evidence="visible_correction",
                                           suggested_answer=corrected["suggested_answer"])
                    self.record.event("answer_correction", round=row["round"], **corrected)
            else:
                if self.current and self.current in self.rounds:
                    row = self.rounds[self.current]
                    if "form_closed_at" not in row:
                        row["form_closed_at"] = now
                        row["elapsed_to_form_close_s"] = now - row["observed_at"]
                        self.record.event("form_closed", round=row["round"], round_elapsed_s=row["elapsed_to_form_close_s"])
                    points = re.search(r"\+(\d+) PTS", state.text)
                    if points and "points" not in row:
                        row["points"] = int(points.group(1))
                        row["result_text"] = state.text
                        details = result_details(state.text, row["points"])
                        row.update(details)
                        self.record.event("round_result", round=row["round"], **details)
                self.deadline.clear()
            return state

    async def watch(self):
        while True:
            await self.read()
            # Expiry stops answering, not observation or the entire seven-round game.
            # Model calls/actions own cancellable deadlines; player waits for the UI result.
            await asyncio.sleep(0.25)


def load_config(path):
    # Explicit file only: never search parent directories for credentials automatically.
    values = dotenv_values(path) if path else {}
    for key in ("BROWSER_USE_API_KEY", "OPENAI_API_KEY", "OPENAI_BASE_URL", "OPENAI_MODEL", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"):
        if values.get(key) and not os.environ.get(key):
            os.environ[key] = values[key]


class TimedModel:
    def __init__(self, model, record):
        self.wrapped, self.record = model, record

    def __getattr__(self, key):
        return getattr(self.wrapped, key)

    def enable_prompt_json(self):
        if isinstance(self.wrapped, ChatOpenAI) and not self.wrapped.dont_force_structured_output:
            self.wrapped.dont_force_structured_output = True
            return True
        return False

    async def ainvoke(self, *args, **kwargs):
        start = time.monotonic()
        try:
            return await self.wrapped.ainvoke(*args, **kwargs)
        finally:
            duration = time.monotonic() - start
            self.record.model_latencies.append(duration)
            self.record.event("model_call", duration_s=duration)


def make_model(args):
    if args.provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            raise ValueError("Set OPENAI_API_KEY")
        return ChatOpenAI(model=args.model, base_url=os.environ.get("OPENAI_BASE_URL") or None,
                          max_retries=0, timeout=None, temperature=None, frequency_penalty=None,
                          max_completion_tokens=args.max_output_tokens, reasoning_effort=args.reasoning)
    if args.provider == "anthropic":
        if args.max_output_tokens is None:
            raise ValueError("Native Anthropic requires --max-output-tokens; use OpenRouter to omit the request cap")
        return ChatAnthropic(model=args.model, max_retries=0, timeout=None,
                             max_tokens=args.max_output_tokens)
    # This adapter counts attempts (not retries); one means no retries.
    return ChatGoogle(model=args.model, max_retries=1, max_output_tokens=args.max_output_tokens)


@asynccontextmanager
async def browser_session(args, record):
    cloud = remote = None
    try:
        if args.browser == "cloud":
            if not os.environ.get("BROWSER_USE_API_KEY"):
                raise ValueError("Set BROWSER_USE_API_KEY or use --browser local")
            cloud = AsyncBrowserUse(max_retries=0)
            remote = await cloud.browsers.create(
                timeout=15, solve_captchas=False, enable_recording=True,
                browser_screen_width=1280, browser_screen_height=800,
                metadata={"project": "krillion-benchmark", "run": record.output.name},
            )
            if not remote.cdp_url:
                raise RuntimeError("Cloud browser did not provide a connection endpoint")
            record.event("cloud_session", session_id=str(remote.id))
        async with async_playwright() as playwright:
            if remote:
                connection = await playwright.chromium.connect_over_cdp(remote.cdp_url)
                context = connection.contexts[0]
            else:
                connection = await playwright.chromium.launch(
                    executable_path=args.executable, headless=not args.headed,
                )
                context = await connection.new_context(viewport={"width": 1280, "height": 800})
            try:
                await context.tracing.start(screenshots=True, snapshots=True)
                page = context.pages[0] if context.pages else await context.new_page()
                page.set_default_timeout(5000)
                await page.set_viewport_size({"width": 1280, "height": 800})
                await page.emulate_media(reduced_motion="reduce")
                await page.goto(args.url, wait_until="domcontentloaded", timeout=30000)
                await page.get_by_role("button", name="▼ BEGIN DESCENT ▼", exact=True).wait_for(timeout=20000)
                record.event("browser_ready", browser=args.browser)
                await page.screenshot(path=str(record.output / "initial.png"))
                try:
                    yield connection, page
                finally:
                    with suppress(Exception):
                        await page.screenshot(path=str(record.output / "final.png"))
                        (record.output / "final.txt").write_text(await page.locator("body").inner_text())
                    with suppress(Exception):
                        await context.tracing.stop(path=str(record.output / "trace.zip"))
            finally:
                await connection.close()
    finally:
        if cloud:
            try:
                if remote:
                    await cloud.browsers.stop(remote.id)
            finally:
                await cloud.close()


async def scripted_baseline(page, observer, answers):
    """Exercises the real controls; does not evaluate an LLM or optimize score."""
    for number in range(1, 8):
        button = "▼ BEGIN DESCENT ▼" if number == 1 else "DESCEND ▼"
        # Real keyboard activation avoids the continuously moving button's coordinates.
        await page.get_by_role("button", name=button, exact=True).press("Enter", timeout=15000)
        field = page.get_by_role("textbox", name="Your answer", exact=True)
        await field.wait_for(timeout=10000)
        state = await observer.read()
        # Human-supplied control answers are never passed to the evaluated agent.
        if state.prompt not in answers:
            raise ValueError("Baseline answer file does not cover this visible prompt")
        answer = answers[state.prompt]
        observer.deadline.check(time.monotonic())
        await field.fill(answer)
        from player import Action, execute
        await execute(Action(kind="click", target="DIVE"), state, observer)
        observer.record.event("baseline_submit", round=number, answer=answer, prompt=state.prompt)
        await field.wait_for(state="hidden", timeout=10000)
        await observer.read()
    await page.get_by_role("button", name="SURFACE ▲", exact=True).press("Enter", timeout=15000)
    await page.get_by_role("button", name="Copy result", exact=True).wait_for(timeout=10000)
    from player import verified_completion
    # The total animates; allow the final UI to settle before checking its sum.
    until = time.monotonic() + 5
    while time.monotonic() < until:
        await observer.read()
        if verified_completion(observer):
            return "baseline_finished"
        await asyncio.sleep(0.1)
    raise RuntimeError("Final scoreboard did not verify seven rounds and total score")


async def play(session, observer, args):
    from player import play_actions
    return await play_actions(observer, TimedModel(make_model(args), observer.record), args.max_steps,
                              args.vision, args.navigation_recovery, args.navigation_timeout, args.model_retries)


async def run(args):
    record = Recorder(args.output)
    observer = None
    status, error = "failed", None
    record.event("config", browser=args.browser, model=args.model, provider=args.provider,
                 vision=args.vision, margin_s=args.margin, command=args.command,
                 max_output_tokens=args.max_output_tokens, model_retries=args.model_retries,
                 navigation_timeout_s=args.navigation_timeout, round_timeout_policy="continue",
                 requested_reasoning=args.reasoning, navigation_recovery=args.navigation_recovery, viewport=[1280, 800], reduced_motion=True)
    try:
        async with browser_session(args, record) as (session, page):
            if args.command == "smoke":
                status = "smoke_passed"
            else:
                observer = Observer(page, record, args.margin)
                answers = json.loads(args.answers_file.read_text()) if args.command == "baseline" else None
                worker = asyncio.create_task(scripted_baseline(page, observer, answers) if args.command == "baseline" else play(session, observer, args))
                watchdog = asyncio.create_task(observer.watch())
                try:
                    done, _ = await asyncio.wait({worker, watchdog}, timeout=args.run_timeout, return_when=asyncio.FIRST_COMPLETED)
                    if not done:
                        raise TimeoutError("Full run deadline reached")
                    if watchdog in done:
                        await watchdog
                    status = await worker
                finally:
                    observer.blocked = True
                    for task in (worker, watchdog):
                        task.cancel()
                    await asyncio.gather(worker, watchdog, return_exceptions=True)
                state = await observer.read()
                record.event("final_state", score=state.score, buttons=state.buttons, text=state.text)
    except Exception as exc:
        # Exception messages can contain authenticated CDP URLs or request headers.
        error = type(exc).__name__
        if isinstance(exc, DeadlineExceeded):
            status = "deadline_exceeded"
        record.event("failure", **error_details(exc),
                     frames=[{"file": Path(f.filename).name, "line": f.lineno, "function": f.name}
                             for f in traceback.extract_tb(exc.__traceback__)])
    report = {"status": status, "error_type": error, "model": args.model,
              "browser": args.browser, "command": args.command,
              "navigation_recovery": args.navigation_recovery,
              "max_output_tokens": args.max_output_tokens, "model_retries": args.model_retries,
              "round_timeout_policy": "continue",
              "model_call_durations_s": record.model_latencies,
              "rounds": list(observer.rounds.values()) if observer else []}
    if observer and observer.last_state:
        report["final_score"] = observer.last_state.score
        report["scoreboard"] = observer.last_state.results
    final = record.output / "final.txt"
    write_report(report, record.output, final.read_text() if final.exists() else "", read_events(record.output))
    print(json.dumps({"status": status, "error_type": error, "output": str(record.output)}))
    return 0 if status in {"smoke_passed", "baseline_finished", "agent_finished"} else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["smoke", "baseline", "play"])
    parser.add_argument("--browser", choices=["local", "cloud"], default="cloud")
    parser.add_argument("--provider", choices=["openai", "anthropic", "google"], default="openai")
    parser.add_argument("--model")
    parser.add_argument("--env-file", type=Path, action="append", default=[])
    parser.add_argument("--url", default="https://krillion.io/")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--executable", help="Local Chromium/Chrome executable path")
    parser.add_argument("--answers-file", type=Path, help="Baseline only: exact visible prompt to control-answer JSON")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--vision", action="store_true", help="Include screenshots in model input (separate evaluation track)")
    parser.add_argument("--margin", type=float, default=3)
    parser.add_argument("--max-steps", type=int, default=50)
    parser.add_argument("--run-timeout", type=float, default=600)
    parser.add_argument("--max-output-tokens", type=int, default=None,
                        help="Optional API output cap; default omits it (provider limits still apply)")
    parser.add_argument("--navigation-timeout", type=float, default=60,
                        help="Inference timeout outside questions; questions use the game deadline")
    parser.add_argument("--model-retries", type=int, default=2,
                        help="Additional same-model retries for transient API failures, within remaining time")
    parser.add_argument("--navigation-recovery", choices=["off", "bounded"], default="bounded",
                        help="Recover stalled non-answer navigation; off is the strict track")
    parser.add_argument("--reasoning", default="low", choices=["minimal", "low", "medium", "high"])
    args = parser.parse_args()
    for path in args.env_file:
        load_config(path)
    args.model = args.model or os.environ.get("OPENAI_MODEL")
    if args.command == "play" and not args.model:
        parser.error("Set --model explicitly or OPENAI_MODEL")
    if args.command == "baseline" and not args.answers_file:
        parser.error("baseline requires --answers-file")
    if args.command != "baseline" and args.answers_file:
        parser.error("--answers-file is only allowed for the scripted baseline")
    if not 1 <= args.margin <= 10:
        parser.error("--margin must be between 1 and 10 seconds")
    if args.max_output_tokens is not None and args.max_output_tokens < 1:
        parser.error("--max-output-tokens must be positive or omitted")
    if not 0 <= args.model_retries <= 10 or not 1 <= args.navigation_timeout <= 120:
        parser.error("--model-retries must be 0–10 and --navigation-timeout must be 1–120")
    args.output = (args.output or Path("artifacts") / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")).resolve()
    raise SystemExit(asyncio.run(run(args)))


if __name__ == "__main__":
    main()
