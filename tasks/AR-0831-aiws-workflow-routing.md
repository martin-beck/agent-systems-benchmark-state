---
{
  "branch": "feature/development-host-workflow-routing",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T10:26:51+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0830"
  ],
  "id": "AR-0831",
  "next_action": "Hold exact unpublished f55f98cc79b75226a537600258dde5e57333bdeb for independent immutable security review; publish only after approval.",
  "observed_branch": "feature/development-host-workflow-routing",
  "observed_dirty": 0,
  "observed_head": "f55f98cc79b75226a537600258dde5e57333bdeb",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0831.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Route explicitly trusted ASB CI jobs to qualified development host runners while preserving disposable public-PR isolation.",
  "task_revision": 20,
  "title": "Integrate development host ASB runners with GitHub workflows",
  "updated_at": "2026-09-07T07:37:51+00:00",
  "worktree_key": "agent-systems-benchmark-development-host-workflow-routing"
}
---
## AR-0831

Route explicitly trusted ASB CI jobs to qualified development host runners while preserving disposable
public pull-request isolation.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T07:26:49+00:00: AR-0003 and AR-0830 are durably done; workflow/actionlint/policy
  ownership is free after the AR-0830 merge, and routing remains limited to trusted manual/protected
  events with disposable PR equivalents.

- 2026-09-07T07:26:51+00:00: Claimed by contracts-20260906.

- 2026-09-07T07:27:13+00:00: Recorded command exit 0; command argv SHA-256
  789d951d350d0a21c46d5e5b54369bbca81c249264d811442011fa43887d16ea.

- 2026-09-07T07:29:20+00:00: Recorded command exit 0; command argv SHA-256
  3724c9d7e41c9dff9e46c2388af57eb2c8952b0701c4f275f76d588eef7d2292.

- 2026-09-07T07:29:32+00:00: Recorded command exit 0; command argv SHA-256
  ed60df3b901474f580fc7b404c8de2cdd185b8f37b32885a24fcd35323367f95.

- 2026-09-07T07:30:16+00:00: Recorded command exit 0; command argv SHA-256
  d92ea52c768851479d93afa5f2c8951d552236c395304a6008045b8190491f89.

- 2026-09-07T07:31:29+00:00: Recorded command exit 0; command argv SHA-256
  cd9f2e2478474f1837b353287ec44027e047ba1241a912ac5ab8f9cbb2fcbb06.

- 2026-09-07T07:32:05+00:00: Recorded command exit 0; command argv SHA-256
  1d4c11bd0ab4bbc5a679cd4367b54fefa5d5a4eb5a9a0ba7b43a6ded3cef298b.

- 2026-09-07T07:32:33+00:00: Recorded command exit 0; command argv SHA-256
  f7391de4c7a060c51ff71f6d369854beb415ab17afdb349fe7edf231b998a94f.

- 2026-09-07T07:33:06+00:00: Recorded command exit 0; command argv SHA-256
  fa147500d58b2189f7dd1197bd5ac10073262e72a5c8aa54c0c1ccbe2bfbde92.

- 2026-09-07T07:34:30+00:00: Recorded command exit 2; command argv SHA-256
  848c10ee316ab82d58b3453082ccf0ae8ec305a7cc3d2b72cb2100564177640a.

- 2026-09-07T07:35:51+00:00: Recorded command exit 0; command argv SHA-256
  1ced257742c07180c9d4b4ccdb5d064d1233ce3d7bad886c43489a31402a8ab4.

- 2026-09-07T07:36:06+00:00: Recorded command exit 0; command argv SHA-256
  4210af8b72a652dd75a767fad1598d1478475dbc4d4b87f7846597985fee0fa0.

- 2026-09-07T07:36:39+00:00: Recorded command exit 0; command argv SHA-256
  3f10886351d474b24a289d1890d0360cde73b3cbe7adf4b485e8bb310107079f.

- 2026-09-07T07:36:58+00:00: Focused signed+DCO candidate f55f98cc79b75226a537600258dde5e57333bdeb
  is clean and limited to four routing workflow, documentation, policy, and negative-test paths.
  Full locked workspace fmt/clippy/test/doc/release build passed; actionlint, zizmor, repository
  policy, complete failure fixtures, runner scripts, exact-range Gitleaks,
  privacy/scope/DCO/signature checks passed. One initial full-gate wrapper failed before build
  because dash rejected pipefail; the corrected explicit Bash run passed. No public PR workflow
  changed, no persistent runner dispatch occurred, and AR-0832/AR-0833 qualification limits remain
  explicit.

- 2026-09-07T07:37:51+00:00: Recorded command exit 0; command argv SHA-256
  f74d24a6d01f4417d03b18e437718bdb6a5a4c71e851ef05c41466e822d43033.
