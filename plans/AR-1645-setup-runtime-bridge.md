# AR-1645 — Setup-to-runtime configuration bridge

Connect persisted setup profiles/defaults to the benchmark planner and runner.
The selected agents, provider, model, and development credential reference must
be consumed directly by `plan`/`run` without a second manual enrollment command.
Reject incompatible selections before mutation and keep missing development
authentication warning-only.
