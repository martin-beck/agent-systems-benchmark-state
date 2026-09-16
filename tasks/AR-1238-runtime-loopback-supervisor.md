---
{
  "branch": "feature/ar-1238-runtime-loopback-supervisor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T10:05:42+00:00",
  "depends_on": [
    "AR-1100",
    "AR-1231"
  ],
  "id": "AR-1238",
  "next_action": "Run exact-head workspace gates, independently review SandboxBackend relay mount and supervisor composition, then release with signed commit d9f42ec; real cassette forwarding remains dependent on sidecar protocol implementation.",
  "observed_branch": "feature/ar-1238-runtime-loopback-supervisor",
  "observed_dirty": 0,
  "observed_head": "d9f42ecb2a205b86250233f4f4c75688a997c063",
  "owner": "asb_ar1238_bwrap_relay_worker",
  "plan": "../plans/AR-1238.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the runtime-owned private-namespace supervisor for loopback replay.",
  "task_revision": 19,
  "title": "Runtime-owned loopback supervisor",
  "updated_at": "2026-09-16T08:05:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1238"
}
---

Own the missing runtime composition seam. A pinned in-tree supervisor must create a private user
and network namespace, bring up only its own loopback interface, mount the authenticated Unix relay,
start the sidecar and adapter together, and report readiness to the runtime. It must never share
host networking, alter global firewall state, invoke ambient `ip`, expose credentials, or affect
unrelated processes.

Acceptance: immutable command identity and route/generation attestation; bounded forwarding and
startup; fail-closed namespace setup; teardown/reaping on success, timeout, cancellation, crash,
restart, duplicate, stale, and partial launch; provider/external egress denial; unrelated-process
non-interference; focused/full locked, privacy, policy, native, signature/DCO, and exact-head gates.

Live capability evidence (2026-09-16): pinned Bubblewrap 0.9.0 with the existing isolated flags
creates a private network namespace whose loopback is already UP; external curl egress fails with
exit 7. Creating `/tmp` as a tmpfs before bind-mounting a per-launch 0600 Unix socket works, and a
host Unix listener was reached from inside the sandbox through that mount. No host-network sharing,
firewall mutation, CAP_NET_ADMIN, ambient `ip`, or unrelated-process changes are required. The
remaining work is launcher integration and real sidecar forwarding, not a host capability blocker.

- 2026-09-16T07:46:08+00:00: Dependencies AR-1100 and AR-1231 verified complete; promote
  runtime-owned loopback supervisor prerequisite.

- 2026-09-16T07:46:43+00:00: Claimed by asb_ar1238_supervisor_worker.

- 2026-09-16T07:49:15+00:00: Implemented validated private supervisor handoff contract in signed
  commit 6fba189; focused and full locked workspace tests, fmt and clippy pass. Blocked: current
  SandboxBackend has no in-tree supervisor executable/process+FD lifecycle seam to create private
  user/network namespace, bring up loopback, mount relay, launch/reap sidecar+adapter, and attest
  readiness. Implementing only a plan would overclaim runtime isolation; no host networking,
  firewall, ambient ip, or privileged helper used.

- 2026-09-16T07:53:08+00:00: User explicitly authorized actual rootless supervisor implementation;
  proceed with fail-closed in-tree executable and launcher integration, no host networking or global
  policy changes.

- 2026-09-16T07:53:11+00:00: Claimed by asb_ar1238_supervisor_worker.

- 2026-09-16T07:55:22+00:00: User-authorized follow-up implemented signed commit 9d982fe: in-tree
  asb_loopback_supervisor executable now requires explicit --unshare-net, rejects host-network
  flags, validates bounded relay/generation/route handoff, binds loopback before starting pinned
  sidecar+adapter, emits readiness, enforces deadline, and reaps both children. Focused runtime
  tests, fmt and clippy pass; full workspace tests previously passed. Remaining blocker:
  SandboxBackend still does not inject this executable into Bubblewrap or provide authenticated Unix
  relay FD/socket mount and actual sidecar forwarding/namespace attestation; binary intentionally
  fails closed when loopback unavailable. No host network, firewall, ambient ip, credentials, or
  unrelated AR changes.

- 2026-09-16T08:00:36+00:00: Live Bubblewrap qualification confirms rootless private loopback and
  bind-mounted 0600 Unix relay are viable; authorize implementation of SandboxBackend integration
  and real sidecar forwarding with no host-network sharing.

- 2026-09-16T08:01:15+00:00: Claimed by asb_ar1238_bwrap_relay_worker.

- 2026-09-16T08:03:31+00:00: Integrated SupervisorPlan into SandboxBackend: validates 0600 Unix
  relay socket, mounts it at /tmp/asb-replay-relay.sock after tmpfs, and launches runtime-owned
  supervisor with namespace-local relay args. Focused runtime tests and full workspace tests pass;
  clippy and rustdoc pass.

- 2026-09-16T08:04:17+00:00: Implemented SandboxBackend composition in signed commit d9f42ec:
  validates an existing private 0600 Unix relay socket, creates tmpfs /tmp before bind-mounting it
  at /tmp/asb-replay-relay.sock, and launches the in-tree supervisor with namespace-local relay
  arguments. Focused runtime 29 tests and full locked workspace tests pass; fmt, clippy, and rustdoc
  pass. Remaining blocker is executable packaging/installation and a real cassette sidecar protocol:
  /usr/bin/asb_loopback_supervisor must be supplied by the trusted runtime bundle, and the sidecar
  must forward authenticated HTTP over the mounted relay with readiness attestation and lifecycle
  tests. No host networking/firewall/ambient ip used.

- 2026-09-16T08:05:39+00:00: User-approved continuation: add and test the in-tree bounded loopback
  sidecar and integrate its relay mount; no host networking or global policy changes.

- 2026-09-16T08:05:42+00:00: Claimed by asb_ar1238_bwrap_relay_worker.
