---
{
  "branch": "fix/runner-isolation-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T09:19:37+00:00",
  "depends_on": [
    "AR-0830",
    "AR-0831"
  ],
  "id": "AR-0836",
  "next_action": "Separate job execution from operator-owned installation, credentials, control state, and diagnostics with a verified immutable boundary.",
  "observed_branch": "fix/runner-isolation-hardening",
  "observed_dirty": 9,
  "observed_head": "a4782cdc467d38996473168cc5d2ccedfae75a25",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0836.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden development-host runner isolation against same-UID job tampering and diagnostic leakage.",
  "task_revision": 22,
  "title": "Harden runner isolation and credential boundaries",
  "updated_at": "2026-09-07T08:06:28+00:00",
  "worktree_key": "agent-systems-benchmark-runner-isolation-hardening"
}
---
## AR-0836

Independent audit found that the runner job identity can traverse or modify installation,
credentials, control files, manifests, and diagnostics, and that diagnostics can expose private
paths and session metadata. Harden before any trusted workflow is dispatched.

Acceptance criteria:

- Use separate operator/service and job identities or an equivalent namespace/broker boundary.
- Make complete installation and control state immutable or operator-owned; verify all relevant files.
- Ensure jobs cannot read registration credentials or poison future registrations.
- Bound and redact diagnostics before storage/upload; add leakage and tamper negative tests.
- Qualify interrupted jobs, reset/recovery, and repeated runs with independent security review.

- 2026-09-07T07:49:35+00:00: Dependencies AR-0830 and AR-0831 are durably done; prioritize P0
  remediation of runner identity separation, credential isolation, immutable control state, bounded
  redacted diagnostics, tamper negatives, and interrupted-run recovery before any further trusted
  dispatch.

- 2026-09-07T07:49:37+00:00: Claimed by quality-20260906.

- 2026-09-07T07:50:01+00:00: Recorded command exit 0; command argv SHA-256
  9a1739e9c710ce7f387f2db688102a1fcc80c6ad43de52642f5a203c2ba519e6.

- 2026-09-07T07:55:50+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T07:57:01+00:00: Recorded command exit 0; command argv SHA-256
  27ac70419368a1d3ddbe62275667441e246bdde59c0eca0883a54627472b9f68.

- 2026-09-07T07:57:52+00:00: Recorded command exit 0; command argv SHA-256
  cc2b0cdf61f91b222db05b6e9f34eb233e5d4faa656f0cde31c361e5d1d9b853.

- 2026-09-07T07:58:30+00:00: Recorded command exit 0; command argv SHA-256
  ccefacb149fdae1a5c214d1ff6e95a8f77c55df373d93bfbdd50163917246584.

- 2026-09-07T08:00:12+00:00: Recorded command exit 0; command argv SHA-256
  cca8fe48e2d3d9221f212048745a9c098a98fee19b5c29afa6a7809bd6ff68a1.

- 2026-09-07T08:00:59+00:00: Recorded command exit 1; command argv SHA-256
  90a5da478cc50ecbbe19f6766816c1d4803b001999e4158892959e0e80654801.

- 2026-09-07T08:01:31+00:00: Recorded command exit 0; command argv SHA-256
  c45a1cb3b8c1fa36ab0ee3a556760bc66e045c4c18dbfa5cd5b3590e81474ea0.

- 2026-09-07T08:02:57+00:00: Recorded command exit 0; command argv SHA-256
  c6603d204547733c7d0dbb0a37c3b0933fbbb68a2e8f17f65cf54b452bb0966b.

- 2026-09-07T08:03:09+00:00: Recorded command exit 0; command argv SHA-256
  eb119a8a48344ba43e77c3b9f2d801d856fe2c7e4a5f67c2462f5f221b9986d7.

- 2026-09-07T08:04:52+00:00: Recorded command exit 1; command argv SHA-256
  24f66769c368b570600c9c24f9660140ffce8bcb300af03447c4a13f47e0bd82.

- 2026-09-07T08:05:30+00:00: Recorded command exit 0; command argv SHA-256
  1f1a7fab33fd09fed4a7339d0c1f640689b0b1820178fcf21e241a9c63b170dd.

- 2026-09-07T08:05:48+00:00: Recorded command exit 0; command argv SHA-256
  6bd8e4f072ef10523763ee459a49038a2d121e1e7d36a08ea22fcb5a222868fd.
