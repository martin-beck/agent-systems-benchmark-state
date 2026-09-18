---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T04:58:01+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Qualify the dedicated self-hosted runner user manager and bus at exact PR head 4d98e1dca; repair only the governed runner bootstrap or workflow portability defect, rerun exact-head hosted checks, then rebuild pristine QEMU fixture and run full-exhaustive after all required CI is green.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-repair2-20260918",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 356,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-18T02:59:05+00:00",
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

- 2026-09-17T22:51:55+00:00: Fresh dispatched exact-head formal workflow 35283911252 failed
  immediately because run_formal_tier hardcoded /srv/data/projects/.asb-tlc, which the hosted CI
  runner cannot create (PermissionError). This was an environment portability defect, not a formal
  result. Repair commit 2f814b1fd derives runner/attestation roots from the checked-out source root,
  preserving local second-disk placement while making disposable CI checkout roots writable. Focused
  29/29, Ruff, format, and mypy pass; pushed to PR #24.

- 2026-09-17T22:52:00+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:52:19+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T22:52:34+00:00: Recorded command exit 0; command argv SHA-256
  525f7e3f731dc2102a9e7d8422504e1f49cde0cd314e4c412b95a77c264cf3cf.

- 2026-09-17T22:53:03+00:00: Recorded command exit 0; command argv SHA-256
  44860d1e32aee0c7eb47a2a133ffe6ee7317204058d0caa5932797cb5042437e.

- 2026-09-17T22:53:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:53:47+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:54:16+00:00: Recorded command exit 0; command argv SHA-256
  8a6f9545cc71f4db70b05cc2ce5a08cfcf7132fe900c207255dcef9f1193e557.

- 2026-09-17T22:54:45+00:00: Recorded command exit 0; command argv SHA-256
  c003821be6eca832590d4763a7671bbd5534131f528c581ecc4425e117908257.

- 2026-09-17T22:55:18+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:55:27+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:55:42+00:00: Second exact-head CI dispatch 35284150750 failed at profile import:
  clean CI checkout could not import namespace package formal.handoffctl (ModuleNotFoundError:
  formal). This was a launcher portability defect, not a formal model result. Signed+DCO repair
  9051f1e8f adds an absolute sibling-file fallback for tier_profiles; focused runner/launcher 29/29,
  Ruff, format, and mypy pass; pushed to PR #24. Wrapper lock-timeout during one test invocation was
  retried safely without repeating external effects.

- 2026-09-17T22:56:09+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T22:56:33+00:00: Recorded command exit 0; command argv SHA-256
  54f50b72463db48082de8b29379188e3dbb80a6262cac2cbb8aa42cb646a055a.

- 2026-09-17T22:56:56+00:00: Recorded command exit 0; command argv SHA-256
  585082135e98e5832901d9af6b9b71874238a0a3911738bfd92b9d6ad1e9f531.

- 2026-09-17T22:57:24+00:00: Recorded command exit 2; command argv SHA-256
  8f364695787cec04b4749eae1f261d85060021cd5ad409bbeac7d66d2684e4eb.

- 2026-09-17T22:58:25+00:00: Recorded command exit 1; command argv SHA-256
  0b5946c1ca1f8c789a16e14cabd11a9433bf3ed3db23e8b9adb2ba362a4f1664.

- 2026-09-17T22:58:51+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:58:54+00:00: Recorded command exit 0; command argv SHA-256
  16d782a9c00fbeffd2c12667f3ab6cef70e6005903a9b1346bcccae7a95c416b.

- 2026-09-17T22:59:26+00:00: Recorded command exit 0; command argv SHA-256
  4355be37210c3ac947dfe174412a86ead21e3b67eb451ce19a73481e933a6f57.

- 2026-09-17T22:59:42+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T22:59:46+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T23:00:03+00:00: Recorded command exit 0; command argv SHA-256
  23f481dd0f8c8fde34617ab1f4594487b9dc9f751e31a5a4e3f22f8e1d86013d.

- 2026-09-17T23:00:27+00:00: Recorded command exit 0; command argv SHA-256
  a55d11da5cf667cb6d9300e5d303286355ac554ae696f9a5657f3f78cd965969.

- 2026-09-17T23:01:01+00:00: Recorded command exit 0; command argv SHA-256
  0d54e74573fd5abc1cad3b0d672844b0537d6305ccd41ae7ab465e0ef7d1b692.

- 2026-09-17T23:01:19+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:01:31+00:00: Recorded command exit 0; command argv SHA-256
  8c7c93d886bd64154492054358eb676dd90dcca669cabd87d9dbb3d66677aa23.

- 2026-09-17T23:01:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:01:57+00:00: Third exact-head formal dispatch 35284735524 reached launcher and
  failed exit 1 with no diagnostic; logs showed `formal tier full-exhaustive failed (exit 1): no
  diagnostic was emitted`. Root cause is required-tier child returning nonzero without reporting its
  bounded classification (tlc_runner only recorded the outcome). Signed+DCO repair a69b29c1c now
  emits a sanitized failure classification for every non-timeout nonzero TLC execution; focused
  29/29, Ruff, format, and mypy pass; pushed PR #24. No formal success is claimed.

- 2026-09-17T23:02:09+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T23:02:25+00:00: Recorded command exit 0; command argv SHA-256
  e1dea8f7c95dd889e991c09642fca8aa89b67bda529026544eac0551e6dd0192.

- 2026-09-17T23:02:40+00:00: Recorded command exit 0; command argv SHA-256
  69d9f181b76c61dafce897c05177b31308442629f284b62924d3d156b549f2ae.

- 2026-09-17T23:03:29+00:00: Recorded command exit 0; command argv SHA-256
  f1a1ac95608ca9e58ccd25bc053e9d7216ea11055b803ce2038ee9dd10f93f7a.

- 2026-09-17T23:03:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:03:55+00:00: Recorded command exit 0; command argv SHA-256
  f4938f740acd58e8a6050813ef5e77f261897edb36b9a34a7e77da48f93cf9e0.

- 2026-09-17T23:04:11+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:04:15+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-17T23:04:37+00:00: Recorded command exit 1; command argv SHA-256
  396639fbd509d8b39d1d52c5ab11c78096456095bf9b61cff37eb1fed9b53973.

- 2026-09-17T23:04:55+00:00: Recorded command exit 0; command argv SHA-256
  5854542fdd46e32f8a556d2a7210bc3b6d4aba67ef713c5477256b6b4e298d6d.

- 2026-09-17T23:05:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:05:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:05:33+00:00: Exact-head workflow 35285103922 at b8db467ee now emits the real
  failure: TLC child diagnostic: Failed to connect to bus: No medium found; required full-exhaustive
  exits 1 and correctly emits no attestation. This proves the hosted state runner has no usable
  per-user systemd bus; it is an infrastructure capacity/runner-property failure, not a model/input
  result. Signed+DCO code b8db467ee adds bounded sanitized child diagnostics and is pushed to PR
  #24. Do not substitute portable mode/private lock for required evidence.

- 2026-09-17T23:06:25+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:07:53+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:08:07+00:00: Recorded command exit 1; command argv SHA-256
  a65a971798b7daeef06dd7ce9aa49bbbb67d0e4ab9a1b74f27be5223478ea9ea.

- 2026-09-17T23:08:36+00:00: Recorded command exit 0; command argv SHA-256
  142174dc2c7daae1d599c7b4b68f15cf1ff2398029eb9b91ee14cea5aeb33c3e.

- 2026-09-17T23:08:53+00:00: Recorded command exit 0; command argv SHA-256
  9f25f65c5a0490c2ba86797791e63c9e9494a33339124f85db5971995251f386.

- 2026-09-17T23:09:18+00:00: Recorded command exit 0; command argv SHA-256
  36a46e1488094ed77ccb01e2b76a3cdeaff530489b8157b4dbfca217abe90709.

- 2026-09-17T23:09:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:10:42+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:10:51+00:00: Recorded command exit 0; command argv SHA-256
  b8f56fa47f367761a2f1de3d7024b72fe8556f0ed582bbd0702e1378830df1f2.

- 2026-09-17T23:13:32+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:18:25+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:19:26+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:21:42+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:26:23+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:26:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:28:23+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:36:40+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:38:19+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:41:04+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:44:50+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:45:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:51:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:56:29+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-17T23:59:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:02:27+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:04:06+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:06:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:08:31+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:09:12+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:10:28+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:11:46+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:12:14+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:13:20+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:14:11+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:14:46+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:17:29+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:17:56+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:19:05+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:19:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:21:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:21:52+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:24:31+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:24:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:25:23+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:26:14+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:26:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:27:01+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:27:29+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:28:52+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:29:21+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:29:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:30:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:31:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:31:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:33:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:33:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:34:03+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:38:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:39:26+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:40:26+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:41:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:42:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:43:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:45:30+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:46:37+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:47:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:49:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:49:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:50:45+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:51:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:51:47+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:52:58+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:53:29+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:54:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:56:46+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:57:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:57:47+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T00:58:12+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:00:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:01:04+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:01:56+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:02:32+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:03:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:04:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:06:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:07:05+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:08:58+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:10:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:11:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:12:53+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:15:15+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:17:07+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:17:59+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:18:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:21:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:22:37+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:23:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:23:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:25:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:26:58+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:28:02+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:29:05+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:29:40+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:30:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:32:19+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:32:52+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:33:20+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:33:49+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:34:18+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:34:46+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:35:16+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:35:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:36:13+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:36:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:37:21+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:37:48+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:38:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:38:45+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:39:14+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:39:40+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:40:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:40:37+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:41:03+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:41:30+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:41:58+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:43:05+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:43:42+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:44:11+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:44:38+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:45:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:45:39+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:46:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:46:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:48:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:50:11+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:50:40+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:51:45+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:52:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:53:30+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:54:03+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:54:31+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:56:24+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:58:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:58:54+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T01:59:27+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:00:40+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:01:49+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:02:15+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:02:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:03:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:03:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:04:03+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:04:28+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:04:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:05:21+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:05:50+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:06:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:06:44+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:07:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:07:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:08:07+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:08:32+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:08:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:09:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:09:50+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:10:15+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:10:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:11:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:11:34+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:12:00+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:12:28+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:12:54+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:13:20+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:13:46+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:14:11+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:14:37+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:15:01+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:15:27+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:15:52+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:16:19+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:16:47+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:17:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:17:43+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:18:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:18:33+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:18:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:19:24+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:19:50+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:20:15+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:20:41+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:21:07+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:21:32+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:21:56+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:22:22+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:22:58+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:23:24+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:23:51+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:24:23+00:00: Recorded command exit 0; command argv SHA-256
  eb930183a098a67b97fd76015f5db87f936c84b507f2678564aed0b0b964fcbe.

- 2026-09-18T02:24:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:26:14+00:00: Canonical reconciliation from worker evidence: stage17 used a pristine
  fixed-UUID image, exact source 01f6e000b, no NIC/host mounts, 32GiB/8vCPU, and a 7800s outer
  bound. The supervisor vanished after about 30 minutes, orphaning QEMU; orphan was terminated.
  Serial had only FULL_EXHAUSTIVE_TRANSIENT_RC=0, with no terminal full RC, attestation, evidence
  validation, or poweroff. Classified as SUBPROCESS_INTERRUPTED/orphaned-supervisor; no full-tier
  success or merge claim.

- 2026-09-18T02:26:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:26:27+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T02:27:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:28:55+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:30:10+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:30:47+00:00: Canonical worker evidence now includes signed+DCO supervision repair
  adfb775a0: run_formal_tier cleans process groups on timeout/interruption/finalization and writes
  bounded private non-success interruption receipts; no success attestation is emitted. Stage17
  remains SUBPROCESS_INTERRUPTED with no full attestation. Worker state branch is pushed; PR branch
  advanced from 01f6e000b to adfb775a0.

- 2026-09-18T02:30:55+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T02:31:04+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:31:14+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T02:32:24+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:33:49+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:34:17+00:00: Recorded command exit 1; command argv SHA-256
  a3d95dd7adbf1f58971137cdb99f661b9a258a76678823ce96fe750d7b7d108a.

- 2026-09-18T02:34:51+00:00: Exact remote verification: feature/ar-1307-portable-tlc-runner-repair =
  d0db32adf21c9f1a13954e3382581681d6ecbe2b; codex/ar-1307-portable-tlc-runner =
  8a7b418a2e78234c2325d6002c8f775b3a173cef. Source repair d0db32adf verifies SSH signature status G
  with allowed signers, DCO Signed-off-by, focused tests 31/31, and clean staging tree with no
  untracked JDK/JAR artifacts. Full-tier remains blocked by prior SUBPROCESS_INTERRUPTED evidence.

- 2026-09-18T02:34:57+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:35:07+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T02:35:48+00:00: Recorded command exit 1; command argv SHA-256
  765f67ff49d64db60508b77ba2516ab9f082e49d112e1e6107676dae57e3d529.

- 2026-09-18T02:36:12+00:00: Recorded command exit 1; command argv SHA-256
  7cc548552eaf6452dd5d85258cca58236da45b18a82e490ff361d86757774c62.

- 2026-09-18T02:36:33+00:00: Recorded command exit 0; command argv SHA-256
  ee8512b31102559ca002c65c1dba05d0e0015c7fcca1a87c1135082247419a85.

- 2026-09-18T02:36:45+00:00: Remote heads verified:
  feature/ar-1307-portable-tlc-runner-repair=d0db32adf21c9f1a13954e3382581681d6ecbe2b (PR #24);
  codex/ar-1307-portable-tlc-runner=5ab4ffe2dcdbd9875807746774462ef26cf7d690 (worker state,
  fast-forward integration of signed repair). Source commit d0db32adf verifies G with allowed
  signers and DCO; staging tree is clean of untracked JDK/JAR artifacts. No new full run started.

- 2026-09-18T02:36:53+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T02:37:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:38:09+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:39:14+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:41:08+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:44:36+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:45:18+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:45:47+00:00: Recorded command exit 1; command argv SHA-256
  08098435ff766eba36d91bf303fba25833569713279bcaf5c4c2bdea299c4176.

- 2026-09-18T02:50:17+00:00: Heartbeat by codex-ar1307-runner-repair-20260918.

- 2026-09-18T02:51:41+00:00: Recovered after worker became idle with no active process and no
  durable progress after exact-head 22fe361. Signed/DCO repair preserved; reassignment required for
  runner-bus bootstrap, CI rerun, and full-tier qualification.

- 2026-09-18T02:52:49+00:00: Claimed by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T02:54:58+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T02:55:09+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T02:55:24+00:00: Takeover progress: AR-1307 claimed by successor. Exact PR worktree
  /srv/data/projects/ar1307-qemu-stage-head is clean at signed+DCO 4d98e1dca (includes 22fe361);
  runner label is online but exact-head formal check failed in user-bus preflight. Current host
  inspection confirms UID 984 lingering user manager and systemd user bus can run a transient unit;
  failure timing/bootstrapping remains under investigation. No formal qualification or merge claim.

- 2026-09-18T02:57:01+00:00: Recorded command exit 0; command argv SHA-256
  1e17191845140a9ea485ed0887415b90d3062661fe8e449e56cc7e2597a28173.

- 2026-09-18T02:57:15+00:00: Recorded command exit 1; command argv SHA-256
  6f32ab8e669c218aaa64a9ab55c48f8d804d6d3e5eb4d3e4365732fe999645ff.

- 2026-09-18T02:57:36+00:00: Recorded command exit 1; command argv SHA-256
  a4d29c6531fc1914c3d6520df57943f19f6e4e272c083d3bf75c28efec4cc11c.

- 2026-09-18T02:58:01+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T02:58:16+00:00: Recorded command exit 0; command argv SHA-256
  19a8039d49c1a4719efafa349d68c88e8980cd4c7b2d3c99c42698bddf7d1aa0.

- 2026-09-18T02:58:31+00:00: Recorded command exit 0; command argv SHA-256
  d13eabd0ca9ee2492f3d1f157cfbfb330931f3af8841c87a1ed7873ad4aa111b.

- 2026-09-18T02:58:40+00:00: Recorded command exit 0; command argv SHA-256
  371c9bad7cfcbd06c0f4dbf77fc9ad117ccb89fc4b39891b5b4f57bb9fd76449.

- 2026-09-18T02:59:05+00:00: Recorded command exit 0; command argv SHA-256
  27edc683b16c94829ad3f68a9bf0eab49fc8c052cf9fc93b1deb777b5b3aba4b.
