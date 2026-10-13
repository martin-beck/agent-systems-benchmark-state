---
{
  "branch": "codex/ar1843-formal-workspace-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T12:03:26+00:00",
  "depends_on": [],
  "id": "AR-1843",
  "next_action": "Run exact-head hosted formal workflow after independent review; local full suite remains environment-limited because unittest discovery hangs in pre-existing test_git_backup concurrent collision and pytest is not a locked project dependency.",
  "owner": "ar1843-formal-workspace-repair-luna",
  "plan": "../plans/AR-1843-hosted-formal-workspace-permission-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1843.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1843.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair hosted formal TLC workspace permissions for the ASB state runner.",
  "task_revision": 22,
  "title": "Hosted formal workspace permission repair",
  "updated_at": "2026-10-13T10:07:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1843-formal-workspace-repair"
}
---

PR #142 exposed a runner-only failure before model execution: the formal
workflow defaults `TLC_WORK_ROOT` to `/tmp/agent-workflow-coordinator-tlc`,
which is owned by the interactive user and is not writable by the
`gha-asb-state` service account. Repair the workflow and runner-owned
per-run workspace initialization using a path under the approved
`/srv/data/projects/.asb-tlc` root. Preserve bounded cleanup, private
permissions, and all formal admission/attestation checks.

Acceptance requires the exact failing PR head to pass the hosted formal job
after the repair, including the same model and implementation contract; no
formal assertion, timeout, or resource-bound gate may be removed or weakened.

- 2026-10-13T09:56:20+00:00: Runner infrastructure repair required by PR #142 formal failure

- 2026-10-13T09:57:02+00:00: Claimed by ar1843-formal-workspace-repair-luna.

- 2026-10-13T09:57:28+00:00: Bound worktree agent-systems-benchmark-ar-1843-formal-workspace-repair
  on branch codex/ar1843-formal-workspace-repair.

- 2026-10-13T09:57:32+00:00: Recorded command exit 128; command argv SHA-256
  e189a5e3d803182795d7e23c66ca2ceb90c07199e43d75be1b0f6b0c04301349.

- 2026-10-13T09:57:50+00:00: Recorded command exit 0; command argv SHA-256
  797db10fe221c9904286e98287c1ead6ef3d6555b9087d739081325c72e2ef0c.

- 2026-10-13T10:03:26+00:00: Heartbeat by ar1843-formal-workspace-repair-luna.

- 2026-10-13T10:03:50+00:00: Recorded command exit 0; command argv SHA-256
  6b6600eb9432102ee0920b8b3ba9bc9e22c585f8c59147fe2673c8ff364f59f0.

- 2026-10-13T10:04:08+00:00: Recorded command exit 0; command argv SHA-256
  14590cffa309da00271ffd6f6df91fa2b424ad5e61c72fe0663939b604ed8dc4.

- 2026-10-13T10:04:37+00:00: Recorded command exit 0; command argv SHA-256
  d0bb0f225f29c2ab539e5bd6d8c001c08e7936bb966e47e146af22bd597588cd.

- 2026-10-13T10:04:44+00:00: Recorded command exit 0; command argv SHA-256
  dda36893048e037a2ed2da5fd2af87fb197fe282814b7dc3f615695e6b4a849a.

- 2026-10-13T10:04:54+00:00: Recorded command exit 0; command argv SHA-256
  8d2a35b5daa95b9ecc5d5155f7c0a7783e31a032707f6f1506276f6cd799249c.

- 2026-10-13T10:05:03+00:00: Recorded command exit 1; command argv SHA-256
  790dfe3b6c7e71b89480c841d5786fa996102711ad00c090d293bc95e7bba002.

- 2026-10-13T10:05:14+00:00: Recorded command exit 0; command argv SHA-256
  0e3c18361c61a878577c1bd1178d162fa0066f5bbb5bf835c479052985b6adc3.

- 2026-10-13T10:05:23+00:00: Recorded command exit 2; command argv SHA-256
  7f3db8f8958c8825b490e224e0ddcbb3c31a6e40d94ce743ff0733d409393b12.

- 2026-10-13T10:05:33+00:00: Recorded command exit 2; command argv SHA-256
  ac5fc4892481c0e57eb5f0243a19ca41baf601970b064e34029d172ba0ae715f.

- 2026-10-13T10:05:44+00:00: Recorded command exit 0; command argv SHA-256
  af064778e82426a93a8e70a9621f754e3b861651448f93ac2e39b03125953028.

- 2026-10-13T10:05:48+00:00: Recorded command exit 2; command argv SHA-256
  ac5fc4892481c0e57eb5f0243a19ca41baf601970b064e34029d172ba0ae715f.

- 2026-10-13T10:06:03+00:00: Recorded command exit 2; command argv SHA-256
  5b595e4f675b08afe5c6639d9251b42b7c1a0ff954bc0e4537b3fe1b024513a9.

- 2026-10-13T10:06:14+00:00: Recorded command exit 0; command argv SHA-256
  18d9e3a8a18c083613f2185119e5f69c02e2263623f7ae83b1548869fb74e999.

- 2026-10-13T10:06:19+00:00: Recorded command exit 1; command argv SHA-256
  dc48d8ba5b8a8ab562f4c5e486907dc015748be86393e77d059c260c2ca15899.

- 2026-10-13T10:07:56+00:00: Focused workflow/vendor tests pass: 17 tests and 25 subtests. bash -n
  passes. Local formal pr-fast cannot initialize a new child under /srv/data/projects/.asb-tlc
  because the approved root is owned by gha-asb-state; this is the hosted runner account and not a
  candidate failure. Initial full pytest failed first with system interpreter missing jsonschema,
  then with uv from wrong cwd (tools import failure), and corrected unittest discovery reached a
  pre-existing test_git_backup concurrent restore collision and was interrupted; no
  candidate-specific assertion failure observed.
