---
{
  "branch": "feature/csb-execution-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T09:23:46+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0104"
  ],
  "id": "AR-0603",
  "next_action": "Acquire and verify an exact public CSB source graph, then specify its bounded subprocess and containment contract.",
  "observed_branch": "feature/csb-execution-assurance",
  "observed_dirty": 2,
  "observed_head": "814397f8f74971589aa02b13da12485169db3e2e",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0603.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Pin and audit CSB provenance and prove a bounded sandboxed execution, cancellation, recovery, artifact, and privacy boundary.",
  "task_revision": 14,
  "title": "Establish pinned CSB execution and conformance boundary",
  "updated_at": "2026-09-07T06:24:53+00:00",
  "worktree_key": "agent-systems-benchmark-csb-execution-assurance"
}
---
## AR-0603

Pin and license-audit one exact public CSB revision and build graph, expose only a bounded
version-negotiated subprocess protocol, and prove containment, cancellation, recovery, artifact,
path, and privacy behavior before ASB may invoke CSB.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T06:07:58+00:00: Coordinator verified AR-0603 dependencies, ownership isolation, and
  user authorization; promote for contracts worker.

- 2026-09-07T06:08:42+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:09:03+00:00: Recorded command exit 0; command argv SHA-256
  456777cb1fc425f81a3c32ba739ecc38b8819118384de19f77b6dbf74d105241.

- 2026-09-07T06:09:47+00:00: Recorded command exit 0; command argv SHA-256
  dbd573af68275a803470007808b024658cc936b348b7eaa681f44480393da696.

- 2026-09-07T06:10:24+00:00: Recorded command exit 0; command argv SHA-256
  ab3f40c0f399fa2c95c83f81150268c71c39dd4fc742b49a5ddd8efb0011ca87.

- 2026-09-07T06:11:04+00:00: Released before product mutation so the newly authorized runner
  activation can take priority. Preserved external research clone
  /srv/data/projects/.asb-local/csb-ar0603-source at official https://github.com/martin-beck/CSB.git
  commit d577c5249501b29e33a87524a677a101477d5579, tree 97d08b39026f7c7d3e6f748b26a20e819a92184f,
  release message v0.4.0, root MIT license, and declared submodule commits 41fee1f9 FlameGraph,
  cebe6d15 benchkit, 49741843 inferno, 44df4dbc syzkaller (not initialized yet). requirements.txt
  remains incompletely pinned, so offline reproducibility is unproven. One checkout attempt used an
  invalid relative handoffctl path and caused no mutation; the absolute wrapped retry succeeded.
  Declared product worktree remains clean at base 814397f with no AR-0603 files. Next action:
  re-claim, initialize and license-audit the complete source graph, then implement the bounded
  version-negotiated subprocess contract under the existing Cargo/schema fence.

- 2026-09-07T06:12:01+00:00: Claimed by contracts-20260906.

- 2026-09-07T06:13:08+00:00: Recorded command exit 0; command argv SHA-256
  8f6d165f368e612e351299eb362c6e5d00629ad90b3554116d933dffd379caae.

- 2026-09-07T06:13:13+00:00: Recorded command exit 0; command argv SHA-256
  de1523e77860b7acb15de2a930a1be5dba0af31cea316857117658c58edcbac3.

- 2026-09-07T06:13:40+00:00: Priority switch to authorized AR-0830 runner repair before product
  mutation. Preserved fully initialized official CSB graph at
  /srv/data/projects/.asb-local/csb-ar0603-source: root d577c524/tree 97d08b39; FlameGraph
  41fee1f9/tree 85d36fd0; benchkit cebe6d15/tree d82f2d7c; inferno 49741843/tree 3e271fe6; nested
  FlameGraph 57207afb/tree 32a15a83; syzkaller 44df4dbc/tree 9586b54e. Root, benchkit, inferno and
  syzkaller licenses located; FlameGraph license provenance still requires inspection. Root
  requirements remain mostly floating and offline reproducibility unproven. Wrapped submodule
  command completed, while its evidence push reported a stale expected ref although remote already
  contained the exact commit; reconcile reached a8a440c5. Declared product worktree remains clean at
  814397f. Next action: license/dependency inventory and bounded subprocess contract after reclaim.

- 2026-09-07T06:23:46+00:00: Claimed by contracts-20260906.
