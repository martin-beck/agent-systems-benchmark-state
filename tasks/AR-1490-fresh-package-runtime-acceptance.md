---
{
  "branch": "qualification/ar-1490-fresh-package-runtime-acceptance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T16:49:58+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1488",
    "AR-1489"
  ],
  "id": "AR-1490",
  "next_action": "Recreate the disposable fixture agent inside the declared AR-1490 worktree, then generate a valid plan and run installed doctor/setup/run/sweep/replay/cancellation/restart/cleanup using unsigned-development verification.",
  "observed_branch": "qualification/ar-1490-fresh-package-runtime-acceptance",
  "observed_dirty": 0,
  "observed_head": "45df6590cbf9ab75f07dcc0b753335949e28d937",
  "owner": "ar1490-dev-acceptance-luna56",
  "plan": "../plans/AR-1490-fresh-package-runtime-acceptance.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run fresh package first-customer runtime acceptance and produce an explicit readiness report.",
  "task_revision": 33,
  "title": "Fresh package runtime acceptance",
  "updated_at": "2026-09-28T14:50:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1490-fresh-package-runtime-acceptance"
}
---

Dependency-safe successor after AR-1489. This task performs actual fresh
package/runtime acceptance where the prior AR documented the contract. It
remains credential-free, local/mock/replay-only, ASB-only, and fail-closed
when exact package or clean-environment inputs are absent.

- 2026-09-27T15:35:00+00:00: Created after AR-1489 completion to produce fresh
  package execution evidence and an explicit first-customer readiness report.

- 2026-09-27T15:36:26+00:00: Dependencies AR-1461, AR-1462, AR-1488, and AR-1489 are done. Promote
  fresh ASB package/runtime acceptance with local/mock/replay-only readiness evidence.

- 2026-09-27T15:36:29+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T15:36:38+00:00: Recorded command exit 0; command argv SHA-256
  13f4f9c5f67aa4aed2c2b85c387264f5d51709a5131bd7ca39d58e9e03b0f72d.

- 2026-09-27T15:37:02+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:37:05+00:00: Recorded command exit 0; command argv SHA-256
  9c871eb63a09d923032d11427c68c4161a79ef46972d321b12953fd680a23d43.

- 2026-09-27T15:37:28+00:00: Recorded command exit 0; command argv SHA-256
  a82b9d78dcb8d4efcf094a688a35b769dde348a2e6f10888f6ea9e7219af138d.

- 2026-09-27T15:38:50+00:00: BLOCKED by missing external qualification inputs, not product failure.
  Approved bounded search via handoffctl covered current worktree and /srv/data/projects for runtime
  bundle archives/manifests; no ASB runtime tar archive or verified release package found.
  docs/RUNTIME_BUNDLES.md and build_runtime_bundle.py require supervisor/sidecar plus signing key,
  allowed-signers, principal, ssh-keygen digest; none are provisioned. Unsigned-development output
  would not be first-customer release evidence and was not substituted. Next action: provision exact
  signed package and rerun clean install/doctor/setup/run/sweep/replay/cleanup acceptance. No
  product/asb-tui/provider changes made.

- 2026-09-28T14:36:37+00:00: User-authorized development build may use the explicit
  unsigned-development bundle profile; preserve customer-release signing evidence as an optional
  future gate and do not treat development output as a customer release.

- 2026-09-28T14:36:40+00:00: Claimed by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:38:48+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-28T14:39:07+00:00: Recorded command exit 0; command argv SHA-256
  9e808f764c153d2f3035fc39bfa8cca7bbe5bc485685eb9f14c5241806c63cb2.

- 2026-09-28T14:39:24+00:00: Heartbeat by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:39:31+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-09-28T14:40:31+00:00: Recorded command exit 0; command argv SHA-256
  f9c92d9ddfe3cd1a3128731ad7e01ed88f99a3d42e745721f25b7aca37e63c8c.

- 2026-09-28T14:41:18+00:00: Recorded command exit 0; command argv SHA-256
  8f88dd87044422ff7dc83e0d414f2d0cc66c2d4276edb4147c1e789c0e383015.

- 2026-09-28T14:42:18+00:00: Recorded command exit 0; command argv SHA-256
  d390d27c4ed46df463802c4ad5b858653ca03e940169f758a71c7c4914ba97c0.

- 2026-09-28T14:43:24+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-28T14:43:57+00:00: Recorded command exit 0; command argv SHA-256
  994b8cdfb6f43f8b69b424c11fe7ddfd0461c3828b69b44f3e46851093275100.

- 2026-09-28T14:44:23+00:00: Recorded command exit 0; command argv SHA-256
  fa1894b0e944e220dc5db5ff43d12d6517531832363cd96f63d4940e49c2fa02.

- 2026-09-28T14:44:49+00:00: Recorded command exit 0; command argv SHA-256
  0ea33d8e77fb93f7bba377fb23d135003b4f010654080aa5fdb5b04249115f0f.

- 2026-09-28T14:45:16+00:00: Recorded command exit 0; command argv SHA-256
  f1e5d98a9666cf7f804f09ac78c31a60f8d63c09089043443bed6014b2d428a3.

- 2026-09-28T14:45:41+00:00: Recorded command exit 0; command argv SHA-256
  2e43c64d82f76986d6dafb407d725bffa3470028320ebbd2848f2226d155eebe.

- 2026-09-28T14:45:58+00:00: Recorded command exit 0; command argv SHA-256
  dcaafadcd6200426c55f6465aa8e70e146bbb580067e67f21a9c79d3cc895da1.

- 2026-09-28T14:46:31+00:00: Recorded command exit 0; command argv SHA-256
  2bd4c84f2d3f9af31bf02cd144d693558fa6e56f91a8b131e1f50267af820bf8.

- 2026-09-28T14:47:31+00:00: Recorded command exit 0; command argv SHA-256
  b04345386e0670e350203b5e5d84e3ced2a7f795d5cdca112ff349e26b25eac2.

- 2026-09-28T14:47:55+00:00: Recorded command exit 0; command argv SHA-256
  43e18db767ce8b56c813e2f36cde7a1b7ad1b85fa3619f7edf6561e62e8c1900.

- 2026-09-28T14:49:34+00:00: Recorded command exit 1; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T14:49:58+00:00: Heartbeat by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:50:12+00:00: Recorded failure: the first fixture-agent creation attempt exited 1
  because apply_patch placed ar1490-fixture-agent.sh in the unrelated agent-workflow-quality
  checkout, so the AR worktree had no fixture file and no product mutation occurred. The stray file
  was immediately deleted. Next action is to create the fixture only in this declared ASB AR
  worktree and continue acceptance.

- 2026-09-28T14:50:31+00:00: Recorded command exit 0; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.
