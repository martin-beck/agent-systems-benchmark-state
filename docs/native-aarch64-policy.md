# AArch64 qualification policy

This policy applies to every current and future AR, including older plans whose historical
completion evidence mentions native ARM64 or AArch64 checks.

Native ARM64 hardware is optional future qualification. Its absence, unavailability, cost,
provider authorization, or failure must not block implementation, review, integration, release,
documentation, or completion of an otherwise accepted AR. Native evidence must still be labeled
accurately and must never be inferred from cross-builds or emulation.

Where an AArch64 behavior can be exercised without a native kernel or architecture-specific
performance counter, the pinned x86_64-hosted QEMU lane delivered by AR-0707 is required. This
includes compilation, userspace runtime, protocol, adapter, replay, packaging, CLI/TUI, and
portable failure-path checks where the dependency closure is available. Required evidence records
the emulator, sysroot/image, toolchain, source revision, and the emulated-aarch64 label.

Native x86_64 remains required where a task needs real kernel, cgroup, PSI, perf, eBPF, timing,
contention, or performance evidence. QEMU AArch64 is not used for native performance baselines,
PMU/eBPF correctness, native-kernel claims, or hardware support claims. Those ARM64-only
observations are documented as optional future tests and unsupported or unqualified until run.

For CI and acceptance:

- required pull-request gates use native x86_64 plus the pinned QEMU AArch64 lane where applicable;
- native ARM64 jobs may run as non-blocking informational or scheduled evidence;
- a missing or failed native ARM64 job cannot prevent an AR from completing;
- support matrices distinguish emulated-aarch64, native-tested, build-only, and unsupported
  without extrapolation; and
- historical evidence remains unchanged.

Broad phrases such as "native matrix", "both architectures", or "x86_64/aarch64 gates" are
governed by this policy: they require native x86_64 and applicable QEMU-emulated AArch64 coverage,
while native ARM64 is optional future qualification.
