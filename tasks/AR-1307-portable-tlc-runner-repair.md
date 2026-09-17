---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T00:51:22+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Get independent complete-diff review of 1fd1432eb and trigger/monitor PR #24 required CI; provision or reuse a reviewed clean QEMU lifecycle from /srv/data/projects with digest-pinned image/JAR, no NIC/host mounts, and execute repeated fresh exact-head portable-smoke before required tiers.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-repair-20260918",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 73,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-17T22:51:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1307-portable-tlc-runner-repair"
}
---

## AR-1307

AR-1302's initial portable runner is not publishable: it directly invokes TLC,
does not use the canonical admission/attestation path, has incomplete
provenance and unbounded subprocess handling, and does not match the AR-1293
tier contracts. Repair it as a state-repository-only successor and produce
fresh exact-head qualification evidence. Do not touch ASB product, asb-tui,
handoffctl, external root-owned locks, or native-ARM-only requirements.

The predecessor AR-1302 is complete and is independently audited by this AR;
AR-1293 remains blocked until the repaired runner is merged and handed off.
See `../plans/AR-1307.md` for the complete scope, gates, evidence contract,
and protected publication sequence.

- 2026-09-17T23:55:00+00:00: Created as the repair successor after independent exact-head review
  found AR-1302's runner bypassed canonical admission/attestation and lacked required bounded
  execution, profile alignment, provenance, and clean publication evidence. Depends only on done
  AR-1302 so it can unblock blocked AR-1293 without a dependency cycle.

- 2026-09-17T21:53:43+00:00: Predecessor AR-1302 done; successor repair required by independent
  audit; dependencies verified.

- 2026-09-17T21:53:50+00:00: Claimed by codex-ar1307-runner-20260917.

- 2026-09-17T21:54:54+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:55:11+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:55:23+00:00: Recorded command exit 0; command argv SHA-256
  521f6d22b7f09ae3d1eb6def263a3533a428c7f246838f6ff3be03012dbb2795.

- 2026-09-17T21:56:51+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:00:50+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:02:30+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:10:29+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:10:39+00:00: Durable checkpoint: feature branch has imported canonical
  tlc_runner/profile/attestation chain and added bounded argv-only process-group execution, private
  /srv/data/projects runtime roots, source/input/runner/artifact provenance, restricted attestation
  paths, UUID privacy fix, and 24/24 focused tests. Full state suite passed 158/158; Ruff check and
  format pass; uv-frozen offline quality environment installed. Mypy tools/tests is blocked only by
  the current branch vendor import context/environment before vendor restoration; vendor verify
  currently fails because imported commits modify immutable formal/handoffctl/README.md and
  verify.sh, which must be restored. Branch checkpoint 50a547dcd plus local repair changes remains
  unpublished.

- 2026-09-17T22:13:51+00:00: Durable checkpoint: imported runner chain initially failed vendor
  verification because immutable formal/handoffctl README.md and verify.sh were modified; both are
  now restored in the AR-1307 worktree and vendor verification passes (agent-workflow-coordinator
  v0.3.7). Focused suite remains 24/24 and full state suite 158/158. Ruff repair is in progress
  after adding bounded launcher/provenance changes; no release or PR claim yet.

- 2026-09-17T22:15:32+00:00: Durable checkpoint: vendor verification passes at v0.3.7; Ruff check
  passes; Ruff format check passes for 22 files; uv-frozen .venv mypy tools/tests passes 19 files.
  Focused runner tests remain 24/24 and full state suite 158/158. The exact launcher/provenance
  implementation is still uncommitted in the feature worktree pending launcher tests and final diff
  review; repeated handoffctl lock timeouts occurred after successful commands and were not
  re-executed.

- 2026-09-17T22:20:01+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:20:10+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:21:48+00:00: Durable checkpoint: repair implementation committed at 9e2341f35
  (signed+DCO). It restores immutable coordinator vendor files, adds bounded argv-only process-group
  timeout/cleanup and DEVNULL output handling, second-disk private defaults,
  source/input/runner/artifact provenance, root-confined attestation, canonical tier launcher, and 4
  launcher tests. Gates: focused runner 24/24; launcher 4/4; full state suite 162/162; Ruff check
  pass; Ruff format 22 files pass; uv-frozen offline mypy tools/tests 20 files pass; vendor verify
  v0.3.7 pass; diff-check/privacy scan pass. No fresh TLC execution yet; host Docker/QEMU/formal
  capacity must be qualified before claiming evidence.

- 2026-09-17T22:21:53+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:23:29+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:24:37+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:25:51+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:27:31+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:30:28+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:30:46+00:00: Independent review found signed repair commit
  eda17a733a56855b851f79e73b65dea4a5879452 clean; PR #24 published. Schema validator still reports
  pre-existing metadata defects, including empty checkpoints; no fresh formal/VM evidence is
  claimed.

- 2026-09-17T22:31:08+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T22:33:16+00:00: Prior worker interrupted; releasing claim for controlled takeover.
  Preserve PR #24 and commit evidence; successor will complete exact-head qualification and repair
  remaining review blockers.

- 2026-09-17T22:33:18+00:00: Claimed by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:33:51+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:34:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:34:38+00:00: Recorded command exit 0; command argv SHA-256
  0e85a9ec52b23d0c5c2bffd0bde2237e985f620f7917e72f6def7b5a7f112297.

- 2026-09-17T22:34:47+00:00: Recorded command exit 0; command argv SHA-256
  252d68cf6a3762058ca6c4f5c343b3e63fe77060e90b5676ff519eb049b94a94.

- 2026-09-17T22:34:57+00:00: Recorded command exit 0; command argv SHA-256
  a6f605c8e3a5597e0cbd12dc02719ac779bb0e7fc2754088aa6d6c9c745d6408.

- 2026-09-17T22:36:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:38:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:38:33+00:00: Recorded command exit 127; command argv SHA-256
  74a411eda4b8ecbfd3b7147b062734afb57efc88807dbfb7726b2a05636f19e9.

- 2026-09-17T22:38:47+00:00: Recorded command exit 1; command argv SHA-256
  12ca69f764cdcbf14c0661d54f759467c97d41a8846f6fdabeaf72348a3a6ec5.

- 2026-09-17T22:39:18+00:00: Recorded command exit 0; command argv SHA-256
  12ca69f764cdcbf14c0661d54f759467c97d41a8846f6fdabeaf72348a3a6ec5.

- 2026-09-17T22:39:37+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:39:40+00:00: Takeover checkpoint: classified exit 127 as missing .venv/bin/python in
  the PR worktree; reran with canonical state .venv and focused runner/launcher suites pass 28/28.
  Repaired verify.sh to require the pinned staged TLA JAR offline (no network fetch), guest seed now
  exports TLC_JAR_PATH/SHA256 directly, and switched default admission lock to the project-wide
  owner-private lock. Added symlink rejection for private directories and updated seed tests.
  Changes remain uncommitted pending full gates.

- 2026-09-17T22:39:54+00:00: Recorded command exit 1; command argv SHA-256
  283ea296807f61d25a86cd8528f4863e1c7f1906cdc3341cb81a48f42d122c32.

- 2026-09-17T22:40:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:40:20+00:00: Recorded command exit 1; command argv SHA-256
  8de440b08dc960abe7f171b6fe8b051352470d1bb70805c3d482f73c16ac4e73.

- 2026-09-17T22:41:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:41:58+00:00: Recorded command exit 0; command argv SHA-256
  38c783821a3449cddf74ebbe24c26d0bd045ddeea68e8bad1269e87d65b322eb.

- 2026-09-17T22:42:54+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:43:07+00:00: Recorded command exit 0; command argv SHA-256
  52ce2688b28de6e8371b03eb5c464a27a2e5b18337b4dbb83aebb23bc51c2bc7.

- 2026-09-17T22:43:22+00:00: Recorded command exit 0; command argv SHA-256
  2800bb2db51a943988d45cd2a7000864d17f7c49541ff318470bb4ddaa94820c.

- 2026-09-17T22:43:36+00:00: Recorded command exit 0; command argv SHA-256
  a11fdf0a056f72a2813ce58450aa9c8588e848cf43a7c3a8a8a2a7d8a07d31a1.

- 2026-09-17T22:43:54+00:00: Recorded command exit 0; command argv SHA-256
  17668c4873480f965cceae6f027c38b0c6e6cb20d81b322d18c0e7b6ffbf6a46.

- 2026-09-17T22:44:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:44:18+00:00: Recorded command exit 0; command argv SHA-256
  cdc3e69a35a66c17946919bac65af40b79f9254903fdd24d82486de403001ca1.

- 2026-09-17T22:44:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:44:42+00:00: Repair commit 7fc6a246b signed+DCO and pushed to PR #24. Correctly
  restored immutable verify.sh/vendor boundary after the first offline-fetch attempt caused vendor
  mismatch. Offline guest seed now validates the pinned JAR digest before using its no-network curl
  shim; runner defaults to exact canonical shared coordinator fence
  /tmp/agent-workflow-coordinator-tlc-admission.lock and does not chmod its /tmp parent;
  private-directory symlink rejection and explicit lock tests added. Focused runner/launcher 29/29
  and vendor verify v0.3.7 pass; earlier exit 127 was missing PR-worktree .venv and earlier exit-1s
  were focused seed expectation plus intentional vendor mismatch from immutable verify.sh edit, all
  corrected. Full suite and fresh formal tiers still pending.

- 2026-09-17T22:45:19+00:00: Recorded command exit 1; command argv SHA-256
  50eec985b3d890adf24922de9fbb303fcbf2d0fec06550f65472356045fe7ca0.

- 2026-09-17T22:46:06+00:00: Recorded command exit 2; command argv SHA-256
  50eec985b3d890adf24922de9fbb303fcbf2d0fec06550f65472356045fe7ca0.

- 2026-09-17T22:46:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:46:23+00:00: Recorded command exit 0; command argv SHA-256
  40bc7e021f3983dc9ffef4fa5650a545a36cc27223737646fb88e10804da95da.

- 2026-09-17T22:46:49+00:00: Recorded command exit 0; command argv SHA-256
  ff052edd1e2f19032f140ceca1cc5232f5c0488311ef3a0b6f27895850b67e60.

- 2026-09-17T22:47:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:47:13+00:00: Repair is now exact PR head 1fd1432eb (signed+DCO), pushed to PR #24.
  Full state suite passed 163/163; Ruff check and format passed; source-header verification passed
  32 files; vendor v0.3.7 verification passed; strict mypy passed 20 files; focused runner/launcher
  passed 29/29. Exit-1 at 22:45:19 was Ruff S108 on the literal canonical /tmp path and is fixed by
  constructed constant; the next exit-2 was an operator-invoked unsupported --check option for
  check_source_headers.py, rerun correctly with --root and passed. No formal VM tier evidence yet.

- 2026-09-17T22:47:45+00:00: Recorded command exit 1; command argv SHA-256
  ddede10932c90a1e37c2ea38edc09848bcb67e22e857fc0e165252f5808464c8.

- 2026-09-17T22:48:14+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:48:16+00:00: Exact PR head 1fd1432eb remains clean, signed/DCO, and pushed. Full
  state unit suite passed 163/163; Ruff and format pass; source headers 32 files; vendor verify
  v0.3.7; mypy tools/tests 20 files. Exit-1 at 22:45:19 was the Ruff S108 literal /tmp
  canonical-lock diagnostic, corrected and rerun. The subsequent gate attempt stopped at an operator
  error: check_source_headers.py has --root, not --check; rerun passed. PR #24 currently reports no
  checks (workflow/path or dispatch state), so no CI green claim yet.

- 2026-09-17T22:48:21+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:48:45+00:00: Recorded command exit 0; command argv SHA-256
  1746c36967fe5e128d156659601c7d3ec71b9406c7d0142b9cbc2543d6e0bcbd.

- 2026-09-17T22:49:15+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T22:49:30+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:49:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:49:50+00:00: Recorded command exit 0; command argv SHA-256
  76c4b7b389a554b61dd5aa92a72e780ab9930a71c2e19d15df0bcf963b5f8bec.

- 2026-09-17T22:50:06+00:00: Recorded command exit 0; command argv SHA-256
  2b34a75896030ce80ffd732a95c5299d76c024b635d1b89ac0f87e8826b4f139.

- 2026-09-17T22:50:20+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:50:48+00:00: Recorded command exit 0; command argv SHA-256
  19dc6a2ef4f0467ce9bc356ef99183b2ab49f86ed1b83b5f4c3882c2c47bbfb3.

- 2026-09-17T22:51:04+00:00: Recorded command exit 0; command argv SHA-256
  fb7bd7a3bb1a8a0c2281289f995d0634f0d228877662a80143922c9d6b47642b.

- 2026-09-17T22:51:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.
