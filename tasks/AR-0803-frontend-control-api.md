---
{
  "branch": "feature/frontend-control-api",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T04:26:28+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204",
    "AR-0801"
  ],
  "id": "AR-0803",
  "next_action": "Define a bounded versioned control/status API between the runner and independent frontends.",
  "observed_branch": "feature/frontend-control-api",
  "observed_dirty": 3,
  "observed_head": "61b5dd33ba04295a476e444d8bfd338ab972507a",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0803.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.",
  "task_revision": 21,
  "title": "Define the frontend control API",
  "updated_at": "2026-09-07T03:23:19+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-control-api"
}
---
## AR-0803

Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.

The benchmark runner remains independently operable when no frontend is present or when a frontend crashes.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T02:56:13+00:00: Dependencies AR-0101, AR-0104, AR-0204 and AR-0801 are durably done;
  AR-0801 exact-main b2833ab CI and post-merge verification are green. Promote the highest-priority
  compatible frontend control boundary after releasing its Cargo/scheduler fences.

- 2026-09-07T02:56:28+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T03:12:45+00:00: Recorded command exit 0; command argv SHA-256
  2112362c51cef85781237610d9b9e060605ef818fbc3842b7637243011b6072d.

- 2026-09-07T03:14:02+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T03:14:55+00:00: Recorded command exit 1; command argv SHA-256
  119a2544b57bc260d3736a8c380cb862336dcb3828b84394350db9659ad2e775.

- 2026-09-07T03:15:19+00:00: Recorded command exit 2; command argv SHA-256
  8bc998ab7b97ddd3689435d527789bef02f835b0eaf4edea3eb44d40eda18b6d.

- 2026-09-07T03:16:20+00:00: Recorded command exit 0; command argv SHA-256
  0abe16459841183b1c87533de5496a6b32348f12b93116537775513a95c9fca7.

- 2026-09-07T03:17:52+00:00: Recorded command exit 0; command argv SHA-256
  fca74cf20e25dfa6f5c081431044ca67513dad3c8d08f41a256e74b0f8c1d7ea.

- 2026-09-07T03:18:35+00:00: Recorded command exit 0; command argv SHA-256
  0d969cea7c6abd88e73a08fa66d0dc0d021ea41dd86666a0bd912be5ae398cf8.

- 2026-09-07T03:20:40+00:00: Recorded command exit 0; command argv SHA-256
  29edb89936fae8949ecff5ce1d8f65f1d5b22895939819c00fd22579efc6be41.

- 2026-09-07T03:21:46+00:00: Recorded command exit 0; command argv SHA-256
  f8c05adc56c7dd166f048c9549d034ce2230c511e4fea79a05c704f84f8bf78d.

- 2026-09-07T03:22:04+00:00: Recorded command exit 127; command argv SHA-256
  6ed4c4670327e5fee3971d31b475508b1557c7b1af50c61f10b93c29ca90ed67.

- 2026-09-07T03:22:22+00:00: Recorded command exit 101; command argv SHA-256
  6d046ec0ea3fcb81dfa5c60c9c2deb6822991c7dd90c1f0a868d691a1bf5f724.

- 2026-09-07T03:22:32+00:00: Recorded command exit 101; command argv SHA-256
  eb4580fb0cfa8ee65783040f56ad5eea0facc89e0a4e083b985002929fe9abc9.

- 2026-09-07T03:22:52+00:00: Recorded command exit 101; command argv SHA-256
  e6dfbd88d5865227dc296f9b320027567ad103fe984418f6601488eccf39b6b1.

- 2026-09-07T03:23:06+00:00: Recorded command exit 0; command argv SHA-256
  f2846dece264eb519b00d71e54c44cc9a4f0841844d4f852f5d36c5e54d56dc0.

- 2026-09-07T03:23:19+00:00: Recorded command exit 101; command argv SHA-256
  eb4580fb0cfa8ee65783040f56ad5eea0facc89e0a4e083b985002929fe9abc9.
