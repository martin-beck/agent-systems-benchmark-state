---
{
  "branch": "test/mockagents-executable-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:47:48+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-0896",
  "next_action": "Replace 97643044 with a same-tree same-parent signed merge commit carrying matching DCO trailer using exact force-with-lease, then verify fresh exact-main gates.",
  "observed_branch": "test/mockagents-executable-qualification",
  "observed_dirty": 0,
  "observed_head": "3f1de4106adf9ad6c34759638d70e9001709ab0a",
  "owner": "codex-longrun-mockagents-20260909",
  "plan": "../plans/AR-0896.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Post-merge DCO policy still rejects GitHub-generated merge; exact main merge boundary must be signed.",
  "task_revision": 27,
  "title": "Qualify the pinned MockAgents executable",
  "updated_at": "2026-09-09T10:20:42+00:00",
  "worktree_key": "agent-systems-benchmark-mockagents-executable-qualification"
}
---
## AR-0896

Qualify only MockAgents v0.5.0 as the candidate executable selected for further
consideration by AR-0890. This repair AR exists because AR-0888 retained all four
candidates as `untested`; it must not substitute README claims or the ASB-owned
synthetic fixture for black-box executable evidence.

- 2026-09-09T09:55:13+00:00: Promote dependency-ready MockAgents executable qualification for the
  development loop.

- 2026-09-09T09:55:19+00:00: Claimed by codex-longrun-mockagents-20260909.

- 2026-09-09T09:55:41+00:00: Recorded command exit 0; command argv SHA-256
  74fbdb117ae7b36fdab88f7db32e8f5c5cceb95c78e3ace34c70a2284134fb26.

- 2026-09-09T10:01:30+00:00: Material milestone: isolated worktree contains closed lock parser,
  bounded archive/license verifier, unprivileged loopback subprocess qualification, protocol probes,
  deterministic semantic hashes, public fixture evidence, and negative archive tests. The exact
  v0.5.0 linux-amd64 release passed the implemented checks. AR-0890 remains blocked; no support
  catalog or CI workflow was changed.

- 2026-09-09T10:01:52+00:00: Recorded command exit 0; command argv SHA-256
  3b63290ca600a5863bd3bbdbf734b37a74913861a7ed3a4ba258ed703676cee1.

- 2026-09-09T10:02:01+00:00: Recorded command exit 0; command argv SHA-256
  d3720a1eb1a6c27cf813d78255327f5faee356be69b97e4080bec4a9769d789e.

- 2026-09-09T10:02:16+00:00: Recorded command exit 0; command argv SHA-256
  06c97c3ac06498041b764894cd0d33f558c890057cf487c180d031982747e27e.

- 2026-09-09T10:02:48+00:00: Heartbeat by codex-longrun-mockagents-20260909.

- 2026-09-09T10:08:28+00:00: PR #115 merged to product main as
  004d87252b065679d80ca9674356b47146754528 after all 14 exact-head checks passed. Post-merge six
  required workflows are running. The implementation does not claim AR-0890 readiness; unsupported
  cases remain explicit.

- 2026-09-09T10:09:06+00:00: Failure evidence: post-merge Repository quality run 34338578572 reports
  merge commit 004d87252b065679d80ca9674356b47146754528 lacks a matching Signed-off-by trailer. No
  product defect was reported. Feature work is preempted pending reviewed DCO repair.

- 2026-09-09T10:09:19+00:00: Recorded command exit 128; command argv SHA-256
  f91ca3b3e311700665846b6ca8b811daee8ab63a18acb5e5d1731ab2565d026b.

- 2026-09-09T10:09:33+00:00: Recorded command exit 0; command argv SHA-256
  745a4502cf795709ed9fa3c1dc45358c99f5f22d61816554f43542ec2335b34e.

- 2026-09-09T10:09:48+00:00: Recorded command exit 0; command argv SHA-256
  10e83e4aa06382cea9a31bd494243d88251f94d9d30ea39b2ea38e9665990c05.

- 2026-09-09T10:11:27+00:00: Recorded command exit 0; command argv SHA-256
  d701ac9e9dcae31de5192b858c0615d3041aea41df2437bcde9a67acc9e0c9d5.

- 2026-09-09T10:11:47+00:00: Recorded command exit 0; command argv SHA-256
  fd9b2d02f542823387ed1643ed1121cba827b4dbdb29267a2708d10bb2797cd7.

- 2026-09-09T10:12:35+00:00: Policy failure 34338751615 showed the Signed-off-by email must match
  configured commit identity martin.beck2@gmx.de. Replaced c72aa306 with signed commit 82d146d5e,
  force-with-lease from the declared branch old head, preserving the same tree and repair scope.

- 2026-09-09T10:12:59+00:00: Recorded command exit 0; command argv SHA-256
  5f9fda1e7ce76a3560f1448a43040fa4972789f2eca3049ad2d0d28d53ddc547.

- 2026-09-09T10:13:15+00:00: Recorded command exit 0; command argv SHA-256
  fcea23512f1ffe77af4a5673653679a3fdb65b6a20ee819ac25f020e63b5a34f.

- 2026-09-09T10:13:33+00:00: Second policy failure showed the first repair commit remained in PR
  ancestry. Rebuilt the follow-up directly on merge 004d87252b065679d80ca9674356b47146754528 as
  signed f25fb319 with matching martin.beck2@gmx.de trailer, and force-with-lease updated PR #116
  from 82d146d.

- 2026-09-09T10:19:40+00:00: PR #116 corrected the merge-boundary DCO failure and all 14 exact-head
  checks passed. It merged as 97643044ba8d782460f633c4852ba832207e9fcc. Six fresh exact-main
  post-merge workflows are active; feature work remains preempted until they settle.

- 2026-09-09T10:20:29+00:00: Failure evidence: Repository quality run 34339582534 reports merge
  commit 97643044ba8d782460f633c4852ba832207e9fcc lacks a matching Signed-off-by trailer despite the
  signed PR follow-up. The policy range includes the GitHub-generated merge commit, so a
  same-tree/same-parent signed merge replacement is required; feature work remains preempted.

- 2026-09-09T10:20:42+00:00: Recorded command exit 0; command argv SHA-256
  faadf5c5a088686d124c05184fea96ad58b6dca798d0d63e97bfb0fa8134ca3d.
