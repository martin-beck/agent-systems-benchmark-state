---
{
  "branch": "feature/ar-1770-descriptor-safe-directory-race-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T21:23:16+00:00",
  "depends_on": [
    "AR-1767"
  ],
  "id": "AR-1770",
  "next_action": "Implement descriptor-relative or equivalent fail-closed directory and atomic publication paths, then complete the hostile filesystem and stream matrix.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1770-descriptor-safe-races",
  "plan": "../plans/AR-1770-descriptor-safe-directory-race-hardening.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "property-or-fuzz",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1770.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1770.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Close remaining directory and atomic-publication replacement races and complete the AR-1767 acceptance matrix.",
  "task_revision": 24,
  "title": "Descriptor-safe directory race hardening and acceptance matrix",
  "updated_at": "2026-10-09T19:33:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1770-descriptor-safe-directory-race-hardening"
}
---

Harden the AR-1767 directory preparation and output publication paths against
replacement between validation and effect. Use descriptor-relative or an
equivalent fail-closed design for every command-owned directory ancestor and
for `write_atomic_private` and `publish_recording_campaign`; never follow an
attacker-replaced symlink or publish through an unvalidated ancestor. Preserve
private modes, fsync/atomicity, transaction-owned cleanup, and existing JSON
and diagnostic contracts.

Complete the missing acceptance evidence: deterministic replacement-race and
concurrent-reuse tests; dry-run no-mutation tests; permission/read-only and
rollback tests; path-specific error and human-notice tests for setup/config,
project, tool, plan, run/sweep, report, record/campaign, easy lifecycle, and
TUI routes; and machine-stream privacy checks. Record any platform-specific
implementation boundary explicitly and keep the product offline after install.

- 2026-10-09T19:22:21+00:00: AR-1767 is released done with exact merge and all post-merge gates;
  promote the descriptor-safe race and acceptance-matrix successor.

- 2026-10-09T19:22:30+00:00: Claimed by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:23:16+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:23:20+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-09T19:23:42+00:00: Recorded command exit 0; command argv SHA-256
  b62f4e4a9a8bbb2a2c7126386b0d66111eba17387cebaf68a7f7c625260419c0.

- 2026-10-09T19:24:04+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T19:24:06+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T19:26:23+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T19:26:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:27:23+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:28:13+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:28:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:29:06+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:30:01+00:00: Recorded command exit 101; command argv SHA-256
  9c9c28ee85d6728d4e0aadfacd9c56ce020d9e24199e795a870dcd65d1732158.

- 2026-10-09T19:30:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:30:51+00:00: Recorded command exit 0; command argv SHA-256
  9c9c28ee85d6728d4e0aadfacd9c56ce020d9e24199e795a870dcd65d1732158.

- 2026-10-09T19:31:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:31:34+00:00: Recorded command exit 1; command argv SHA-256
  dc3363f7c4f58aaf68ba66c9d95e87e4378322324b1d06f02ef51515642b019e.

- 2026-10-09T19:32:00+00:00: Recorded command exit 101; command argv SHA-256
  c64f85e92f4319f5a3e74e135910802ef4e5808bce669c08396bff4a9f271605.

- 2026-10-09T19:32:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:32:56+00:00: Recorded command exit 101; command argv SHA-256
  d7efc4b5867af3e11acc4adf06c7ef77432dc45f5f69d8d5b2a810794db57cee.

- 2026-10-09T19:33:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:33:45+00:00: Recorded command exit 0; command argv SHA-256
  d7efc4b5867af3e11acc4adf06c7ef77432dc45f5f69d8d5b2a810794db57cee.
