---
{
  "branch": "feature/ar-1784-command-dependency-registry-and-preflight",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1776"
  ],
  "id": "AR-1784",
  "next_action": "Wait for all exact-main workflows at 14de8bce to finish green, then perform post-merge verification and close AR-1784 with durable evidence.",
  "observed_branch": "feature/ar-1784-command-dependency-registry-and-preflight",
  "observed_dirty": 1,
  "observed_head": "e85e6872f055209fb54de3e4e5c3f62353db80f5",
  "owner": "",
  "plan": "../plans/AR-1784-command-dependency-registry-and-preflight.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:e7c553413f7c1d4ed9af151651fc42bf2b2911a514808d9c4c54d67d8248f673",
    "evidence_ref": "github/pr575/14de8bce/ar1784-closeout",
    "spec_ref": "specs/AR-1784.json",
    "spec_revision": 2,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1784.json",
  "spec_revision": 2,
  "status": "done",
  "summary": "PR #575 merged at signed local merge 14de8bce.",
  "task_revision": 105,
  "title": "Command dependency registry and preflight",
  "updated_at": "2026-10-11T11:44:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1784-command-dependency-registry-and-preflight"
}
---

Create a generated, typed registry that maps every public ASB command, adapter,
monitor, runtime path, and source-build recipe to the exact executable tools,
workload bundles, libraries, and host capabilities it needs. A dependency is
either an `asb tool install` supported ID, an `asb workload install` supported
ID, a catalog-pinned project build dependency, or an explicitly host-only
capability with a concrete platform remediation. No command may invoke or assume
an undeclared executable.

The initial required executable IDs are: `aider`, `codex`, `gemini`, `goose`,
`mini-swe`, `opencode`, `opendesk`, `openhands`, `openjiuwen`, `qwen-code`,
development-only `cli2key`, optional `perf`, and optional `bpftool`. Provider
APIs are not installable tools. Core procfs/cgroup collection needs no external
binary. Linux/cgroup-v2/user-systemd/Bubblewrap and kernel permission/BTF/PMU
conditions are host capabilities, not pretend downloads; preflight must report
them before execution with the owner/action needed to repair them.

Expose an `asb` preflight/status view that reports readiness, missing supported
IDs with exact install commands, missing project-local dependencies, and
uninstallable host-only conditions before a run starts. Generate coverage from
authoritative dispatch/adapter/build/workload declarations, so adding future
tools or workloads requires catalog, command-dependency, preflight, selection,
and end-to-end development-run tests in the same change.

- 2026-10-11T08:10:08+00:00: AR-1776 is complete and its tool catalog is available; promote
  dependency-ready AR-1784 for implementation.

- 2026-10-11T08:10:11+00:00: Claimed by ar1784_dependency_registry_luna56.

- 2026-10-11T08:10:16+00:00: Heartbeat by ar1784_dependency_registry_luna56.

- 2026-10-11T08:10:39+00:00: Recorded command exit 0; command argv SHA-256
  431771e25c6fcb63cee2c212739b3c89638fc0e4eea3b496d3f3b0603f464748.

- 2026-10-11T08:11:05+00:00: Recorded command exit 0; command argv SHA-256
  a80c3db7ed242b537b65e8f3b4a3ddb2554300ce2b1a5e4f8d3ac0651f3d0869.

- 2026-10-11T08:12:21+00:00: Recorded command exit 0; command argv SHA-256
  c7323847342774673319b7ffd857e626b77892358d868ecb570bff056d311898.

- 2026-10-11T08:12:46+00:00: Recorded command exit 0; command argv SHA-256
  ebd2395a6f3af72a541d6b9dd8ffecb9ec9085e6f64d76d108293c9c622d6a56.

- 2026-10-11T08:13:14+00:00: Recorded command exit 101; command argv SHA-256
  0e8b8ec438821ebf3b5b185af8adff8c05c54025dba46010f1057a05ba1d6d2b.

- 2026-10-11T08:13:41+00:00: Recorded command exit 0; command argv SHA-256
  c7323847342774673319b7ffd857e626b77892358d868ecb570bff056d311898.

- 2026-10-11T08:14:06+00:00: Recorded command exit 0; command argv SHA-256
  a4eb05d6d82c911062a7e91d765c0bcdc391fb7aa6781e391d86d09d8ae4a11b.

- 2026-10-11T08:14:33+00:00: Recorded command exit 0; command argv SHA-256
  47bcc84d3b9fdd5b3bb1e5ae460b912d8bf60595e58088926ab03e366e708695.

- 2026-10-11T08:14:49+00:00: Recorded command exit 101; command argv SHA-256
  0e8b8ec438821ebf3b5b185af8adff8c05c54025dba46010f1057a05ba1d6d2b.

- 2026-10-11T08:15:24+00:00: Recorded command exit 0; command argv SHA-256
  c7323847342774673319b7ffd857e626b77892358d868ecb570bff056d311898.

- 2026-10-11T08:15:54+00:00: Recorded command exit 101; command argv SHA-256
  0e8b8ec438821ebf3b5b185af8adff8c05c54025dba46010f1057a05ba1d6d2b.

- 2026-10-11T08:16:37+00:00: Root cause of repeated exit 101: preflight was added as an
  InvocationKind while an accidental stale CommandKind::Preflight arm remained after family mapping
  to Doctor. Remove stale arm and rerun cargo check. Wrapper post-reconcile also repeatedly saw
  disposable handoffctl pycache size guard; preserve and quarantine generated bytecode.

- 2026-10-11T08:16:46+00:00: Recorded command exit 101; command argv SHA-256
  0e8b8ec438821ebf3b5b185af8adff8c05c54025dba46010f1057a05ba1d6d2b.

- 2026-10-11T08:17:18+00:00: Recorded command exit 0; command argv SHA-256
  0e8b8ec438821ebf3b5b185af8adff8c05c54025dba46010f1057a05ba1d6d2b.

- 2026-10-11T08:18:03+00:00: Recorded command exit 0; command argv SHA-256
  82b893c0185fef6d76635523b4de3b7a2baadcdf82314f52f1db386a60d2503d.

- 2026-10-11T08:18:38+00:00: Recorded command exit 0; command argv SHA-256
  eadb1624311d49cd479c401aed6471f8f6a4eeac5e00ffdf4dc1da70c5b0b256.

- 2026-10-11T08:19:21+00:00: Recorded command exit 0; command argv SHA-256
  c7323847342774673319b7ffd857e626b77892358d868ecb570bff056d311898.

- 2026-10-11T08:20:25+00:00: Recorded command exit 0; command argv SHA-256
  2bd70e0c26aa986612d3eee65d9d3a6c101e21a93620f69f0b2353ef488adf00.

- 2026-10-11T08:21:15+00:00: Recorded command exit 0; command argv SHA-256
  c50160c33f34ec7955196138b6f40b52c9c3006f8928e00c37e1ca66932c1fee.

- 2026-10-11T08:21:51+00:00: Recorded command exit 101; command argv SHA-256
  770ef66e05618edaf585abd6d89f8f4b9cea6dae022116745e9147ef57d01a1d.

- 2026-10-11T08:23:11+00:00: Complete asb-cli suite exposed three concrete failures: optional
  perf/bpftool host-tool remediation was incorrectly asserted as ASB-installable (test fixed to
  require install syntax only for mandatory tools); public command inventory lacked its preflight
  golden fixture (fixture row added); one existing human error-presentation assertion was
  environment/baseline-sensitive and showed output-parent wording, to be rechecked independently.

- 2026-10-11T08:23:33+00:00: Recorded command exit 1; command argv SHA-256
  6e451b47efa59de3b300c2fe3ff0278cab5c6d099c43967c15fb3b77515626c2.

- 2026-10-11T08:23:58+00:00: Recorded command exit 0; command argv SHA-256
  82b893c0185fef6d76635523b4de3b7a2baadcdf82314f52f1db386a60d2503d.

- 2026-10-11T08:24:47+00:00: Recorded command exit 101; command argv SHA-256
  634ca9b663d7d070b704cdbbf6ef7bfaccf7ae3bff834259c9289b273eaac204.

- 2026-10-11T08:25:36+00:00: Recorded command exit 0; command argv SHA-256
  634ca9b663d7d070b704cdbbf6ef7bfaccf7ae3bff834259c9289b273eaac204.

- 2026-10-11T08:26:21+00:00: Recorded command exit 0; command argv SHA-256
  71438883e0e7f3c41f793a3d738713da6206360a4d1273aa78f4b4aaa64205e4.

- 2026-10-11T08:27:10+00:00: Recorded command exit 0; command argv SHA-256
  fb41037a684c4eacabd62eb60a0ae25a18a6247d6c01ca1a8338a3de1e54b7d4.

- 2026-10-11T08:27:39+00:00: Recorded command exit 101; command argv SHA-256
  770ef66e05618edaf585abd6d89f8f4b9cea6dae022116745e9147ef57d01a1d.

- 2026-10-11T08:27:57+00:00: Full asb-cli rerun is deterministic for AR-1784 changes: 348/349
  passed; only existing
  human::tests::error_presentations_name_cause_state_and_recovery_without_private_text fails on
  legacy output-parent-unavailable wording (expected state-change phrase absent; output says
  requested input/configuration needs correction and no successful state change). New
  dependency_registry tests all pass, and preflight public-command golden/inventory test passes. Do
  not mask or weaken unrelated diagnostic gate.

- 2026-10-11T08:29:01+00:00: Recorded command exit 0; command argv SHA-256
  c7323847342774673319b7ffd857e626b77892358d868ecb570bff056d311898.

- 2026-10-11T09:29:17+00:00: Recorded command exit 0; command argv SHA-256
  e45166d416386a84ac1c6ccdf6568aba68edc9b31afe819c372007130238329b.

- 2026-10-11T09:29:37+00:00: Recorded command exit 0; command argv SHA-256
  f78e3317aefc8f52c370a779a97f3484553f21ee8ffb202c888e81a132b00656.

- 2026-10-11T09:29:59+00:00: Recorded command exit 0; command argv SHA-256
  f421d2315b13a7cc6c1a2251112d50358fb36085cf0f632589e3285b16e5b562.

- 2026-10-11T09:30:21+00:00: Recorded command exit 0; command argv SHA-256
  7926f54e20391f644ebf2185aacdb6c382142b5d8ec883e1b3fd77ddc6089183.

- 2026-10-11T09:31:24+00:00: Recorded command exit 0; command argv SHA-256
  e45166d416386a84ac1c6ccdf6568aba68edc9b31afe819c372007130238329b.

- 2026-10-11T09:31:44+00:00: Recorded command exit 0; command argv SHA-256
  01eb88adfb050b8b8649d5893923b92287e25bba35e8674c9ff74a68d8ca56a6.

- 2026-10-11T09:32:27+00:00: Recorded command exit 0; command argv SHA-256
  7af55055d07e2aed222127bc595e9652065a57d1f50c732e68a57cbcf8c828ce.

- 2026-10-11T09:32:53+00:00: Recorded command exit 0; command argv SHA-256
  01eb88adfb050b8b8649d5893923b92287e25bba35e8674c9ff74a68d8ca56a6.

- 2026-10-11T09:33:15+00:00: Recorded command exit 0; command argv SHA-256
  87167633cfbb13f5ffd91b788b8781aa9a81f57cf0608ef0ab21bb5189a4d96d.

- 2026-10-11T09:33:38+00:00: Recorded command exit 0; command argv SHA-256
  7926f54e20391f644ebf2185aacdb6c382142b5d8ec883e1b3fd77ddc6089183.

- 2026-10-11T09:39:25+00:00: Recorded command exit 101; command argv SHA-256
  4b288bcd4f1927b4bc826087dc4dc078390cd66f9f99e0dab0414e6104b9ef63.

- 2026-10-11T09:39:53+00:00: Recorded command exit 0; command argv SHA-256
  ef50617ff709bf8e7686cbd7892ab63ad22bb7aee69f48d4236f8af274539698.

- 2026-10-11T09:40:22+00:00: Recorded command exit 101; command argv SHA-256
  4b288bcd4f1927b4bc826087dc4dc078390cd66f9f99e0dab0414e6104b9ef63.

- 2026-10-11T09:41:21+00:00: Recorded command exit 0; command argv SHA-256
  40bc78a21c6c5e34ef380e3b19d623f398ed92864ee20f7cc2366b00757f0698.

- 2026-10-11T09:41:47+00:00: Recorded command exit 0; command argv SHA-256
  40bc78a21c6c5e34ef380e3b19d623f398ed92864ee20f7cc2366b00757f0698.

- 2026-10-11T09:42:15+00:00: Recorded command exit 0; command argv SHA-256
  9e8775e61128fa971ae313f6b8828b350904401e170e8484ed582650a6308f13.

- 2026-10-11T09:42:44+00:00: Recorded command exit 0; command argv SHA-256
  99d1f1b413a966aeb493056b8f075ff1c47d2e8b75980d6a408305299b0289dc.

- 2026-10-11T09:43:03+00:00: Recorded command exit 0; command argv SHA-256
  99d1f1b413a966aeb493056b8f075ff1c47d2e8b75980d6a408305299b0289dc.

- 2026-10-11T09:43:24+00:00: Recorded command exit 0; command argv SHA-256
  71b25dfc2446951b8b04ab969950782fb899ba42308a05f3d1ccf517685b9584.

- 2026-10-11T09:43:45+00:00: Recorded command exit 0; command argv SHA-256
  7926f54e20391f644ebf2185aacdb6c382142b5d8ec883e1b3fd77ddc6089183.

- 2026-10-11T09:53:17+00:00: Recorded command exit 0; command argv SHA-256
  e0145d657e4bdd6ab9cb86d9e618cbcaa0121423831c4382af2eb944cd5749d0.

- 2026-10-11T09:53:35+00:00: Recorded command exit 0; command argv SHA-256
  21f9e61762b427517f783bc4bbd7769ef5ef41939bed4b43947fe27d1067f1e2.

- 2026-10-11T09:53:55+00:00: Recorded command exit 0; command argv SHA-256
  e76a761bd64efd6a8a2c3e4ed48a18f3996dd40669b235f4d466de0bced3ea2f.

- 2026-10-11T09:54:18+00:00: Recorded command exit 0; command argv SHA-256
  7926f54e20391f644ebf2185aacdb6c382142b5d8ec883e1b3fd77ddc6089183.

- 2026-10-11T10:09:28+00:00: Heartbeat by ar1784_dependency_registry_luna56.

- 2026-10-11T10:09:33+00:00: Independent review P1 findings recorded: preflight currently lacks
  human-readable default output; readiness evaluates all 11 agent IDs instead of selected
  command/runtime scope. Preserve --json parity and fail-closed selected-scope checks.

- 2026-10-11T10:17:54+00:00: Signed DCO checkpoint e8e3b9e7: asb preflight supports selected --agent
  and --runtime host|local scopes, keeps --json equivalent, and executable default renders human
  output. Added selected-scope positive/negative tests, human/JSON integration coverage, refreshed
  448 reviewed diagnostic identities, and updated workflow provenance digest. Full asb-cli package
  tests pass.

- 2026-10-11T10:23:46+00:00: Heartbeat by ar1784_dependency_registry_luna56.

- 2026-10-11T10:28:29+00:00: Signed DCO repair b4ae226c adds project-aware fail-fast selected
  dependency preflight before run/sweep execution and before each benchmark-live matrix entry,
  preserving local-mock semantics. Synced protected main af75cd06 via signed merge 80062618;
  refreshed 435 diagnostic identities plus one final lib.rs and 13 project_run.rs identities, and
  provenance CLI digest to 89aa603de1ba5a23b2dab766fec5852ecfb1bec8e988441293dc0ee196ceb28f. Focused
  diagnostic/provenance gates, cargo fmt, and full asb-cli package tests pass. Pushed exact PR #573
  head e85e6872c0e2dd9bfaa94ea7fc1e3b7178baf005.

- 2026-10-11T10:29:25+00:00: PR #573 exact head e85e6872 has all checks queued; local focused/full
  gates pass. Portable protected-main provenance failed because existing merge 80062618 is followed
  by regular e85e6872, violating synchronization-merge-must-be-topic-tip. Existing branch/PR is
  preserved; no force-push or merge. Fresh clean superseding topic is required.

- 2026-10-11T10:31:30+00:00: Recorded command exit 1; command argv SHA-256
  776b65925810e8eb462189cd2abf9fb0a8246af2db7700172159b339b3f138ea.

- 2026-10-11T10:31:58+00:00: Recorded command exit 0; command argv SHA-256
  776b65925810e8eb462189cd2abf9fb0a8246af2db7700172159b339b3f138ea.

- 2026-10-11T10:32:26+00:00: Fresh clean branch feature/ar-1784-command-dependency-registry-clean
  starts at protected main af75cd06 and linearly replays signed AR-1784 commits, ending exact head
  5cabf776ce5218c25ebebc4650937f15eddac87a. No merge commits were introduced in the PR range. Local
  cargo fmt, focused diagnostic/provenance tests, and full asb-cli package tests pass. Published
  replacement PR #575 through handoffctl; stale PR #573 remains preserved and unmodified.

- 2026-10-11T10:43:53+00:00: Heartbeat by ar1784_dependency_registry_luna56.

- 2026-10-11T10:44:07+00:00: Hosted policy run 38132284859 failed workspace line coverage at 89.96%
  (97647/107446 lines), specifically newly exercised dependency preflight paths. Added bounded
  positive/negative tests covering valid project inventory and status, selected local/host scope
  behavior, unsupported runtime rejection, registry JSON projection, and invalid project config
  fail-closed handling. Focused dependency_registry tests and cargo fmt pass locally. Signed DCO
  commit e5f378aa4a82c058abb76c8476d6a1a5a10a75dc pushed to PR #575; awaiting exact-head hosted
  checks.

- 2026-10-11T11:13:38+00:00: Independent review complete; coordinator resumes repair.

- 2026-10-11T11:13:47+00:00: Claimed by coordinator.

- 2026-10-11T11:13:52+00:00: Recorded command exit 0; command argv SHA-256
  ce06dd6d8af853309253830a51a79d8139e15ea5719866600b13de710a9b9f91.

- 2026-10-11T11:14:50+00:00: Recorded command exit 0; command argv SHA-256
  e787c9858acf0d8c87c0638b9d5d13209c8270eee6e705e3308c903556beffec.

- 2026-10-11T11:15:02+00:00: Recorded command exit 0; command argv SHA-256
  d7b22b2bd57c86649e947a60c7424e0b0e602f6da64839dfe161d09be972fd6a.

- 2026-10-11T11:15:10+00:00: Recorded command exit 0; command argv SHA-256
  a34464c250ce2ca18df6aca5106817468471f520c0f3eee00b47a3200240001f.

- 2026-10-11T11:15:23+00:00: Recorded command exit 0; command argv SHA-256
  f430faa65ec173e7dff0287c21397e56a01e3c81a7a2216762898d71d594b307.

- 2026-10-11T11:15:35+00:00: Independent review found live run/sweep/benchmark-live scopes omitted
  Linux/cgroup-v2/user-systemd/bubblewrap host dependencies. Added mandatory host IDs and
  non-vacuous tests; focused dependency_registry 13 passed; signed/DCO repair b8a1d6a1 pushed.

- 2026-10-11T11:15:40+00:00: Heartbeat by coordinator.

- 2026-10-11T11:16:32+00:00: Recorded command exit 101; command argv SHA-256
  a0c780a3386af68b0d1556fb27352dc1f3e6cc8f01d7e0b6fb6367eedddbaa99.

- 2026-10-11T11:16:44+00:00: Recorded command exit 0; command argv SHA-256
  b6533a4fdf3fb41e1b00dfab206baaaa10e1271d1a0a78fc5806b4d8c60f66fb.

- 2026-10-11T11:17:42+00:00: Recorded command exit 101; command argv SHA-256
  a0c780a3386af68b0d1556fb27352dc1f3e6cc8f01d7e0b6fb6367eedddbaa99.

- 2026-10-11T11:17:58+00:00: Recorded command exit 0; command argv SHA-256
  d6927b0c010b3ea7c4139ab9409f2c9937d1d582e408103d35663d7c7054dfa3.

- 2026-10-11T11:19:14+00:00: Recorded command exit 0; command argv SHA-256
  a0c780a3386af68b0d1556fb27352dc1f3e6cc8f01d7e0b6fb6367eedddbaa99.

- 2026-10-11T11:19:37+00:00: Fresh independent review PASS: host IDs present in
  run/sweep/benchmark-live and tests non-vacuous. Full workspace cargo llvm-cov passed at 90.29%;
  focused PTY and tool-discovery reruns passed. No merge until hosted gates are green.

- 2026-10-11T11:19:45+00:00: Heartbeat by coordinator.

- 2026-10-11T11:31:03+00:00: Independent review passed repaired head b8a1d6a1; all PR checks were
  green. Signed local merge-integrity produced two-parent merge 14de8bce with base af75cd06, head
  b8a1d6a1, tree b4ca9f20, and published it with force-with-lease.

- 2026-10-11T11:34:42+00:00: Heartbeat by coordinator.

- 2026-10-11T11:42:47+00:00: Recorded command exit 0; command argv SHA-256
  6afe991853bdf2b485aaf037284e37360a9d18718760c9f43e9ec7ee2bcef4ac.

- 2026-10-11T11:43:02+00:00: Recorded command exit 1; command argv SHA-256
  ace39bb09538f1f0979104a67e77168d7973d230510a0fb8bbe97978f87e3473.

- 2026-10-11T11:43:18+00:00: Recorded command exit 1; command argv SHA-256
  f48acabcb1cfa0053e1ec555abb9647071d9a049a398432bf5e116a8ff2b801e.

- 2026-10-11T11:43:33+00:00: Recorded command exit 1; command argv SHA-256
  7aaf09526d6b9e24c5b20f1c2bd5d92ee77415d4ab90c71ab0f62ac59ef33913.

- 2026-10-11T11:43:43+00:00: Recorded command exit 1; command argv SHA-256
  cc1a4cdbbd266ebdf391db942e3f5a28781861c066d17e50bbdeb112501fbdf0.

- 2026-10-11T11:43:56+00:00: All exact-main workflows passed at 14de8bce, including repository
  quality.

- 2026-10-11T11:43:58+00:00: Recorded command exit 0; command argv SHA-256
  b4269758b07783f61eb48e766ffbed9792b63410e1f57f15d2455b63f13e5b36.

- 2026-10-11T11:44:08+00:00: Post-merge verification complete: all exact-main workflows passed at
  14de8bce, including repository quality.
