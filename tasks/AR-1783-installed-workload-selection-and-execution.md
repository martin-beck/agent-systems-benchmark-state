---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T02:00:59+00:00",
  "depends_on": [
    "AR-1763",
    "AR-1764",
    "AR-1782"
  ],
  "id": "AR-1783",
  "next_action": "Integrate every development-supported installed workload bundle into selection and prove full run/sweep/report/compare consumes its exact recorded identity.",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "d86694333eff92cea4d548a74bed3d3a62c503bd",
  "owner": "ar1783_workload_selection_luna56",
  "plan": "../plans/AR-1783-installed-workload-selection-and-execution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1783.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1783.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Select every development external workload and prove ASB uses its exact project-local identity end to end.",
  "task_revision": 22,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-12T00:08:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1783-installed-workload-selection-and-execution"
}
---

Make generated project catalogs and run/sweep consume the dedicated `asb workload`
records. Selection validates the installed workload's exact catalog revision,
identity, digest, license/terms compatibility, preparation state, adapter
version, and resource/platform requirements. Execution binds this identity into
the plan/run/record/report/compare evidence and rejects ambient, stale, revoked,
missing, incompatible, or manually substituted workload directories before a run
starts. Cover every AR-1781 workload ID—including SWE-mini—through a fresh
project's install, selection, bounded run and sweep, report, and comparison
journey. Development runs may use a controlled local/development backend where
needed; lack of production authorization or hosted qualification must not block
the suite from this end-to-end path.

- 2026-10-12T00:00:59+00:00: Dependencies are now complete; open AR-1783 for implementation.

- 2026-10-12T00:00:59+00:00: Claimed by ar1783_workload_selection_luna56.

- 2026-10-12T00:01:58+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-12T00:04:04+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:04:13+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T00:04:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:04:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:04:54+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:05:30+00:00: Recorded command exit 0; command argv SHA-256
  7176a4996c16f289722a1ef4fdd225749fc51f58c34b0fcfb9c0f5689d2ab4a6.

- 2026-10-12T00:05:51+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:06:16+00:00: Recorded command exit 101; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:06:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T00:06:35+00:00: Recorded command exit 0; command argv SHA-256
  665c8e3f3b5ce28b9d9834c286a1da3f3e4189b3cfd5796fc061ff512c2e5c79.

- 2026-10-12T00:07:03+00:00: Recorded command exit 0; command argv SHA-256
  a1f8aedb7512b2eee19aac363063c66eb8c928cc3ddea4e50326dc00d77d230f.

- 2026-10-12T00:07:06+00:00: Recorded command exit 0; command argv SHA-256
  bb06a585a3c5274ee01d31c6141787822697874b6d86e64cee19e848885fea39.

- 2026-10-12T00:07:47+00:00: Recorded command exit 0; command argv SHA-256
  653ce9b81a4efbec43e5a667e890163176daab33a0f0336a5ce142c465f3afda.

- 2026-10-12T00:08:26+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
