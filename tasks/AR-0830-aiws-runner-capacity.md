---
{
  "branch": "feature/development-host-runner-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T08:54:45+00:00",
  "depends_on": [
    "AR-0002",
    "AR-0003",
    "AR-0103"
  ],
  "id": "AR-0830",
  "next_action": "Obtain independent review of exact cdf18c6; live service identity, one-job ephemeral re-registration, protected canary and GitHub-side label proof remain gated on an authorized secret/admin boundary.",
  "observed_branch": "feature/development-host-runner-capacity",
  "observed_dirty": 2,
  "observed_head": "cdf18c6bf11b4f9cf36f3d5d20396b935001e176",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0830.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add isolated, disposable ASB self-hosted CI capacity on development host beside existing runners.",
  "task_revision": 50,
  "title": "Provision hardened development host ASB runner capacity",
  "updated_at": "2026-09-07T06:01:08+00:00",
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

- 2026-09-07T05:53:56+00:00: Coordinator audit at 07:53Z found no active ASB runner
  implementation/test process and no successor since 7c7f1e0; preserve exact clean product
  checkpoint and reopen for immediate reassignment.

- 2026-09-07T05:54:45+00:00: Claimed by contracts-20260906.

- 2026-09-07T05:55:20+00:00: Recorded command exit 0; command argv SHA-256
  9ac6c2e106c0c3008b4e32c5e9c83063df907bb77844288ed8fdb9178ed1ec9d.

- 2026-09-07T05:55:42+00:00: Recorded command exit 0; command argv SHA-256
  3c97331e21d9f762268b3f87598a189141713c71c4e536c47403ea8cd1599a91.

- 2026-09-07T05:55:54+00:00: Recorded command exit 0; command argv SHA-256
  33695ba02531ef9d46afdbeeceb7e44ef808daf379a0d7113cef9a7fa5152002.

- 2026-09-07T05:56:00+00:00: Recorded command exit 0; command argv SHA-256
  49b393ff70b691b048563f264a0d8aeb9b013a77dc60eb6b9cfefac7b8f76bf9.

- 2026-09-07T05:56:14+00:00: Signed+DCO successor 40d54709e923172d6953d212190c95c0b103df84 hardens
  reset with a nonblocking 0600 lock, atomic same-filesystem quarantine before replacement, repeated
  symlink/type validation, and bounded quarantine deletion. Health now rejects permissive
  lease/manifest modes. Added malformed, expired, permissive and concurrently locked lease negatives
  plus lifecycle documentation requiring pinned ephemeral registration, no default labels,
  secret-out-of-band registration, dedicated identity, stop confirmation, and AR-0832 qualification
  before activation. Wrapper-run sh -n, focused positive/negative tests, diff check, privacy grep
  and core-residue audit passed; worktree is clean.

- 2026-09-07T05:57:46+00:00: Independent review BLOCKS 40d5470 as a final candidate. common.sh
  accepts any canonical absolute ASB_STORAGE_ROOT rather than proving it resolves beneath
  /srv/data/projects and does not enforce same-filesystem placement. Three separate custom labels
  cannot enforce complete-set-only routing: GitHub matches every label requested by a job, so a job
  requesting any subset can still select this runner; use one composite versioned label with
  --no-default-labels. setup.sh rejects an existing verified installation, contrary to idempotence
  acceptance. No dedicated service identity, restart/reconnect, orphan/uninstall, protected canary,
  or GitHub-side exact-label evidence exists yet. Official GitHub documentation confirms ephemeral
  runners deregister after one job, requiring external lifecycle automation, and recommends external
  diagnostic log retention; this host has no authorized registration token/admin boundary in scope,
  so live provisioning must remain blocked rather than handling secrets unsafely.

- 2026-09-07T05:58:00+00:00: Recorded command exit 0; command argv SHA-256
  169c0474f8fa47f461cddd7801e492fec1df6fd6855f4881346a41cf4a757c24.

- 2026-09-07T05:58:05+00:00: Recorded command exit 0; command argv SHA-256
  0d4e725070c786dcd716ac191b052c3560298b66fe7f828cc3a95c1859304a8f.

- 2026-09-07T05:58:43+00:00: Recorded command exit 0; command argv SHA-256
  98215f058339ccb9d95ba73438ee78828c29884fa0c3d2cbce837467f50a173a.

- 2026-09-07T05:58:59+00:00: Recorded command exit 0; command argv SHA-256
  6f9044834e816b8ebd1a73cef127b64e653bbdba70db88c3d58e7ec056498ef0.

- 2026-09-07T05:59:22+00:00: Recorded command exit 0; command argv SHA-256
  7564b25547d7b07317120bb2e413e0479f852823ff1f144a899e5d5603b42920.

- 2026-09-07T05:59:33+00:00: Recorded command exit 0; command argv SHA-256
  24d128b0afe3e840487a099dd4a17e25d86237f11b8fe037dd137937dc3989a1.

- 2026-09-07T05:59:40+00:00: Recorded command exit 0; command argv SHA-256
  0189f002b3e4d8e3fdc8477fc1f5f3c6808bca60510fbae12ddfa2347fda1ed7.

- 2026-09-07T05:59:55+00:00: Signed+DCO successor cdf18c6bf11b4f9cf36f3d5d20396b935001e176 closes
  the locally repairable review blockers: storage roots must resolve beneath /srv/data/projects,
  runner parent/root devices must equal the configured storage device, one indivisible versioned
  capability label prevents partial-label routing, and repeated setup succeeds only for an exact
  private manifest and required entry points. Added idempotence and outside-storage negatives
  without creating any material outside /srv/data/projects. Wrapper-run sh -n, focused suite, diff
  check, privacy scan, worktree residue and forbidden /srv/data/asb-ci-runners absence checks
  passed. Live registration remains unattempted because no authorized registration token/admin
  boundary is available.

- 2026-09-07T06:01:03+00:00: Recorded command exit 0; command argv SHA-256
  a508f868166d6884c4fe9f1613affbc839a82243e714b8e4615f5ade482e6437.

- 2026-09-07T06:01:08+00:00: Recorded command exit 0; command argv SHA-256
  1c02c62de1a0ffa04e1de97412203f67fac85dfbcf961ee324b3e303a8203b08.
