---
{
  "branch": "feature/ar-1308-full-exhaustive-qemu-capacity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1308",
  "next_action": "Promote after AR-1304 review; provision disposable x86_64 QEMU capacity and qualify the exact AR-1307 full-exhaustive liveness run without changing its 3G/3G contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1308.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide governed disposable capacity for exact full-exhaustive TLC liveness qualification.",
  "task_revision": 2,
  "title": "Full-exhaustive QEMU capacity qualification",
  "updated_at": "2026-09-18T13:45:32+00:00",
  "worktree_key": "agent-systems-benchmark-asb-ar-1308-full-exhaustive-qemu-capacity"
}
---

# AR-1308

AR-1307's exact-head full-exhaustive qualification reached approximately 45.77M generated and
37.99M distinct states, then failed because Java ran out of memory during liveness checking under
the existing 3G memory and 3G swap contract. This follow-on owns only the disposable capacity and
evidence needed to rerun that exact qualification truthfully; it must not weaken AR-1307's limits,
model, admission, or attestation gates.

The dependency on AR-1304 provides the reviewed required-tier QEMU runner and user-bus foundation.
The run must consume the exact signed AR-1307 head and pinned TLC/JDK/model inputs, without changing
source code or treating a capacity failure as a model result.


- 2026-09-18T13:45:32+00:00: AR-1304 is done; promote capacity follow-on to open for independent
  worker assignment. Preserve AR-1307 3G/3G contract and exact-head dependency.
