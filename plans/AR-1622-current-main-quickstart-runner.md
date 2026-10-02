# AR-1622 — current-main fresh-user quickstart runner and operator guide

Provide one disposable, executable qualification runner and concise operator
guide for the shortest supported journey: clone current main, install the
default `dev` channel, launch the TUI, select OpenRouter plus an available
model and coding agents, enter an API key without echoing it, run selected or
all workloads, record responses, seal the cassette, run offline, and compare
the results. Human-readable output remains the default and every command has
an explicit `--json` form.

The runner must use generated development fixtures when credentials are absent,
report each selectable step and failure remediation, and leave no durable
user secrets. Require paired ASB/TUI exact-SHA evidence and independent review.
