---
{
  "branch": "fix/tmux-live-fixture-isolation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1060",
  "next_action": "Create the isolated asb-tui worktree at exact main 69fecc01 and serialize only the five live tmux fixtures without changing authentication or product behavior.",
  "owner": "",
  "plan": "../plans/AR-1060.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Diagnose and isolate concurrent trusted tmux fixture contention.",
  "task_revision": 1,
  "title": "Isolate concurrent trusted tmux fixtures",
  "updated_at": "2026-09-11T05:29:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-live-fixture-isolation"
}
---

Exact-main Trusted run `34565894753` failed all five live tmux fixtures under the default-parallel
test binary after AR-1058 exposed `socket_connect_rejected` and `server_before_unavailable` stages.
Test process-local serialization is the next bounded experiment. Authentication, cleanup and all
product/UI behavior remain unchanged.
