---
{
  "branch": "feature/native-platform-lab",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0701",
    "AR-0103",
    "AR-0201",
    "AR-0401"
  ],
  "id": "AR-0703",
  "next_action": "Provision credential-isolated disposable booted Debian and openEuler x86_64/aarch64 qualification capacity with bounded cost and availability.",
  "owner": "",
  "plan": "../plans/AR-0703.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide genuine disposable native hosts for required Debian and openEuler platform qualification.",
  "task_revision": 1,
  "title": "Provision native platform qualification capacity",
  "updated_at": "2026-09-07T03:19:17+00:00",
  "worktree_key": "agent-systems-benchmark-native-platform-lab"
}
---
## AR-0703

Provide genuine disposable native hosts for required Debian and openEuler platform qualification.

This task was added after AR-0702 proved that the available development machine supplies only a
bare-metal Ubuntu x86_64 cell and that the public native-arm runner does not supply booted
openEuler or Debian kernel evidence. Containers, cross-builds and emulation cannot satisfy it.
