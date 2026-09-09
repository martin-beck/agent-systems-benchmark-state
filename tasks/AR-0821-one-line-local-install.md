---
{
  "branch": "feature/one-line-local-install",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T08:37:19+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0820"
  ],
  "id": "AR-0821",
  "next_action": "Create the missing declared worktree from exact origin/main, then implement and test the guided installation workflow.",
  "observed_branch": "feature/one-line-local-install",
  "observed_dirty": 3,
  "observed_head": "096dc4f275c05ad81772f443b6f22dddfb92da3d",
  "owner": "codex-longrun-one-line-install-20260909",
  "plan": "../plans/AR-0821.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Turn a single documented command into a safe guided local ASB and TUI first run.",
  "task_revision": 19,
  "title": "Add guided one-line local installation",
  "updated_at": "2026-09-09T06:38:20+00:00",
  "worktree_key": "agent-systems-benchmark-one-line-install"
}
---

## AR-0821

Turn a single documented command into a safe guided local ASB and TUI first run.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T06:29:46+00:00: Dependencies AR-0803, AR-0804, AR-0805, and AR-0820 are released done;
  promote guided one-line installation as the next actionable P1 track. AR-0704 remains
  authorization-gated and AR-0832 remains native-capacity-gated.

- 2026-09-09T06:29:52+00:00: Claimed by codex-longrun-one-line-install-20260909.

- 2026-09-09T06:29:58+00:00: Heartbeat by codex-longrun-one-line-install-20260909.

- 2026-09-09T06:30:11+00:00: Recorded command exit 1; command argv SHA-256
  78d7942e237f6cd1e3138a4ba81d7a545221768e49381e07ac9757d8363bdf9c.

- 2026-09-09T06:30:27+00:00: First worktree observation failed: declared path
  /srv/data/projects/agent-systems-benchmark-one-line-install was absent and no matching live
  worktree was listed. No product mutation occurred; creating the declared isolated worktree is
  required before implementation.

- 2026-09-09T06:30:30+00:00: Recorded command exit 0; command argv SHA-256
  25e5fe5d71720f64e877ee7a599da60d2c9f070238bca30155d0e145bc6c6aed.

- 2026-09-09T06:33:26+00:00: Recorded command exit 0; command argv SHA-256
  ed7cb040e8c2d311e974dd246480021afeb9270d236292f6e1847e3077c19c9c.

- 2026-09-09T06:33:45+00:00: Recorded command exit 0; command argv SHA-256
  744f24a82da354c12ef3776f86a226138471b2b75d889567fc1577299668c27d.

- 2026-09-09T06:34:50+00:00: Recorded command exit 1; command argv SHA-256
  ed7cb040e8c2d311e974dd246480021afeb9270d236292f6e1847e3077c19c9c.

- 2026-09-09T06:35:15+00:00: Recorded command exit 0; command argv SHA-256
  08e54d0c3c663fc8015792d5d22227bdd8b4f0d9a4470c91e06e804d2b6f9e5c.

- 2026-09-09T06:36:20+00:00: Recorded command exit 0; command argv SHA-256
  08e54d0c3c663fc8015792d5d22227bdd8b4f0d9a4470c91e06e804d2b6f9e5c.

- 2026-09-09T06:37:19+00:00: Heartbeat by codex-longrun-one-line-install-20260909.

- 2026-09-09T06:37:22+00:00: Recorded command exit 127; command argv SHA-256
  92d0408a8b48f85efe278a5de0177c07e27f4e5c720c49246d93156cdeffa01e.

- 2026-09-09T06:37:49+00:00: Recorded command exit 0; command argv SHA-256
  b14c6dbd1fb3757f91d1171cd5d89ad807625c5599573eda1beee66d21586559.

- 2026-09-09T06:38:04+00:00: Recorded command exit 0; command argv SHA-256
  a78ff073484658b9bc27db985fb97ff1e6042f90b0ea8d8c1e3a33353dd6c97c.

- 2026-09-09T06:38:20+00:00: Recorded command exit 0; command argv SHA-256
  7934aa9a0438ca3b46449253756d91b429cb698a5b3630b5066368a784c1a422.
