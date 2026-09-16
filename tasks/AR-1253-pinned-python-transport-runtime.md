---
{
  "branch": "feature/ar-1253-pinned-python-transport-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:21:58+00:00",
  "depends_on": [
    "AR-1252"
  ],
  "id": "AR-1253",
  "next_action": "Pin and validate exact source docker-library/python and source_revision python:3.13.15-slim-bookworm; add source/revision tamper negatives and rerun focused/full gates before review/publication.",
  "observed_branch": "feature/ar-1253-pinned-python-transport-runtime",
  "observed_dirty": 0,
  "observed_head": "b7797d05c1a12f4e5cdd8d7df2a7b26c72425052",
  "owner": "asb_ar1253_python_runtime",
  "plan": "../plans/AR-1253.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision pinned Python transport fixture runtime.",
  "task_revision": 16,
  "title": "Provision pinned Python transport fixture runtime",
  "updated_at": "2026-09-16T13:23:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1253"
}
---

Implement only the linked AR-1253 plan using ASB development documentation and handoffctl.
Keep runtime images, caches, provenance, and all test activity under `/srv/data/projects`.

- 2026-09-16T13:18:48+00:00: AR-1252 completed with reviewed immutable Python image allowlist and
  exact-head evidence; promote runtime fixture successor.

- 2026-09-16T13:18:50+00:00: Claimed by asb_ar1253_python_runtime.

- 2026-09-16T13:19:05+00:00: Recorded command exit 0; command argv SHA-256
  eaa6bca78b91f67bb7aa44895c2a2056ccb44cfde9e2427c8f5830265b90b196.

- 2026-09-16T13:20:35+00:00: Recorded command exit 2; command argv SHA-256
  d4e2bee60595fe120ad7eded61b8217ae4d6ccf96558c587157ea92b28a28d2a.

- 2026-09-16T13:20:53+00:00: Recorded command exit 0; command argv SHA-256
  28d43d22f359a22bd0ca7c607add0b0027c1e04c9b8f12bc98809f42868628e8.

- 2026-09-16T13:21:09+00:00: Recorded command exit 0; command argv SHA-256
  d69b5a31244652575d15b16bc359c8417cd569327e00697c5d7e7433783e358b.

- 2026-09-16T13:21:30+00:00: Recorded command exit 0; command argv SHA-256
  5b8c4fcdfcf12bee36d6fc6d1845f6648b4842ffda7ce0cdb34bfb28fb335255.

- 2026-09-16T13:21:56+00:00: Signed+DCO commit edbbb8c pushed. Added closed python-runtime-v1.json
  provenance contract binding Python 3.13.15 amd64 to immutable image
  python@sha256:ed86c822...220c3e6e, network none, and site initialization disabled; validator
  rejects unknown fields, mutable tags, digest drift, wrong version/architecture, and isolation
  drift. Focused runtime tests 2/2 and full llm-double-spike suite 17/17 pass; source policy headers
  and diff checks pass. Actual pinned Docker probe with read-only root, dropped caps, bounded
  resources, private IPC, tmpfs and --network none reports Python 3.13.15. Prior combined probe exit
  2 was shell quoting and was corrected with split commands.

- 2026-09-16T13:21:58+00:00: Heartbeat by asb_ar1253_python_runtime.

- 2026-09-16T13:22:53+00:00: Independent review of signed head edbbb8c found provenance gap:
  python_runtime.load_manifest enforces field closure, Python version/amd64/image/network/site
  settings but accepts arbitrary source and source_revision values. This violates AR-1253 plan
  requirement for pinned source/interpreter/package provenance. Add exact source/revision validation
  and negative tests; do not publish edbbb8c yet.

- 2026-09-16T13:23:33+00:00: Recorded command exit 0; command argv SHA-256
  321942e0f0153a2d8cbd19eedd393105a4c68944659dfc47ca8844b9bec09b94.
