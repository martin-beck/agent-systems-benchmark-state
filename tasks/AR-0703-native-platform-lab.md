---
{
  "branch": "feature/native-platform-lab",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T12:04:33+00:00",
  "depends_on": [
    "AR-0701",
    "AR-0103",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0703",
  "next_action": "Provision credential-isolated disposable booted Debian and openEuler x86_64/aarch64 qualification capacity with bounded cost and availability.",
  "observed_branch": "feature/native-platform-lab",
  "observed_dirty": 0,
  "observed_head": "b1669203308db5a75fee1e78a45c6fc8e71f17ce",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0703.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide genuine disposable native hosts for required Debian and openEuler platform qualification.",
  "task_revision": 4,
  "title": "Provision native platform qualification capacity",
  "updated_at": "2026-09-07T10:34:46+00:00",
  "worktree_key": "agent-systems-benchmark-native-platform-lab"
}
---
## AR-0703

Provide genuine disposable native hosts for required Debian and openEuler platform qualification.

This task was added after AR-0702 proved that the available development machine supplies only a
bare-metal Ubuntu x86_64 cell and that the public native-arm runner does not supply booted
openEuler or Debian kernel evidence. Containers, cross-builds and emulation cannot satisfy it.

- 2026-09-07T10:34:30+00:00: Dependencies AR-0701, AR-0103, AR-0201, and AR-0401 are durably done;
  branch, remote ref, and declared worktree are absent. Promote for fail-closed native capacity
  feasibility and provider availability audit without spend or emulation.

- 2026-09-07T10:34:33+00:00: Claimed by quality-20260906.
