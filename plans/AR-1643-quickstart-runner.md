# AR-1643 — Executable fresh-user quickstart runner

Provide one disposable runner covering clone/current dev install, wizard
selection, workload execution, cassette record/seal, offline replay, and result
comparison for ASB and the standalone TUI. It must use selection-driven prompts,
clear human output, explicit `--json`, and development fixtures when credentials
are absent.
