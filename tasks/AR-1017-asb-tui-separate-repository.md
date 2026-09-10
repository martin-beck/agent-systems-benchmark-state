---
{
  "branch": "feature/asb-tui-separate-repository",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T11:57:32+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0806",
    "AR-0851"
  ],
  "id": "AR-1017",
  "next_action": "Create the standalone asb-tui repository boundary and stable CLI/JSON protocol contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1017.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Build asb-tui as an isolated optional repository and extension.",
  "task_revision": 20,
  "title": "Create the standalone asb-tui extension repository",
  "updated_at": "2026-09-10T09:04:21+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-separate-repository"
}
---
Create a separate public asb-tui repository containing the optional terminal frontend only. Consume
the latest immutable releases of `martin-beck/agent-workflow-coordinator` and
`martin-beck/agent-workflow-quality`, recording exact tags/commits, artifact digests, signatures,
licenses, and compatibility in a lock manifest. Define a versioned, capability-negotiated CLI/JSON
protocol to the installed ASB program; do not share Cargo
workspace manifests, provider code, benchmark execution, or private coordination history.

Acceptance criteria: isolated repository and worktree, latest-release discovery that rejects mutable
or unsigned inputs, pinned coordinator/quality/Ratatui/Crossterm inputs, explicit
unverified-extension classification, protocol compatibility matrix, sanitized SBOM/license/provenance
metadata, and tests proving the main benchmark runs independently when the TUI is absent.

- 2026-09-10T08:55:59+00:00: Promote standalone asb-tui extension boundary after dependency
  preflight.

- 2026-09-10T08:57:32+00:00: Claimed by contracts_20260906.

- 2026-09-10T08:58:06+00:00: Recorded command exit 0; command argv SHA-256
  42a502c9a2ee9cf5bea7b8a16c82cd4845a0f513fde9cfb55f13095b40b120a4.

- 2026-09-10T08:58:20+00:00: Recorded command exit 0; command argv SHA-256
  b0ed9dcaecd924d95cf0a33d420a9fe950657c7e20599add0036d47e052af603.

- 2026-09-10T08:58:39+00:00: Recorded command exit 0; command argv SHA-256
  92dd972edd1a176a56751859e55d72e93598cd4098694b248effb76fa55a9631.

- 2026-09-10T08:58:53+00:00: Recorded command exit 0; command argv SHA-256
  b93e4b1ba3ebf72928cac6689e8562cc6c1e940c8a1759dc1b3e981716383910.

- 2026-09-10T08:59:24+00:00: Recorded command exit 0; command argv SHA-256
  039b3d941d87ac86cad296adfafbdc9796ba83101c5caaf4931819d9a8882cd1.

- 2026-09-10T08:59:39+00:00: Recorded command exit 0; command argv SHA-256
  32a88ae86cc5fbf7432fbe927dceb0991be96a2d887d97236eb13974b5a4f2ce.

- 2026-09-10T09:00:15+00:00: Recorded command exit 0; command argv SHA-256
  8263cda2fb83351a7edb6515297ece9ab9662d798e47289ddc1c507d64c188d2.

- 2026-09-10T09:00:30+00:00: Recorded command exit 0; command argv SHA-256
  ef982609348a8ad8faf8e30be27203612be964d8c882149e3c277bc3badf634d.

- 2026-09-10T09:00:44+00:00: Recorded command exit 0; command argv SHA-256
  40749e3991b223ead911d8e01cf832c92e28f2051609c742edf99f60e891754f.

- 2026-09-10T09:01:01+00:00: Recorded command exit 0; command argv SHA-256
  b660253513b6f1a7d329e6db0e7ee94ff4d6f90e47787e902b4a905fdfbd67f9.

- 2026-09-10T09:01:17+00:00: Recorded command exit 0; command argv SHA-256
  df08122c9f0ffc13e535e5b90e79ec634cbeb03bd8229cc98ab78a02678a01c8.

- 2026-09-10T09:01:33+00:00: Recorded command exit 0; command argv SHA-256
  09b5ebfd4677044848b7f66313a4fc3049cead1179f01044fa2f84f4e1c8a61e.

- 2026-09-10T09:01:49+00:00: Recorded command exit 0; command argv SHA-256
  bcd330af3d24dd224d6bc8afc73e1dd9e2e849a9b3054cf9e7bf44e80a3f8d2f.

- 2026-09-10T09:02:02+00:00: Recorded command exit 0; command argv SHA-256
  0d0e6a324b1df14543667b5d7cbcfe87e720cba4492e30367e40378558461177.

- 2026-09-10T09:02:22+00:00: Recorded command exit 0; command argv SHA-256
  12b49793e1aea457d66ae255f5fb905f39de3448c982ff569206380867b9c386.

- 2026-09-10T09:03:55+00:00: Recorded command exit 0; command argv SHA-256
  af44f955b3bb5ea94a585a4edb54fb4f496e8134f5b166b115d291c267f22083.

- 2026-09-10T09:04:21+00:00: Recorded command exit 0; command argv SHA-256
  f268d9008f582b67afa8d9632b4a0268a4826e525c5a3aac343cf9cb80370703.
