---
{
  "branch": "feature/ar-1767-safe-directory-preparation-and-notice",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T20:42:45+00:00",
  "depends_on": [
    "AR-1766"
  ],
  "id": "AR-1767",
  "next_action": "Run full cargo test -p asb-cli and git diff review; then implement or explicitly document remaining TOCTOU/dry-run matrix gaps before signed commit.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1767-directory-preparation",
  "plan": "../plans/AR-1767-safe-directory-preparation-and-notice.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1767.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1767.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Implementing safe directory preparation and notices for command-owned ASB outputs.",
  "task_revision": 42,
  "title": "Safe automatic directory preparation with clear notice",
  "updated_at": "2026-10-09T18:44:30+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1767-safe-directory-preparation-and-notice"
}
---

Audit and normalize every ASB setup-like command and output path that assumes a
directory for configuration, project metadata, installed tools, generated
catalogs, plans, run results, reports, recordings, cassettes, lifecycle state, or
other command-owned files. If a safe missing directory is required, human mode
must say concisely which directory ASB will create and why, then create it without
requiring the user to run `mkdir` or reconstruct a parent path.

Do not auto-create input locations or weaken path safety. Missing input, an
existing non-directory, a symlinked/replaced ancestor, unsafe traversal,
permission denial, read-only storage, ownership/mode rejection, and concurrent
replacement remain distinct typed failures. Creation must retain private modes
where configuration or credential references require them, use descriptor-safe
and atomic publication where applicable, and clean only transaction-owned
temporary artifacts.

The pre-effect notice belongs on the human diagnostic/progress stream so it
cannot corrupt `--json` stdout. Dry-run says what would be created and performs
no mutation. Successful output identifies a created or reused directory only
when useful; repeated commands must not claim an existing directory was new.


- 2026-10-09T18:20:19+00:00: AR-1766 is released done with all post-merge gates; promoting
  diagnostic follow-up.

- 2026-10-09T18:20:28+00:00: Claimed by codex-ar1767-directory-preparation.

- 2026-10-09T18:20:59+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:21:12+00:00: Recorded command exit 0; command argv SHA-256
  98f5431e8dc98b26a060a4f4013f007fe195fe41ab9e671f68ad46a03857e36b.

- 2026-10-09T18:21:40+00:00: Recorded command exit 0; command argv SHA-256
  d0ece56679d6230bfa4ead84bdb4f2dfe364fc73f2a618c57d06130183ef6582.

- 2026-10-09T18:22:03+00:00: Recorded command exit 255; command argv SHA-256
  2c7fa74981fd8a14c97a3f8012adc6dc195f6871931853b919ed83dc9480d2b8.

- 2026-10-09T18:22:26+00:00: Recorded command exit 0; command argv SHA-256
  e8fdc6d25a72c71618842ed1478c8fcc866bc52b9f9f48e124fe6bbc8c529831.

- 2026-10-09T18:23:27+00:00: Checkpoint: verified AR-1767 docs/spec and AR-1766 merged diagnostic
  catalog; audited ConfigStore, project init, tool install, easy lifecycle, plan-create, run roots,
  recording and TUI output paths. Initial wrapped worktree bootstrap recorded a post-reconcile
  failure because generated tools/__pycache__/handoffctl.cpython-312.pyc exceeded the state size
  guard; repaired the worktree identity to the declared exact key. Begin central safe directory
  primitive and notice wiring.

- 2026-10-09T18:25:11+00:00: Recorded command exit 0; command argv SHA-256
  04597771a78482782e94f4b4a7461fdfebe693705c12334334d2989f552076d3.

- 2026-10-09T18:25:48+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:26:59+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:27:04+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:28:06+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:28:45+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:29:22+00:00: Recorded command exit 0; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:30:53+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:30:58+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:31:24+00:00: Recorded command exit 101; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:31:54+00:00: Recorded command exit 0; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:33:05+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:33:17+00:00: Checkpoint 2026-10-09T18:33Z: exact worktree/branch is prepared and
  current diff is limited to directory-preparation wiring plus human error path context. Prior cargo
  check passed before the latest wrapper cleanup; rerunning once now, then advancing immediately to
  focused tests. Wrapper post-reconcile may report COMMAND_RECORDED_POST_RECONCILE_FAILED because
  generated tools/__pycache__/handoffctl.cpython-312.pyc exceeds the 200 KiB repository evidence
  limit; preserve that failure as durable infrastructure evidence.

- 2026-10-09T18:33:24+00:00: Recorded command exit 0; command argv SHA-256
  5aeee75da362015528ba446d4ea84b5ce1f343e91b43718b1ab6b9f8514cc5a2.

- 2026-10-09T18:34:13+00:00: Recorded command exit 101; command argv SHA-256
  b470b3aef8671ea54bcc1116d5e74efb4c80157f0f5583e2241674d1e4d21dfb.

- 2026-10-09T18:35:09+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:35:14+00:00: 2026-10-09T18:35Z: cargo check -p asb-cli completed successfully
  (Finished dev profile), but handoffctl post-reconcile reported
  COMMAND_RECORDED_POST_RECONCILE_FAILED because tools/__pycache__/handoffctl.cpython-312.pyc
  exceeds the 200 KiB evidence limit. First cargo test --no-run exposed two stale test call sites
  (removed test-only tool wrapper and missing None progress argument); both are repaired, and
  focused directory tests were added with positive creation/reuse, exact stderr notice,
  traversal/file/symlink rejection, and machine-JSON path redaction coverage.

- 2026-10-09T18:35:24+00:00: Recorded command exit 101; command argv SHA-256
  b470b3aef8671ea54bcc1116d5e74efb4c80157f0f5583e2241674d1e4d21dfb.

- 2026-10-09T18:35:48+00:00: 2026-10-09T18:36Z: cargo test -p asb-cli --no-run reached test
  compilation but -D warnings rejected an unused legacy guided_setup wrapper. Removed that dead
  wrapper; no product behavior was implicated. The wrapper again recorded the command then failed
  only in post-reconcile because tools/__pycache__/handoffctl.cpython-312.pyc exceeds the 200 KiB
  evidence limit.

- 2026-10-09T18:36:01+00:00: Recorded command exit 0; command argv SHA-256
  b470b3aef8671ea54bcc1116d5e74efb4c80157f0f5583e2241674d1e4d21dfb.

- 2026-10-09T18:36:24+00:00: Recorded command exit 0; command argv SHA-256
  3b0d15419d3d4080957c0b6e6cf1af4e9bd96a1ef8da0277aca8a0360dc53f97.

- 2026-10-09T18:37:02+00:00: Gate evidence 2026-10-09T18:38Z: cargo test -p asb-cli --no-run
  compiled all unit/integration test binaries successfully. Focused command cargo test -p asb-cli
  owned_directory_preparation -- --nocapture passed 2/2 new tests; positive creation/reuse and exact
  stderr notice passed, traversal/file/symlink rejection and machine-JSON path redaction passed.
  handoffctl returned COMMAND_RECORDED_POST_RECONCILE_FAILED only after recording because
  tools/__pycache__/handoffctl.cpython-312.pyc exceeds the 200 KiB state evidence limit.

- 2026-10-09T18:39:12+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:39:20+00:00: 2026-10-09T18:40Z: TUI audit found lifecycle state/cache paths are
  command-owned and previously lacked stderr notices. Added human-only notice plumbing from CLI
  dispatch into TUI dispatch/execute for dev lifecycle state, stable release cache, and active
  remove state while preserving JSON stdout. Independent review additionally requires fail-closed
  TOCTOU/symlink race handling in central output preparation/atomic writers and expanded
  dry-run/matrix/docs coverage; these remain open gates and are not being hidden.

- 2026-10-09T18:39:32+00:00: Recorded command exit 0; command argv SHA-256
  b470b3aef8671ea54bcc1116d5e74efb4c80157f0f5583e2241674d1e4d21dfb.

- 2026-10-09T18:41:29+00:00: Recorded command exit 1; command argv SHA-256
  0d0fbfe76c0a53aebfe44e2053981071db08fc02d39713dbf1147e07dee33700.

- 2026-10-09T18:41:57+00:00: Recorded command exit 0; command argv SHA-256
  b5ac1bdc1404e1f700e90d066796809b668b376321a3f181578f5521e9969fee.

- 2026-10-09T18:42:45+00:00: Heartbeat by codex-ar1767-directory-preparation.

- 2026-10-09T18:42:54+00:00: 2026-10-09T18:44Z: TUI notice test passed 1/1 after dispatch/execute
  wiring; earlier central directory tests remain 2/2 passing and test-binary compilation passed. A
  deliberately invalid combined cargo test filter was recorded as an expected CLI usage failure (two
  filters are not accepted by cargo test), then the correct single-filter TUI run passed. Added
  user-facing workspace, command-output, and TUI lifecycle documentation. Added post-rename symlink
  detection to atomic output writer. Independent review still flags descriptor-relative race
  hardening and broader dry-run/permission/route matrix as open before commit.

- 2026-10-09T18:43:08+00:00: Recorded command exit 101; command argv SHA-256
  10a701b2424e5ed226b0455eb01ce19376ff98a24fb81ec0200c779f16f8a3dc.

- 2026-10-09T18:43:31+00:00: Recorded command exit 101; command argv SHA-256
  549c53379c38a273156fe1754366dabf545c0468319863b1a2a228b09f930796.

- 2026-10-09T18:43:59+00:00: Recorded command exit 0; command argv SHA-256
  549c53379c38a273156fe1754366dabf545c0468319863b1a2a228b09f930796.

- 2026-10-09T18:44:30+00:00: Recorded command exit 101; command argv SHA-256
  10a701b2424e5ed226b0455eb01ce19376ff98a24fb81ec0200c779f16f8a3dc.
