"""Monotonic deadlines independent of model calls and browser actions."""

from dataclasses import dataclass
import math


class DeadlineExceeded(RuntimeError):
    pass


@dataclass
class RoundDeadline:
    margin: float = 3.0
    key: str | None = None
    expires: float | None = None

    def observe(self, key: str, seconds: float, now: float) -> None:
        if not math.isfinite(seconds) or not 0 <= seconds <= 25:
            raise ValueError("Unrecognized game timer")
        # The UI rounds to whole seconds. Subtract one to avoid overestimating.
        candidate = now + max(0, seconds - 1 - self.margin)
        if self.key != key:
            self.key, self.expires = key, candidate
        else:
            self.expires = min(self.expires, candidate)

    def remaining(self, now: float) -> float:
        return math.inf if self.expires is None else self.expires - now

    def check(self, now: float) -> None:
        if self.remaining(now) <= 0:
            raise DeadlineExceeded("Round submission deadline reached")

    def clear(self) -> None:
        self.key = self.expires = None
