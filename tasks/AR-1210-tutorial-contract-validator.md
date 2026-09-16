---
{
  "branch": "docs/ar-1210-tutorial-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T05:46:46+00:00",
  "depends_on": [],
  "id": "AR-1210",
  "next_action": "Promote after review; define the versioned offline tutorial-step schema and ASB syntax validator.",
  "observed_branch": "docs/ar-1210-tutorial-contract",
  "observed_dirty": 0,
  "observed_head": "0c0bd514fb866af4dafed022c4ec7dec479df86c",
  "owner": "asb_ar1210_tutorial_contract",
  "plan": "../plans/AR-1210.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define offline tutorial steps and validate them against the ASB CLI grammar.",
  "task_revision": 36,
  "title": "Tutorial contract and syntax validator",
  "updated_at": "2026-09-16T03:47:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1210"
}
---

Implement the linked plan. This AR is syntax/contract infrastructure only: tutorial commands must
never execute in its CI job and no provider, credential, network, benchmark, or LLM connection may
be required.

- 2026-09-16T03:37:51+00:00: Dependencies are empty; complete AR and plan reviewed; promote offline
  tutorial contract validator.

- 2026-09-16T03:38:15+00:00: Claimed by asb_ar1210_tutorial_contract.

- 2026-09-16T03:38:34+00:00: Recorded command exit 0; command argv SHA-256
  e3b9a332a7c8c8505da0721ffec4ce224178ee74d001aaa4ceb35174cea23b8b.

- 2026-09-16T03:38:56+00:00: Heartbeat by asb_ar1210_tutorial_contract.

- 2026-09-16T03:38:59+00:00: Recorded command exit 0; command argv SHA-256
  b6d7eee1dda9b25741f0d3b279e6d35e80811f6a727fedaac12fff8ea4578e3d.

- 2026-09-16T03:39:07+00:00: Recorded command exit 0; command argv SHA-256
  1090d7d308df15a5135c752b74b8b1cd16c73ff7253299bb77ecb1fe45d538db.

- 2026-09-16T03:39:16+00:00: Recorded command exit 0; command argv SHA-256
  70b6a267b6c2bd11031f54db74892e7afc85e3a32e65cad9bb055049173b5f03.

- 2026-09-16T03:40:44+00:00: Heartbeat by asb_ar1210_tutorial_contract.

- 2026-09-16T03:42:03+00:00: Heartbeat by asb_ar1210_tutorial_contract.

- 2026-09-16T03:42:08+00:00: Recorded command exit 0; command argv SHA-256
  4b866a61a939ff1592762d034f882243a35f8b3ee058634868b1ba40a476710e.

- 2026-09-16T03:42:49+00:00: Recorded command exit 0; command argv SHA-256
  f397688459a38e4f80675ba6c15f49c359643953df5bb55f9276889f9b20cea0.

- 2026-09-16T03:42:57+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-16T03:43:08+00:00: Heartbeat by asb_ar1210_tutorial_contract.

- 2026-09-16T03:43:10+00:00: Recorded command exit 0; command argv SHA-256
  c8b16bd630d77ba4a5ae696c249062e263bfa336ea7a8960855f986dc78bfc63.

- 2026-09-16T03:43:20+00:00: Recorded command exit 0; command argv SHA-256
  f468f1ffb8bcd1a7de0fdea6af2688cf52054d4e470a0659e626523c9640590d.

- 2026-09-16T03:43:33+00:00: Recorded command exit 0; command argv SHA-256
  137c1e3ccb6d71d08c765dad9063cb1466d0d9481a38c40537431fa049d2afad.

- 2026-09-16T03:43:52+00:00: Recorded command exit 0; command argv SHA-256
  fc938500a17e36370331bf3576daf5be9d55bbf59f0c329da0c3a4da4c73fc5c.

- 2026-09-16T03:44:00+00:00: Recorded command exit 0; command argv SHA-256
  10c03613ffdcbd72e5ff8d463b371551dc6085af8c37cd9d1879fa5519d02fb9.

- 2026-09-16T03:44:18+00:00: Recorded command exit 0; command argv SHA-256
  1d9b6d32b2f06613c14df162c0fed69cb6a41440a397bbcf4a3b4ab1fd7d97a5.

- 2026-09-16T03:44:27+00:00: Recorded command exit 0; command argv SHA-256
  69d5dc04426b98244cb739e08439e672bdb29e8306aef7dadb92751755806bfd.

- 2026-09-16T03:45:40+00:00: Recorded command exit 0; command argv SHA-256
  4b866a61a939ff1592762d034f882243a35f8b3ee058634868b1ba40a476710e.

- 2026-09-16T03:45:51+00:00: Recorded command exit 0; command argv SHA-256
  f397688459a38e4f80675ba6c15f49c359643953df5bb55f9276889f9b20cea0.

- 2026-09-16T03:46:09+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-16T03:46:18+00:00: Recorded command exit 0; command argv SHA-256
  e38ae343b9cc396273e8929cb503faa5297f992f452a9e0186ff25eb759082bf.

- 2026-09-16T03:46:29+00:00: Recorded command exit 0; command argv SHA-256
  33717b6e18ce63a265700ade1f86caf77261992965881ad8dca93516f9f5ba8f.

- 2026-09-16T03:46:46+00:00: Heartbeat by asb_ar1210_tutorial_contract.

- 2026-09-16T03:46:52+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T03:47:13+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.
