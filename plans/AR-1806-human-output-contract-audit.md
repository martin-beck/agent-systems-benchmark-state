# AR-1806 plan: exhaustive human output contract audit

Use the route manifest to run deterministic CLI journeys through every command
and subcommand. Test normal success, user mistakes, missing prerequisites, and
typed operational failures in TTY and redirected mode. Replace default raw
serialization with concise human presentations, retaining exact JSON only
behind `--json`. Enforce that the output router is the sole ASB-owned writer.
