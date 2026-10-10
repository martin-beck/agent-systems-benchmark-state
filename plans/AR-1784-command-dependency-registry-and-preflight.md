# AR-1784 plan: command dependency registry and preflight

1. Inventory every public command, adapter, monitor, runtime path, workload
   adapter, and source-build recipe for external executable/library/host needs.
2. Define typed dependency roles: tool-install ID, workload-install ID,
   project-built dependency, and host-only capability; include ownership,
   platform compatibility, and remediation.
3. Seed the registry with all current agent, cli2key, perf, bpftool, provider,
   procfs/cgroup, Bubblewrap, systemd, and build-toolchain distinctions.
4. Implement fail-fast preflight/status output and generated exact install or
   host-remediation guidance before execution.
5. Add mechanical coverage rejecting an undeclared executable invocation or a
   newly supported tool/workload lacking acquisition, dependency, and preflight
   metadata; test every initial ID and host-only negative.
