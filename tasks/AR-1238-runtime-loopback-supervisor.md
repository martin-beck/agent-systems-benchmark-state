---
{
  "branch": "feature/ar-1238-runtime-loopback-supervisor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T09:53:11+00:00",
  "depends_on": [
    "AR-1100",
    "AR-1231"
  ],
  "id": "AR-1238",
  "next_action": "Implement and qualify a pinned in-tree supervisor that composes a private user/network namespace, raises only its own loopback, mounts the per-launch Unix relay, and supervises sidecar plus adapter without host networking.",
  "observed_branch": "feature/ar-1238-runtime-loopback-supervisor",
  "observed_dirty": 0,
  "observed_head": "6fba189fd839a954d2e0724f696114b607242cb0",
  "owner": "asb_ar1238_supervisor_worker",
  "plan": "../plans/AR-1238.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the runtime-owned private-namespace supervisor for loopback replay.",
  "task_revision": 7,
  "title": "Runtime-owned loopback supervisor",
  "updated_at": "2026-09-16T07:53:11+00:00",
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
