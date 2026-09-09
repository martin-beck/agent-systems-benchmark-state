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
  "next_action": "Obtain explicit provider/account and cost authorization, least-privilege external credentials, quotas, and four genuine disposable Debian 13.6/openEuler 24.03 LTS-SP2 x86_64/aarch64 hosts; then implement reservation/provision/collect/destroy evidence without emulation.",
  "observed_branch": "feature/native-platform-lab",
  "observed_dirty": 0,
  "observed_head": "b1669203308db5a75fee1e78a45c6fc8e71f17ce",
  "owner": "",
  "plan": "../plans/AR-0703.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide genuine disposable native hosts for required Debian and openEuler platform qualification.",
  "task_revision": 8,
  "title": "Provision native platform qualification capacity",
  "updated_at": "2026-09-09T10:52:47+00:00",
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

- 2026-09-07T10:34:48+00:00: Recorded command exit 0; command argv SHA-256
  5cf8f13c336b7864586e3daa48e5aa4818767fb7d2ea53803b4e5bd5b1131d08.

- 2026-09-07T10:36:59+00:00: Fresh feasibility audit made no provisioning or spend effects.
  Repository Actions runner API reports zero registered self-hosted runners; organization
  runner/custom-image administration is unavailable for this user-owned repository. The only local
  native capacity remains bare-metal Ubuntu 24.04 x86_64; no provider CLI, provider credential
  environment, or provider configuration directory exists under /srv/data/projects. GitHub standard
  hosted Linux runners provide Ubuntu x86_64/aarch64 only, not booted Debian/openEuler. Official
  Debian 13 cloud AMIs and openEuler 24.03 LTS-SP2 x86_64/aarch64 release images establish image
  feasibility but not authorized native capacity. No cost authorization, cloud account, quotas,
  billing boundary, or credential-injection/revocation path is available, so all four required
  native provision-run-destroy cycles are blocked fail-closed. One initial read-only audit shell had
  a syntax failure after the runner query and made no mutation; a corrected audit completed.

- 2026-09-07T10:37:02+00:00: Released blocked without product changes or capacity claims. Exact
  blocker: no authorized credential-isolated provider/account, cost ceiling, quota/billing
  visibility, or genuine disposable Debian 13.6 and openEuler 24.03 LTS-SP2 x86_64/aarch64 hosts.
  Resume only after coordinator supplies explicit spend authorization and least-privilege capacity;
  containers, cross-builds, QEMU/TCG, and current Ubuntu hosted runners remain non-evidence.

- 2026-09-09T10:52:47+00:00: Native ARM64 capacity is optional future qualification and no longer
  blocks AR-0702 or other development.
