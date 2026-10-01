# AR-1612 — selected-workload recording campaign controls

Add a human-readable and `--json` control/API contract for selecting one, many,
or all currently implemented workloads and agents for response recording. The
operation must show the selected provider/model/agent defaults, reject invalid
combinations without mutating configuration, seal a complete cassette, and
make it selectable by the following offline benchmark run. Preserve bounded
timeouts, cancellation, redaction, and provider-egress denial during replay.
