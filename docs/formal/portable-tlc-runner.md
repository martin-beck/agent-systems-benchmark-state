# Portable TLC resource bounds

The state runner keeps virtual address-space admission separate from the
attested physical and swap envelope. `memory_max=3G` and `swap_max=3G` remain
the publication contract; portable execution applies `RLIMIT_AS=8G` so the
JVM's native mappings cannot be mistaken for 3 GiB of physical memory.

The 8 GiB address-space limit is bounded and is recorded as
`resource_bounds.address_space_max` in every success attestation. It is not a
replacement for the physical/swap limits, and lowering or removing either
bound is invalid. A requested address-space limit at or below the JVM heap is
rejected before admission.

The runner's default queue, temporary model state and attestation roots are
owner-private directories below `/srv/data/projects/.asb-tlc`. Admission uses
the exact coordinator-wide `/tmp/agent-workflow-coordinator-tlc-admission.lock`
fence; replacing it with a private lock is diagnostic-only and cannot qualify
publication evidence. Callers cannot redirect the runtime root or attestation
outside that approved project root. Every TLC process is started
without a shell, with output sent to bounded sinks rather than retained in
evidence, and has a finite deadline plus process-group teardown. Each durable
outcome binds the reviewed source commit/tree, runner and input digests,
effective profile, queue/lock/artifact paths, and exit classification.

`portable-smoke` is the only tier allowed to use `timeout`/`prlimit`; required
publication and exhaustive tiers continue to require the canonical
`systemd-run --user` cgroup boundary. All tiers use the exact profiles in
`formal/tier-evidence.json` and execute through `verify.sh` and
`tools/tlc_runner.py`, never by invoking TLC directly from a helper.
