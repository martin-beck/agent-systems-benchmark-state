---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "ab485f767fbddbd8adfc27b5120f3df0a045b762",
  "claim_expires": "2026-09-26T19:07:24+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "PR #25 is open at exact signed+DCO head ab485f767, but full-exhaustive formal CI run 35342513872 failed truthfully after Java OOM during liveness checking at the unchanged 3G/3G/2-worker contract. AR-1308 provides the prepared 32 GiB/64 GiB offline QEMU capacity; bind the exact signed bundle and rerun only after its seed/JDK/TLC preflight passes. Do not qualify or weaken the contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "969eef05834a4ce5f711bbafaa5798549abd95c8",
  "owner": "coordinator-ar1307-audit",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 736,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-26T18:47:39+00:00",
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

The `unsigned-development` profile is diagnostic-only: local unsigned
fixtures may exercise preflight and bounded runner plumbing, but cannot be
reported as formal qualification, canonical full attestation, publication
evidence, or release evidence. Full-tier preflight must reject missing,
unsigned, stale, or profile-mismatched inputs and must require the exact
reviewed signed bundle.
The validator's `signed` profile is the default and the only profile that may
authorize qualification, publication, or release evidence; selecting
`unsigned-development` must produce a labelled diagnostic result.

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

- 2026-09-18T02:59:14+00:00: Recorded command exit 0; command argv SHA-256
  816d662057ed053b4b6d7f3484b4ed99f8041c6c42b6c0ede3c1987a2ccc18c5.

- 2026-09-18T02:59:31+00:00: Recorded command exit 0; command argv SHA-256
  d32ff6e347f70565791bd2b92f7ced60c3a2eb2d5c8ddd0110cd435f71aae50f.

- 2026-09-18T03:00:01+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:00:57+00:00: Recorded command exit 0; command argv SHA-256
  ce3812a59264e886d1ee9def1978b14eccaf39ff5044cdef326a4387e05e7151.

- 2026-09-18T03:01:06+00:00: Recorded command exit 0; command argv SHA-256
  d13eabd0ca9ee2492f3d1f157cfbfb330931f3af8841c87a1ed7873ad4aa111b.

- 2026-09-18T03:01:15+00:00: Recorded command exit 1; command argv SHA-256
  371c9bad7cfcbd06c0f4dbf77fc9ad117ccb89fc4b39891b5b4f57bb9fd76449.

- 2026-09-18T03:01:29+00:00: Recorded command exit 0; command argv SHA-256
  b156ef3a25db2d2d38a909e60e314880622c886cf405ed0db2ef2313dce57a35.

- 2026-09-18T03:01:38+00:00: Recorded command exit 0; command argv SHA-256
  371c9bad7cfcbd06c0f4dbf77fc9ad117ccb89fc4b39891b5b4f57bb9fd76449.

- 2026-09-18T03:01:50+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:02:02+00:00: Recorded command exit 0; command argv SHA-256
  d3fb12c01d221831faa9d1a83f0c180198c04b46aff12bdfa1a17d502c302dd6.

- 2026-09-18T03:02:12+00:00: Recorded command exit 0; command argv SHA-256
  4bd76932997128cae485cfd1d537e78e8e4c581e64285946fe7d6bfe77c15349.

- 2026-09-18T03:02:28+00:00: Recorded command exit 0; command argv SHA-256
  d32ff6e347f70565791bd2b92f7ced60c3a2eb2d5c8ddd0110cd435f71aae50f.

- 2026-09-18T03:02:57+00:00: Recorded command exit 0; command argv SHA-256
  2b55a39f67dc031919cdb1b04b2fccb97a61a3561aebb8c97bd09c9e39e7ee3f.

- 2026-09-18T03:03:07+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:04:50+00:00: Recorded command exit 1; command argv SHA-256
  9f5c5a27ddbc27a8fed4a38e1243514b5f87c6227fdd44ac1d53b296ddec174c.

- 2026-09-18T03:05:07+00:00: Recorded command exit 1; command argv SHA-256
  a680aca3b53c5b420be80fee4f6b2a90aee5fb5f59d91da7bdbe1aafb6eaef38.

- 2026-09-18T03:05:27+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:05:57+00:00: Recorded command exit 0; command argv SHA-256
  402bfca34f1533177444510813721fabfdc8f9638f4d705031fe3f1c97edf27b.

- 2026-09-18T03:06:07+00:00: Recorded command exit 2; command argv SHA-256
  c131ec376ccf6c4a7ca24f01020f5dbf6eca452f05b243972448e85d3a1a3066.

- 2026-09-18T03:07:33+00:00: Recorded command exit 0; command argv SHA-256
  305c4ee4187eaf2e573bc14d92c9949a008f4aef9d3386e3eb746d7133d4d89b.

- 2026-09-18T03:07:42+00:00: Recorded command exit 1; command argv SHA-256
  d13eabd0ca9ee2492f3d1f157cfbfb330931f3af8841c87a1ed7873ad4aa111b.

- 2026-09-18T03:08:07+00:00: Recorded command exit 0; command argv SHA-256
  d13eabd0ca9ee2492f3d1f157cfbfb330931f3af8841c87a1ed7873ad4aa111b.

- 2026-09-18T03:08:16+00:00: Recorded command exit 0; command argv SHA-256
  371c9bad7cfcbd06c0f4dbf77fc9ad117ccb89fc4b39891b5b4f57bb9fd76449.

- 2026-09-18T03:08:25+00:00: Recorded command exit 0; command argv SHA-256
  ce3812a59264e886d1ee9def1978b14eccaf39ff5044cdef326a4387e05e7151.

- 2026-09-18T03:09:12+00:00: Recorded command exit 0; command argv SHA-256
  402bfca34f1533177444510813721fabfdc8f9638f4d705031fe3f1c97edf27b.

- 2026-09-18T03:10:16+00:00: Recorded command exit 2; command argv SHA-256
  3eb4936622520b17b8a92e67bb4bd79fcfa602ae7fef5fcc0f7039c41f2b9ff2.

- 2026-09-18T03:11:02+00:00: Recorded command exit 0; command argv SHA-256
  1ae7a765b985187cb321b3a36f46b5fa8d5f3ae1f89f893d67e3e43c70742220.

- 2026-09-18T03:11:38+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:13:02+00:00: Recorded command exit 0; command argv SHA-256
  305c4ee4187eaf2e573bc14d92c9949a008f4aef9d3386e3eb746d7133d4d89b.

- 2026-09-18T03:13:12+00:00: Recorded command exit 1; command argv SHA-256
  ee88b4d3f1603c13d035944eae3880e11b0f1005c799b2086af3b32820584bdb.

- 2026-09-18T03:13:33+00:00: Recorded command exit 0; command argv SHA-256
  305c4ee4187eaf2e573bc14d92c9949a008f4aef9d3386e3eb746d7133d4d89b.

- 2026-09-18T03:13:42+00:00: Recorded command exit 0; command argv SHA-256
  ee88b4d3f1603c13d035944eae3880e11b0f1005c799b2086af3b32820584bdb.

- 2026-09-18T03:13:51+00:00: Recorded command exit 1; command argv SHA-256
  f69974fba1ae286bc3c580f7ac7b69b6eb574909862821b643471fcfb58a2fe0.

- 2026-09-18T03:14:22+00:00: Recorded command exit 0; command argv SHA-256
  ee88b4d3f1603c13d035944eae3880e11b0f1005c799b2086af3b32820584bdb.

- 2026-09-18T03:14:31+00:00: Recorded command exit 0; command argv SHA-256
  f69974fba1ae286bc3c580f7ac7b69b6eb574909862821b643471fcfb58a2fe0.

- 2026-09-18T03:15:55+00:00: Recorded command exit 0; command argv SHA-256
  b156ef3a25db2d2d38a909e60e314880622c886cf405ed0db2ef2313dce57a35.

- 2026-09-18T03:16:05+00:00: Recorded command exit 1; command argv SHA-256
  a0750c4439abd5be886aa84424abec18b380b9c6f369854155c21700c70013c4.

- 2026-09-18T03:16:38+00:00: Recorded command exit 0; command argv SHA-256
  a0750c4439abd5be886aa84424abec18b380b9c6f369854155c21700c70013c4.

- 2026-09-18T03:16:48+00:00: Recorded command exit 0; command argv SHA-256
  f7658aa4d651f814163ee34c5cea11a02df11684168fbc3759fcd25d765b36d5.

- 2026-09-18T03:16:57+00:00: Recorded command exit 0; command argv SHA-256
  841652631b62f968093949a14694c83f82e35842be7a390db02488a6c2c76e46.

- 2026-09-18T03:17:42+00:00: Recorded command exit 0; command argv SHA-256
  1ae7a765b985187cb321b3a36f46b5fa8d5f3ae1f89f893d67e3e43c70742220.

- 2026-09-18T03:18:21+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:18:30+00:00: Recorded command exit 0; command argv SHA-256
  57dce348a48333d1201c9f110842bbdcf702e9df25299e9399d607bf10f0aa44.

- 2026-09-18T03:18:39+00:00: Recorded command exit 0; command argv SHA-256
  44d58e4a726d3c7fdf9919adf76aaf6c90e24e1fc3b4bbf3c82af451757ac6c2.

- 2026-09-18T03:18:55+00:00: Recorded command exit 0; command argv SHA-256
  d32ff6e347f70565791bd2b92f7ced60c3a2eb2d5c8ddd0110cd435f71aae50f.

- 2026-09-18T03:19:11+00:00: Recorded command exit 0; command argv SHA-256
  2b55a39f67dc031919cdb1b04b2fccb97a61a3561aebb8c97bd09c9e39e7ee3f.

- 2026-09-18T03:19:21+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:20:22+00:00: Recorded command exit 0; command argv SHA-256
  3fc5101b3c9fc02668f6d9eaf04fa5c4ed974350bd3dad39abbc3210ac09ccf9.

- 2026-09-18T03:20:31+00:00: Recorded command exit 1; command argv SHA-256
  a128cd0d67da986b2e37728e5e28785379f20628ac23c4b18906a3edb8f83778.

- 2026-09-18T03:20:44+00:00: Recorded command exit 0; command argv SHA-256
  305c4ee4187eaf2e573bc14d92c9949a008f4aef9d3386e3eb746d7133d4d89b.

- 2026-09-18T03:20:54+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:20:56+00:00: Recorded command exit 1; command argv SHA-256
  6da19056d20b13bf652d2a0d74e4b3c88e6788535b36563c58dc0a5f7817c881.

- 2026-09-18T03:21:13+00:00: Recorded command exit 0; command argv SHA-256
  9561760df1d636a39d1100849c2266035885a1c29c3b463985f9124fc1038d52.

- 2026-09-18T03:21:31+00:00: Recorded command exit 0; command argv SHA-256
  b165332b74d889e5642ca5aae6f54e0850875cdc6fcea8414c7b3c8fedfabb89.

- 2026-09-18T03:21:40+00:00: Recorded command exit 0; command argv SHA-256
  968b3168ced94be8f4dc89fee3eb3e11a420d31ea1eaa4a0d3aa2b8b7b5ca579.

- 2026-09-18T03:21:57+00:00: Recorded command exit 0; command argv SHA-256
  d32ff6e347f70565791bd2b92f7ced60c3a2eb2d5c8ddd0110cd435f71aae50f.

- 2026-09-18T03:22:34+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:22:53+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:23:03+00:00: Recorded command exit 1; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:23:14+00:00: Recorded command exit 1; command argv SHA-256
  ced6e0b339a746aa0c4e05ef94196d870d61d73fa0f1d14db7e5c1a5129d8a77.

- 2026-09-18T03:23:38+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:23:48+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:23:57+00:00: Recorded command exit 0; command argv SHA-256
  f97fe1b943f3af42645eb4605f6bc72c0c7650978ba536ff5c11f1dfc450e194.

- 2026-09-18T03:24:07+00:00: Recorded command exit 1; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:24:17+00:00: Recorded command exit 0; command argv SHA-256
  79004fb1ac91ee12d4d9b4fecd01b13cf19256dac3b45db6fdd8e39bcd3c9e46.

- 2026-09-18T03:24:27+00:00: Recorded command exit 1; command argv SHA-256
  ce145ac3041f93b93defb85943432a561e2254ba07738112c22000001402e284.

- 2026-09-18T03:24:36+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:24:45+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:24:54+00:00: Recorded command exit 0; command argv SHA-256
  d0f5805af731fe621d15f2d8314c156319d1f97c4e83f4526658e75be7ece643.

- 2026-09-18T03:25:04+00:00: Recorded command exit 0; command argv SHA-256
  f97fe1b943f3af42645eb4605f6bc72c0c7650978ba536ff5c11f1dfc450e194.

- 2026-09-18T03:25:13+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:25:22+00:00: Recorded command exit 0; command argv SHA-256
  79004fb1ac91ee12d4d9b4fecd01b13cf19256dac3b45db6fdd8e39bcd3c9e46.

- 2026-09-18T03:25:31+00:00: Recorded command exit 0; command argv SHA-256
  2b55a39f67dc031919cdb1b04b2fccb97a61a3561aebb8c97bd09c9e39e7ee3f.

- 2026-09-18T03:25:41+00:00: Recorded command exit 0; command argv SHA-256
  ce145ac3041f93b93defb85943432a561e2254ba07738112c22000001402e284.

- 2026-09-18T03:25:51+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:25:59+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:26:08+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:26:24+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:26:33+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:27:29+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:27:38+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:27:49+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:28:03+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:29:33+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:29:43+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:29:52+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:30:09+00:00: Recorded command exit 0; command argv SHA-256
  ffb1e3d3d7f2e88a9528f4e8e8fb7a255599f414e9530a5f0a908f5afde02c30.

- 2026-09-18T03:30:18+00:00: Recorded command exit 0; command argv SHA-256
  2c1914a8c3736bbbbfef9e90464921759f1bb1b3ef58b97c3ffbe4c3de0b8596.

- 2026-09-18T03:30:28+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:30:43+00:00: Recorded command exit 0; command argv SHA-256
  a0d42e453f9eaa9daa8a38c11db57ad03dcfe56555fca93f6a0d3fb543b8651f.

- 2026-09-18T03:31:03+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:31:30+00:00: Recorded command exit 0; command argv SHA-256
  ef688222e3b1aaf582f040cc8a5bfc97b9fefbe3842320199e9430097122974d.

- 2026-09-18T03:31:39+00:00: Recorded command exit 0; command argv SHA-256
  f933aae837bb5b31e79c71ea9b139e3e75a83358403a27d180984f9bec3508fd.

- 2026-09-18T03:31:49+00:00: Recorded command exit 0; command argv SHA-256
  b13c3640b759c7d858356f0859fbc864bdfcf46bda53e6d3f982f3220da70976.

- 2026-09-18T03:31:58+00:00: Recorded command exit 1; command argv SHA-256
  23694d87344ac68e20c6978e65883d8776280528961811e4aac650700d7baa8e.

- 2026-09-18T03:32:08+00:00: Recorded command exit 0; command argv SHA-256
  e9ad9364e23538647c4ab7cfe8ac2a0154ad2daa4f1c8737ee7e8bc1b9cda93f.

- 2026-09-18T03:32:17+00:00: Recorded command exit 0; command argv SHA-256
  cf5ad88b193fc852275862bc50b8853a856fecfda5b438d091447d09a9edb6a1.

- 2026-09-18T03:32:37+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:33:03+00:00: Runner repair is active and service online. The previous formal failure
  was from the run launched before provisioning: chmod of /srv/data/projects/.asb-tlc failed under
  the old root-owned runtime. Provisioned .asb-tlc, attestations, and queue for gha-asb-state mode
  0700 through handoffctl. Previous coordination failure is existing generated metadata validation:
  AR-1301/1306 next_action over schema maximum and AR-1304/1305/1307 empty checkpoint_commit; must
  be repaired in canonical state before rerun.

- 2026-09-18T03:33:14+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:34:45+00:00: Recorded command exit 128; command argv SHA-256
  b4e72b619bcfcf843df36ec7eb9a12dde1c0ba2106d4686775fdc4509b45107a.

- 2026-09-18T03:35:05+00:00: Recorded command exit 0; command argv SHA-256
  62a4a01bd791f18a0fabca2d5ff3fd74c2854f54a8c5669b45bd853fcc1147cb.

- 2026-09-18T03:35:15+00:00: Recorded command exit 128; command argv SHA-256
  b4e72b619bcfcf843df36ec7eb9a12dde1c0ba2106d4686775fdc4509b45107a.

- 2026-09-18T03:35:32+00:00: Recorded command exit 1; command argv SHA-256
  b4e72b619bcfcf843df36ec7eb9a12dde1c0ba2106d4686775fdc4509b45107a.

- 2026-09-18T03:35:55+00:00: Recorded command exit 1; command argv SHA-256
  b4e72b619bcfcf843df36ec7eb9a12dde1c0ba2106d4686775fdc4509b45107a.

- 2026-09-18T03:36:22+00:00: Recorded command exit 0; command argv SHA-256
  2ed5f480dfcb96f61c695e6448b6113fdd2b284ec361ac604bdd84b3e2da27b8.

- 2026-09-18T03:36:31+00:00: Recorded command exit 0; command argv SHA-256
  8448e2ee0e0d923a89863cfffe8f949cc9025c971f446714aef82ebfbc242a57.

- 2026-09-18T03:36:39+00:00: Recorded command exit 1; command argv SHA-256
  4323956038e662b64fb21d4105d34828a4927d64f1aec7489446d2fb8adf376f.

- 2026-09-18T03:36:50+00:00: Recorded command exit 0; command argv SHA-256
  23b2cad55d063096f1db1ccc3f3d836e4b2a7b710b948912fa96bcb9825162c3.

- 2026-09-18T03:36:59+00:00: Recorded command exit 0; command argv SHA-256
  1ba08d2a5279a3ba1bcbccdffd10279d4202c78a17f480227551f0a8042c4746.

- 2026-09-18T03:37:14+00:00: Recorded command exit 0; command argv SHA-256
  80a4dffc47649a7327bf3404781f7dfbabe8c62a22c33bdc31697905e8d1ed35.

- 2026-09-18T03:37:40+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:37:48+00:00: Recorded command exit 128; command argv SHA-256
  3a65ce341909c09a1de5244a16337f3cea627544170e0927a627ff7d8c741421.

- 2026-09-18T03:38:20+00:00: Recorded command exit 128; command argv SHA-256
  d9bbb090342dcbd1264ef4ebb69d30537fe9cec4317d8b643eee50a236059713.

- 2026-09-18T03:38:30+00:00: Recorded command exit 0; command argv SHA-256
  ff25cc5424043e6d4df53b68db13e4d864635b6355eb9981db89effe9200e6cc.

- 2026-09-18T03:38:40+00:00: Recorded command exit 0; command argv SHA-256
  b4feb56af55b73bd27d431f6f637dd21055975fdfbb53e2c5ccafa2a10f1e20a.

- 2026-09-18T03:38:49+00:00: Recorded command exit 1; command argv SHA-256
  3a65ce341909c09a1de5244a16337f3cea627544170e0927a627ff7d8c741421.

- 2026-09-18T03:38:59+00:00: Recorded command exit 0; command argv SHA-256
  3c7898f278252722f03400a2aa7aff498cc22d0c018b6ec2c137f7f88d0dec85.

- 2026-09-18T03:39:09+00:00: Recorded command exit 128; command argv SHA-256
  447e218eaa6a2653d68dbbcb19b7afcf66ee72ae5d9faec454a73dd5e978a439.

- 2026-09-18T03:39:24+00:00: Recorded command exit 0; command argv SHA-256
  7b9738eb5bb1f3ea4a60ff93ee27b2f0a1eb00ac6a7c430fdfe5053296836c95.

- 2026-09-18T03:39:41+00:00: Recorded command exit 0; command argv SHA-256
  b4feb56af55b73bd27d431f6f637dd21055975fdfbb53e2c5ccafa2a10f1e20a.

- 2026-09-18T03:39:51+00:00: Recorded command exit 0; command argv SHA-256
  4f56634a5866d9c7e8598b2e2f45c8a30ac560441e341d2d908eff1cde8f9d42.

- 2026-09-18T03:40:00+00:00: Recorded command exit 0; command argv SHA-256
  b41216aef39569540d84941b9917ede93550f06a8c469fb0c28f3790f0f940cc.

- 2026-09-18T03:40:09+00:00: Recorded command exit 1; command argv SHA-256
  85b21952e1dbaf75e772abf89c35712d3f94510dfc5c6376e9fd0307f62b7e55.

- 2026-09-18T03:40:20+00:00: Recorded command exit 0; command argv SHA-256
  e54e527abf332bd4323517503eb7ede3b9934dffd14caff47613721eada35cb8.

- 2026-09-18T03:40:29+00:00: Recorded command exit 0; command argv SHA-256
  344264000c28ddb1a66c137000b12b498a19662b05a65aa2db0dfe7a90eb6300.

- 2026-09-18T03:40:38+00:00: Recorded command exit 1; command argv SHA-256
  d8cacf625c2ece703436e8512f4db7fcecc6ab66bd08a25848533bca3055214d.

- 2026-09-18T03:40:48+00:00: Recorded command exit 0; command argv SHA-256
  6de133fd4ec14a04897ba4e7d8ffbf0ce212c5b03d49a5862cf5885a3b881f10.

- 2026-09-18T03:40:57+00:00: Recorded command exit 0; command argv SHA-256
  b4feb56af55b73bd27d431f6f637dd21055975fdfbb53e2c5ccafa2a10f1e20a.

- 2026-09-18T03:41:06+00:00: Recorded command exit 0; command argv SHA-256
  17b43a7c826a95908dbc80c2245b87acdf3aad22f4d08a56f3439a972693545e.

- 2026-09-18T03:41:15+00:00: Recorded command exit 0; command argv SHA-256
  ca5426a5bef595261d46ac4e7c6950e1eb16d87edddc8a9e16f15ca1f02487d4.

- 2026-09-18T03:41:25+00:00: Recorded command exit 0; command argv SHA-256
  e54e527abf332bd4323517503eb7ede3b9934dffd14caff47613721eada35cb8.

- 2026-09-18T03:41:34+00:00: Recorded command exit 0; command argv SHA-256
  d8cacf625c2ece703436e8512f4db7fcecc6ab66bd08a25848533bca3055214d.

- 2026-09-18T03:41:45+00:00: Recorded command exit 0; command argv SHA-256
  b4feb56af55b73bd27d431f6f637dd21055975fdfbb53e2c5ccafa2a10f1e20a.

- 2026-09-18T03:41:54+00:00: Recorded command exit 0; command argv SHA-256
  2b55a39f67dc031919cdb1b04b2fccb97a61a3561aebb8c97bd09c9e39e7ee3f.

- 2026-09-18T03:42:05+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:43:17+00:00: Recorded command exit 0; command argv SHA-256
  5d8a81985e1d59659e7345b70753dcfb76e9d5e50894751a62f1347f79815a1b.

- 2026-09-18T03:43:26+00:00: Recorded command exit 0; command argv SHA-256
  5d8a81985e1d59659e7345b70753dcfb76e9d5e50894751a62f1347f79815a1b.

- 2026-09-18T03:43:36+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:43:45+00:00: Recorded command exit 0; command argv SHA-256
  69452ab6d7741db266ec2e88b5d318cf26619c3620f6b9b21c5c99cb614e2d1b.

- 2026-09-18T03:43:54+00:00: Recorded command exit 0; command argv SHA-256
  ebda9cc6dc6f481861c689a1c983b9582778e91a77ce7e65d1b1dd773018e757.

- 2026-09-18T03:44:03+00:00: Recorded command exit 0; command argv SHA-256
  c5dc8b3450edc8c1b03618b7b9cff2310bc2f515a0c767e2e905e17942a0fdb4.

- 2026-09-18T03:44:13+00:00: Recorded command exit 0; command argv SHA-256
  f3cd999d96a24a1dec2668112fd15abc5def31f5712312fc745ee0c718ee543b.

- 2026-09-18T03:44:25+00:00: Recorded command exit 0; command argv SHA-256
  68f6249b8d9158bc1d4156fa36a342156cc1ee068229abe96adbacef059022f2.

- 2026-09-18T03:46:48+00:00: Recorded command exit 0; command argv SHA-256
  83904fe776de846f86c9d0bd3a48f7a2fda735d01419fb4694534bf07aa628b1.

- 2026-09-18T03:46:57+00:00: Recorded command exit 0; command argv SHA-256
  703379e89fb68673077ec0b36bde881902efebf600add79c83164a128e20acd6.

- 2026-09-18T03:47:32+00:00: Recorded command exit 0; command argv SHA-256
  5517bbf1b8eccb2481addd26d2a46c868ed5d4b80bc4ac16890827d11efd6d6e.

- 2026-09-18T03:47:41+00:00: Recorded command exit 0; command argv SHA-256
  cedf7d8258c1e8e5c644678884a289ab0833229025187cf68ebcef2cebab247d.

- 2026-09-18T03:47:43+00:00: Recorded command exit 0; command argv SHA-256
  83904fe776de846f86c9d0bd3a48f7a2fda735d01419fb4694534bf07aa628b1.

- 2026-09-18T03:47:59+00:00: Recorded command exit 0; command argv SHA-256
  703379e89fb68673077ec0b36bde881902efebf600add79c83164a128e20acd6.

- 2026-09-18T03:48:14+00:00: Recorded command exit 0; command argv SHA-256
  336a1e61275a6dc3d11e7762a024fcaa6381d0489cda16098954535dc3aacf55.

- 2026-09-18T03:48:46+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T03:49:37+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:50:22+00:00: Fresh formal run 35304602667 is active after bus/cgroup and
  runtime-root repairs. Prior formal failures were immediate admission-lock permission errors. The
  canonical /tmp lock resides in the sticky directory; group access alone cannot open a file owned
  by another account. The runner-owned inode now admits gha-asb-state; coordinator-user
  compatibility remains an external AR-1294 lock-boundary issue and must not be hidden or bypassed.

- 2026-09-18T03:53:56+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:54:29+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:55:05+00:00: Recorded command exit 0; command argv SHA-256
  3c7898f278252722f03400a2aa7aff498cc22d0c018b6ec2c137f7f88d0dec85.

- 2026-09-18T03:55:15+00:00: Recorded command exit 1; command argv SHA-256
  71477336e01cc495e6e13f5cba39f9e7a42fa82661c1c4dd270a05a6f9abdb29.

- 2026-09-18T03:55:42+00:00: Recorded command exit 1; command argv SHA-256
  c592644c77d05e57fd8df547c6e2e5fa696e7fb5aa0ddd3fab6bf7adaf174163.

- 2026-09-18T03:55:57+00:00: Recorded command exit 0; command argv SHA-256
  8aa949aba4c6534360cf50003b60b386182f413690889cf65db8839d412c2c3b.

- 2026-09-18T03:56:19+00:00: Recorded command exit 0; command argv SHA-256
  17b43a7c826a95908dbc80c2245b87acdf3aad22f4d08a56f3439a972693545e.

- 2026-09-18T03:56:53+00:00: Recorded command exit 0; command argv SHA-256
  e23b8f7635647108873a3ca536a0c130491535517d7cc9d60eb761324b00d52c.

- 2026-09-18T03:57:05+00:00: Recorded command exit 0; command argv SHA-256
  68f6249b8d9158bc1d4156fa36a342156cc1ee068229abe96adbacef059022f2.

- 2026-09-18T03:57:34+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:57:36+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:57:49+00:00: Refreshed PR #24 onto current remote main with signed merge 436edb9cb;
  GitHub now reports mergeable=true, eliminating stale-base metadata failures. Superseded formal
  35304602667 on old head c75e1f391 was cancelled before terminal attestation; fresh exact-head
  coordination/formal runs are dispatched as 35305103755/35305104802. Do not claim formal success
  until the new run is terminal.

- 2026-09-18T03:57:58+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T03:58:24+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T04:00:56+00:00: Recorded command exit 1; command argv SHA-256
  4a26b9b2a0c8fab130b4120432e41bbeab69cb4f7770a098e467c8e109433718.

- 2026-09-18T04:01:37+00:00: Recorded command exit 0; command argv SHA-256
  6a83bd5bdd2d8995ab0ff63713774dd94c4998f5a9885ec64e909e44d70697a1.

- 2026-09-18T04:01:47+00:00: Recorded command exit 0; command argv SHA-256
  1534280499ffccb0ac81d4f26007426070f31fa576c46eba60efdb6c1bf6b8bc.

- 2026-09-18T04:01:56+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T04:02:13+00:00: Recorded command exit 0; command argv SHA-256
  17b43a7c826a95908dbc80c2245b87acdf3aad22f4d08a56f3439a972693545e.

- 2026-09-18T04:02:23+00:00: Recorded command exit 0; command argv SHA-256
  c8f42588fc15f089b11514e4f047865ddf9d106fc53ea2135d30ffa80c9ab7f8.

- 2026-09-18T04:02:36+00:00: Recorded command exit 0; command argv SHA-256
  68f6249b8d9158bc1d4156fa36a342156cc1ee068229abe96adbacef059022f2.

- 2026-09-18T04:04:01+00:00: Recorded command exit 0; command argv SHA-256
  423511aa0e6bcddc10ce1481b3b338b1c290fdc1db238a515ee25a211e43702b.

- 2026-09-18T04:04:17+00:00: Recorded command exit 0; command argv SHA-256
  21e00e7d121467608a989663d137c4d9781740c0f9f4b3581af59af91b6f989a.

- 2026-09-18T04:04:28+00:00: Recorded command exit 0; command argv SHA-256
  17b43a7c826a95908dbc80c2245b87acdf3aad22f4d08a56f3439a972693545e.

- 2026-09-18T04:04:52+00:00: Recorded command exit 0; command argv SHA-256
  dd01ecff25965f47552e3c1dd7fad75f4e79f7783aa882981932839391eff278.

- 2026-09-18T04:05:05+00:00: Recorded command exit 0; command argv SHA-256
  68f6249b8d9158bc1d4156fa36a342156cc1ee068229abe96adbacef059022f2.

- 2026-09-18T04:05:24+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-09-18T04:06:57+00:00: Recorded command exit 0; command argv SHA-256
  ec665afa3f54b0920de3af3e2544f39830b6f72b8f7d45fddbb8e144d6666ef9.

- 2026-09-18T04:07:15+00:00: Heartbeat by codex-ar1307-runner-repair2-20260918.

- 2026-09-18T04:07:58+00:00: Recorded command exit 0; command argv SHA-256
  3c7898f278252722f03400a2aa7aff498cc22d0c018b6ec2c137f7f88d0dec85.

- 2026-09-18T04:08:08+00:00: Recorded command exit 1; command argv SHA-256
  4072af302c4ca8a38151f6ad94ba9ea7e7536396674b813828a2c5962586f159.

- 2026-09-18T04:08:19+00:00: Worker interrupted after no progress beyond DCO gate; preserve PR #24
  and exact runner evidence for successor takeover.

- 2026-09-18T04:09:09+00:00: Claimed by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:09:11+00:00: Heartbeat by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:10:29+00:00: Heartbeat by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:11:32+00:00: Recorded command exit 0; command argv SHA-256
  55d215a24c8642c903b584523b5a9cfe0163d869aca6bb6f7f2f8caf668e274b.

- 2026-09-18T04:11:42+00:00: Heartbeat by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:11:58+00:00: Recorded command exit 0; command argv SHA-256
  70215bbe2ff075d1b3b6a4b143595077aad0e611d1553ef476d3ab6c3abfbf98.

- 2026-09-18T04:12:21+00:00: Recorded command exit 0; command argv SHA-256
  81f29cc480b425d081e48b84c5fa7679828251c2b4df650de783b33052a2e98d.

- 2026-09-18T04:12:31+00:00: Heartbeat by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:12:48+00:00: Recorded command exit 1; command argv SHA-256
  086e293ea833c564a0ebb1a64d1fc50406e160df8e98c09afdb873971a483131.

- 2026-09-18T04:13:38+00:00: Recorded command exit 0; command argv SHA-256
  e9aa24498c19381ad0bc8b34c7f22f51743ba83f4f764afaca9fd94b2417eaf1.

- 2026-09-18T04:13:51+00:00: Heartbeat by codex-ar1307-dco-repair-20260918.

- 2026-09-18T04:14:04+00:00: Recorded command exit 1; command argv SHA-256
  1c0a9556dac7eda968d67bf1cdf594ae4a3c85fe924051aeedd70573c03c73bd.

- 2026-09-18T04:14:35+00:00: Successor produced no DCO repair commit after repeated governed
  commands; preserve PR #24 and record exit-1 evidence for fresh takeover.

- 2026-09-18T04:15:25+00:00: Claimed by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:15:53+00:00: Heartbeat by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:16:22+00:00: Recorded command exit 0; command argv SHA-256
  2dded3768c49dbefc34cfffcf29b0ef1c16f855ff82571be4089c1156564aee1.

- 2026-09-18T04:16:47+00:00: Heartbeat by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:16:50+00:00: Recorded command exit 0; command argv SHA-256
  bf6cbe5471761fdb54b8f5bfbfee8052aab39d08056d680d4dff3b2429fe857d.

- 2026-09-18T04:17:09+00:00: Recorded command exit 0; command argv SHA-256
  5d44ebb43f6307901ce4b238cc103750638fd9bca2359f9de7713b8e3e705a4b.

- 2026-09-18T04:17:28+00:00: Recorded command exit 0; command argv SHA-256
  d2b5f586b0a27ef05ad8d15e848b321b1f51bca6e3426c5bb770cb5ea816dc55.

- 2026-09-18T04:17:48+00:00: Recorded command exit 1; command argv SHA-256
  02397c757f588240e41698378509a3419fe067ed09cfa550dce44272c57b30b5.

- 2026-09-18T04:18:08+00:00: Recorded command exit 0; command argv SHA-256
  480c00aa7181724bdc51778707a7f9992db53837eb92dc4d8435cf7425bf22d1.

- 2026-09-18T04:18:45+00:00: Recorded command exit 1; command argv SHA-256
  c9857d5f70b92759fb7f7cca67c6f29f0d8ed40e166d96178775ed0fa24b32d1.

- 2026-09-18T04:19:19+00:00: Recorded command exit 0; command argv SHA-256
  f503bd40cd8ad1c6e3a5da6867fffb52507a581f6a8d71294568eb1aceadf1fd.

- 2026-09-18T04:19:39+00:00: Heartbeat by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:19:53+00:00: Recorded command exit 0; command argv SHA-256
  62e51ca62d0261a5229f4fad0f99b3eff59471c013e0a11125615bc37c1ccc3e.

- 2026-09-18T04:20:10+00:00: Signed-history reconstruction complete: fresh worktree from base
  48c7251dd reproduced the exact 19-file implementation tree as one SSH-signed conventional commit
  969eef058 with matching author DCO. PR #24 had been closed during an erroneous canonical-HEAD
  push; the remote branch was safely corrected with a live lease and PR #25 opened at exact head
  969eef058. No merge or gate bypass occurred.

- 2026-09-18T04:20:25+00:00: Recorded command exit 0; command argv SHA-256
  e0d2a10e980da4c6e60e665aab8579043c3a2097ffcb1041ab193de4d79a27bd.

- 2026-09-18T04:20:36+00:00: Recorded command exit 0; command argv SHA-256
  61900688844340ad901685f4dc9847309292dd43b04f8e47c9c54fbe75a8403e.

- 2026-09-18T04:20:47+00:00: Recorded command exit 0; command argv SHA-256
  b19eda0c96138d0e9051838ebd16b2716de88dc262bf92d23752983e7d765df6.

- 2026-09-18T04:20:58+00:00: Recorded command exit 1; command argv SHA-256
  8ab363c01ec37f617bf12556679f69796a187be6b630df59b1eab82fa6b19be3.

- 2026-09-18T04:21:08+00:00: Recorded command exit 0; command argv SHA-256
  587fbb1c2422faa98a6f323445d4e1d84a1cffa865529a722812320944e787d0.

- 2026-09-18T04:21:19+00:00: Recorded command exit 1; command argv SHA-256
  8927f312afd1c452bdb84228a9bbadb7808c236b8b311ef06f35dee39aecc502.

- 2026-09-18T04:21:29+00:00: Recorded command exit 1; command argv SHA-256
  72fe637a4c51f06ef784af9eafb4872fb1c877213c4d3e1f7569eb32c38798ec.

- 2026-09-18T04:21:54+00:00: Recorded command exit 0; command argv SHA-256
  073ff4d7b0d402dc89da50e3cef413e9ed3c4e26d974b30429bf37bf175c6155.

- 2026-09-18T04:22:34+00:00: Recorded command exit 0; command argv SHA-256
  d5e4493105ea2babbc66a4e88d16de3bc5a5546fb9f21ba874089cd0153cc8bc.

- 2026-09-18T04:22:45+00:00: Recorded command exit 0; command argv SHA-256
  7a865997aece28f5168717aaca0df97e98252898f2295a8a8f6850ea732278ee.

- 2026-09-18T04:22:56+00:00: Recorded command exit 0; command argv SHA-256
  134753a9517a0c3e5ea0911c2882a85561281d535882acb1145b93fa0329b4ce.

- 2026-09-18T04:23:07+00:00: Recorded command exit 0; command argv SHA-256
  2b55a39f67dc031919cdb1b04b2fccb97a61a3561aebb8c97bd09c9e39e7ee3f.

- 2026-09-18T04:23:18+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T04:23:33+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T04:23:44+00:00: Recorded command exit 0; command argv SHA-256
  555b57488f4ca463442cedc0f8c220b3b9b3c6ec8a7f9dece458a7f4663a291c.

- 2026-09-18T04:23:56+00:00: Recorded command exit 0; command argv SHA-256
  90324e68a8218c374c59c66a9a68b489ce047dea97d73091bbf9cf63b2b1ba08.

- 2026-09-18T04:24:13+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T04:24:25+00:00: Recorded command exit 0; command argv SHA-256
  4ad2a0043330ee14b807dc825bdbbb56042256a1fe3f8b1c4bd605b8df60099e.

- 2026-09-18T04:25:08+00:00: Recorded command exit 0; command argv SHA-256
  99ca51039acb1eb7ac4037dddd0c1ff06ae3fd1577521df105449ff7c884bd7a.

- 2026-09-18T04:28:27+00:00: Qualification is active at exact PR #25 head 969eef058. Hosted
  coordination 35306743512, Huawei headers 35306794847, and AWQ shadow 35306806803 passed. Formal
  35306838470 passed runner/user-bus setup and is executing the exhaustive model. Stale formal
  35305564895 from closed PR #24 was canceled after confirming no process or admission-lock holder.

- 2026-09-18T04:42:58+00:00: Recorded command exit 0; command argv SHA-256
  b0e7cd52047c90483fbd7dbe9a751e40e20aee93f107df8643206e4be9fde988.

- 2026-09-18T04:43:58+00:00: Recorded command exit 0; command argv SHA-256
  a1e68d7cb07d03bc3813b7fd0f4fbd27d981c2f7850bc5b0b113683345c72d0c.

- 2026-09-18T04:44:33+00:00: Recorded command exit 0; command argv SHA-256
  e77d924b8c969291ab12953afb5874659af542f62e7b3c66cf7bdc9b6019bf9d.

- 2026-09-18T04:45:02+00:00: Formal run 35306838470 at PR #25 exact head 969eef058 was canceled
  after exceeding the 15-minute workflow budget (active 04:25:35-04:43:10Z); it produced no
  qualification result. Cancellation left TLC PGID 1802733; exact stale process was terminated. Four
  older orphan TLC process groups (1418396, 1425100, 1501586, 1555250, 1578798) were also verified
  against zero active formal runs and terminated through governed cleanup. Coordination 35308021341
  failed on canonical metadata (AR-1293 next_action length and missing observed heads/checkpoints);
  main metadata repair and PR refresh are required before the next formal run.

- 2026-09-18T04:45:06+00:00: Heartbeat by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:46:26+00:00: Heartbeat by codex-ar1307-signed-history-20260918.

- 2026-09-18T04:46:49+00:00: Worker stopped after cleanup with no metadata-repair commands; preserve
  PR #25 and formal cancellation evidence for fresh takeover.

- 2026-09-18T04:47:59+00:00: Claimed by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T04:48:46+00:00: Recorded command exit 1; command argv SHA-256
  c9b630ff5832780fd6e79aadbbc0de855766c9f9ee8d6c6ab7a89aa97d80b620.

- 2026-09-18T04:49:20+00:00: Recorded command exit 1; command argv SHA-256
  d0714db67a0615f15cdb0e07755954cced2e0de4fae2ddb5cbd22dfd9adddb10.

- 2026-09-18T04:49:46+00:00: Recorded command exit 0; command argv SHA-256
  d231e1be1f2229323360a85ad24d6bb68b55aa5e1651e0b7fbb8e9cacbdb1796.

- 2026-09-18T04:50:23+00:00: Recorded command exit 0; command argv SHA-256
  16f8d5fa50edfc6346880e6b75220f38d567904789e219ac352735dda1752c4e.

- 2026-09-18T04:50:41+00:00: Recorded command exit 0; command argv SHA-256
  83f67eb7b93e437e52dd3293e2e504de27b4a180d0495679315faaa6d106876b.

- 2026-09-18T04:51:14+00:00: Recorded command exit 0; command argv SHA-256
  970039ba3b995d45350cb6b8bbf35de451893de49fd0ea159c1aaf3184471027.

- 2026-09-18T04:51:24+00:00: Recorded command exit 0; command argv SHA-256
  abae92fb336bfb1d1b2946a3655d20712aa179c0d9964f6f3376b7bdda983ebe.

- 2026-09-18T04:51:38+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-18T04:52:09+00:00: Recorded command exit 0; command argv SHA-256
  5c9f6dd02d2a6bb9881aa920884767bd803b8fefe6e1a5f9b59746f8596b8a6d.

- 2026-09-18T04:52:23+00:00: Recorded command exit 1; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T04:52:54+00:00: Recorded command exit 0; command argv SHA-256
  05dc4d67fec9a6f2dbb0d5d09d2981b7d49a4c8aba9be27d1ac9a42cbdf55e7d.

- 2026-09-18T04:53:04+00:00: Recorded command exit 128; command argv SHA-256
  0078fb6010687bc03868593a2946a5f25404844f6a919ccf2374086dd70ea6f5.

- 2026-09-18T04:53:18+00:00: Recorded command exit 0; command argv SHA-256
  dbd59e4625cbb09c41bf08d0c8a777b023f55aa72218f99e0c2dfa5c0432c165.

- 2026-09-18T04:53:58+00:00: Recorded command exit 0; command argv SHA-256
  37888fdab1ee927f56467b97c1d38a46bcd27c49d9bd63d57f612459e40fec5c.

- 2026-09-18T04:54:07+00:00: Recorded command exit 0; command argv SHA-256
  e3b429d935995216848e305ea515a90d24e8de42def81761352afac9bdb9c176.

- 2026-09-18T04:54:16+00:00: Recorded command exit 0; command argv SHA-256
  376abacbd7300efd0048e1edceda21b7c30df504d8978b30a13809b9dbe9fda8.

- 2026-09-18T04:54:38+00:00: Recorded command exit 0; command argv SHA-256
  eb4df5fab7f6ef09de04f34d69429f595466c894d312394e4e8fa379c8f1baaf.

- 2026-09-18T04:54:47+00:00: Recorded command exit 0; command argv SHA-256
  3ea546a29e89dac02ad15308e15d9bc43c5b34fd9674b950870fcfa3e3bc70ba.

- 2026-09-18T04:55:03+00:00: Recorded command exit 0; command argv SHA-256
  e36cf196280844f9fe407c6bb682880f8f06ef122b2b71097f4415f753e1cb64.

- 2026-09-18T04:56:38+00:00: Recorded command exit 0; command argv SHA-256
  5c9f6dd02d2a6bb9881aa920884767bd803b8fefe6e1a5f9b59746f8596b8a6d.

- 2026-09-18T04:56:47+00:00: Recorded command exit 1; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T04:57:05+00:00: Recorded command exit 0; command argv SHA-256
  12e44f59ff090b4553d6d3a18ed1dad104246071110212e71a06c7aa83c3f52a.

- 2026-09-18T04:57:15+00:00: Recorded command exit 0; command argv SHA-256
  9952b461450f036400e6670991337464829337a8c9d3288dcef9289337cd6639.

- 2026-09-18T04:57:24+00:00: Recorded command exit 0; command argv SHA-256
  dbd59e4625cbb09c41bf08d0c8a777b023f55aa72218f99e0c2dfa5c0432c165.

- 2026-09-18T04:57:57+00:00: Recorded command exit 0; command argv SHA-256
  9e1b95c9789ef4dc0be0d9c782ca13435b612d5da0618d006ce4da6ee17c57aa.

- 2026-09-18T04:59:13+00:00: Recorded command exit 0; command argv SHA-256
  2ff89a80259af4c0c030172c92b9b7029d3a3dc5fc7cf8873a47aefabd4e2848.

- 2026-09-18T04:59:22+00:00: Recorded command exit 0; command argv SHA-256
  5d6fa4f1e0857b97a02a1917ff8916b1bed295106780d305ca0a7596baa35ee8.

- 2026-09-18T04:59:31+00:00: Recorded command exit 0; command argv SHA-256
  2adace28d5a45d073f5ea31113b0759b1604f74fe7c53d323341da1169cf7f96.

- 2026-09-18T04:59:54+00:00: Recorded command exit 0; command argv SHA-256
  723077027dd3209d7c4de232e9a080a1ad509adcf5d568101e069808baf547dc.

- 2026-09-18T05:01:12+00:00: Recorded command exit 0; command argv SHA-256
  31a4e8cc49dceb837d44645471bcd5ae0ea7ee11334cf36a750e217a6569d24f.

- 2026-09-18T05:01:21+00:00: Recorded command exit 0; command argv SHA-256
  9952b461450f036400e6670991337464829337a8c9d3288dcef9289337cd6639.

- 2026-09-18T05:01:30+00:00: Recorded command exit 0; command argv SHA-256
  24e2da4a36fccb3a0fc4ee87e7d3fbb5d402bfd58f3f2b99797bcc4a208cd95a.

- 2026-09-18T05:01:51+00:00: Recorded command exit 1; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T05:02:07+00:00: Recorded command exit 0; command argv SHA-256
  12e44f59ff090b4553d6d3a18ed1dad104246071110212e71a06c7aa83c3f52a.

- 2026-09-18T05:02:16+00:00: Recorded command exit 0; command argv SHA-256
  9952b461450f036400e6670991337464829337a8c9d3288dcef9289337cd6639.

- 2026-09-18T05:02:26+00:00: Recorded command exit 0; command argv SHA-256
  dbd59e4625cbb09c41bf08d0c8a777b023f55aa72218f99e0c2dfa5c0432c165.

- 2026-09-18T05:02:49+00:00: Recorded command exit 0; command argv SHA-256
  c5d43a58421492ed72061cf201f83f05afb9449eea6317df0d180e4f69268ec1.

- 2026-09-18T05:04:02+00:00: Recorded command exit 0; command argv SHA-256
  52e8d819883bdb6609bdded4ea222914a9427d62d52051c2d319f806f1bb6538.

- 2026-09-18T06:03:33+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T06:03:52+00:00: Formal run 35309351851 at exact head
  b2010efb550b26954216122dbfd573350080c24f terminated at 06:00:52Z with full-exhaustive exit 1: TLC
  execution failed closed and emitted no success attestation. Qualification is not established;
  preserve this failure as the blocking evidence.

- 2026-09-18T06:05:16+00:00: Recorded command exit 0; command argv SHA-256
  5c9f6dd02d2a6bb9881aa920884767bd803b8fefe6e1a5f9b59746f8596b8a6d.

- 2026-09-18T06:05:25+00:00: Recorded command exit 1; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T06:05:43+00:00: Recorded command exit 0; command argv SHA-256
  fc62cc39ea472564a0c0f6dff2605161cd79ce67d5fa61915c294c71d0382e80.

- 2026-09-18T06:05:52+00:00: Recorded command exit 0; command argv SHA-256
  5d6fa4f1e0857b97a02a1917ff8916b1bed295106780d305ca0a7596baa35ee8.

- 2026-09-18T06:06:02+00:00: Recorded command exit 1; command argv SHA-256
  dbd59e4625cbb09c41bf08d0c8a777b023f55aa72218f99e0c2dfa5c0432c165.

- 2026-09-18T06:06:16+00:00: Recorded command exit 1; command argv SHA-256
  bdfff1441cdb607f8f38b1b88268caabde80c04bc511e213369abacb9787f616.

- 2026-09-18T06:06:30+00:00: Recorded command exit 1; command argv SHA-256
  bdfff1441cdb607f8f38b1b88268caabde80c04bc511e213369abacb9787f616.

- 2026-09-18T06:06:44+00:00: Recorded command exit 0; command argv SHA-256
  bdfff1441cdb607f8f38b1b88268caabde80c04bc511e213369abacb9787f616.

- 2026-09-18T06:07:07+00:00: Recorded command exit 0; command argv SHA-256
  e3ca701ac439f201fb5728ff19f6da83b6bcb3544668d640768e63918e114e22.

- 2026-09-18T06:07:16+00:00: Recorded command exit 0; command argv SHA-256
  de1681974b12374cc96b87b5d3d52965140e37aacf020b5aa236da23ebcad0d1.

- 2026-09-18T06:07:25+00:00: Recorded command exit 0; command argv SHA-256
  8bcc7b28e40a74ed11b11b7ba339d994a34666b8e2e2886b85a9a93429f7698b.

- 2026-09-18T06:11:16+00:00: Recorded command exit 2; command argv SHA-256
  cf4ba9666053762f36317a651254413a2cf9c7bb10bcd34b359d2781caae2dd3.

- 2026-09-18T06:11:37+00:00: Recorded command exit 2; command argv SHA-256
  4b034b36a0a3c9b99e0f80c0ddb0a6939f1f1dadb797afe53fab47827c9631b9.

- 2026-09-18T06:11:53+00:00: Recorded command exit 0; command argv SHA-256
  89d5ee043b0d73389da2dd7818b7f06769d7f3cd0f93cb04e31800be286cbb4a.

- 2026-09-18T06:12:17+00:00: Recorded command exit 0; command argv SHA-256
  985fc24287413e2a4f2dce40842ed82247f31ce2d8992373716ddfcf472922d1.

- 2026-09-18T06:12:32+00:00: Recorded command exit 0; command argv SHA-256
  ebfae1e745d76cc3ac0bc02906a32ffd0c572458db0fc1c4cb4f537da1262417.

- 2026-09-18T06:13:20+00:00: Recorded command exit 0; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T06:13:45+00:00: Recorded command exit 0; command argv SHA-256
  f3fc3934df4dee817adf6d4702641c8286e0f9944ac55b04fa56556f5dbb4212.

- 2026-09-18T06:14:06+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T06:14:28+00:00: Formal run 35309351851 terminated 2026-09-18T06:00:52Z at exact head
  b2010efb5 with exit 1: TLC execution failed closed and emitted no success attestation. Corrective
  change 25ab3b860 now requires an offline preloaded non-symlink TLC JAR with reviewed SHA-256,
  rejects network fallback, removes guest curl probing, and adds negative coverage. PR #25 was
  rebased onto current main and force-with-lease pushed; exact head is 25ab3b860. Remaining
  measured-attestation and isolated-runner evidence gates are unresolved.

- 2026-09-18T06:15:25+00:00: Recorded command exit 0; command argv SHA-256
  47e2a8aae25a481f256bc44385000d949087e0d58dffc080eb85ccd6108d9a02.

- 2026-09-18T06:15:34+00:00: Recorded command exit 0; command argv SHA-256
  03e320525e6e65b8e2c7297cd352831b7378dec8c8b3371b6cd8b52de55117bf.

- 2026-09-18T06:15:52+00:00: Recorded command exit 0; command argv SHA-256
  b16a582181226e889b4aefee4766b22f9c7c055eae316a4689ec2207b459272e.

- 2026-09-18T06:17:04+00:00: Recorded command exit 0; command argv SHA-256
  a83ed8fda2b9bed5456e3d72d7279694cee35f1ac6c6b671cfe91efd87c6540c.

- 2026-09-18T06:17:13+00:00: Recorded command exit 0; command argv SHA-256
  6faef4144b15fc1cb3bd14c1ba10a369fba21d8a3edec3568188bad000d43b06.

- 2026-09-18T06:17:30+00:00: Recorded command exit 0; command argv SHA-256
  94773150445c6eb0da915a639ca86724b5dcc0b83f92fe61170089292a94043a.

- 2026-09-18T06:18:45+00:00: Recorded command exit 0; command argv SHA-256
  89d5ee043b0d73389da2dd7818b7f06769d7f3cd0f93cb04e31800be286cbb4a.

- 2026-09-18T06:19:01+00:00: Recorded command exit 0; command argv SHA-256
  120f88ac029857aba3a22cfa602de3316ddb38c621a7540bc356789abfed8724.

- 2026-09-18T06:19:10+00:00: Recorded command exit 0; command argv SHA-256
  3aba22e82c2358ac15793d1d347b7e31a65e8ca3162e5f37f9ac9a4a24b440ad.

- 2026-09-18T06:19:27+00:00: Recorded command exit 0; command argv SHA-256
  c797acf72d668ca2af6d60b41797423c0d4fdd8dd97930ef5a575612cb501d55.

- 2026-09-18T06:19:48+00:00: Exact-head formal run 35314250213 on 57fcb60eb failed closed before
  TLC: runner could not open host-owned /tmp/agent-workflow-coordinator-tlc-admission.lock
  (permission denied). Corrective signed head cd33b1b04 relocates the canonical shared admission
  fence to /srv/data/projects/.asb-tlc/admission.lock and updates focused tests/docs. Focused tests
  passed (61); pushed with force-with-lease. No qualification or merge claim.

- 2026-09-18T06:20:23+00:00: Recorded command exit 0; command argv SHA-256
  af9af4914ab50cd5a7c99d853b116f42da6960721689ceb3cced5416e2fe63ba.

- 2026-09-18T06:20:32+00:00: Recorded command exit 0; command argv SHA-256
  49410a7c0823a8b7fcad6a1f809d8657ace7ac733c85b1386fa3334e3e57a54d.

- 2026-09-18T06:20:43+00:00: Recorded command exit 0; command argv SHA-256
  e675c83ca414267e8a75949663be628075f423f0ea4e210079a9858933632b83.

- 2026-09-18T07:30:28+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T07:30:48+00:00: Formal run 35314479090 reached terminal failure at 2026-09-18T07:21:49Z
  on exact head 9c06f0108. Offline artifact preflight and admission succeeded, but full-exhaustive
  TLC failed closed with exit 1 and emitted no success attestation. Strict consistency additionally
  reported Ruff formatting required at tests/test_tlc_runner.py:534. Lease renewed through
  2026-09-18T09:30:28Z; owner preserved.

- 2026-09-18T07:31:19+00:00: Recorded command exit 1; command argv SHA-256
  459b61b713802798fa25e4b0f6d8c0f70efc7b1c826e044597da33a87152bb03.

- 2026-09-18T07:32:44+00:00: Recorded command exit 0; command argv SHA-256
  89d5ee043b0d73389da2dd7818b7f06769d7f3cd0f93cb04e31800be286cbb4a.

- 2026-09-18T07:33:07+00:00: Recorded command exit 0; command argv SHA-256
  6b410db74070775f5b0be75bdfef15cb035aeeb53dd9fe0ca4297861912b4462.

- 2026-09-18T07:33:18+00:00: Recorded command exit 0; command argv SHA-256
  ebc6b8f6877ce985463b0de844dfc95c2653f3290b7249216b89a3288cae5d57.

- 2026-09-18T07:33:35+00:00: Recorded command exit 0; command argv SHA-256
  e819c0f0383ba16de699e705921636269f94694e773c4d3c4fbeaa3145df1d7c.

- 2026-09-18T07:33:59+00:00: Root cause investigation reproduced the post-admission failure locally:
  attest.py rejected the approved /srv/data/projects runtime evidence path because it incorrectly
  required paths under the source checkout. Portable-smoke then passed after binding path validation
  to the approved runtime root. Corrective signed head f33c250cb also fixes Ruff formatting in
  tests/test_tlc_runner.py. Focused tests 61 passed; Ruff format/check passed. Prior full run
  35314479090 remains failed and is not reused as qualification.

- 2026-09-18T08:45:59+00:00: Formal run 35320006238 reached terminal failure at 2026-09-18T08:36:56Z
  on exact head f33c250cb. Offline preflight/admission passed, but full-exhaustive TLC failed closed
  with exit 1 and no success attestation. This repeats the prior TLC exit-1 after the attestation
  path fix; no qualification or merge claim. Strict consistency also requires generated
  CURRENT_MANIFEST_SHA256 to match coordinator.vendor.json.

- 2026-09-18T08:46:22+00:00: Recorded command exit 150; command argv SHA-256
  7473069b52932a64def25a1a7aac8d4f615f77111c4e5bb377934b297d543dac.

- 2026-09-18T08:47:53+00:00: Recorded command exit 0; command argv SHA-256
  8823ebcb3594bbdbe901b61fd203e52dbfccb33741e50b8281b0c6640b9036f2.

- 2026-09-18T08:48:10+00:00: Recorded command exit 0; command argv SHA-256
  69de86c42d2ab064eadb704136aa14fb359c6c6ddeed6a494b4ddae5a4092a04.

- 2026-09-18T08:48:21+00:00: Recorded command exit 0; command argv SHA-256
  2864f7dfa7b13861ad533a1223a91f11024730195e70a5044d1ac012025ebc00.

- 2026-09-18T08:48:38+00:00: Recorded command exit 0; command argv SHA-256
  4b8d9e442d53e7dec4d7d74066a0543533fe714d28d09d92fe236a27afcb6a02.

- 2026-09-18T08:49:32+00:00: Recorded command exit 0; command argv SHA-256
  56cab30f39e4d9acd7a29da80507d04eb320927112481952941dc173fb87f45e.

- 2026-09-18T08:49:51+00:00: Recorded command exit 0; command argv SHA-256
  86d93339f32b489572659749577ec463a7b89d5ed5ce089a6f4f0bdbe6856568.

- 2026-09-18T08:50:02+00:00: Recorded command exit 0; command argv SHA-256
  04d13a8fe1a39467cd8054d16631c7943f641ad1b6551594d970d0ac412e295a.

- 2026-09-18T08:50:19+00:00: Recorded command exit 0; command argv SHA-256
  71bfff740cf83bc2f932ddeb467f18ce69d26b0d549b15fabb5de52878f3173e.

- 2026-09-18T08:50:42+00:00: Generated vendor manifest fixture was refreshed to
  coordinator.vendor.json SHA-256 69e39095876e048d25f7fb0a661e72e34421d9bc758e7d635c427a0982a63af8;
  vendor suite passed 8 tests/6 subtests. Repeated full-exhaustive failure remains exit 1 with no
  stderr detail. Signed head fb90e13f7 now captures bounded sanitized TLC stdout plus stderr on
  nonzero exit, preserving fail-closed behavior and enabling diagnosis on the next required formal
  run. Focused suite: 69 passed, 6 subtests.

- 2026-09-18T09:23:26+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T09:55:54+00:00: Formal run 35326417135 terminated at 2026-09-18T09:42:53Z on exact head
  fb90e13f7. Offline preflight/admission passed; TLC ran with 2 workers/2 cores, approximately
  1979MB heap and 64MB offheap, reaching about 32.86M generated, 27.20M distinct states, and 10.8M
  queued states before exit 1. No invariant/OOM detail appeared in bounded diagnostics and no
  success attestation was emitted. This is a truthful formal failure, not qualification.

- 2026-09-18T09:56:59+00:00: Recorded command exit 0; command argv SHA-256
  9534ff79d2070569dbb5ef70f5426132813a345733894b15c3af55cccb73055c.

- 2026-09-18T09:57:22+00:00: Recorded command exit 0; command argv SHA-256
  993f351065a75ef29e29982de1a25f42d21afd0093f387a7e09d42597b403d4f.

- 2026-09-18T09:57:49+00:00: Recorded command exit 0; command argv SHA-256
  b9d269555ef5771ea36092e556f5d7760a270906193e950850a500bc5f40865a.

- 2026-09-18T09:58:14+00:00: Reconstructed feature history onto current main and re-signed every
  commit with SSH signatures. Author is Martin Beck <martin.beck2@gmx.de>; each rewritten commit now
  includes matching Signed-off-by Martin Beck <martin.beck2@gmx.de> (legacy huawei trailer
  retained). Force-with-lease pushed exact head 590dd6c5d. Formal failure 35326417135 remains
  recorded: ~32.86M generated, ~27.20M distinct, ~10.8M queued states, exit 1, no attestation. No
  merge or qualification claim.

- 2026-09-18T11:06:35+00:00: Formal run 35332252619 failed at 2026-09-18T11:00:00Z on exact head
  590dd6c5d after approximately 62 minutes. TLC used 2 workers/2 cores, ~1979MB heap and 64MB
  offheap, reached ~33.145M generated, ~27.489M distinct states, and ~10.805M queued states, then
  exited 1. No invariant, OOM, or explicit termination text was emitted. DCO/vendor/strict CI is
  green; formal evidence remains failed. Do not widen limits or claim success.

- 2026-09-18T11:07:20+00:00: Recorded command exit 0; command argv SHA-256
  ca3bf4b5e4c41b9198930ceec09c95237dd912bde652a01c535e1dfa690d6de4.

- 2026-09-18T11:08:31+00:00: Recorded command exit 0; command argv SHA-256
  ca3bf4b5e4c41b9198930ceec09c95237dd912bde652a01c535e1dfa690d6de4.

- 2026-09-18T11:12:03+00:00: Recorded command exit 0; command argv SHA-256
  86d93339f32b489572659749577ec463a7b89d5ed5ce089a6f4f0bdbe6856568.

- 2026-09-18T11:12:14+00:00: Recorded command exit 0; command argv SHA-256
  b9266ea2169b554aa92f49e91e4a3ba4bf1ab08273b77654d988a80eb7f572bb.

- 2026-09-18T11:12:22+00:00: Recorded command exit 128; command argv SHA-256
  3aa8227eccc225182e16d94abd6aeaae5b3140cd5c61742d77fa0605350f6ae7.

- 2026-09-18T11:14:45+00:00: Recorded command exit 0; command argv SHA-256
  cefabea447aa1bc89820f8e48ebbf27621b6d2c25b0e140b7b7bd4097ae82de7.

- 2026-09-18T11:16:27+00:00: Recorded command exit 128; command argv SHA-256
  3aa8227eccc225182e16d94abd6aeaae5b3140cd5c61742d77fa0605350f6ae7.

- 2026-09-18T11:29:16+00:00: Recovered expired claim formerly owned by
  codex-ar1307-metadata-repair-20260918. Recovered expired AR-1307 claim during routine coordination
  doctor; no product mutation or worker launch performed. Preserve next_action and require explicit
  re-claim before work resumes.

- 2026-09-18T11:33:26+00:00: Claimed by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T11:33:40+00:00: Reclaimed after lease expiry. Local signed PR head c5f6ad076 preserves
  bounded TLC terminal-tail diagnostics; remote remains 590dd6c5d. Governed publication is blocked
  by GitHub HTTPS 403: account email must be verified. State claim/update is local-only until that
  external blocker is cleared; no credential bypass or push retry.

- 2026-09-18T11:54:52+00:00: Recorded command exit 0; command argv SHA-256
  3aa8227eccc225182e16d94abd6aeaae5b3140cd5c61742d77fa0605350f6ae7.

- 2026-09-18T11:57:02+00:00: Recorded command exit 1; command argv SHA-256
  e7ea8081082b5a1c09fe998e9f3669738759a142e3c9e1ab3c35ebe101528297.

- 2026-09-18T11:57:29+00:00: Recorded command exit 0; command argv SHA-256
  e7ea8081082b5a1c09fe998e9f3669738759a142e3c9e1ab3c35ebe101528297.

- 2026-09-18T11:57:43+00:00: Recorded command exit 0; command argv SHA-256
  167de933fa2cc9c13527301cebf87538309c13bbdf36b7db0be25b59537e0c0c.

- 2026-09-18T11:57:56+00:00: Recorded command exit 0; command argv SHA-256
  b06f2f731b92610fff2de2d71517ce00b36f79839a47b4420bdbf0c528602874.

- 2026-09-18T11:58:16+00:00: Recorded command exit 0; command argv SHA-256
  0e92e196575dc8ec44c6e1c9af547c4f4e069e052f47e7299a7a04d858a4cf49.

- 2026-09-18T11:58:31+00:00: Recorded command exit 0; command argv SHA-256
  9e3a05058d9782060af052b30d8edabed1bc1e990156ecc35b5176f7bec30b14.

- 2026-09-18T11:58:47+00:00: Recorded command exit 0; command argv SHA-256
  93c88769ba907764b56da5c5e4001556dd231fa98028dc114fb40f18614d057b.

- 2026-09-18T11:59:55+00:00: Recorded command exit 1; command argv SHA-256
  e7ea8081082b5a1c09fe998e9f3669738759a142e3c9e1ab3c35ebe101528297.

- 2026-09-18T12:00:27+00:00: Recorded command exit 0; command argv SHA-256
  e7ea8081082b5a1c09fe998e9f3669738759a142e3c9e1ab3c35ebe101528297.

- 2026-09-18T12:00:44+00:00: Recorded command exit 0; command argv SHA-256
  86d93339f32b489572659749577ec463a7b89d5ed5ce089a6f4f0bdbe6856568.

- 2026-09-18T12:01:07+00:00: Recorded command exit 0; command argv SHA-256
  f24e2f30b3ff7c12f32b6e634acac8f6f4fa11933fadcd76960cf8e3db67ea2b.

- 2026-09-18T12:01:26+00:00: Recorded command exit 0; command argv SHA-256
  b3975316cf31e1e1d808b06fff1d9348a96fbc473193c439170ad45c82e765f7.

- 2026-09-18T12:02:58+00:00: Resolved GitHub email-verification 403. Published signed diagnostics
  repair head ab485f767 after fixing fresh-run and direct-test temp-directory initialization.
  Exact-head verify, AWQ shadow, and strict coordination checks are green; formal run 35342513872 is
  active. No qualification or merge claim yet.

- 2026-09-18T12:04:30+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T12:35:28+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T13:06:10+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T13:37:41+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T13:37:55+00:00: Terminal formal evidence: run 35342513872, exact head ab485f767, failed
  closed because Java ran out of memory during liveness checking after approximately 45.77M
  generated and 37.99M distinct states; no invariant error. Existing 3G memory and 3G swap limits
  were not widened. AR-1307 remains in progress and unqualified pending governed capacity
  successor/acceptance decision.

- 2026-09-18T13:40:17+00:00: Recorded command exit 0; command argv SHA-256
  298c7f934e72d4c00af00f4795e93de1eb7f2d7d7ffd218e818f4bc2311ffb32.

- 2026-09-18T13:40:39+00:00: Recorded command exit 0; command argv SHA-256
  cab31349ac235baaea2cea9382b0c34a892b15caa7c4bd3235edb0de243162a2.

- 2026-09-18T13:41:06+00:00: Created follow-on AR-1308 with dependency on done AR-1304. It owns
  measured disposable QEMU/container capacity, exact AR-1307 inputs, bounded diagnostics and
  terminal full-exhaustive qualification; no limit widening or gate weakening. AR-1307 remains open
  and claimed.

- 2026-09-18T13:46:24+00:00: Heartbeat by codex-ar1307-metadata-repair-20260918.

- 2026-09-18T14:22:58+00:00: Recovered expired claim formerly owned by
  codex-ar1307-metadata-repair-20260918. 2026-09-18T16:26:00+02:00: Expired metadata-repair claim
  found with no active worker; released claim for safe future reassignment. No implementation state
  changed.

- 2026-09-18T16:25:22+00:00: Claimed by codex-ar1307-qualification-20260918.

- 2026-09-18T16:26:41+00:00: Qualification audit 2026-09-18: PR #25 exact head ab485f767 has green
  coordination/AWQ/source-header checks but required formal workflow 35342513872 failed closed
  during liveness checking after 37,986,996 distinct states because Java exhausted the existing 3G
  heap/swap contract; no attestation was emitted. AR-1308 is the approved capacity follow-on and is
  currently blocked after its first disposable QEMU bootstrap produced no evidence due the reviewed
  fixture/seed JDK path mismatch. Preserve the runner implementation and 3G/3G limits; no merge or
  qualification claim. Next action: wait for AR-1308 to repair and validate the disposable x86_64
  QEMU fixture and produce exact AR-1307-head capacity evidence, then rerun canonical
  full-exhaustive through verify.sh/tlc_runner.py without changing limits.

- 2026-09-26T18:47:21+00:00: Reopen for coordinator audit: current PR #25 head is ab485f767, while
  prior metadata expected 969eef058; hosted formal still fails only at full-exhaustive liveness due
  Java OOM. Refresh exact dependency and preserve fail-closed status.

- 2026-09-26T18:47:24+00:00: Claimed by coordinator-ar1307-audit.

- 2026-09-26T18:47:39+00:00: Coordinator audit refreshed current PR and formal failure evidence; no
  source mutation and no qualification claim.
