# AR-1660 — fresh-user setup-to-comparison acceptance runner

Provide a disposable, selection-driven runner that proves a fresh user can
install the default dev channel, configure OpenRouter and coding agents/models,
set shared defaults, run selected workloads, record responses, replay offline,
and compare results. Emit concise human output by default and stable `--json`
evidence for the paired ASB/TUI release gate.
