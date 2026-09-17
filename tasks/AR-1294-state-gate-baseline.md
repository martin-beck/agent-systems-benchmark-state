---
{
  "branch": "repair/ar-1294-state-gate-baseline",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1294",
  "next_action": "Audit the vendor lock/digest mismatch and root-owned TLC admission lock; repair only through immutable provenance and owner-safe lock handling, then rerun full state/formal gates.",
  "observed_branch": "repair/ar-1294-state-gate-baseline",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1294.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Restore vendor and formal admission baseline integrity needed to qualify AR-1293.",
  "task_revision": 17,
  "title": "State formal-gate baseline integrity",
  "updated_at": "2026-09-17T05:00:34+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1294-gate-baseline"
}
---

## AR-1294

AR-1293 exposed two pre-existing state-gate failures. This AR owns only
provenance-safe vendor reconciliation and owner-safe formal admission. It must
not touch ASB product or asb-tui sources, modify/extract handoffctl, weaken
formal checks, or manipulate another service's lock.

- 2026-09-17T04:56:19+00:00: Independent infrastructure repair for AR-1293 baseline gates; no
  product or handoffctl scope.

- 2026-09-17T04:56:51+00:00: Claimed by asb-ar1294-vendor-lock.

- 2026-09-17T04:56:58+00:00: Recorded command exit 1; command argv SHA-256
  73f9955b98d559c2b06ace66138b995891af97bf31e3ccac58358f49ca9f9a2e.

- 2026-09-17T04:57:12+00:00: Recorded command exit 0; command argv SHA-256
  b9bdf1362a5e638d1cc8808b53f040d5e310932d3e399b44047e65eb7e8d3121.

- 2026-09-17T04:57:26+00:00: Recorded command exit 0; command argv SHA-256
  4fb9a350290cf0d34094df009ae398978b04211f084d1bb146a061b21530d220.

- 2026-09-17T04:57:42+00:00: Recorded command exit 0; command argv SHA-256
  29249b4e8201fa2f1f60ff13612b01a7a3096a992741a1267682aacc2fc18937.

- 2026-09-17T04:57:51+00:00: Recorded command exit 0; command argv SHA-256
  57d851d6371c11504c1ecb0ac1fc6f9be1d6afdb10eceab55818797b72b614c9.

- 2026-09-17T04:58:10+00:00: Recorded command exit 0; command argv SHA-256
  6c1ca67ab4525400e82cac74ce31c94bb83851868b63dbfed667985b2b5f5d26.

- 2026-09-17T04:58:49+00:00: Recorded command exit 0; command argv SHA-256
  73f9955b98d559c2b06ace66138b995891af97bf31e3ccac58358f49ca9f9a2e.

- 2026-09-17T04:58:59+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T04:59:07+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-17T04:59:21+00:00: Recorded command exit 0; command argv SHA-256
  8ce4299f19818ff900b084b2ae703a82588599c58fce6f8d71fe8e9618222ab1.

- 2026-09-17T04:59:31+00:00: Recorded command exit 0; command argv SHA-256
  4b75eba7b907203ae98559a689e21bee85d890f99f755fcc2566c1216ccce9cf.

- 2026-09-17T04:59:50+00:00: Recorded command exit 2; command argv SHA-256
  8ad19f5dfe2e7b2007d75bc1202a25e517cd4cb6ca4e53a00b2a1c440331dbdf.

- 2026-09-17T05:00:15+00:00: Heartbeat by asb-ar1294-vendor-lock.

- 2026-09-17T05:00:34+00:00: Verified immutable coordinator pin v0.3.7 at
  550c014c440cc9bc45727fea71d90a9025c554c3. Restored vendored docs digest and moved local
  merge/post-merge policy into docs/COORDINATOR_LOCAL_POLICY.md; handoffctl_vendor verify passes.
  Formal portable smoke reaches missing tools/tlc_runner.py on main; existing
  /tmp/agent-workflow-coordinator-tlc-admission.lock and queue are external
  gha-workflow-coordinator-owned and untouched. No product, asb-tui, or handoffctl source changes.
  AR-1293 must supply an isolated owner-safe runner path, then rerun formal gates.
