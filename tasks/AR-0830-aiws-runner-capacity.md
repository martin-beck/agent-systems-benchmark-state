---
{
  "branch": "feature/development-host-runner-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T08:51:21+00:00",
  "depends_on": [
    "AR-0002",
    "AR-0003",
    "AR-0103"
  ],
  "id": "AR-0830",
  "next_action": "Harden reset against concurrent path substitution, add service registration and lifecycle controls, and extend lease/isolation/fault negatives before immutable review.",
  "observed_branch": "feature/development-host-runner-capacity",
  "observed_dirty": 0,
  "observed_head": "7c7f1e0f711398907c2094d92357f7196154d03f",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0830.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add isolated, disposable ASB self-hosted CI capacity on development host beside existing runners.",
  "task_revision": 27,
  "title": "Provision hardened development host ASB runner capacity",
  "updated_at": "2026-09-07T05:52:31+00:00",
  "worktree_key": "agent-systems-benchmark-development-host-runner-capacity"
}
---
## AR-0830

Provision isolated, disposable ASB self-hosted CI capacity on development host without modifying existing
Agent Relay runners.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T05:39:21+00:00: Promote isolated development-host ASB runner capacity after dependency
  and privacy review; implementation remains gated by qualification and trusted-only routing.

- 2026-09-07T05:41:47+00:00: Claimed by contracts-20260906.

- 2026-09-07T05:43:25+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T05:43:58+00:00: Recorded command exit 0; command argv SHA-256
  2afda77a52dc29239748ea4b7ff1f8ef37c6b736e0e38ee2314e6ec133848068.

- 2026-09-07T05:44:14+00:00: Recorded command exit 0; command argv SHA-256
  3f870e1e32d1fa23108b3be93a49526ba99abd621e6d435ac2983c2dcc55ca4d.

- 2026-09-07T05:44:26+00:00: Repaired the runner plan after audit: all runner state is constrained
  beneath the configured /srv/data/projects root; default labels are forbidden; only a protected
  manual qualification canary is permitted before independent qualification and separate activation;
  public-PR caches are trust-separated; names/logs are privacy-safe; disk/network/service fault
  injection is bounded and no host reboot is claimed without separate authorization. The initial
  wrapped apply_patch invocation exited 2 because wrapper stdin was not forwarded; the
  explicit-argument retry applied the exact diff, then signed+DCO state commit 4cf79b71 committed it
  and wrapper evidence commit cf5aa8e7 recorded success. AR-0703 is not an AR-0830 dependency;
  removal from AR-0832 requires coordinator-owned metadata serialization.

- 2026-09-07T05:44:28+00:00: Recorded command exit 0; command argv SHA-256
  8c3de4fb198c6929d0013603bbfa10e6c71d486a4015ae1d75e22776de8280e3.

- 2026-09-07T05:44:52+00:00: Recorded command exit 0; command argv SHA-256
  4cdf4642873857f04ddcd4780ccfdc560a9b8dd1b12934d1e36e41de2043ad79.

- 2026-09-07T05:45:31+00:00: Recorded command exit 0; command argv SHA-256
  c1a59eac5d0e4172e8e3aa6a06b0eecf220392778b97e034451e721e30ef82fb.

- 2026-09-07T05:48:07+00:00: Recorded command exit 0; command argv SHA-256
  b9d192e3ade062eb927a23986cc9c1af98d69c0eb4a5bee22985e4b25d117a36.

- 2026-09-07T05:48:12+00:00: Lease expired at 06:11Z; coordinator verified no active implementation
  process, no dirty worktree, no product checkpoint, and preserved inventory/plan state before
  reopening.

- 2026-09-07T05:48:39+00:00: Claimed by contracts-20260906.

- 2026-09-07T05:49:08+00:00: Recorded command exit 0; command argv SHA-256
  ede89728daa684df245aeaccdfc55f62fb79cfd0f9063d75a1c770c5dae2b3b0.

- 2026-09-07T05:49:14+00:00: Recorded command exit 0; command argv SHA-256
  8f23f601379b72d8f067ac81429ee194d621fb89d0a75ccd468db04d4126e453.

- 2026-09-07T05:49:19+00:00: Recorded command exit 0; command argv SHA-256
  0d4e725070c786dcd716ac191b052c3560298b66fe7f828cc3a95c1859304a8f.

- 2026-09-07T05:49:34+00:00: Recorded command exit 0; command argv SHA-256
  169c0474f8fa47f461cddd7801e492fec1df6fd6855f4881346a41cf4a757c24.

- 2026-09-07T05:50:20+00:00: Lease expired with no active runner implementation process; product
  worktree still has only untracked files and no checkpoint. Preserved untracked work for worker
  reinspection before any reclaim.

- 2026-09-07T05:51:21+00:00: Claimed by contracts-20260906.

- 2026-09-07T05:51:34+00:00: Recorded command exit 0; command argv SHA-256
  4a1cb90cf50761f520b8359565713f239c0d26fcf63bebd8ea93b66a9fa668d9.

- 2026-09-07T05:51:55+00:00: Recorded command exit 0; command argv SHA-256
  725cdae2a71404cec2cac380b0140eb027970a6a63a9782293d8960c31bf4f18.

- 2026-09-07T05:52:02+00:00: Recorded command exit 0; command argv SHA-256
  67f37f4e768534fc9bda5727eaaf625b4edc85bbbc059dcb20575b589da091db.

- 2026-09-07T05:52:31+00:00: Focused signed+DCO product checkpoint
  7c7f1e0f711398907c2094d92357f7196154d03f adds isolated setup, health, reset and runner-script
  tests. Wrapper-run sh -n, positive health/reset, symlink rejection, expired-lease rejection,
  generic-label rejection, source privacy grep, and repository core-residue check passed. Worktree
  is clean; ShellCheck and shfmt remain unavailable on the host and must be addressed by pinned CI
  or explicit tooling provision.
