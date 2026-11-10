# Billing capture

New execution plans should use the billing capture revision in `harness/billing_capture.py`. The current immutable benchmark execution keeps its original source until fully drained; a new plan must record the updated source hashes before using this revision.

Gameplay deadlines still cancel the caller at the original time. The HTTP accounting task can finish independently, and its response is collected for up to 60 seconds after gameplay. No delayed answer can become a browser action. Usage is captured before structured output parsing. Missing usage or cost is reconciled using only generation IDs returned by that run and the authenticated OpenRouter generation metadata endpoint.

Generation IDs and authorization headers remain in memory and are never included in events or public exports. Reports contain numeric usage and a count of unresolved requests. Provider failures and responses without usable identifiers remain unresolved; they are never assigned zero cost. Existing immutable clean games are not replayed to repair accounting.

Average calculations use complete accounting samples. Daily can show recorded partial totals with a lower-bound marker. No partial total is described as a full billed cost.
