---
{
  "branch": "feature/ar-1293-state-tla-admission",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1293",
  "next_action": "Blocked on AR-1307 qualification and AR-1308 capacity/input repair: remote AR-1307 is ab485f767 while task requires 969eef058; AR-1308 preflight failed closed on 4.9 GiB approved-root free versus 16 GiB minimum and missing lock/JDK/TLC at runtime root. Reopen only with exact current input bundle and passing preflight; do not run formal TLC locally.",
  "observed_branch": "feature/ar-1293-state-tla-admission",
  "observed_dirty": 0,
  "observed_head": "f1931686c9297f5661446bf1871870b659d69684",
  "owner": "",
  "plan": "../plans/AR-1293.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Repair the state-repository TLA admission runner and truthful worktree metadata.",
  "task_revision": 746,
  "title": "State-scoped TLA admission runner",
  "updated_at": "2026-09-18T21:04:30+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1293-tla-admission"
}
---

## AR-1293

AR-1181 identified a coordination boundary defect: state formal/handoffctl
verification references `tools/tlc_runner.py`, but the task points at an ASB
product worktree and no state runner exists. This successor owns only truthful
state metadata and bounded runner implementation. It must not edit product code,
modify or extract handoffctl, weaken formal verification, or touch asb-tui.

- 2026-09-17T04:42:32+00:00: State-scoped runner successor is independent of product ARs and repairs
  the truthful worktree boundary.

- 2026-09-17T04:43:08+00:00: Claimed by codex-ar1293-tlc-admission-20260917.

- 2026-09-17T04:43:47+00:00: Recorded command exit 0; command argv SHA-256
  16c0838341ddca5d4b65a8ff791042a83c2f9378785860e38372cbe4b6e7f8e9.

- 2026-09-17T04:45:16+00:00: Recorded command exit 0; command argv SHA-256
  dc14245e4f21dd5a411424ad34d792846c147a8f704213431d10914ed636b361.

- 2026-09-17T04:45:25+00:00: Recorded command exit 0; command argv SHA-256
  48ef0a4e7fa688f98b7d6196a72b4ebd0d4108853007fe18c1b0b3e952c9b251.

- 2026-09-17T04:46:48+00:00: Heartbeat by codex-ar1293-tlc-admission-20260917.

- 2026-09-17T04:47:38+00:00: Recorded command exit 0; command argv SHA-256
  50aaa6c6cb930bfebdb3fdc6605de95fed493be288112a9a3251f3111a8432b0.

- 2026-09-17T04:48:05+00:00: Recorded command exit 2; command argv SHA-256
  87a995b1783b823af5b6d72547fbc457943a0b2851883a5965b11d85be96f4b3.

- 2026-09-17T04:48:29+00:00: Recorded command exit 1; command argv SHA-256
  4be48d1554a9693adfee682c331adba51ae71ed9f91e57290681927c91e46430.

- 2026-09-17T04:49:36+00:00: Recorded command exit 1; command argv SHA-256
  427236591f7d2a971d824ad15f7eff6e53a63c6e00114a09c5f822c244436751.

- 2026-09-17T04:49:57+00:00: Recorded command exit 1; command argv SHA-256
  320230293fd894d4cb42eb259ddc36877212643db12bc7c7a9cf13813f958933.

- 2026-09-17T04:50:10+00:00: Recorded command exit 0; command argv SHA-256
  591a874cddcae0eb0ecd0c23a88f8d36bc22fbeba95b22000796998d8560af43.

- 2026-09-17T04:50:19+00:00: Recorded command exit 0; command argv SHA-256
  fe077bc6af7fdeb53fa1d9e53d61813e9d84bc2160640f395cf543fb741fe18f.

- 2026-09-17T04:50:52+00:00: Recorded implementation candidate and exact gate blockers; no
  handoffctl/product changes.

- 2026-09-17T04:50:54+00:00: Blocked ownerless after candidate 885d14159. Focused runner tests, Ruff
  and mypy pass; full state suite and canonical formal smoke remain blocked by the baseline vendor
  mismatch and host admission-lock ownership above. Preserve the signed candidate for follow-up.

- 2026-09-17T05:00:54+00:00: AR-1294 restored immutable coordinator vendor integrity; reopen to
  repair candidate private lock/queue paths, attestation fixtures and malformed-input gates.
  External root-owned lock remains untouched.

- 2026-09-17T05:01:25+00:00: Claimed by codex-ar1293-tlc-repair-20260917.

- 2026-09-17T05:01:27+00:00: Heartbeat by codex-ar1293-tlc-repair-20260917.

- 2026-09-17T05:05:22+00:00: Recorded command exit 1; command argv SHA-256
  99507bccd8d44a64a7ea3ca2b3ec6a034cb8ff17fc35afda3930de22a6afae24.

- 2026-09-17T05:05:36+00:00: Recorded command exit 0; command argv SHA-256
  aff23e064183050bb8c0f6a2ad711a95cf033e5787c706b62ebdf19dbc0e6d86.

- 2026-09-17T05:05:49+00:00: Recorded command exit 1; command argv SHA-256
  4d451e478e21e29579d31a2f4329d256ae07fc4b7a814f237af2d9c638ecd947.

- 2026-09-17T05:06:23+00:00: Recorded command exit 0; command argv SHA-256
  968f2e53121cacf2bd49d2a20922f4733c556af5dfbdb33c5d4ca5fb29422760.

- 2026-09-17T05:06:38+00:00: Recorded command exit 1; command argv SHA-256
  5d755f51066dcb6b844e47368cbe39a08c994c34c44de026cb17cd8d61f12252.

- 2026-09-17T05:06:57+00:00: Recorded command exit 2; command argv SHA-256
  808b7012d0e43c7819fa6f9a7cae27be017f9aeea265252da6b28d8e25103073.

- 2026-09-17T05:07:10+00:00: Recorded command exit 0; command argv SHA-256
  f04f74ab672293135fb3bb74ae330fa6416552383070ceea1093b75cf6406492.

- 2026-09-17T05:08:13+00:00: Recorded command exit 1; command argv SHA-256
  446387fae377a2b2d9117793c36555d90f1bdb3fb13f898b032c8e13d790e74e.

- 2026-09-17T05:08:22+00:00: Heartbeat by codex-ar1293-tlc-repair-20260917.

- 2026-09-17T05:09:20+00:00: Recorded command exit 0; command argv SHA-256
  3932dd833f7a1448f881fdb8771a5c7b9057f221ea200b9b4767ae5c695df1b4.

- 2026-09-17T05:09:29+00:00: Recorded command exit 0; command argv SHA-256
  9a191e41853225b4eafcc2dd651779e0e822ca2e4be79cd7dfd6e6f95c9073a3.

- 2026-09-17T05:10:26+00:00: Audited candidate 885d14159 and implemented signed commit 53dd96389:
  owner-private per-worker queue/lock defaults and verify wiring, strict formal/tier-evidence
  validation, malformed/duplicate manifest rejection, and negative tests. Focused tests (8) plus
  mypy and ruff pass. Full state unittest ran 133 tests with 1 failure and 2 errors in pre-existing
  vendor fixtures expecting v0.3.5/digest f91226... while coordinator.vendor.json is v0.3.7; formal
  portable-smoke downloaded the pinned JAR but TLC failed before model execution with JVM EAGAIN
  (Cannot create VM thread/host resource exhaustion). No PR or publication.

- 2026-09-17T05:10:28+00:00: Blocked ownerless pending vendor baseline reconciliation and host
  capacity for TLC VM; candidate repair commit 53dd96389 remains unpublished until exact full gates
  are green.

- 2026-09-17T05:44:21+00:00: AR-1295 v0.3.7 fixtures, AR-1296 quality gates, and AR-1298 metadata
  cleanup are complete; requalify signed runner candidate 53dd96389 with owner-safe formal paths and
  host-capacity evidence.

- 2026-09-17T05:44:40+00:00: Claimed by codex-ar1293-requalify.

- 2026-09-17T05:44:58+00:00: Recorded command exit 0; command argv SHA-256
  7276c53f368be456bb4fdaecac5ea0b08215599a9551c3ac78ebd8e5f292a4ff.

- 2026-09-17T05:45:07+00:00: Recorded command exit 0; command argv SHA-256
  968f2e53121cacf2bd49d2a20922f4733c556af5dfbdb33c5d4ca5fb29422760.

- 2026-09-17T05:45:17+00:00: Recorded command exit 0; command argv SHA-256
  f04f74ab672293135fb3bb74ae330fa6416552383070ceea1093b75cf6406492.

- 2026-09-17T05:45:31+00:00: Recorded command exit 1; command argv SHA-256
  d4b00a15d4683192b85d8f30078413562c88c6853482bdc039aef391b253bfae.

- 2026-09-17T05:45:44+00:00: Recorded command exit 0; command argv SHA-256
  17107a977e7719d4230ed83f00008300ec052c89c71139388ee493c2be099baf.

- 2026-09-17T05:46:03+00:00: Recorded command exit 1; command argv SHA-256
  5d755f51066dcb6b844e47368cbe39a08c994c34c44de026cb17cd8d61f12252.

- 2026-09-17T05:46:57+00:00: Recorded command exit 1; command argv SHA-256
  446387fae377a2b2d9117793c36555d90f1bdb3fb13f898b032c8e13d790e74e.

- 2026-09-17T05:47:12+00:00: Requalification evidence: main contains signed state-quality repair
  8aa9e0c4c and candidate 53dd96389 is independently signature/DCO-valid on
  feature/ar-1293-state-tla-admission. Focused runner suite (8), Ruff, and mypy pass. Full candidate
  suite ran 133 tests with 1 failure and 2 errors: vendor fixtures still expect v0.3.5/digest f91226
  while coordinator vendor is v0.3.7. Private-path portable-smoke downloaded the pinned JAR but JVM
  failed before TLC with EAGAIN Cannot create VM thread; bounded host probe recorded 32 CPUs, 216
  processes, load 8.06/7.94/6.02. External root lock was not touched.

- 2026-09-17T05:47:14+00:00: Blocked ownerless: exact full state and formal gates are red for the
  recorded vendor fixture mismatch and host JVM thread-capacity failure. No publication or merge.

- 2026-09-17T05:48:15+00:00: AR-1295 fixture repair is on current main; prior candidate branch still
  carries stale v0.3.5 tests. Rebase candidate onto current signed main, rerun full suite, and
  classify remaining TLC EAGAIN separately.

- 2026-09-17T05:48:56+00:00: Claimed by codex-ar1293-requalify-v2.

- 2026-09-17T05:49:08+00:00: Recorded command exit 0; command argv SHA-256
  d988a6478c878f178a51a9a3b5b29a0dffa23a9cf9a3884956399ae935dde3bf.

- 2026-09-17T05:49:19+00:00: Recorded command exit 0; command argv SHA-256
  5949847f5448c62c98a0a9c850f21a8ec1099ce0ed07ae7ec666c8d9bccb2431.

- 2026-09-17T05:50:53+00:00: Recorded command exit 0; command argv SHA-256
  3d512ac8750dc3d8e9d8eeb6215a6da9fc7756556cfc331297a8ba03b193cce0.

- 2026-09-17T05:51:03+00:00: Recorded command exit 0; command argv SHA-256
  b97527766b0c4b16affcb1873a07a3a86835f5a8b13fef9e1407828d1571ac17.

- 2026-09-17T05:51:15+00:00: Recorded command exit 0; command argv SHA-256
  68bc0008bc4624ac493310e206b959e197c683ac0bd65fe5157a068340da8150.

- 2026-09-17T06:48:57+00:00: Recovered expired claim formerly owned by codex-ar1293-requalify-v2.
  UTC lease expired and prior owner process absent; recovered without impersonation

- 2026-09-17T06:49:00+00:00: Claimed by codex-ar1293-recovery-20260917.

- 2026-09-17T06:50:59+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T06:55:38+00:00: Progress checkpoint: candidate v2 rebased onto current main e00bd0782;
  full state suite passed 144 tests and focused TLC runner suite passed 10 tests. Ruff, mypy, and
  source headers pass. Candidate formal vendor files still need restoration to the immutable v0.3.7
  digests after the worker-private runner changes; then rerun vendor and formal gates. No product,
  asb-tui, or external root-owned lock touched.

- 2026-09-17T06:56:47+00:00: Progress checkpoint: restored formal/handoffctl vendor files to
  immutable v0.3.7 digests; vendor verify, Ruff, mypy, headers, and diff checks pass. Added explicit
  one-process HandoffctlPR.cfg fixture and changed CI workflow to invoke verify.sh --tier
  full-exhaustive. Candidate signed/DCO commit f16d2cb41. Portable formal execution reached TLC but
  host JVM failed with EAGAIN Cannot create VM thread; a prior unscoped portable attempt also failed
  attestation because TLC_CGROUP_MODE was absent. No external root-owned lock touched.

- 2026-09-17T06:57:21+00:00: Formal recheck: TLC portable-smoke model itself passes under required
  systemd containment, but attestation correctly rejects the required mode for portable tier; under
  TLC_CGROUP_MODE=portable the JVM fails before TLC with EAGAIN Cannot create VM thread. Candidate
  checkpoint commit 11f53a0d0 records the run. This confirms the remaining blocker is host thread
  admission, not a model failure; CI must supply the tier-specific containment environment.

- 2026-09-17T06:58:02+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T06:59:25+00:00: Infrastructure probe complete: Docker socket is inaccessible to the
  worker; unprivileged bwrap lacks a usable filesystem setup; systemd-run --user works. Running
  portable-smoke as martin fails before TLC with EAGAIN Cannot create VM thread because portable
  prlimit nproc=64 conflicts with the already high per-user thread count. Running as the dedicated
  gha-asb-state user avoids EAGAIN but fails JVM native allocation because host swap is exhausted
  (only 76 KiB free) while other workloads consume resources. No safe container/VM runner is
  available to this worker without changing unrelated host workloads or weakening portable
  attestation. Candidate remains unpublished.

- 2026-09-17T06:59:36+00:00: Released ownerless after infrastructure probe: no safe local portable
  runner; Docker unavailable, bwrap unusable, host user portable mode hits EAGAIN under nproc=64,
  dedicated CI user hits native allocation failure with swap exhausted. Preserve candidate f16d2cb41
  and resume only on a clean CI/VM runner with portable containment capacity.

- 2026-09-17T09:20:15+00:00: Clean isolated runner provisioned at
  /srv/data/projects/asb-state-tlc-vm and recorded in state commit 188130a56: pinned Ubuntu image
  SHA-256 612b2c..., QEMU 8.2.2 x86_64, 4 vCPU, 16 GiB RAM, 16 GiB guest swap, disposable qcow2
  overlay, no network device, no host mounts. Reclaim and rerun portable-smoke there; preserve
  fail-closed attestation and record guest Java/TLC toolchain evidence.

- 2026-09-17T09:21:03+00:00: Claimed by codex-ar1293-clean-vm-20260917.

- 2026-09-17T09:33:09+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:34:29+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:35:36+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:36:37+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:38:45+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:39:33+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:40:48+00:00: Recorded command exit 0; command argv SHA-256
  2b571841f680fd0f7816506372771c7e709a76ffe241dfca1dfaf77bb1fcabd9.

- 2026-09-17T09:41:37+00:00: Clean VM evidence: /srv/data/projects/asb-state-tlc-vm, Ubuntu 24.04.5
  guest kernel 6.8.0-139-generic x86_64, QEMU 8.2.2, 4 vCPU, 16 GiB RAM, 16 GiB guest swap, no
  network/no host mounts. Through handoffctl run, formal/handoffctl/verify.sh --tier portable-smoke
  completed exit 0 at 2026-09-17T09:40:42Z using pinned TLA JAR SHA-256
  936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88; TLC generated 9 states, 4
  distinct, no error. Attestation status success, commit f16d2cb41721bf8f17aa5aa75ab01520aeb91eb8,
  profile portable-smoke, tree b1707846a525b845cf9cf118ef4566df1c6cc355, model outcome
  HandoffctlBinding success, resource bounds heap 2048m/memory 3G/swap 3G/workers 2. This is
  non-exhaustive and does not prove implementation correspondence or full claims.

- 2026-09-17T09:41:51+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T09:49:44+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T09:53:13+00:00: Recorded command exit 0; command argv SHA-256
  729e464b6cbe1c0c58b0a5fae2fef36f405854fe2e11a85a4f02ef93bccc3a9b.

- 2026-09-17T09:59:20+00:00: Recorded command exit 0; command argv SHA-256
  729e464b6cbe1c0c58b0a5fae2fef36f405854fe2e11a85a4f02ef93bccc3a9b.

- 2026-09-17T10:01:47+00:00: Recorded command exit 0; command argv SHA-256
  729e464b6cbe1c0c58b0a5fae2fef36f405854fe2e11a85a4f02ef93bccc3a9b.

- 2026-09-17T10:05:34+00:00: Recorded command exit 0; command argv SHA-256
  90751d86384b4e7d2dd13be35910f8f4c2544e074fb739d36b48caa8919c2778.

- 2026-09-17T10:07:02+00:00: Recorded command exit 0; command argv SHA-256
  b0f5a8f25d7d55a12057e572a7d1d63091f58b4216eebd78fa48c963829001a9.

- 2026-09-17T10:11:26+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T10:17:07+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T10:20:24+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T10:22:42+00:00: Heartbeat by codex-ar1293-clean-vm-20260917.

- 2026-09-17T10:23:50+00:00: Worker was idle with only heartbeats after portable-smoke; coordinator
  interrupted it and released the claim for reassignment. Portable-smoke evidence is retained;
  focused/pr-publication gates remain outstanding.

- 2026-09-17T10:24:31+00:00: Claimed by ar1293_gate_recovery.

- 2026-09-17T10:25:07+00:00: Recorded command exit 0; command argv SHA-256
  72ef98f03916cc7bdc0191a01b358d681133ffc1a60fd9243117fd17fea58d2b.

- 2026-09-17T10:30:38+00:00: Recorded command exit 0; command argv SHA-256
  c76e24bd1292fcf38a839c268a0e5e08c4e38eaf8d05773cc68aae82a433d57a.

- 2026-09-17T10:30:58+00:00: Recorded command exit 0; command argv SHA-256
  b19e1411924112143230b9b8d1a1026a307c35e0284ea5e0903fc93bccff761e.

- 2026-09-17T10:31:14+00:00: Recorded command exit 0; command argv SHA-256
  9c69e97366a70fed5ead0e86891b2c1ddfc3fb16d0489543051cfc192159af0b.

- 2026-09-17T10:31:33+00:00: Recorded command exit 1; command argv SHA-256
  3fd75ef7935496110e71a125148bc739d2b76a4579b90fdcef7812d8ed6796f8.

- 2026-09-17T10:32:23+00:00: Recorded command exit 0; command argv SHA-256
  d97a032d7a609231e0d675cc94bd9275de3b963b7b721ff7df06204155d09725.

- 2026-09-17T10:32:54+00:00: Gate evidence: focused test_tlc_runner suite passed 10/10; vendor
  verify, Ruff and mypy passed. The 10:31:33Z exit-1 pr-publication attempt was a console-injection
  failure, not a TLC/formal gate result:
  /srv/data/projects/asb-state-tlc-vm-32g/private/pr-publication-pr2.serial.log ends with bash
  history-expansion error `-bash: !/bin/sh: event not found` immediately after the injected command.
  It contains no __ASB_RC marker, no attestation begin/end, and no model completion/failure, so no
  formal claim is made. Remediation is to use a history-safe noninteractive command (disable history
  expansion before injection or avoid `#!` text entirely) on the approved VM; do not classify this
  as product/model failure.

- 2026-09-17T10:33:45+00:00: Recorded command exit 0; command argv SHA-256
  780c22a2b0ed7da203ed3b8f44dea500934ec764028fab108351f75816cb3339.

- 2026-09-17T10:34:07+00:00: Recorded command exit 0; command argv SHA-256
  7d34b0ae95fe90a9d30d35d2c114f9af81d54cd828bfe3fd07f720ff0771cc93.

- 2026-09-17T10:34:51+00:00: Recorded command exit 0; command argv SHA-256
  2537ed1d58dce5c4b1614faa8d037415c9f4ecba58ba1279dbd0d080a2c462fa.

- 2026-09-17T10:35:12+00:00: Recorded command exit 0; command argv SHA-256
  6d771dc3a87be22467daa030c163d0fbb24ff082d60941b19ec748be81fc1029.

- 2026-09-17T10:35:33+00:00: Recorded command exit 0; command argv SHA-256
  b994645d1b189e9a91fdc088ba363525b8518753eea1d230459bc77f15c7af7a.

- 2026-09-17T10:36:00+00:00: Recorded command exit 0; command argv SHA-256
  70b6fc77cb9937cec4ce7c628a4e687484d3f619a7aa21d77e3557e7704afa1d.

- 2026-09-17T10:36:36+00:00: History-safe retry reached verify.sh and validated the pinned TLA jar,
  but terminal gate failed before TLC model completion: TLC emitted `java.lang.InternalError: Error
  loading java.security file` with the mounted runtime (environment defect, no attestation). Retried
  after switching to the VM guest fixed JVM; TLC started and parsed HandoffctlBinding, then failed
  `insufficient memory for the Java Runtime Environment` / `Native memory allocation (malloc) failed
  to allocate 16 bytes`, exit 1, with no attestation. Host evidence at retry: SwapFree=100 kB,
  multiple concurrent QEMU/worker workloads. This is runner capacity/JVM environment failure, not a
  model or product failure. Focused 10/10, vendor verify, Ruff, mypy remain green; full unittest was
  running separately and no product/asb-tui changes were made.

- 2026-09-17T10:37:28+00:00: Recorded command exit 0; command argv SHA-256
  943ccbd8d219e99d60ee4bfc40cca9ab173d1863e08b6522cd7744ae0c9fb186.

- 2026-09-17T10:37:51+00:00: Full state unittest suite completed 144 tests in 28.476s with OK on
  candidate worktree. Focused 10/10, vendor verification, Ruff, and mypy also passed. Formal
  pr-publication remains unqualified: mounted JVM failed java.security initialization; guest fixed
  JVM reached TLC but failed native malloc due host SwapFree=100 kB and concurrent VM load, with no
  attestation. No safe additional local formal action remains while the approved 32G runner is
  occupied; preserve evidence for AR-1302.

- 2026-09-17T10:38:01+00:00: Released ownerless blocked for AR-1302 handoff. Candidate
  f16d2cb41721bf8f17aa5aa75ab01520aeb91eb8 has complete focused and full local state evidence:
  test_tlc_runner 10/10, full unittest 144/144 in 28.476s, vendor verify, Ruff, mypy. Portable-smoke
  previously passed on the clean VM with valid attestation. PR-publication/full-exhaustive are not
  passed: history-safe retry reached verify.sh but mounted JVM had java.security initialization
  failure; fixed guest JVM then failed native memory malloc with host swap only 100 KiB free and
  concurrent VM load, no attestation. This is infrastructure-only; AR-1302 should rerun formal tiers
  on a clean 32G runner with available swap and fixed guest JVM. No product/asb-tui changes.

- 2026-09-17T12:52:41+00:00: Implement reviewed runner-contract repair required by AR-1302: separate
  bounded virtual address space from 3 GiB physical/swap bounds, add positive/negative tests and
  formal evidence updates.

- 2026-09-17T12:52:43+00:00: Claimed by codex-ar1293-as-limit-repair.

- 2026-09-17T12:54:45+00:00: Recorded command exit 1; command argv SHA-256
  a3dec3fd5d7612e7bf7011863dd1b5facb4e34dd27ac2331b5daa4aed2b4f234.

- 2026-09-17T12:54:57+00:00: Recorded command exit 1; command argv SHA-256
  ebe6668b45e19d657fa6172e32256625399f0b4b009522af50ceb701f127a387.

- 2026-09-17T12:56:39+00:00: Heartbeat by codex-ar1293-as-limit-repair.

- 2026-09-17T12:56:55+00:00: Recorded command exit 0; command argv SHA-256
  1c392fb0778612383246ebed9af16ed19327880a119d30b4e17464f003c938c1.

- 2026-09-17T12:57:21+00:00: Contract repair did not start: two worker commands exited 1, worktree
  remains clean at 53dd96389. Preserve AR-1302 evidence. Next action: inspect the exact failing
  command/environment, then implement and test a separate bounded virtual-address-space limit
  without changing the 3 GiB physical/swap attestation.

- 2026-09-17T12:57:33+00:00: Retry with a different worker: inspect prior command failures and
  implement separate bounded virtual-address-space contract with tests/evidence; preserve
  physical/swap attestation.

- 2026-09-17T12:57:36+00:00: Claimed by codex-ar1293-as-limit-repair-v2.

- 2026-09-17T12:59:25+00:00: Heartbeat by codex-ar1293-as-limit-repair-v2.

- 2026-09-17T12:59:28+00:00: Recorded command exit 0; command argv SHA-256
  61f62ba3d4d589316cbddbcc4d3facbe29809984a08193dc0be95b0c7557d66c.

- 2026-09-17T12:59:43+00:00: Recorded command exit 0; command argv SHA-256
  2cbd3d87c22bfcac9296b5a12ffee8b142fea56a499af18bcce73c3bf46b98cb.

- 2026-09-17T13:00:06+00:00: Recorded command exit 0; command argv SHA-256
  5fee026f8e9a7f506fee8acb40e6d7ba17ca1871cd06c4470eab260e3070f672.

- 2026-09-17T13:00:18+00:00: Recorded command exit 0; command argv SHA-256
  57aa684661b9badaf5caf256706c0ff03f2aa97681862aa8ba378effbed4e08c.

- 2026-09-17T13:00:29+00:00: Recorded command exit 0; command argv SHA-256
  b39a86595fdff2d53bb611c0b0ba124d1b7628a3cd61c31f0af8283fc7e6cce7.

- 2026-09-17T13:00:40+00:00: Recorded command exit 0; command argv SHA-256
  338fc6f3230dcd08505b7b3f8a9403b0b4155b28c6f79566bf87e8dac570731e.

- 2026-09-17T13:01:27+00:00: Recorded command exit 0; command argv SHA-256
  8748d80ab4e2e26f12007733f30176c678ac2c05f8f7ceec77cc4c47b40de8a1.

- 2026-09-17T13:02:16+00:00: Recorded command exit 0; command argv SHA-256
  8748d80ab4e2e26f12007733f30176c678ac2c05f8f7ceec77cc4c47b40de8a1.

- 2026-09-17T13:02:36+00:00: Recorded command exit 0; command argv SHA-256
  8a06f8edff110a8a88de70737d3e39299d6b3c39574ed65ad87dd418656202d7.

- 2026-09-17T13:02:46+00:00: Recorded command exit 0; command argv SHA-256
  54af23619beca5b79aa3a59d5b32c8a355104f2ee91b5257665a5878aee1f45e.

- 2026-09-17T13:03:12+00:00: Recorded command exit 0; command argv SHA-256
  526d21ac44c29df8de6737fdc3a7f74a6b33def98aab3a9addc43f1056db1595.

- 2026-09-17T13:03:22+00:00: Recorded command exit 0; command argv SHA-256
  3a39c72b623858328b00216d86cb92fd116c69b8472c909882e60f73043f6e39.

- 2026-09-17T13:03:36+00:00: Second contract worker performed only repository/tooling probes; no
  working-tree diff or repair commit was produced. Preserve AR-1302 evidence. Next action remains
  implementing a separate bounded virtual-address-space limit in tools/tlc_runner.py with
  attestation/schema and positive/negative tests, then requalifying portable-smoke.

- 2026-09-17T13:03:59+00:00: Coordinator implementation authorized after two workers produced no
  diff: add explicit bounded portable virtual-address-space contract, positive/negative tests, and
  attestation evidence without weakening 3G physical/swap.

- 2026-09-17T13:04:02+00:00: Claimed by coordinator-ar1293-as-limit-repair.

- 2026-09-17T13:05:55+00:00: Recorded command exit 5; command argv SHA-256
  dab4e6e1d517264d7285304b8328aaaf2c842f2f33d119d7b4f59450b9f96167.

- 2026-09-17T13:06:13+00:00: Recorded command exit 0; command argv SHA-256
  855d6dd716c1a10e3b61098b27c6cd0cae45d0279287d588277fbb2f50fd09c8.

- 2026-09-17T13:06:28+00:00: Recorded command exit 0; command argv SHA-256
  b44de7d1b0474b618e20ca946cdd3458dbf31836e854f805a5a2717f68fae943.

- 2026-09-17T13:06:38+00:00: Recorded command exit 0; command argv SHA-256
  2e7e236d01b48372788e5f3918b0007b14fd2b95d90dde587a444c777c3a6e43.

- 2026-09-17T13:06:58+00:00: Recorded command exit 1; command argv SHA-256
  968f2e53121cacf2bd49d2a20922f4733c556af5dfbdb33c5d4ca5fb29422760.

- 2026-09-17T13:07:18+00:00: Recorded command exit 0; command argv SHA-256
  968f2e53121cacf2bd49d2a20922f4733c556af5dfbdb33c5d4ca5fb29422760.

- 2026-09-17T13:07:28+00:00: Recorded command exit 0; command argv SHA-256
  855d6dd716c1a10e3b61098b27c6cd0cae45d0279287d588277fbb2f50fd09c8.

- 2026-09-17T13:07:45+00:00: Recorded command exit 0; command argv SHA-256
  0b73d5d0d470de63e67e268d167511d55b76314effef12be2ccb78299bd374df.

- 2026-09-17T13:07:55+00:00: Recorded command exit 0; command argv SHA-256
  adb41f0d68fffc53dfa61841c21bf0f67d69df15cfa8546a47d7cb6438fc515a.

- 2026-09-17T13:08:15+00:00: Recorded command exit 1; command argv SHA-256
  1c199fe7b569da817ff7e90ab3e87bf5a5ac226cbccc2a36e3f1d70000052b72.

- 2026-09-17T13:08:36+00:00: Implemented signed+DCO commit 1c7f8f4: portable runner now uses
  separate bounded 8G RLIMIT_AS while retaining attested 3G physical/swap bounds; tier evidence and
  attestation schema record the bound; positive/negative tests added. Focused tests 9/9 and Ruff
  pass. Ready for independent review and fresh VM qualification.

- 2026-09-17T13:08:39+00:00: Recorded command exit 0; command argv SHA-256
  216282fcc01dc202d4397e193365784265c003a9ce8c9a69ec926da04cba90e3.

- 2026-09-17T13:09:26+00:00: Recorded command exit 1; command argv SHA-256
  ffac5f6d122a535b0fada7431be634d4aa9c201990b1e56a2064d7a51d1e28fb.

- 2026-09-17T13:10:03+00:00: Recorded command exit 1; command argv SHA-256
  a05f0e706732822def9eb99a7b68d8abf429e86264082a2e2e59c04e116837fa.

- 2026-09-17T13:10:24+00:00: Recorded command exit 1; command argv SHA-256
  780561af55f9a7b6fd624845efa95563ad0962a47d76ace7063fd4b6c59751fd.

- 2026-09-17T13:10:34+00:00: Recorded command exit 0; command argv SHA-256
  8fcc0db99c74e1b02720a1f6cfd730cdb42298276909b814d8e2e0fd1f02aeb9.

- 2026-09-17T13:11:15+00:00: Recorded command exit 0; command argv SHA-256
  4e1e0e32c53ac5f397e4617462f7a2e9c04d68f712dc63abe1e6bccb8c2488ea.

- 2026-09-17T13:11:26+00:00: Recorded command exit 0; command argv SHA-256
  e637f87a4b74e38ca3e6aea68d8870f11a73ced5e8dfa3ddd49cb18b1707156f.

- 2026-09-17T13:11:48+00:00: Recorded command exit 1; command argv SHA-256
  780561af55f9a7b6fd624845efa95563ad0962a47d76ace7063fd4b6c59751fd.

- 2026-09-17T13:12:40+00:00: Recorded command exit 0; command argv SHA-256
  8d85552bad4579be0b2f21409c7c66f91fd559022a7aebd3f438e760cd7b3b0c.

- 2026-09-17T13:12:51+00:00: Recorded command exit 0; command argv SHA-256
  8f684aad7bf0681452558f8b0761e8a67d78fd7afa620a816c29bb2c65af7e0f.

- 2026-09-17T13:13:01+00:00: Recorded command exit 0; command argv SHA-256
  6a329ba970f1baeafab1dbeb9306f8ec81253c81c614abf29c6c60959d8e735e.

- 2026-09-17T13:13:32+00:00: Independent review complete for signed heads 1c7f8f4 and f1931686c.
  Diff is limited to tools/tlc_runner.py and its focused tests; vendored coordinator files and tier
  schema restored unchanged. Focused tests 9/9, Ruff format/check, and mypy pass. Full state suite
  ran 134 tests with the known baseline vendor fixture mismatch (1 failure, 2 errors); vendor verify
  reports the pre-existing locked README digest mismatch. No VM rerun yet.

- 2026-09-17T13:13:35+00:00: Recorded command exit 0; command argv SHA-256
  0b9e4ac02598b939ffd52958ea8f41dbb99de90137430d0ec26332188bfc9dc8.

- 2026-09-17T14:11:29+00:00: AR-1302 runner is now done with exact f1931686c portable-smoke success
  attestation 0993b7c3... and fresh data image 488655f4.... Release the idle pre-runner claim; next
  worker must use the qualified runner and requalify AR-1293 exact 8G address-space/3G memory+swap
  contract before required/full.

- 2026-09-17T14:11:52+00:00: Claimed by codex-ar1293-requalify-fresh.

- 2026-09-17T14:13:20+00:00: Checkpoint: fresh runner evidence is
  /srv/data/projects/asb-state-tlc-vm-32g; exact prior portable invocation was
  formal/handoffctl/verify.sh --tier portable-smoke with attestation 0993b7c3... and data image
  488655f4.... Candidate repair is signed 39c8933f5; no required/full gate is authorized for it
  until portable evidence matches this candidate.

- 2026-09-17T14:13:32+00:00: Recorded command exit 1; command argv SHA-256
  93fa831e262a4bbc89ef1374fd632e82a946fd2f31121ca0ea6d9743678b1d85.

- 2026-09-17T14:13:59+00:00: Blocked fail-closed: receipt verification found current
  /srv/data/projects/asb-state-tlc-vm-32g/ar1302-integrated-data.raw SHA256
  5b2bb2599d04d33a4cd3cfa84e6dbd8c832cf063adcf38ecb73b0116397bbd41, not the authorized
  488655f4c9caf3aa7e56aab29bd19d09760f4cba15428f7215b519cf570a70c. The prior 0993b7c3... portable
  attestation is tied to exact f1931686c and the old image, not candidate 39c8933f5. No
  required/pr/full gate was run. Next action: provision a fresh immutable data image containing
  39c8933f5, verify its digest and exact 8G/3G attestation, then run portable-smoke before
  required/full.

- 2026-09-17T14:15:35+00:00: Resume authorized to provision a fresh candidate-specific data image
  from exact signed 39c8933f5; preserve fail-closed portable-before-required/full ordering.

- 2026-09-17T14:15:38+00:00: Claimed by codex-ar1293-requalify-fresh2.

- 2026-09-17T14:15:50+00:00: Recorded command exit 0; command argv SHA-256
  3e2cf4056e2f738229728bd3021226d2624aa8e338c2c2e9be01ddb8e5cd8d1e.

- 2026-09-17T14:16:12+00:00: Recorded command exit 0; command argv SHA-256
  4b2311506b6c7f7d64d643d7da499cc2a3750c89abdbdf46cfd9c8e93db9f076.

- 2026-09-17T14:16:34+00:00: Recorded command exit 0; command argv SHA-256
  94dd7e089371e3fc7f5c3fc772c9de74ce8980a0381d7058c90f4322b1601112.

- 2026-09-17T14:16:57+00:00: Recorded command exit 0; command argv SHA-256
  9b66a4779dd162a72d70ad4e8bbf0e756b38484831e8b84f9ff5c93bb429a00a.

- 2026-09-17T14:17:46+00:00: Recorded command exit 0; command argv SHA-256
  3a0762b74d22cc8a16d2e9dedcc9d3fd6e0fb67ebb3cb80de4ede16fef3b8eed.

- 2026-09-17T14:18:59+00:00: Recorded command exit 0; command argv SHA-256
  baf15d17911fba5a9927a857d82b73896ea9a69b1564323e8b4b1ff08bb45bce.

- 2026-09-17T14:19:42+00:00: Recorded command exit 1; command argv SHA-256
  fbda87d8507b11f78a32600eca51d366944feb9ac8ff083c02d45580f29f4d6d.

- 2026-09-17T14:20:00+00:00: Recorded command exit 0; command argv SHA-256
  faf8a90328b2f182586cd608903a96cf837fd69f30522c9d6aaf2cc981b47156.

- 2026-09-17T14:21:28+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:22:00+00:00: Recorded command exit 0; command argv SHA-256
  75b2526448c31019c1604bf76fa08b14849b35715cb041d52a390fc07170fdc3.

- 2026-09-17T14:22:19+00:00: Recorded command exit 0; command argv SHA-256
  73b82bf07d8dd72ac7ff8181472993433c4b0081ac614719abd04406b4a3b2d0.

- 2026-09-17T14:22:40+00:00: Recorded command exit 0; command argv SHA-256
  c40f4860393bd52408c965f9492c3dfbab233183461e430a04e89124604bf224.

- 2026-09-17T14:23:33+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:24:05+00:00: Recorded command exit 0; command argv SHA-256
  75b2526448c31019c1604bf76fa08b14849b35715cb041d52a390fc07170fdc3.

- 2026-09-17T14:24:24+00:00: Recorded command exit 0; command argv SHA-256
  adf5eae46fe3af5ea5e0a214cee276ba26f26bca4f4ca8e24bb4bff55baaffc3.

- 2026-09-17T14:24:49+00:00: Portable requalification terminal green: fresh data image
  /srv/data/projects/asb-state-tlc-vm-32g/ar1293-39c8933f5-data.raw SHA256
  15c826232de7726b421a0ac0df883f2a2d95be89472fc2873d866750698f89; guest git HEAD
  39c8933f555af7add5e39b3d2b88d1726152f471; PORTABLE_SMOKE_RC=0; attestation SHA256
  6fffdbbfa6daf877c69ed4fe869415841d187488405fed969f2bef5104890472; status success,
  portable-timeout-prlimit, address_space_max 8G, memory_max 3G, swap_max 3G, heap 2048m, workers 2.
  Prior RC=1 was seed/env and JDK symlink infrastructure, repaired fail-closed.

- 2026-09-17T14:25:45+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:26:18+00:00: Recorded command exit 0; command argv SHA-256
  0cb07dbf66d93193e58ee414a9d6dd3458dc62d3f099b4f6425b8809d6f9d955.

- 2026-09-17T14:27:24+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:28:00+00:00: Recorded command exit 0; command argv SHA-256
  4f839ba0dabd018b1e2980b28a3ca2480478ded3738494047437315794775ee2.

- 2026-09-17T14:29:11+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:29:44+00:00: Recorded command exit 0; command argv SHA-256
  a28c8bb22e897ded67e87b8cecd2ceb266c6ee27419fb462b70635c85088aef0.

- 2026-09-17T14:30:49+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:31:22+00:00: Recorded command exit 0; command argv SHA-256
  f852b648f06ee1f22cbbef8e9b291d286fcde74aa00c87c0359229f4ee46be5d.

- 2026-09-17T14:31:49+00:00: Recorded command exit 32; command argv SHA-256
  bd6f7d7498aaca401963eeaba0f76d998001d7075c5b7c56c29ea260568d1ffb.

- 2026-09-17T14:32:08+00:00: Recorded command exit 1; command argv SHA-256
  90ec2f6cfe95be9b70a24e2f1cfab2d0606c27835b03ea435ea89df516aedd0a.

- 2026-09-17T14:33:09+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:33:43+00:00: Recorded command exit 0; command argv SHA-256
  2e2b4c84b134fea9ab1f667587a6b4be1007973d96d3902708918565caf0aca7.

- 2026-09-17T14:34:53+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:35:44+00:00: Recorded command exit 0; command argv SHA-256
  2ecc8d15bfff237db204d26dcb1549ffeffffb4dc9a661cb88d4d87ab296a2d4.

- 2026-09-17T14:36:09+00:00: Recorded command exit 0; command argv SHA-256
  8936a48d4309ee2381fd2a2d94299819ce77f36de2c4c397aee560d547ee980f.

- 2026-09-17T14:37:19+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:37:51+00:00: Recorded command exit 0; command argv SHA-256
  9b6b71cfd0136d4830be105edcadb69e685256e4d45b148d35396b5ea166adb7.

- 2026-09-17T14:38:20+00:00: Recorded command exit 0; command argv SHA-256
  2ba86d4821f977b9d197ce52fedbf8b7aa781fbd8e5fa03d0c2420a9a57b35b4.

- 2026-09-17T14:39:14+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:39:48+00:00: Recorded command exit 0; command argv SHA-256
  1cfaca4e1c9315295ecc40c6f97a130760404d2f6e241b59dc6cb2a0f13008d1.

- 2026-09-17T14:40:25+00:00: Heartbeat by codex-ar1293-requalify-fresh2.

- 2026-09-17T14:40:29+00:00: Recorded command exit 0; command argv SHA-256
  d20c4ca9261dfe2c5263e4bf80733f7639919455146dd61b5c9e40fb3e7295c8.

- 2026-09-17T14:41:21+00:00: Recorded command exit 0; command argv SHA-256
  072a574d65ec12d5656a81f67a03f56c43b9a424df127a070a84e3b6a9ca7463.

- 2026-09-17T14:41:56+00:00: Recorded command exit 0; command argv SHA-256
  c08c66e7c13a9096086af1be3b2cb3cfd8ba22627c6d10db7de7f4940c7e9922.

- 2026-09-17T14:42:27+00:00: Required/pr-publication gate is blocked after portable success. Exact
  candidate guest reached all six TLC models with no model errors, then attest.py rejected portable
  mode as expected; required attempts failed with Failed to connect to bus: No medium found. Guest
  diagnostics showed user-runtime-dir@1000 active, user@1000 active, busctl --user status healthy,
  but systemd-run transient invocation did not produce a result and wrapper interception was not
  selected by the runner (no wrapper log). No pr-publication attestation exists; full-exhaustive was
  not run.

- 2026-09-17T14:42:30+00:00: Blocked after portable-smoke success for exact 39c8933f5.
  Required/pr-publication cannot attest because guest systemd-run --user fails No medium despite
  healthy user bus; wrapper attempt was not used by runner, so no containment weakening is accepted.
  Preserve candidate and image evidence; next action is repair the runner-level systemd launcher or
  use a clean approved guest where required transient containment succeeds, then rerun
  pr-publication before full-exhaustive.

- 2026-09-17T16:49:06+00:00: Dependency AR-1304 is now done and independently reviewed at exact head
  56001d6e2. Accepted required PR8 evidence: candidate 39c8933f5, receipt
  ca9c4d9368f8c137d65354fd22c54c118d33d7e1a9af5ef4e5af99b3466c1c11, direct systemd-run, exact
  markers, six successful models. Resume to rerun required/pr-publication and then full-exhaustive
  only after required gate passes.

- 2026-09-17T16:49:09+00:00: Claimed by codex-ar1293-recovery-20260917.

- 2026-09-17T16:49:46+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:49:49+00:00: Recorded command exit 0; command argv SHA-256
  b604085a5064e31f29fa5a40107687ccb38e559fd7cdeebcdc891c78ac051e40.

- 2026-09-17T16:51:10+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:51:13+00:00: Recorded command exit 1; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T16:51:43+00:00: Recorded command exit 1; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T16:52:51+00:00: Recorded command exit 0; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T16:53:02+00:00: Recorded command exit 0; command argv SHA-256
  29abee1d367a7d53ffb092b5d9cb5485ad399df0bfb62890b58a506ab959e67e.

- 2026-09-17T16:53:18+00:00: Recorded command exit 0; command argv SHA-256
  10c16b95251b90bac1da701d208da802618e2e07128663571b01befef36b7c21.

- 2026-09-17T16:54:00+00:00: Full-exhaustive attempt reached TLC and several models completed, but
  failed at Handoffctl model state persistence with OSError Errno 28 No space left on device on the
  512M data image; FULL_EXHAUSTIVE_RC=1 and no full attestation. Required PR8 evidence remains
  independently validated green. Next action is an explicit larger fresh data image, not an
  unchanged rerun.

- 2026-09-17T16:54:11+00:00: Recorded command exit 1; command argv SHA-256
  033208de9a2ce72a037fb7f3a2cf8e3433426c0bdfd7e01ca563d0e3e540fe97.

- 2026-09-17T16:54:36+00:00: Recorded command exit 0; command argv SHA-256
  349224fe9991c5b6f13f01a494d8e0887c38c4588ee84a4f3aef8dbce31f3eca.

- 2026-09-17T16:54:54+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:56:14+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:56:53+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:58:14+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T16:59:27+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:01:15+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:03:34+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:05:24+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:06:17+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:13:00+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:16:07+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:18:09+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:20:09+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:22:36+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:24:35+00:00: Heartbeat by codex-ar1293-recovery-20260917.

- 2026-09-17T17:25:12+00:00: Recorded command exit 0; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T17:26:57+00:00: Second full-exhaustive run used the fresh 4GiB image and reached the
  large Handoffctl model, but terminated at approximately 1812s with FULL_EXHAUSTIVE_RC=1 because
  the seed hardcoded RuntimeMaxSec=1800; no full attestation was produced. Serial evidence shows TLC
  itself progressing, not a model error. This is a timeout-profile defect; do not claim full
  success.

- 2026-09-17T17:27:48+00:00: Recorded command exit 0; command argv SHA-256
  1c392fb0778612383246ebed9af16ed19327880a119d30b4e17464f003c938c1.

- 2026-09-17T17:29:05+00:00: Recorded command exit 0; command argv SHA-256
  6928eb60ff8a2c7c9538b6b0df66e06680232360bf49330ee1a23c016bb7f469.

- 2026-09-17T17:29:21+00:00: Recorded command exit 0; command argv SHA-256
  c091fc8436a2aab95ae5218a338a64e767d3ab3d8d9b991f7c336cadb2bb1b79.

- 2026-09-17T17:29:31+00:00: Recovered idle worker after timeout-profile diagnosis; private scripts
  were untracked and no signed implementation had been produced. Preserve required/pr evidence and
  timeout failure record. Reclaim for active implementation with explicit full-profile timeout,
  tests, receipt binding, signed commit, review, and fresh run.

- 2026-09-17T17:29:37+00:00: Claimed by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:30:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:30:33+00:00: Recorded command exit 1; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T17:31:01+00:00: Fresh full-run invocation first failed before QEMU: private helper
  imported qemu_runner while AR-1304 tools package shadowed AR-1302 qemu_seed, causing
  ModuleNotFoundError tools.qemu_seed. This is a helper import-path defect only; no image/VM
  mutation occurred. Corrected by placing the AR-1302 package path first and using its qemu_runner
  module.

- 2026-09-17T17:31:48+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:33:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:37:34+00:00: Recorded command exit 0; command argv SHA-256
  bfed98255c8f3ca4af77d55b79d2b072f237a0a555c1140c7d16bf5c45388cc9.

- 2026-09-17T17:39:16+00:00: Recorded command exit 1; command argv SHA-256
  3b2e23c40f9994a8d4767a3d81231659d2cc297169a084bce8e52a21eca0178a.

- 2026-09-17T17:39:35+00:00: Recorded command exit 0; command argv SHA-256
  3b2e23c40f9994a8d4767a3d81231659d2cc297169a084bce8e52a21eca0178a.

- 2026-09-17T17:39:56+00:00: Execution wiring is now tracked in candidate worktree: verify.sh
  derives TIMEOUT_SECONDS via tier_profiles.timeout_for_tier and passes --timeout-seconds to every
  tlc_runner invocation; tier_profiles/seed_profile define required=1800 and full=7200 with bounded
  memory/address limits; workflow timeout is 720 minutes; 17 focused tests, Ruff, and diff checks
  pass. The 17:39:16 exit-1 was a test-loader import error: seed_profile.py could not import
  tier_profiles when loaded standalone; fixed by explicit test module registration. No VM was
  launched for that failed command.

- 2026-09-17T17:40:08+00:00: Recorded command exit 0; command argv SHA-256
  3e43456453757f7d1ae5cfa616f5d812fdde527ad90c811907829cf345bf4e30.

- 2026-09-17T17:40:32+00:00: Tracked execution wiring committed as bcf65ad29 (SSH-signed+DCO):
  verify.sh resolves tier timeout through tier_profiles and passes --timeout-seconds into every
  tlc_runner invocation; seed_profile exposes required=1800/full=7200 plus 3G/3G/8G bounds; workflow
  timeout is finite 720 minutes; execution-level tests now cover verify wiring and guest environment
  profiles. Commit signature verified. No full VM retry started after this commit; waiting for
  independent review.

- 2026-09-17T17:42:08+00:00: Recorded command exit 1; command argv SHA-256
  ec8f58fab78d1ecd08fe31d90df2b85c86c23ed49d9619ae5631799ace43cb80.

- 2026-09-17T17:42:23+00:00: Recorded command exit 1; command argv SHA-256
  a61993e1431461553f9a3543d33d51d8c29cd5efeed8593167f50eb67f72a42a.

- 2026-09-17T17:42:38+00:00: Recorded command exit 0; command argv SHA-256
  52fe3dc51f9e4255ef744213e59102666c704dff8d915a5dc91db3d7fca9d3ac.

- 2026-09-17T17:43:04+00:00: Recorded command exit 0; command argv SHA-256
  a99c521adcc56ac96fac1cb225af6d4e6cfbc6441f88103b9bfc8884288cde8a.

- 2026-09-17T17:43:29+00:00: Recorded command exit 0; command argv SHA-256
  6cfa19deced2f5b052738cc8336633037dfe705422e3838c9698740d1b92b753.

- 2026-09-17T17:44:08+00:00: Recorded command exit 1; command argv SHA-256
  79c7853595adf8b96201f5a8b348da08c21fb17a4d7b76947ad98a2b111a2957.

- 2026-09-17T17:44:29+00:00: Recorded command exit 0; command argv SHA-256
  60d2d80b0cba297a69f2adba73c8e11d0e64d60630b75518e205205bc96dd8ef.

- 2026-09-17T17:44:55+00:00: Guest integration is now tracked, not private-only: AR-1304 seed commit
  2b7ed3732 imports tools/seed_profile.py, build_user_data(tier) exports TLC_TIMEOUT_SECONDS and
  sets matching RuntimeMaxSec, with generated-seed positive/negative tests (4/4 green); v2 commit
  8be1d2f83 adds guest_seed.py rendering the same execution contract and tests (18/18 green). README
  bound correction is signed in 0190d6678. Earlier 17:42 failures were test invocation/import
  errors: unittest module path was invalid, then PYTHONPATH omitted so tools package was
  unavailable; corrected with PYTHONPATH=. discover. No VM rerun.

- 2026-09-17T17:48:10+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:48:22+00:00: Checkpoint: replacing minimal guest seed with complete state-owned
  contract: pinned data UUID mount, offline curl shim, user bus/systemd transient preflight, tier
  timeout/profile env, bounded verify, attestation validation, cleanup and poweroff. Next add
  contract tests and wire the durable launcher to build_user_data(tier) directly; no VM rerun before
  independent review.

- 2026-09-17T17:48:51+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:48:54+00:00: Recorded command exit 1; command argv SHA-256
  19707c45cf8a518ab649bb28e053b9efecac12ea3b5c0d28a4e3ab4d3ba125c2.

- 2026-09-17T17:49:06+00:00: Recorded command exit 5; command argv SHA-256
  92499f6f4294dd7658e8821c34165281687f26be2182921ebb24743c5b46a438.

- 2026-09-17T17:49:16+00:00: Recorded command exit 0; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T17:49:32+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:49:41+00:00: Focused contract work complete in candidate (uncommitted): guest seed
  now covers pinned UUID mount, offline curl shim, user-runtime/user bus startup and socket
  assertion, bounded transient properties, tier timeout/profile env, GIT/TMPDIR/attestation paths,
  evidence validation, cleanup and poweroff. Added positive/negative tests; direct candidate
  invocation via handoffctl: 20/20 passed. Earlier exit-1/5 records were invalid module/path
  invocations (tests.test_tlc_runner from state cwd and unittest discover from wrong cwd), not
  product failures; corrected absolute candidate script command passed. Next run source/quality
  gates, commit signed+DCO, request independent review.

- 2026-09-17T17:49:50+00:00: Recorded command exit 0; command argv SHA-256
  a6b25844d54f6cb4811a906c872b80312bd069c61a2c19e5a17651b13e2a95b0.

- 2026-09-17T17:50:01+00:00: Recorded command exit 0; command argv SHA-256
  2a9caceccf5c0700cc6b9628f28d4336b8d00eb0cb3d23b21a798e103f3de6b1.

- 2026-09-17T17:50:16+00:00: Recorded command exit 1; command argv SHA-256
  f17f6049b6101d7f363cd727cfacf925bd91b677facbfeddf1e1ab94cbaacd9e.

- 2026-09-17T17:50:27+00:00: Recorded command exit 0; command argv SHA-256
  cf7282b4747951ef3d06bb086a04767973f1e27707611c760b6c7f718cec013a.

- 2026-09-17T17:50:39+00:00: Quality gates: source headers passed; Ruff passed; first mypy
  invocation failed only because the command omitted MYPYPATH for the repository's local
  tier_profiles import (missing import tier_profiles), then corrected MYPYPATH=.../formal/handoffctl
  and mypy passed with no issues. This is an invocation/environment correction, not a product
  defect. Focused guest-seed tests remain 20/20.

- 2026-09-17T17:50:52+00:00: Recorded command exit 0; command argv SHA-256
  0d63815b6adb0e464af4d7b665ed77abc33abbc95e62748adb389e93ed45e91a.

- 2026-09-17T17:51:06+00:00: Recorded command exit 0; command argv SHA-256
  4a6a4005422e21500c43cfe11895291db512131e63e07305cea964b4badad2a9.

- 2026-09-17T17:51:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:51:40+00:00: Implementation committed in candidate as signed+DCO
  f434b4a49b78a5f1e2681b13a82c4d0df25f95e0 (Good SSH signature
  SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE; matching Signed-off-by). Complete guest seed
  now includes UUID/data mount, offline curl, user runtime/user bus, bounded systemd transient, tier
  timeout/profile, GIT/TMPDIR/attestation, validator, cleanup and poweroff. Tests 20/20 passed;
  headers/Ruff passed; mypy first exited 1 due missing local tier_profiles import path, corrected
  with MYPYPATH and passed. Candidate clean. AR-1304 durable launcher required_seed.py already
  directly calls build_user_data(tier) via commit 2b7ed3732 and runner receipt binds helper/image
  hashes; no private helper or VM run started after this fix. Latest 17:50:16 exit-1 was the initial
  mypy invocation environment error, now resolved.

- 2026-09-17T17:52:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:54:41+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:55:14+00:00: Recorded command exit 1; command argv SHA-256
  c3d776c7758fde6f98efd3e779858216d6ef6d3b85c8a1e75b1df156123b45ce.

- 2026-09-17T17:55:23+00:00: Recorded command exit 1; command argv SHA-256
  b6eede5bde770de2f5ca4419ccde5e37082bb493d8331f06f507890143a63880.

- 2026-09-17T17:55:38+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:55:41+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:55:44+00:00: Recorded command exit 0; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T17:55:53+00:00: Recorded command exit 0; command argv SHA-256
  b6eede5bde770de2f5ca4419ccde5e37082bb493d8331f06f507890143a63880.

- 2026-09-17T17:56:03+00:00: Recorded command exit 0; command argv SHA-256
  fdf8452a56bb85b9d71f7b66aed9c6571bfca973a845984c8388c13293d56692.

- 2026-09-17T17:56:19+00:00: Recorded command exit 0; command argv SHA-256
  d40b4f126020165175bcd9c0f6905c9721f766df270275022513cc57a807c415.

- 2026-09-17T17:56:29+00:00: Recorded command exit 0; command argv SHA-256
  6fa4b9229459c727ea018fdaa3a53e689420aca287dc04e8fd5eb772ad99864d.

- 2026-09-17T17:56:39+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:56:41+00:00: Recorded command exit 0; command argv SHA-256
  21f070bca934edc2d896e1238fb0406bd924222e9ac8603d8988116f3db41d32.

- 2026-09-17T17:56:51+00:00: Recorded command exit 0; command argv SHA-256
  af0911b8fa4947505dffe1e72346c0541538e6dddc77acd4de69d3ad954bc2a6.

- 2026-09-17T17:57:31+00:00: Recorded command exit 0; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T17:57:41+00:00: Recorded command exit 0; command argv SHA-256
  5f794007cb863acb8dfa046d868ce5d5fcb788bce3592e30169942f0ab5058ed.

- 2026-09-17T17:57:51+00:00: Recorded command exit 0; command argv SHA-256
  5649b7cfdb9884507cdb5d074fc3da7e5d79ccfce3f8eb0495c715e25bc0e7f5.

- 2026-09-17T17:58:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:58:30+00:00: Recorded command exit 0; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T17:58:45+00:00: Recorded command exit 0; command argv SHA-256
  62d63b577407da3e292eef32fcb031c230bc7a8af67d178ccfc53ed019bc654a.

- 2026-09-17T17:58:54+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T17:58:56+00:00: Recorded command exit 0; command argv SHA-256
  e6fd8b2713b69eebdee1435223f71e91d60090a9e7919a35490bd7dbb582e4bd.

- 2026-09-17T17:59:14+00:00: Implementation now complete and clean in candidate: signed commits
  f434b4a49 (complete guest seed), b8f1caff1 (normal tier-profile import fallback), 2c7fab4d4
  (tracked offline QEMU argv launcher), 36440a1e1 (digest-only tiered receipt). Candidate launcher
  writes the complete tier seed, emits networkless QEMU argv (32768 MiB guest, 4 vCPU, no NIC/host
  mounts), and writes receipt binding candidate/seed source commit, root/data/seed hashes, QEMU
  version, 3G memory+swap, 8G AS, 200% CPU, TasksMax 64, workers 2, and tier timeout 1800/7200.
  Focused candidate suite passes 23/23; normal import rendering passes. AR-1304 companion commit
  923378246 also records tiered receipt binding. Earlier AR-1304 test exit-1 was an assertion typo (
  missing ), corrected and both suites pass (5/5 and 4/4). No VM run started pending independent
  review.

- 2026-09-17T17:59:25+00:00: Correction: prior state update shell interpolation emitted a harmless
  shell error because the note contained backticks around runtime-max,string; the durable update
  still committed. The corrected AR-1304 assertion was the missing name=opt/formal prefix, and
  AR-1304 tests then passed 5/5 and 4/4. Candidate remains clean at signed 36440a1e1; 23/23 focused
  tests pass. No VM started pending independent review.

- 2026-09-17T17:59:33+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:02:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:03:30+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:04:09+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:04:11+00:00: Recorded command exit 0; command argv SHA-256
  6e98ee7887a8ce0cf4e9b833044b44a404631ae2e368266f290c168a465efb59.

- 2026-09-17T18:04:21+00:00: Recorded command exit 2; command argv SHA-256
  77efa95b51f8d6adece97ddb2c520d6fbc626e0236a2e3525391e5beb5cef0ac.

- 2026-09-17T18:04:37+00:00: Recorded command exit 1; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T18:04:58+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:05:07+00:00: Recorded command exit 0; command argv SHA-256
  810f29485e39ca46cfd61b7069906075ec1058aacb2efcbb32502b447a0a26f3.

- 2026-09-17T18:05:18+00:00: Recorded command exit 0; command argv SHA-256
  205636dc8079b569772f4969ffd0ef7be96c444f633039763069383251e3dfa1.

- 2026-09-17T18:05:29+00:00: Recorded command exit 0; command argv SHA-256
  8d57b35d8c1cdbc585e1fed1df411cf9b772ee6a5a15addcc2188bf18d257cff.

- 2026-09-17T18:05:39+00:00: Recorded command exit 0; command argv SHA-256
  50bb0d7da5637eb7a143e433f142749a0a1d9bfed261038a195ac93a3af293c7.

- 2026-09-17T18:05:59+00:00: Review fixes committed as signed+DCO
  2bbf0b285b026578bf4139cfabfd77baaf48cece. Shared VM_VCPU_COUNT=8 and tier timeout_for_tier are
  used; normal package imports work. qemu_runner now executes argv-only QEMU with bounded timeout,
  captures serial, and writes result receipt. Command binds no NIC, 32GiB/8-vCPU VM, data UUID
  serial/fw_cfg, tier runtime. Receipt binds candidate==seed source, command/serial/image/JAR/JDK
  digests, architecture, UUID, VM containment and result. Ruff check+format pass, mypy with
  follow-imports=skip passes, focused suite 23/23 passes. Latest test exit-1 was stale test call
  missing new receipt command/serial/result parameters; corrected and rerun green. Candidate
  worktree clean.

- 2026-09-17T18:07:30+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:08:21+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:09:48+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:09:59+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:10:02+00:00: Recorded command exit 0; command argv SHA-256
  9e837e0354285f6a2b6a22a1d73daa58fa23b4617b8868c9e1208b65114a43a9.

- 2026-09-17T18:10:12+00:00: Recorded command exit 0; command argv SHA-256
  480e45c358df52d0cce3ecc4b38df78f496574bd3f090376082371a28a58f30f.

- 2026-09-17T18:10:27+00:00: Review fixes committed signed+DCO as
  658424efced1472ab19124012c42d3b7be8f8c1e. Exact CI commands now pass without MYPYPATH: uv run
  --frozen --offline ruff check tools tests; uv run --frozen --offline ruff format --check tools
  tests; uv run --frozen --offline mypy tools tests (20 files); focused tests 23/23. Canonical
  package import fixed by using formal.handoffctl.tier_profiles and updating verify.sh. Receipt now
  derives timeout and vCPU from shared tier_profiles, requires JAR/JDK, hashes persisted command
  JSON bytes, validates/binds guest attestation, and records failed timeout receipts. qemu_runner
  returns result on TimeoutExpired (124), writes failed attestation/serial evidence, and receipt
  remains durable. Candidate worktree clean.

- 2026-09-17T18:10:45+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:11:52+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:13:18+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:13:20+00:00: Recorded command exit 0; command argv SHA-256
  16c43d416890ba0a0f2715eed18889910a49e7422a62388c02ea3975adb42bda.

- 2026-09-17T18:13:30+00:00: Recorded command exit 0; command argv SHA-256
  f48e2add0ec4ea36cf671fa4fd2bdae6c364b0c7c52766f050e0ea5f0ddcd13e.

- 2026-09-17T18:13:58+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:14:05+00:00: Recorded command exit 0; command argv SHA-256
  5f794007cb863acb8dfa046d868ce5d5fcb788bce3592e30169942f0ab5058ed.

- 2026-09-17T18:14:15+00:00: Recorded command exit 0; command argv SHA-256
  57e763c838bdc1458bd57b118836ca749e1207780e025bdfa4f7c472d9dbeccc.

- 2026-09-17T18:14:30+00:00: Runtime review fixes committed as signed+DCO afb9e7da8 (real
  cloud-localds seed image, disposable qemu-img writable overlay, guestfish post-run attestation
  extraction) and bc49937f6 (overlay no longer readonly; extraction failures create failed
  attestation/result receipt). Exact uv offline Ruff check/format, mypy tools tests, and focused
  suite all pass (23/23). Candidate clean. No VM launched.

- 2026-09-17T18:15:25+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:15:44+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:16:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:16:23+00:00: Recorded command exit 0; command argv SHA-256
  5f794007cb863acb8dfa046d868ce5d5fcb788bce3592e30169942f0ab5058ed.

- 2026-09-17T18:16:33+00:00: Recorded command exit 0; command argv SHA-256
  b591cf271173d81ad6b2c145d4155e7c69cdf5794cf3c3da596ab1b743c934e6.

- 2026-09-17T18:16:45+00:00: Final extraction fix committed signed+DCO dfff5a008: guestfish now
  probes list-partitions and selects /dev/sda1 for partitioned images or direct /dev/sda for direct
  ext4 data.raw; unsupported layouts fail closed. Tests cover partitioned, direct, and unsupported
  layouts. Exact offline Ruff check/format, mypy tools tests, and 23/23 focused tests pass. Fresh
  required-tier run remains pending independent review; direct ext4 data image must be used.

- 2026-09-17T18:16:57+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:19:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:20:41+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:20:51+00:00: Fresh required-tier attempt from dfff5a008 failed immediately with
  result 125 before guest boot. Sanitized serial error: QEMU rejected raw drive option serial
  because serial was attached to the raw backend; correct syntax is an if=none drive plus
  virtio-blk-pci device serial. No attestation was accepted. Product fix staged: explicit
  root/data/seed drive IDs and virtio-blk-pci devices, data UUID serial only on device, regression
  test forbids raw backend serial. Exact Ruff/format/mypy and 23/23 focused tests pass.

- 2026-09-17T18:20:59+00:00: Recorded command exit 0; command argv SHA-256
  5f794007cb863acb8dfa046d868ce5d5fcb788bce3592e30169942f0ab5058ed.

- 2026-09-17T18:21:08+00:00: Recorded command exit 0; command argv SHA-256
  bace42aae868822cbc43290651c6849ae6823f581066a4e20df7f369d0e3b5cc.

- 2026-09-17T18:21:28+00:00: Signed fix f1b81fe23 attaches serial only to virtio-blk-pci devices via
  explicit if=none drive IDs; raw backend no longer receives serial. Exact offline Ruff/format/mypy
  and 23/23 focused tests pass. Prior result-125 QEMU serial error is durably recorded. Candidate
  clean.

- 2026-09-17T18:21:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:25:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:25:09+00:00: Fresh f1b81fe23 required guest reached clean shutdown with
  PR_PUBLICATION_RC=0 and EVIDENCE_OK, but host result 125 occurred because guestfish/libguestfs
  supermin lacked permission to read /boot/vmlinuz. Receipt/serial evidence captured; no attestation
  accepted. Debug inspection of the direct-ext4 data image found stale attestation commit 39c8933f5,
  so the old image is rejected. Next repair is argv-only debugfs extraction for direct ext4,
  commit-equality validation, and a newly populated data image from exact reviewed candidate.

- 2026-09-17T18:25:51+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:25:54+00:00: Recorded command exit 0; command argv SHA-256
  62d63b577407da3e292eef32fcb031c230bc7a8af67d178ccfc53ed019bc654a.

- 2026-09-17T18:26:04+00:00: Recorded command exit 0; command argv SHA-256
  51971ccbd2c1ab4b77a8dac6624e0fb0af2703f087889c2f117eb71f9a4d025f.

- 2026-09-17T18:26:19+00:00: Direct ext4 evidence repair committed signed+DCO 519ba3dd4. Extraction
  now probes partition layout, uses argv-only /usr/sbin/debugfs dump from /evidence/... for direct
  ext4, preserves guestfish for partitioned images, unlinks stale output, and fails closed on
  missing/unsupported evidence. Receipt validates attestation profile and commit equality to
  candidate/seed source. Exact offline Ruff/format/mypy and 23/23 focused tests pass. Existing f1
  required guest evidence remains PR_PUBLICATION_RC=0/EVIDENCE_OK but stale 39c image is rejected;
  no acceptance yet.

- 2026-09-17T18:27:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:27:14+00:00: Recorded command exit 0; command argv SHA-256
  c08ac6377089ee0ff96175438788f50f0ddb2a42761952e8408ba7cf76674a86.

- 2026-09-17T18:27:23+00:00: Recorded command exit 0; command argv SHA-256
  2eb62bbffbbb6538572d0b22d649fd507a2091b3b9b05a45815a0c57f08f98c6.

- 2026-09-17T18:27:35+00:00: Recorded command exit 0; command argv SHA-256
  1b318ae5afc5df41a557b09385a4d99d1910faee225d0526703d6f91ce57e7bf.

- 2026-09-17T18:27:45+00:00: Recorded command exit 0; command argv SHA-256
  aa35940469d81dafa274d5f18f12edaba42b9b98495aa6a317f44cf472ad8494.

- 2026-09-17T18:27:54+00:00: Recorded command exit 0; command argv SHA-256
  b14d59f084036d84de9980d181d677693d2b207991b1dc1544e97aecbc970cb6.

- 2026-09-17T18:28:04+00:00: Recorded command exit 0; command argv SHA-256
  ee41e14d433d19e9edf3a57b35cbfff4847b05799c72c122138f5d6a207883d2.

- 2026-09-17T18:28:19+00:00: Recorded command exit 0; command argv SHA-256
  4d4eb3e9a3fddaf278436be4c2428803a6699f165aad2544fe8265627901b1ca.

- 2026-09-17T18:28:28+00:00: Recorded command exit 0; command argv SHA-256
  2492bef1abbbc937cec46ff1054a63c68088e7a29f82bad4acbeae13522e9272.

- 2026-09-17T18:28:38+00:00: Recorded command exit 128; command argv SHA-256
  1d7972369f9c1b1aa67ff70d316e18ab3f1acdbdf74d91309f8db9b63cf69b27.

- 2026-09-17T18:28:49+00:00: Recorded command exit 0; command argv SHA-256
  9272aeaf83d2d18613b94be11ddfdd8665c8ce2cea7707c48c4ecb2fa112d6df.

- 2026-09-17T18:29:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:29:21+00:00: Recorded command exit 0; command argv SHA-256
  3614ef2742ec7a8967872eb2ffe444a7f93d6d211924cf8837cd92aa34440715.

- 2026-09-17T18:29:31+00:00: Recorded command exit 0; command argv SHA-256
  494e9b204208de7a17faedbdd14db816353c65e243f02caddb301186f57508ed.

- 2026-09-17T18:29:40+00:00: Recorded command exit 0; command argv SHA-256
  47b5d1a378ab82bd108c4b6190b2f8bea191cf0323ccb0bab7be66e3e9bbad05.

- 2026-09-17T18:30:18+00:00: Fresh data image rebuilt deterministically at the private runner path
  from a new ext4 filesystem using the pinned data UUID; copied exact candidate state worktree and
  bare git clone, with top-level state/git/jvm/tla2tools.jar. Bare git HEAD resolves candidate
  519ba3dd4e0298ec443e290b007f6cd7e36152b8. Unmounted and e2fsck -fy then e2fsck -fn both clean.
  Image SHA256 b593012b198396f58d1cc00c5034610783c544cdbc948eac389e3c927f42b027. Previous image/run
  was rejected for stale 39c attestation and corrupt/recovery-needed filesystem; no reuse.

- 2026-09-17T18:31:14+00:00: Recorded command exit 1; command argv SHA-256
  bfccc7569e6ef27d190d12ed7fc1814cce7ce0fa73d4f7377720653332dda7b9.

- 2026-09-17T18:31:24+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:32:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:32:10+00:00: Recorded command exit 0; command argv SHA-256
  0d63815b6adb0e464af4d7b665ed77abc33abbc95e62748adb389e93ed45e91a.

- 2026-09-17T18:32:20+00:00: Recorded command exit 0; command argv SHA-256
  7c529023bddb0a0e425a703bef3d4178e0ed1af5fbb3db98e7c47dca716b601e.

- 2026-09-17T18:32:43+00:00: Recorded command exit 0; command argv SHA-256
  1b318ae5afc5df41a557b09385a4d99d1910faee225d0526703d6f91ce57e7bf.

- 2026-09-17T18:32:53+00:00: Recorded command exit 0; command argv SHA-256
  f53b7fdc44477545aba7d6ff4457940ff0142ae1ffd642c8c8d485da5ac86a77.

- 2026-09-17T18:33:02+00:00: Recorded command exit 0; command argv SHA-256
  ee41e14d433d19e9edf3a57b35cbfff4847b05799c72c122138f5d6a207883d2.

- 2026-09-17T18:33:11+00:00: Recorded command exit 0; command argv SHA-256
  4d4eb3e9a3fddaf278436be4c2428803a6699f165aad2544fe8265627901b1ca.

- 2026-09-17T18:33:21+00:00: Recorded command exit 0; command argv SHA-256
  2492bef1abbbc937cec46ff1054a63c68088e7a29f82bad4acbeae13522e9272.

- 2026-09-17T18:33:31+00:00: Recorded command exit 0; command argv SHA-256
  9272aeaf83d2d18613b94be11ddfdd8665c8ce2cea7707c48c4ecb2fa112d6df.

- 2026-09-17T18:33:40+00:00: Recorded command exit 0; command argv SHA-256
  3614ef2742ec7a8967872eb2ffe444a7f93d6d211924cf8837cd92aa34440715.

- 2026-09-17T18:33:50+00:00: Recorded command exit 0; command argv SHA-256
  47b5d1a378ab82bd108c4b6190b2f8bea191cf0323ccb0bab7be66e3e9bbad05.

- 2026-09-17T18:34:04+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:34:10+00:00: Recorded command exit 0; command argv SHA-256
  26792d8c71da7a322bce3902951934c72b662cd949ae77834324a411d50e64f7.

- 2026-09-17T18:34:20+00:00: Recorded command exit 0; command argv SHA-256
  29b24c33fc0a1f8c7b765ca6c5def35557366025a7dc76329987794769225a96.

- 2026-09-17T18:34:29+00:00: Recorded command exit 0; command argv SHA-256
  7b747274d792a8007382008d4472d6ddde8ce274dc9b99b4fe8bda576b8ae50c.

- 2026-09-17T18:34:38+00:00: Recorded command exit 0; command argv SHA-256
  07c3101e7013f697550a7e53de0dbb47210bf9b489eef6a6546f4e05b4a71354.

- 2026-09-17T18:34:48+00:00: Recorded command exit 0; command argv SHA-256
  044d92dc9d390fdf998bbf8e95ae950db91856f1fb95398eb056465fa314aa09.

- 2026-09-17T18:34:57+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:35:00+00:00: Recorded command exit 0; command argv SHA-256
  86895e3088f0678ed827228c74f9fcb365e9b21d8d8d43961d2fa2859e407533.

- 2026-09-17T18:35:24+00:00: Recorded command exit 0; command argv SHA-256
  de0696fee8fc2fdfb40c362eaa9b893663272b997e8c29554f025b6df4104d0c.

- 2026-09-17T18:35:34+00:00: Recorded command exit 0; command argv SHA-256
  a9aae4032074b2bb990449a49d4d2795844b6bc24fcdcb03cfe8d60c892c7506.

- 2026-09-17T18:35:43+00:00: Recorded command exit 0; command argv SHA-256
  22e0fb8bddf08a28e934069e033a465b7796925b45530b693c8b476663e9efc4.

- 2026-09-17T18:35:54+00:00: Recorded command exit 0; command argv SHA-256
  7fb31a62e60e82601e42c9161ea6e5693cbc321e07a990729d617aeb94baafad.

- 2026-09-17T18:36:03+00:00: Recorded command exit 0; command argv SHA-256
  515d32542237e1dd81aad8ca5da313004967d9b9c16b40d027a2a04c0aad45c7.

- 2026-09-17T18:36:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:36:15+00:00: Recorded command exit 0; command argv SHA-256
  6f5b861512f14f068df23124c7ff362c5796334a768f5c4f0083f28deba617df.

- 2026-09-17T18:36:30+00:00: Recorded command exit 0; command argv SHA-256
  515d32542237e1dd81aad8ca5da313004967d9b9c16b40d027a2a04c0aad45c7.

- 2026-09-17T18:37:02+00:00: Fresh direct-ext4 image rebuilt from scratch at private runner path for
  exact candidate 6a1249fc8. Populated top-level state/git/jvm/jar, bare git HEAD resolves
  6a1249fc8, unmounted before checks. e2fsck -fy followed by e2fsck -fn both complete clean with no
  reported errors. Final image SHA256
  8e45429efd5e1ea3d22dbfe63a99e9210f4a214f66a1cd3fe17bd3146554566d. Earlier 519 image/run is
  rejected and not reused for qualification.

- 2026-09-17T18:37:20+00:00: Recorded command exit 1; command argv SHA-256
  ae0b636ce67abc5bd46cea0535db9735f2ad036af390f71c47f193ba92954d26.

- 2026-09-17T18:38:02+00:00: Fresh exact-6a required invocation was attempted but QEMU failed before
  boot with raw data image write-lock error: another process already holds
  ar1293-6a1249fc8-data.raw. Serial contains only the QEMU lock diagnostic; no guest mount/PR
  result/attestation. The clean image itself remains fsck-verified and exact candidate-populated. Do
  not kill unrelated holder; next action is isolate a copy/new image path, verify no holder, then
  rerun.

- 2026-09-17T18:38:16+00:00: Recorded command exit 0; command argv SHA-256
  3bd8ccb328402eb54ef757b462a10a96a0f1ee44f718ca9f2d5637cdc1e23f7b.

- 2026-09-17T18:38:26+00:00: Recorded command exit 0; command argv SHA-256
  76d3c84325ef636bda4ab323c6b93cf9068fe7791bbf3ad9d721e5858d8047af.

- 2026-09-17T18:39:14+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:39:17+00:00: Recorded command exit 0; command argv SHA-256
  0d63815b6adb0e464af4d7b665ed77abc33abbc95e62748adb389e93ed45e91a.

- 2026-09-17T18:39:27+00:00: Recorded command exit 0; command argv SHA-256
  a46c4bd8f34ea2f192b727420aae2f15032e6f4a166c49af6417ae92d7a52f59.

- 2026-09-17T18:40:02+00:00: Fresh exact-6a image run reached guest but mount failed because virtio
  by-id path was absent; serial showed cd /mnt/asb-data/state missing and no formal RC. QEMU image
  layout and fsck were clean. Root/data/seed device order is fixed root=vda, data=vdb, seed=vdc;
  signed commit 5f3f647b1 switches guest seed to /dev/vdb, asserts mountpoint and verifies pinned
  filesystem UUID with bounded shell check, with tests green 23/23. Prior 6a run receipt was
  rejected for missing/stale attestation and is not accepted.

- 2026-09-17T18:40:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:40:31+00:00: Recorded command exit 0; command argv SHA-256
  e02cb4acd71e7323a6fffdae63cb56f1ba9d57a364d1d0a9ab116f8fb58c2480.

- 2026-09-17T18:40:41+00:00: Recorded command exit 0; command argv SHA-256
  845d84b27b1f3213cf9698e529cb4707047df0b370d18c1f6c470cc84bb8cbdc.

- 2026-09-17T18:40:50+00:00: Recorded command exit 0; command argv SHA-256
  24db24432f23823ee21671050a1e085c7a2c5391505e02c8fe28d1fd7a1e6136.

- 2026-09-17T18:41:00+00:00: Recorded command exit 0; command argv SHA-256
  0df6c5f744c1ed6d14e2df7d2b2b2188ac95b4dd20dd488959769a32fdead52c.

- 2026-09-17T18:41:10+00:00: Recorded command exit 0; command argv SHA-256
  3ef04545ef3df93503d264f6887aac451167866a9db20b287c76f9c8e9e96c8f.

- 2026-09-17T18:41:19+00:00: Recorded command exit 0; command argv SHA-256
  7c90d03a3d653fb116755c0354954c354806d12c9873cc5e39daced1a6172e6a.

- 2026-09-17T18:41:55+00:00: Recorded command exit 0; command argv SHA-256
  f94993d1bd8e27962781d46c0f650a427d4d8d776723f234ea4a37bc32707ae1.

- 2026-09-17T18:42:05+00:00: Recorded command exit 0; command argv SHA-256
  436f4afed751dc09cee8fa95d90fb59b2b558e8997a31fe435f2b81ba5d74732.

- 2026-09-17T18:42:14+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:42:16+00:00: Recorded command exit 0; command argv SHA-256
  bb0f0aab22432dad31f825bd8305d7a0aa0470002f30c01dfe29d227e9b072bb.

- 2026-09-17T18:42:56+00:00: Final fresh 5f3f647b1 data image now rebuilt and corrected: initial
  copied bare ref mismatch was observed and not run; state was recopied and bare clone recreated.
  debugfs packed-refs now binds feature/ar-1293-state-tla-admission-v2 to exact
  5f3f647b15f69fc75670897d6739c239fadda120. Image unmounted, e2fsck -fn clean, SHA256
  1f83e49b9f117f464c163b16f9cb0c9f3944b1e46c6cff23cc187c4c74c917c4. Candidate/state and image
  provenance are now aligned.

- 2026-09-17T18:43:15+00:00: Recorded command exit 1; command argv SHA-256
  6d67283d4b5659108adc55be869d539bdf0bbdc3f8d0d07ea1ccc9fdc0b7c30c.

- 2026-09-17T18:44:16+00:00: Required invocation against exact 5f image did not boot: QEMU reported
  data image write-lock contention before guest start; serial contains only Failed to get write lock
  and no mount/PR/attestation. fuser now shows no holder, but image path is treated as contaminated
  for this attempt. Receipt rejected due failed attestation. Next use a new unheld copy of the
  fsck-clean exact 5f image and rerun.

- 2026-09-17T18:44:54+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:45:56+00:00: Recorded command exit 0; command argv SHA-256
  d0b44aee7a1d357426d8498a75c1b382377405e51ea7f474f6fb3c453be5afc2.

- 2026-09-17T18:47:19+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:47:22+00:00: Recorded command exit 0; command argv SHA-256
  0d63815b6adb0e464af4d7b665ed77abc33abbc95e62748adb389e93ed45e91a.

- 2026-09-17T18:47:31+00:00: Recorded command exit 0; command argv SHA-256
  307a56be74c30871ee440a144ce1dfc6614e6691ca49aca6c731ebc05661e146.

- 2026-09-17T18:47:55+00:00: Actual exact-5f guest run evidence recorded: /dev/vdb mounted and PR
  transient preflight passed, but TLC failed before PR result/attestation with Java InternalError:
  Error loading java.security file. Root cause is JDK conf/security absolute symlinks targeting
  absent host /etc/java-17-openjdk. Signed fix d57b495b9 copies pinned guest JDK to jvm-fixed,
  replaces java.security/java.policy/nss.cfg from guest system security files, exports
  JAVA_HOME/PATH, and tests the contract. Exact offline Ruff/format/mypy and 23/23 tests pass.

- 2026-09-17T18:48:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:49:27+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:49:35+00:00: Recorded command exit 0; command argv SHA-256
  fb00f9c578f30197d1ad1f0d5ffd0223daa4d35b8171f58f4ebefaa4669e82a9.

- 2026-09-17T18:49:45+00:00: Recorded command exit 0; command argv SHA-256
  9c7e1effef33c7a7cd868e22181d8a2325dcadc1e4f5d009350062eb202c1058.

- 2026-09-17T18:49:55+00:00: Recorded command exit 0; command argv SHA-256
  8bd3db2a81c612a73bd4f36a19b49cafe9884e2eb9f855b59a91dd36f9c402e3.

- 2026-09-17T18:50:05+00:00: Recorded command exit 0; command argv SHA-256
  804b85600bcacf9770067c6b8f58ed178e46f1e6216cf9ade3d6ace75c9768ec.

- 2026-09-17T18:50:14+00:00: Recorded command exit 0; command argv SHA-256
  f45fe54d11eca2a3b1ecda570a49189b5d9865d73601a4cac4daf6371a270e4c.

- 2026-09-17T18:50:27+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:50:36+00:00: Recorded command exit 0; command argv SHA-256
  ed42549092b719045a64079a03aa7af69b1ad74e057cb94b9fe298078aecc29f.

- 2026-09-17T18:50:46+00:00: Recorded command exit 0; command argv SHA-256
  6e99f250ca664b3dc7a97dc0f43ff69898feab61be273a9c6e43e335ada5157c.

- 2026-09-17T18:50:56+00:00: Recorded command exit 0; command argv SHA-256
  226cecbe6c891a4f5100a25423d3fdeb696199f5e38331f05b90b107e9a6c672.

- 2026-09-17T18:51:05+00:00: Recorded command exit 0; command argv SHA-256
  9910223ba906c3e50f3f01ce2e19ae368e080d6269092661e8376141664cb76f.

- 2026-09-17T18:51:40+00:00: Fresh d57 image corrected after an intermediate failed command typo
  left the image state/refs unchanged. Bare Git was recreated from the exact candidate; debugfs
  packed-refs now resolves feature/ar-1293-state-tla-admission-v2 to
  d57b495b9150efd0a5114b09c45b9e31d83228ff. Image unmounted and e2fsck -fn clean. Final image SHA256
  804c6e67e11a7ffdfbe897bcca5771e51d15f52ae27ae087c79f9a653a6912c1. The typo was ./tools.handoffctl
  (missing slash), corrected; no VM run on mismatched refs.

- 2026-09-17T18:51:56+00:00: Recorded command exit 1; command argv SHA-256
  83ea272821399d70be079d3d3b34959a5bddcbb36c7e51d4e9c93e1742d6ba3b.

- 2026-09-17T18:52:40+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:53:10+00:00: Recorded command exit 1; command argv SHA-256
  172d88874bc4917ef791d783b763d5fc4f032c791953cbddb7813b4737845e41.

- 2026-09-17T18:53:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:53:45+00:00: Recorded command exit 0; command argv SHA-256
  1a6196b6780bbf0fcf2e1ffcfdd7df435ea324e8c252cc450f9b889131d9106b.

- 2026-09-17T18:53:54+00:00: Recorded command exit 0; command argv SHA-256
  4df27f0ba84fe4ef8d86d0af2f3b37d4aac1c3d44d22d8d581eb4b5f3d1a5638.

- 2026-09-17T18:54:09+00:00: Recorded command exit 0; command argv SHA-256
  a64a7d0b815a692455fa42b5cfb3c0666dd16ed92643a6f6ab7466913c9a3e83.

- 2026-09-17T18:54:19+00:00: Recorded command exit 0; command argv SHA-256
  3c64e4be86e02e4efab3ad4deea143ea5f0cb02fc44669e29ee8aecc6956c1c1.

- 2026-09-17T18:54:40+00:00: Recorded command exit 0; command argv SHA-256
  4185c27f469f7a4568894b0575162e7ba7be533e8b43509491fdae1242c5fbc1.

- 2026-09-17T18:54:50+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:54:52+00:00: Recorded command exit 0; command argv SHA-256
  5fe47ad0da15eb98f409648faa9a5911e9001aa832f7f590d8a740b97c48ede6.

- 2026-09-17T18:55:02+00:00: Recorded command exit 0; command argv SHA-256
  cf317472dc2ca0966eda4b29f56b045d3bfbc47136fd3f27d459a47438ae1873.

- 2026-09-17T18:55:12+00:00: Recorded command exit 0; command argv SHA-256
  b9ace8603484c32ca341a15a1ffc6eb1e1f66d92c3da46bb1bfdd835d8c2a8a0.

- 2026-09-17T18:55:37+00:00: Recorded command exit 0; command argv SHA-256
  c90e84191845a74aef503bb79c89f274531bc77b580abe84af9edbf1e29c540c.

- 2026-09-17T18:55:46+00:00: Recorded command exit 0; command argv SHA-256
  b1d5efe7d85517bbd825f5ff0f13264b111409b0594bb05fe54a7afce1205184.

- 2026-09-17T18:55:56+00:00: Recorded command exit 0; command argv SHA-256
  6a82f9dc7ab909acf52abd953d60396db329ed0afb67c30a7647b627ed26f595.

- 2026-09-17T18:56:06+00:00: Recorded command exit 0; command argv SHA-256
  893f15973c1caf6470af27cc2cc26f31f9dc6bd3ac652f59d4d5a34368beca01.

- 2026-09-17T18:56:15+00:00: Recorded command exit 0; command argv SHA-256
  ba7722eab20af0c63925e3d79b52a69a0cff044e4488024b7e3056284e68fe13.

- 2026-09-17T18:56:25+00:00: Recorded command exit 0; command argv SHA-256
  6cc5c72a03f7c81e141d738c5aa6eef54e1c38aeffb40aa824f48acc5dad4cc2.

- 2026-09-17T18:56:34+00:00: Recorded command exit 32; command argv SHA-256
  6cc5c72a03f7c81e141d738c5aa6eef54e1c38aeffb40aa824f48acc5dad4cc2.

- 2026-09-17T18:57:09+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T18:57:14+00:00: Recorded command exit 0; command argv SHA-256
  3c64e4be86e02e4efab3ad4deea143ea5f0cb02fc44669e29ee8aecc6956c1c1.

- 2026-09-17T18:57:32+00:00: Recorded command exit 0; command argv SHA-256
  c90e84191845a74aef503bb79c89f274531bc77b580abe84af9edbf1e29c540c.

- 2026-09-17T18:57:41+00:00: Recorded command exit 0; command argv SHA-256
  b1d5efe7d85517bbd825f5ff0f13264b111409b0594bb05fe54a7afce1205184.

- 2026-09-17T18:57:51+00:00: Recorded command exit 0; command argv SHA-256
  6a82f9dc7ab909acf52abd953d60396db329ed0afb67c30a7647b627ed26f595.

- 2026-09-17T18:58:05+00:00: Recorded command exit 0; command argv SHA-256
  ba7722eab20af0c63925e3d79b52a69a0cff044e4488024b7e3056284e68fe13.

- 2026-09-17T18:58:24+00:00: Recorded command exit 0; command argv SHA-256
  6cc5c72a03f7c81e141d738c5aa6eef54e1c38aeffb40aa824f48acc5dad4cc2.

- 2026-09-17T18:58:33+00:00: Recorded command exit 0; command argv SHA-256
  d9eeeb77fc59f5437c8b18b4f84fef9c63e2318438b06251efe73dafad2b6a2f.

- 2026-09-17T18:58:43+00:00: Recorded command exit 32; command argv SHA-256
  6cc5c72a03f7c81e141d738c5aa6eef54e1c38aeffb40aa824f48acc5dad4cc2.

- 2026-09-17T19:00:19+00:00: Recorded command exit 0; command argv SHA-256
  92272268196c102767d88d55bd18912e10fb492f82896df24a31c02a4b206d80.

- 2026-09-17T19:01:00+00:00: Recorded command exit 0; command argv SHA-256
  69feb50eb32a6f6530084dd77fce73c4e13463cfcb6c2f1bd331148a2d019f6c.

- 2026-09-17T19:01:55+00:00: Candidate 9b9491d08 is signed and DCO-compliant. Focused gates pass:
  Ruff check, Ruff format, mypy, and 23 focused tests. The exact 922 image was validated with the
  candidate ref and security fixture but its guest run failed because dangling JDK security symlinks
  rejected cp; the tracked seed now removes those links before copying pinned files. Disposable
  image was repaired with e2fsck; rebuild is required for the new seed/candidate.

- 2026-09-17T19:02:04+00:00: Recorded command exit 0; command argv SHA-256
  ccb5bf770069b206646e67f644984c7d0dc70bd1f728facf1508878cca74b718.

- 2026-09-17T19:02:18+00:00: Recorded command exit 0; command argv SHA-256
  2d0572b35c82183d0ec2c4600bdbf0d62232848da59c65e11a51a4dd181e2a0d.

- 2026-09-17T19:02:37+00:00: Recorded command exit 0; command argv SHA-256
  f2c1bb0d992ea610791c9706975660e10d28922e70638924dd98f792e0629219.

- 2026-09-17T19:02:52+00:00: Recorded command exit 0; command argv SHA-256
  00b78a4a234c3d42fd4e54581b1d45e9eefcc780ccf334b843c7752cd9cd1dd8.

- 2026-09-17T19:03:02+00:00: Recorded command exit 0; command argv SHA-256
  c018a06feee2e3afaecab2ac07d1a27ed23df1c6d24fd5ac3ba99c2e771e1fdc.

- 2026-09-17T19:03:50+00:00: Recorded command exit 2; command argv SHA-256
  5e65e7d6da5f1779bdb275bbd6c91e24b42af4b1c31ee57a7c562cef39dec881.

- 2026-09-17T19:04:11+00:00: Recorded command exit 1; command argv SHA-256
  09e8711fe407a16992e709c8a8071c7b56f32f26de14cafeb9812121fe3caba7.

- 2026-09-17T19:05:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:05:20+00:00: Recorded command exit 1; command argv SHA-256
  6dc8b9b3d8e88657946a71e4f896316c5721d09604589840407cd4c203689285.

- 2026-09-17T19:05:55+00:00: Recorded command exit 0; command argv SHA-256
  69feb50eb32a6f6530084dd77fce73c4e13463cfcb6c2f1bd331148a2d019f6c.

- 2026-09-17T19:06:21+00:00: Required VM using candidate 9b9491d08 booted with the data mount, JDK
  security repair, transient containment, and TLC all successful. It failed only when the asb
  process attempted to write the pre-existing root-owned evidence directory; the launcher then
  correctly rejected missing attestation. Candidate 0ce2726e2 adds explicit ownership for
  temporary/evidence directories and a focused regression assertion. Focused Ruff, format, mypy, and
  23-test gates pass; commit is SSH-signed with DCO.

- 2026-09-17T19:06:31+00:00: Recorded command exit 0; command argv SHA-256
  00ac73f10b77b0cc62bedfa7e082c6cdef28622d39d2bf2cb954e9bad6da384f.

- 2026-09-17T19:06:42+00:00: Recorded command exit 0; command argv SHA-256
  a700226ab3f5732e725c1075baeb7a34b00b4e7898576d5ea3e15d7eebd56d62.

- 2026-09-17T19:07:01+00:00: Recorded command exit 0; command argv SHA-256
  28da2d4deedd0560bdc3327ed33e8203861c7b3ee3d304c062db4c191132baad.

- 2026-09-17T19:07:11+00:00: Recorded command exit 0; command argv SHA-256
  80f7f0d551e76f52ba8548e6f39094a8216012ab155ed3281a654776b757ff1d.

- 2026-09-17T19:07:20+00:00: Recorded command exit 0; command argv SHA-256
  5d9ee77973bda546a20f285dd262b48741020b5f42b9f08b80aaeabcd929ddaa.

- 2026-09-17T19:08:22+00:00: Recorded command exit 1; command argv SHA-256
  b4dfa7aba94744b74d567c7371789f9f604602ff7dc016b63d12dede7cf6c567.

- 2026-09-17T19:10:13+00:00: Recorded command exit 0; command argv SHA-256
  69feb50eb32a6f6530084dd77fce73c4e13463cfcb6c2f1bd331148a2d019f6c.

- 2026-09-17T19:10:41+00:00: Required VM for candidate 0ce2726e2 reached PR_PUBLICATION_RC=0 and
  PR_PUBLICATION_EVIDENCE_OK after the JDK and evidence ownership fixes. Runner rejected the result
  because extraction invoked guestfish list-partitions without launching the appliance; direct
  evidence was present but extraction failed. Candidate ac971b996 replaces this with a launched
  list-filesystems probe (direct /dev/sda, partition fallback /dev/sda1) and adds a regression
  assertion. Focused Ruff, format, mypy, and 23 tests pass; commit is SSH-signed with DCO.

- 2026-09-17T19:10:51+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:11:09+00:00: Recorded command exit 0; command argv SHA-256
  42424be8f25365afceee151c4d136c3f0c016e9c1422e1c2df60a5796fcf02a5.

- 2026-09-17T19:11:19+00:00: Recorded command exit 0; command argv SHA-256
  9506e91615a64921d7c01e9e52be0d7a3f94b153f64e3072a30bd5223975bc5b.

- 2026-09-17T19:11:28+00:00: Recorded command exit 0; command argv SHA-256
  1b923b4120820fbccd1ba65fd6d0ad005029e2e6581fadceb85ada47bfed1c67.

- 2026-09-17T19:11:38+00:00: Recorded command exit 0; command argv SHA-256
  9cdea5d29a5fbb9e72f1f6f866c7c9dec77136c6ee28f1c50cda0c7dffda4f73.

- 2026-09-17T19:11:47+00:00: Recorded command exit 0; command argv SHA-256
  fc5e6fdbdb54c761a2ef13f31ca917b9d1e1b2db560f2cd6a25609168483b662.

- 2026-09-17T19:13:06+00:00: Recorded command exit 1; command argv SHA-256
  a3ba513516f7c9e02014aade8225b8c040304680aa3f59b2859d6e362f291b34.

- 2026-09-17T19:14:18+00:00: Recorded command exit 0; command argv SHA-256
  69feb50eb32a6f6530084dd77fce73c4e13463cfcb6c2f1bd331148a2d019f6c.

- 2026-09-17T19:14:43+00:00: Candidate ac971b996 required VM again reached PR_PUBLICATION_RC=0 and
  PR_PUBLICATION_EVIDENCE_OK. Host extraction failed because the guestfish supermin probe requires
  unavailable privileged host access, despite the direct ext4 image already containing valid
  evidence. Candidate 903a87844 now attempts direct debugfs extraction first and keeps guestfish
  only as a partitioned-image fallback. Focused Ruff, format, mypy, and 23 tests pass; commit is
  SSH-signed with DCO.

- 2026-09-17T19:14:59+00:00: Recorded command exit 0; command argv SHA-256
  de390041ff22a74ea368bf1ec15b274244c1841cae1bbb18e635f3746dead0e3.

- 2026-09-17T19:15:09+00:00: Recorded command exit 0; command argv SHA-256
  cfca7e2fe7399275bd8fb8dd8df3def6c49c984537ac50077239134347aae168.

- 2026-09-17T19:15:19+00:00: Recorded command exit 0; command argv SHA-256
  2380cd7a5a30945d83beca562ce48ce70121de8b23073bee6c8ab691f4307406.

- 2026-09-17T19:15:28+00:00: Recorded command exit 0; command argv SHA-256
  60be5a751128d3a66cec70e80e582d05a096f9c2181a5dfacc7a63ed9f905759.

- 2026-09-17T19:15:38+00:00: Recorded command exit 0; command argv SHA-256
  8c112d1e52c2a5faf1b5efcd8b70d2b446434968dfe9b25b579237d18d830d52.

- 2026-09-17T19:17:00+00:00: Recorded command exit 0; command argv SHA-256
  2dba5776fcb2d21f97c8fe5f1f9a1bae1c138e270650243c1ac9d3e94aea8c54.

- 2026-09-17T19:17:46+00:00: Required-tier qualification is green at signed candidate
  903a87844cfec56e9735112ef7749db792b98afd. Fresh fsck-clean data image SHA-256 is
  0b30ea04552732fd7acfe0a118d8ad73056f98c9d22cae3c85322a93dab17cd9. Guest markers:
  PR_PUBLICATION_TRANSIENT_RC=0, PR_PUBLICATION_RC=0, PR_PUBLICATION_EVIDENCE_OK. Attestation
  status=success/profile=pr-publication/commit matches candidate/containment_mode=required. Receipt
  result=0 records 1800s runtime, 3G memory+swap, 200% CPU, TasksMax64, 8G AS, 8 vCPUs, 2 workers.
  Direct debugfs extraction succeeded without privileged guestfish. Full-exhaustive remains
  outstanding.

- 2026-09-17T19:17:56+00:00: Recorded command exit 0; command argv SHA-256
  24b42aa3dc7d1d1fbc7d80ff20a8bfb1204f645985d8349430bb0cc9b2032204.

- 2026-09-17T19:19:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:23:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:28:43+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:32:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:34:53+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:39:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:43:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:45:10+00:00: Recorded command exit 0; command argv SHA-256
  b5ccc42c1eff4c35258691dc906dfcff7f88f369fd97a3586c66c4e19608c812.

- 2026-09-17T19:45:20+00:00: Recorded command exit 1; command argv SHA-256
  47bb7ef5819ed2f8b82379339d60ff223c3477925f05e08ffa608ee8366cf8d3.

- 2026-09-17T19:45:54+00:00: The approved full-exhaustive run was terminated after a truthful guest
  failure at approximately 39.2M generated states: TLC threw java.io.IOException while merging
  Handoffctl state files, with No space left on device under /mnt/asb-data/tmp. This is disposable
  data-image scratch exhaustion, not a model result. The failed QEMU was terminated through
  handoffctl; no full attestation or receipt is accepted. Required-tier evidence remains green and
  unchanged.

- 2026-09-17T19:46:11+00:00: Recorded command exit 0; command argv SHA-256
  e60e7f35d7abdb7def9e07db50785057a81a524a7120a547bf25c70d9de11ea6.

- 2026-09-17T19:46:20+00:00: Recorded command exit 0; command argv SHA-256
  61d88b4d18c524b346335aa7ca30fddc02ef457ae27217a723593a1636ec837d.

- 2026-09-17T19:46:31+00:00: Recorded command exit 1; command argv SHA-256
  0b78cfd26c779c04408f08e40b8a2df77945b4c8687a7948ba1d6c643fb44cf0.

- 2026-09-17T19:46:40+00:00: Recorded command exit 0; command argv SHA-256
  5323686c965fa0c5f7727f36346e349cbaa7495ce82cda12a51869b830ae756c.

- 2026-09-17T19:46:50+00:00: Recorded command exit 0; command argv SHA-256
  e06d93b494a7f24308a4a002b545053edad59ecf2bde0c7f1331ad78cfa6027d.

- 2026-09-17T19:47:34+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:50:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T19:59:40+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:04:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:05:18+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:20:54+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:21:25+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:24:28+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:25:38+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:28:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:29:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:32:30+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:33:52+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:35:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:36:39+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:37:35+00:00: Runner configuration audit while full run is active: command JSON uses
  no NIC, 32768 MiB VM memory, 8 vCPUs, separate writable qcow2 overlay, read-only seed, raw data
  image with stable virtio serial, and tier runtime 7200s. Guest seed enforces 3G MemoryMax, 3G
  MemorySwapMax, 200% CPUQuota, TasksMax64, 8G address-space bound, 2 TLC workers, offline curl
  shim, and no host mounts. Receipt binds candidate/seed/image/JAR/JDK/command/serial/attestation
  digests. Full run is active; no missing clean-runner property found.

- 2026-09-17T20:37:47+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:38:08+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:39:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:39:32+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:39:52+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:40:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:40:34+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:40:48+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:41:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:41:03+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:41:23+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:41:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:42:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:43:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:43:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:43:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:44:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:44:12+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:44:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:44:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:44:56+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:45:12+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:45:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:45:53+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:46:06+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:46:21+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:46:35+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:46:52+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:47:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:47:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:47:35+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:47:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:02+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:33+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:46+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:48:58+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:49:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:49:30+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:49:48+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:50:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:50:14+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:50:25+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:50:38+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:50:50+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:51:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:51:19+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:51:40+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:52:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:52:14+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:52:28+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:52:41+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:52:53+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:53:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:53:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:53:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:53:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:53:55+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:54:09+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:54:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:54:35+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:54:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:55:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:55:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:55:32+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:56:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:56:59+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:57:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:57:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:57:56+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:58:39+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:58:50+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:59:04+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:59:18+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:59:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T20:59:47+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:00:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:00:43+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:00:52+00:00: Recorded command exit 1; command argv SHA-256
  8e5099aac9ddeb366c8275c0bacb49afa9eb9a984fa0951271284a0c682cbfee.

- 2026-09-17T21:01:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:01:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:02:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:02:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:02:37+00:00: The fresh 16GiB full-exhaustive retry passed the prior disk-capacity
  point and progressed beyond 46M generated states, but terminated at 21:00:52 with Java
  out-of-memory during TLC liveness checking. No full attestation or receipt was produced and the
  run is not accepted. Required-tier evidence remains green. Next action is the independently
  reviewed receipt/serial integrity hardening followed by a larger isolated runner.

- 2026-09-17T21:03:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:03:32+00:00: Recorded command exit 0; command argv SHA-256
  69feb50eb32a6f6530084dd77fce73c4e13463cfcb6c2f1bd331148a2d019f6c.

- 2026-09-17T21:04:18+00:00: Full 16GiB run terminated with Java out-of-memory during TLC liveness;
  no attestation/receipt accepted. Candidate ada383cea adds mandatory overlay image SHA-256 to the
  receipt and requires all three exact success markers in serial for result=0; focused Ruff, format,
  mypy, and 23 tests pass, signed+DCO. The active failed VM is stopped. Next runner remains
  offline/no-NIC/q35 KVM-or-TCG, 32GiB guest memory, 8 vCPUs, 3G memory+swap cgroup, 8G AS bound, 2
  TLC workers.

- 2026-09-17T21:04:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:04:47+00:00: Recorded command exit 0; command argv SHA-256
  f634507031283a9b0ba3531ef6fe84af9303d5f2d6ef34bf103013da489b5723.

- 2026-09-17T21:04:56+00:00: Recorded command exit 0; command argv SHA-256
  9e24d426fb9daa044076c3a51c77e0250e5921c610444376e275d364b4251aab.

- 2026-09-17T21:05:14+00:00: Recorded command exit 0; command argv SHA-256
  80eef1cb74bd38ba2aa2f2b2adb9a3fb0a73a95145242c8a1fbc96a8c6a3f73f.

- 2026-09-17T21:05:23+00:00: Recorded command exit 0; command argv SHA-256
  57536e172e332a14ccd5f165f3688605d932766ae6cc0252c88a6a204f04b9c4.

- 2026-09-17T21:05:32+00:00: Recorded command exit 0; command argv SHA-256
  aa04beea08f04d27f731de34926fa3e01bb33a0358379e28ab9d1e4980d57771.

- 2026-09-17T21:06:34+00:00: Recorded command exit 0; command argv SHA-256
  89bcc57ff4181f820cd76c9b63592c02a9f90074505b91c90b01022a5ee5a44f.

- 2026-09-17T21:06:44+00:00: Recorded command exit 0; command argv SHA-256
  1ecd2b473467b54a008399bc31efaa9ec4c5d86dc4bed89fba10d86e376389a4.

- 2026-09-17T21:06:54+00:00: Recorded command exit 0; command argv SHA-256
  7a84b98c98ab53106ec3b71193d42c67688f623cf5915502a91c881f24179bc2.

- 2026-09-17T21:07:05+00:00: Recorded command exit 0; command argv SHA-256
  5940b9fed568726f15cd0c7b8e7f63050984080209fea9bb5f4be6bfd819d6ad.

- 2026-09-17T21:08:00+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:08:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:08:59+00:00: Provisioned and validated fresh 32GiB direct-ext4 data image for signed
  candidate ada383cea: SHA-256 735afc1e1ad89648f9bc18932f9576e3cbe5ae577d89a829d680bafde4707153,
  fsck-clean, exact bare ref, pinned JDK security files present. Started fresh full-exhaustive QEMU
  with no NIC/host mounts, 32GiB guest memory, 8 vCPUs, tier timeout 7200s, and unchanged required
  containment bounds. Receipt now requires overlay digest and exact transient/result/evidence
  markers.

- 2026-09-17T21:10:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:10:58+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:11:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:12:06+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:13:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:13:51+00:00: Recorded command exit 1; command argv SHA-256
  2cf71230822403541f4afa4293cbfa288e600d57bca65c7a68384428321876e1.

- 2026-09-17T21:14:18+00:00: Recorded command exit 2; command argv SHA-256
  2cf71230822403541f4afa4293cbfa288e600d57bca65c7a68384428321876e1.

- 2026-09-17T21:14:27+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:14:34+00:00: Recorded command exit 0; command argv SHA-256
  271c04f5e3cb3cebf52220eb5393ea43ae02845b387509b6f9b46be423802fa1.

- 2026-09-17T21:15:12+00:00: Independent review found formal/handoffctl/attest.py duplicated tier
  timeout constants and the formal Ruff formatting gate failed. Candidate fa57625d9 imports shared
  timeout_for_tier(), and formal Ruff check/format plus tools/tests mypy and 23 focused tests pass.
  The currently active ada383cea VM predates this commit and its evidence cannot qualify fa57625d9;
  it remains unmodified until terminal exit.

- 2026-09-17T21:15:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:16:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:16:58+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:17:02+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:17:51+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:18:10+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:19:08+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:19:11+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:20:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:20:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:20:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:20:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:21:22+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:21:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:21:50+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:22:14+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:22:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:22:57+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:23:25+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:23:48+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:24:04+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:24:19+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:24:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:25:09+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:26:04+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:26:34+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:27:24+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:27:38+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:28:08+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:28:27+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:28:46+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:29:11+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:29:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:29:37+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:29:53+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:30:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:31:07+00:00: Recorded command exit 0; command argv SHA-256
  45d31a3bc1fbc2b27ad7e26544994a69819c17b755d7a74a839b892e34ae0353.

- 2026-09-17T21:31:17+00:00: Recorded command exit 0; command argv SHA-256
  b9da3d47bbb0820b233d74309d3f0bdba866042e675fac3bc792a77dc0b56435.

- 2026-09-17T21:32:36+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:33:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:34:06+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:34:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:34:42+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:35:35+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:36:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:36:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:37:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:38:03+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:38:41+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:39:06+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:39:28+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:39:32+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:40:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:40:43+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:43:50+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:44:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:47:59+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:49:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:51:43+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:52:39+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:52:44+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:53:12+00:00: Recorded command exit 128; command argv SHA-256
  d9cca565383b6e42d55296ebdc2163a4ac6d6527e410710831a62e5a445439df.

- 2026-09-17T21:53:27+00:00: Recorded command exit 0; command argv SHA-256
  c51e74206232b3729eff4fd9b7d17801bcd59d357d2788535a171977e15dd140.

- 2026-09-17T21:55:08+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:56:46+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T21:58:02+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:00:35+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:01:44+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:02:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:03:33+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:06:01+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:11:03+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:14:37+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:19:56+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:24:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:27:26+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:31:03+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:34:12+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:36:16+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:36:18+00:00: Recorded command exit 0; command argv SHA-256
  ab5bda0c4316b4cf69c21dd366e327064678aef1448bad7c38cfa353c1def964.

- 2026-09-17T22:36:29+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:36:34+00:00: Recorded command exit 0; command argv SHA-256
  d4b57fb671d366607343e48aa57bf170df625f10287de0c8742123f99e3094d5.

- 2026-09-17T22:36:49+00:00: Recorded command exit 0; command argv SHA-256
  28ab38ab9a72014b7e692218f941ee2fdad466080cba7841091e77df31b289b4.

- 2026-09-17T22:37:17+00:00: 2026-09-17T22:37Z: Inspected terminated ada383cea full VM through
  handoffctl. QEMU is absent; serial ends at 22:27:34 during liveness progress (47,029,477
  generated; 38,798,900 distinct; 10,713,755 queued). No terminal FULL_EXHAUSTIVE_RC, EVIDENCE_OK,
  attestation, or receipt exists. This run is rejected as interrupted/incomplete; no model
  success/failure is inferred. AR-1307 is still in_progress with PR #24 open, so exact fa57625d9
  rerun must wait for runner repair/handoff.

- 2026-09-17T22:38:17+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:40:05+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:41:27+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:42:49+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:44:04+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:46:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:48:24+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:49:25+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:50:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:51:57+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:53:31+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:55:13+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T22:59:09+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:01:40+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:03:39+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:05:07+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:06:20+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:07:55+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-17T23:09:15+00:00: Heartbeat by codex-ar1293-timeout-repair-20260917.

- 2026-09-18T01:10:56+00:00: Recovered expired claim formerly owned by
  codex-ar1293-timeout-repair-20260917. Recovered stale AR-1293 claim after owner stopped
  heartbeating at 2026-09-17T23:09:15Z; preserve blocked status and evidence, leave ownerless for
  reassignment after AR-1307 runner handoff.

- 2026-09-18T21:04:05+00:00: Claimed by codex-ar1293-audit-20260918.

- 2026-09-18T21:04:20+00:00: Evidence-only audit 2026-09-18: AR-1307 remains blocked ownerless, task
  head 969eef058 but remote feature ref is ab485f767; its required formal run 35342513872 previously
  failed closed on Java OOM under unchanged 3G/3G and emitted no attestation. AR-1308 remains
  blocked ownerless; latest bounded preflight (20:47:46Z) had no active QEMU, stale AR-1307 input
  ab485f767, only ~4.9 GiB approved-root free versus 16 GiB minimum, and missing admission lock,
  pinned JDK, and TLC JAR. Receipt preserves x86_64 QEMU 8.2.2, network none/no host mounts, 8
  vCPU/16 GiB guest swap and 3G/3G/2-worker/2-core/8G/7200s contract. No safe in-scope preparation
  or formal execution performed; unrelated processes and caches untouched.

- 2026-09-18T21:04:30+00:00: Released ownerless after evidence-only audit. AR-1307 remains
  unqualified: required runner head is 969eef058 but remote branch is ab485f767 and prior formal run
  35342513872 failed Java OOM under unchanged 3G/3G with no attestation. AR-1308 remains blocked:
  latest preflight failed closed on stale input ab485f767, ~4.9 GiB approved-root free versus 16 GiB
  minimum, and missing lock/JDK/TLC runtime inputs. No safe local preparation or formal execution is
  authorized; resume only after exact current input bundle and passing isolated preflight.
