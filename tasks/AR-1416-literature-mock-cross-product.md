---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1415",
    "AR-1401",
    "AR-1402"
  ],
  "id": "AR-1416",
  "next_action": "Promote after AR-1415 is done; exercise every locally executable literature selector through plan, mock run, replay, and report paths.",
  "owner": "",
  "plan": "../plans/AR-1416.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Prove end-to-end selectable literature workloads with deterministic local or LiteLLM-compatible mocks and no live provider dependency.",
  "task_revision": 2,
  "title": "Literature workload local-mock cross-product",
  "updated_at": "2026-09-24T18:20:25+00:00",
  "worktree_key": ""
}
---

This AR owns executable development coverage only. It does not qualify upstream
benchmarks, native platforms, external evaluators, or live model providers.

Acceptance requires a bounded deterministic fixture (or LiteLLM-compatible local
mock) for every literature family marked locally executable. Each fixture must
exercise preparation, agent interaction, grading, timeout/failure, reset, record,
replay, and report paths with content-addressed evidence and resource limits.
Provenance-only or unavailable records remain selectable for inspection but fail
closed before execution. Tests must prove that no API key, public network,
privileged container, or native host is needed.

Verify focused cross-product tests, privacy and formal checks, full quality gates,
exact-head CI, independent review, and all required post-merge workflows.

- 2026-09-24T18:20:25+00:00: AR-1415 is durably done at merge c533734a with all seven post-merge
  workflows successful. Dependencies AR-1401 and AR-1402 are complete; promote AR-1416 for bounded
  local-mock cross-product execution coverage with no live provider or network.
