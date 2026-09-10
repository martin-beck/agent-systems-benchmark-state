---
{
  "branch": "docs/asb-cli-workflow-captures",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T23:03:42+00:00",
  "depends_on": [
    "AR-0872"
  ],
  "id": "AR-1028",
  "next_action": "Implement real-CLI normalized transcript fixture, provenance hash checks, drift/privacy negatives, and workflow documentation link.",
  "observed_branch": "docs/asb-cli-workflow-captures",
  "observed_dirty": 4,
  "observed_head": "32df706413a6f165f086941426a5c793bd5e01e8",
  "owner": "codex-ar1028-cli-captures-20260910",
  "plan": "../plans/AR-1028.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Produce reproducible ASB CLI transcripts separately from standalone TUI screenshots.",
  "task_revision": 30,
  "title": "Generate ASB CLI workflow captures",
  "updated_at": "2026-09-10T20:15:22+00:00",
  "worktree_key": "agent-systems-benchmark-asb-cli-workflow-captures"
}
---
Generate documentation transcripts from actual synthetic ASB CLI executions. This AR owns no
renderer, terminal application, Ratatui/Crossterm dependency, or asb-tui source.

- 2026-09-10T20:01:56+00:00: AR-0872 is durably done; CLI-only capture scope is dependency-ready and
  disjoint from all standalone TUI work.

- 2026-09-10T20:01:59+00:00: Claimed by codex-ar1028-cli-captures-20260910.

- 2026-09-10T20:02:02+00:00: Recorded command exit 0; command argv SHA-256
  48ce8c035d66a7ab0478204d6ea9ff42e080068ac6938ca529e2c4005f2449e2.

- 2026-09-10T20:03:42+00:00: Heartbeat by codex-ar1028-cli-captures-20260910.

- 2026-09-10T20:03:55+00:00: Recorded command exit 0; command argv SHA-256
  a2808036e9be365682dfe9eed52cfb76668c7c24ed86fdc4b59d26b160043f7d.

- 2026-09-10T20:05:21+00:00: Initial audit complete at ASB 32df706. Scope is text-only CLI evidence:
  doctor, plan, run, report, compare, record, replay. No screenshots, terminal renderer, TUI
  application, Ratatui/Crossterm, or asb-tui source. Classified initial exit 2 as read-only sed
  using the state checkout instead of sibling product docs; no mutation.

- 2026-09-10T20:06:55+00:00: Recorded command exit 0; command argv SHA-256
  f77810c92a0ebdfe32daa24865be55ae1eaea4ef4a8523cd21925d923d6398ad.

- 2026-09-10T20:07:14+00:00: Recorded command exit 1; command argv SHA-256
  b39a8657e7638c0d52bd7ae6598b66d354c724969e6652b04659a3d39031a608.

- 2026-09-10T20:07:34+00:00: Recorded command exit 1; command argv SHA-256
  50dd3b0a658894857771de996141353284c2c380d6df2e69c1f64f0e505170ba.

- 2026-09-10T20:08:24+00:00: Recorded command exit 0; command argv SHA-256
  3777663016dafb2aa452a2971970c2bf7b9a3b4b30550c6882721f884df87970.

- 2026-09-10T20:08:49+00:00: Recorded command exit 101; command argv SHA-256
  ea451be96ab8726202248243e4827970911249b4d9f6e8cd106d24161a2ded1b.

- 2026-09-10T20:09:08+00:00: Recorded command exit 0; command argv SHA-256
  073aaf5a610bb4ac17adf985b2f5f9e7093548fa83d630d5f919d6906a0fee27.

- 2026-09-10T20:09:30+00:00: Recorded command exit 101; command argv SHA-256
  ea451be96ab8726202248243e4827970911249b4d9f6e8cd106d24161a2ded1b.

- 2026-09-10T20:09:56+00:00: Recorded command exit 0; command argv SHA-256
  8f05ff0b25e655f1fa2b730779b307da9b69051882f2fbe685110477a529fcff.

- 2026-09-10T20:10:22+00:00: Recorded command exit 0; command argv SHA-256
  3777663016dafb2aa452a2971970c2bf7b9a3b4b30550c6882721f884df87970.

- 2026-09-10T20:10:53+00:00: Recorded command exit 101; command argv SHA-256
  ea451be96ab8726202248243e4827970911249b4d9f6e8cd106d24161a2ded1b.

- 2026-09-10T20:11:46+00:00: Recorded command exit 1; command argv SHA-256
  b944276dfcd20959651955a013bec4e3733f8435012693beb537948168a91fee.

- 2026-09-10T20:12:10+00:00: Recorded command exit 1; command argv SHA-256
  487f8165bd64427d261366914b4abae817f9ad5788f16d79f33db3d142d1958f.

- 2026-09-10T20:12:31+00:00: Recorded command exit 0; command argv SHA-256
  03687c55ebffd801fe731427e1de555fe731b50abf1997684df90ea9dd66101b.

- 2026-09-10T20:12:51+00:00: Recorded command exit 0; command argv SHA-256
  5f94206576aafecfbec49eeb439c696f168d09a60b2446629fbac5c23dd717fb.

- 2026-09-10T20:13:22+00:00: Recorded command exit 0; command argv SHA-256
  ea451be96ab8726202248243e4827970911249b4d9f6e8cd106d24161a2ded1b.

- 2026-09-10T20:13:45+00:00: Recorded command exit 0; command argv SHA-256
  81475ba38a4efb1bb51258bdb3cc0ada45510fbe6468a7a570d91d24d9ff6192.

- 2026-09-10T20:14:07+00:00: Recorded command exit 0; command argv SHA-256
  1b935ee631904565417b2796dc612fa9e2d7725fb1af8e5963d5f887aef6f871.

- 2026-09-10T20:14:27+00:00: Recorded command exit 0; command argv SHA-256
  59f7fbcde84acbdb28323c508e85be0db5438716725a67e091209096a7dec507.

- 2026-09-10T20:14:48+00:00: Recorded command exit 0; command argv SHA-256
  f49d549bc9b9291aae54923fbb268ed2cc1d2922b902a669c70d4d2f81ef649b.

- 2026-09-10T20:15:02+00:00: Recorded command exit 0; command argv SHA-256
  1998f534aa23fab5a5f3d35d18c637e0bb9291490da8c16c1aadbc24649d8733.

- 2026-09-10T20:15:22+00:00: Recorded command exit 0; command argv SHA-256
  fa9193624ba790c33787832baa3ab5f4726311de0a303ad4bcca53ee46e80742.
