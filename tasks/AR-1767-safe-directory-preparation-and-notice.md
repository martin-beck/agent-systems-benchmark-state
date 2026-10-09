---
{
  "branch": "feature/ar-1767-safe-directory-preparation-and-notice",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T20:20:59+00:00",
  "depends_on": [
    "AR-1766"
  ],
  "id": "AR-1767",
  "next_action": "Implement safe automatic directory preparation and concise pre-effect human notices for every ASB command-owned output destination identified by AR-1766.",
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
  "summary": "Tell human users which command-owned directory will be created, create it safely, and report precise path-specific failures.",
  "task_revision": 8,
  "title": "Safe automatic directory preparation with clear notice",
  "updated_at": "2026-10-09T18:22:26+00:00",
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
