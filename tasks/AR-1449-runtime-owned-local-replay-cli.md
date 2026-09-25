---
{
  "branch": "feature/ar-1449-runtime-owned-local-replay-cli",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T19:55:07+00:00",
  "depends_on": [
    "AR-1443",
    "AR-1448"
  ],
  "id": "AR-1449",
  "next_action": "Implement and verify a runtime-owned local replay authority acquisition path for the ordinary ASB CLI, then integrate it into AR-1338 without synthetic authority or native-host gating.",
  "observed_branch": "feature/ar-1449-runtime-owned-local-replay-cli",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1449-replay-luna56",
  "plan": "../plans/AR-1449.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide fail-closed runtime-owned local replay authority for the guided CLI wrapper.",
  "task_revision": 2,
  "title": "Runtime-owned local replay CLI authority",
  "updated_at": "2026-09-25T16:55:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1449-runtime-owned-local-replay-cli"
}
---

AR-1338 exposes the guided replay route, but the normal argument-only CLI intentionally receives no ReplayLaunchAuthority. This successor must provide a runtime-owned local deterministic replay acquisition boundary using the existing AR-1448 source and AR-1443 replay contracts.

Requirements:
- derive cassette identity from the validated cassette before any authority issuance;
- acquire bounded private relay, benchmark lease, network-denied sandbox input and runtime attestation inside the runtime boundary;
- inject one-shot authority into the ordinary CLI without accepting caller-built authority or secret bytes;
- preserve strict replay, cancellation, teardown, path confinement, offline operation and direct or alternate egress denial;
- provide positive and hostile tests for stale, copied, mismatched and unavailable authority;
- use local deterministic fixtures or LiteLLM-compatible mocks only; external providers and native hosts are not required.

Do not weaken AR-1448 or make live provider reachability a prerequisite.

- 2026-09-25T16:55:07+00:00: Claimed by ar1449-replay-luna56.
