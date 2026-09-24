---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1424", "AR-1417", "AR-1418"],
  "id": "AR-1425",
  "next_action": "Promote only after AR-1424, AR-1417, and AR-1418 are released; independently verify the complete built-in plus literature workload surface and all release gates.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1425-literature-workload-release-readiness.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Independently verify release readiness of the complete built-in and literature workload surface.",
  "task_revision": 1,
  "title": "Literature workload release-readiness gate",
  "updated_at": "2026-09-24T20:00:00+00:00",
  "worktree_key": ""
}
---

This is a final audit and integration gate. It never requires live providers,
upstream dataset downloads, native hosts, or signed bundles for development
fixtures; those remain independently labeled evidence boundaries.

Its evidence table must cover the seven built-in software-engineering fixtures
plus SWE-bench Lite/Verified and Pro, Terminal-Bench, Aider Polyglot and
Exercism tracks, BigCodeBench, EvalPlus, LiveCodeBench, SWE-Lancer, SWE-rebench,
SWE-Perf, SWE-fficiency, CORE-Bench, AgentBench, tau-bench, and AgentDojo.
Harbor, Inspect AI, HAL, AgentOps, and HELM remain explicit non-workload
boundaries unless separately proven.
