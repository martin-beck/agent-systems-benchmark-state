---
{
  "branch": "recovery/ar-1815-provenance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1815",
  "next_action": "Exact merge e57982a is published. Repository quality attempt 4 is in progress after attempt 3 non-reproducible source_checkout Err(Unavailable); monitor attempt 4 and all remaining exact-main workflows to terminal-success before receipt/release.",
  "observed_branch": "recovery/ar-1815-provenance",
  "observed_dirty": 0,
  "observed_head": "ab4f4c6a81f543e049759d199cca675c7370a1dc",
  "owner": "",
  "plan": "../plans/AR-1815-protected-main-merge-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:7b085cf88dca04871a16632551b51f2ced70c2c3af263c8354fed143f0a1b512",
    "evidence_ref": "quality/AR-1815-protected-main-recovery-postmerge-receipt.txt",
    "spec_ref": "specs/AR-1815.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1815.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Recover protected-main merge provenance without rewriting the preserved GitHub merge.",
  "task_revision": 40,
  "title": "Protected-main signed merge recovery",
  "updated_at": "2026-10-12T12:25:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1815-provenance"
}
---

AR-1815 is the narrowly scoped successor for the exact-main failures on
AR-1805/PR #608. Preserve merge `15c80511`; recover only through the local
signed integration path. Do not weaken gates, rewrite history, force-push, or
introduce a TLC/model-check dependency for development.


- 2026-10-12T11:38:40+00:00: Claimed by ar1805_postmerge_repair.

- 2026-10-12T11:40:17+00:00: Bound worktree agent-systems-benchmark-ar-1815-provenance on branch
  recovery/ar-1815-provenance.

- 2026-10-12T11:40:37+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:40:47+00:00: Recorded command exit 0; command argv SHA-256
  96a0af41a541f5236a5894e26c9eb7ff32fa914aac46bb58bd7dabecaaa5c33e.

- 2026-10-12T11:41:12+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:41:16+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-12T11:41:20+00:00: Recorded command exit 0; command argv SHA-256
  02033fc75602c6d6d6bfd7e30319ecdddd5bc0961a13ff8c93f000ecb73e9902.

- 2026-10-12T11:41:37+00:00: Recorded command exit 0; command argv SHA-256
  f9bbe1c589a3669657a75f784f9cf5be2dcca32c9aa8bcdbea78bfad2db9ec69.

- 2026-10-12T11:41:56+00:00: Recorded command exit 0; command argv SHA-256
  02970c2d8860d638f41bff4ed6e5e563ac93ac98b50be6b487e02ab3468b60d2.

- 2026-10-12T11:41:57+00:00: Recorded command exit 0; command argv SHA-256
  de0f9a0651ffde4b5362e5bb246b136d877b74395650384e51588c2dca8120fd.

- 2026-10-12T11:42:05+00:00: Recorded command exit 0; command argv SHA-256
  99df30ca0ed805631b5a3fe2055833ee120579ed5e644b7bc0e120f71be6c943.

- 2026-10-12T11:42:15+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:42:18+00:00: Published signed DCO recovery topic ab4f4c6a via PR #609; preserved
  merge 15c80511 and reviewed tree unchanged. PR checks are running; no TLC/live-provider gate.

- 2026-10-12T11:43:39+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:54:13+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:54:17+00:00: All PR #609 required checks terminal-success: Rust, emulated AArch64,
  policy/coverage/supply-chain, credential-free, TUI/PTY, fuzz, mutation, models, Kani, platform,
  headers, provenance, retained faults, and AWQ shadow evidence. No TLC/live-provider dependency.

- 2026-10-12T11:56:56+00:00: Recorded command exit 0; command argv SHA-256
  6c90071b197ea99a41c00a564ecc1e3fd1178e79785e841c9751e7f4499cdea8.

- 2026-10-12T11:57:18+00:00: Recorded command exit 0; command argv SHA-256
  8df134f290ec84989599f4894d2a42e955805e4ddda15e6b222758c199b2df67.

- 2026-10-12T11:57:40+00:00: Recorded command exit 0; command argv SHA-256
  8f8f1ceb8194b695841e2a5db0025ba5f51163901c3ed6da7831b188811c6116.

- 2026-10-12T11:58:34+00:00: Independent exact-head review approved PR #609 at
  ab4f4c6a81f543e049759d199cca675c7370a1dc: base is exact protected main
  15c80511cd2cb55947fe3ee1e130affed4c76b4d, merge-base is base, head is SSH-signed by certified
  martin.beck2@gmx.de, author/committer/signer/DCO identities match, and head tree
  60b7fca30b4c3344d029d4858bb2cce6371a7298 equals preserved merge tree and exact merge preview. Diff
  is intentionally metadata-only and empty against the preserved merge; no privacy or source-content
  changes. repository_policy exact base..head passed; focused portable-provenance/merge-shape suite
  passed 9 tests plus 7 subtests; signature/DCO/failure-path suite passed 7 tests plus 2 subtests.
  PR #609 required checks are terminal-success, including Rust, emulated AArch64,
  policy/coverage/supply-chain, credential-free, TUI/PTY, fuzz, mutation, models, Kani, platform,
  headers, provenance, retained faults, and AWQ shadow evidence. No TLC/live-provider gate.
  Independent review approved; do not merge via web; proceed only with established signed
  merge_pr.py and post-merge exact-main verification.

- 2026-10-12T11:59:15+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T11:59:25+00:00: Recorded command exit 0; command argv SHA-256
  28900371f2089412eeacbcf5de9ffd2ed9a5068dcba5b68357bf245e591dcd37.

- 2026-10-12T11:59:57+00:00: Heartbeat by ar1805_postmerge_repair.

- 2026-10-12T12:00:00+00:00: merge_pr.py --push published forward-only signed two-parent merge
  e57982a79fafa464bfac6b3c858226ffe08737e7 with first parent preserved 15c80511, reviewed topic
  ab4f4c6a, tree 60b7fca3; no web merge, force update, or gate weakening. Exact-main workflows
  started; provenance and headers already green.

- 2026-10-12T12:00:46+00:00: Post-merge exact-main run 38246184722 Repository quality failed at
  install digest-pinned repository analyzers after repeated curl HTTP 504 responses. This is an
  infrastructure download failure, not a product/policy failure; all other observed workflows remain
  successful or in progress. Preserve merge and retry failed workflow only.

- 2026-10-12T12:00:51+00:00: Recorded command exit 0; command argv SHA-256
  ee0828b2e7ad086de644de4f38823e83462721ce84eb45f16d6c8557ef024050.

- 2026-10-12T12:01:23+00:00: Reran only failed Repository quality workflow 38246184722 through
  handoffctl; attempt 2 is queued for exact merge e57982a. Archived generated state pycache outside
  repository to keep doctor/command recording healthy. No product or gate changes.

- 2026-10-12T12:02:43+00:00: Repository quality attempt 2 again failed at the same digest-pinned
  analyzer download with HTTP 504 after retries; optional artifact classification failed
  consequentially. No product/policy assertion failed. Repeated infrastructure failure recorded;
  retry only the failed workflow, never bypass the gate.

- 2026-10-12T12:02:46+00:00: Recorded command exit 0; command argv SHA-256
  ee0828b2e7ad086de644de4f38823e83462721ce84eb45f16d6c8557ef024050.

- 2026-10-12T12:03:22+00:00: Authoritative GitHub API confirms Repository quality run 38246184722
  attempt 3 is in_progress; it is executing pinned quality-tool setup. Earlier attempts 1 and 2
  failed only at analyzer download HTTP 504. No rerun was lost.

- 2026-10-12T12:11:49+00:00: Recorded command exit 0; command argv SHA-256
  b99dca4b44e69c6ac3d32ba3f22ae88f7d41df110a1c3e3b14d1107ecf57e348.

- 2026-10-12T12:12:40+00:00: Post-merge Repository quality attempt 3 reached coverage and failed one
  fixture checkout test with Err(Unavailable); no source/policy assertion failure. Independent local
  repeated focused run passed 5/5 on current main, so failure is non-reproducible runner/environment
  behavior. Preserve gate and rerun the same exact-main workflow; no repair AR or product change
  warranted.

- 2026-10-12T12:12:45+00:00: Recorded command exit 0; command argv SHA-256
  ee0828b2e7ad086de644de4f38823e83462721ce84eb45f16d6c8557ef024050.

- 2026-10-12T12:13:14+00:00: Authoritative GitHub API confirms Repository quality run 38246184722
  attempt 4 is in_progress. Attempt 3 failed one source_checkout fixture test, while independent
  local repeated run passed 5/5. Rerun is bounded classification evidence; no product changes or
  gate weakening.

- 2026-10-12T12:24:00+00:00: Recorded command exit 0; command argv SHA-256
  1eaaea0727076ab1c5adbbbeaa575c28e2ec3b7b74653ed09f6fd50f5fdaa387.

- 2026-10-12T12:24:18+00:00: Recorded command exit 0; command argv SHA-256
  dbdb1d013c00408501772cd67cee883b204f3ed64eaddf35a46485380133ec99.

- 2026-10-12T12:25:20+00:00: Hosted acceptance: PR #609 signed forward-only merge e57982a preserves
  15c80511 and reviewed tree; all PR and exact-main workflows terminal-success. Repository quality
  attempt 4 passed after attempt 3 non-reproducible source_checkout fixture failure; local repeated
  5/5. Receipt is committed and privacy-safe.

- 2026-10-12T12:25:25+00:00: AR-1815 complete: signed forward-only merge e57982a published from
  preserved 15c80511 and reviewed topic ab4f4c6a; all PR checks and all ten exact-main workflows
  terminal-success, Repository quality run 38246184722 attempt 4 passed after documented
  non-reproducible attempt 3 fixture failure. Acceptance passed with receipt digest
  sha256:7b085cf88dca04871a16632551b51f2ced70c2c3af263c8354fed143f0a1b512.
