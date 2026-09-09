---
{
  "branch": "feat/llm-fixture-scenario-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:27:33+00:00",
  "depends_on": [
    "AR-0888"
  ],
  "id": "AR-0889",
  "next_action": "Specify and implement the selected synthetic fixture and scenario contract with strict evidence labels, privacy bounds, and fail-closed validation.",
  "observed_branch": "feat/llm-fixture-scenario-contract",
  "observed_dirty": 0,
  "observed_head": "4d15bbc7e1d06e26b21364c3fdbc00827803e584",
  "owner": "codex-longrun-llm-fixture-contract-20260909",
  "plan": "../plans/AR-0889.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define generated synthetic LLM scenarios without weakening the existing content-addressed cassette replay contract.",
  "task_revision": 34,
  "title": "Define the LLM fixture and scenario contract",
  "updated_at": "2026-09-09T08:27:37+00:00",
  "worktree_key": "agent-systems-benchmark-llm-fixture-scenario-contract"
}
---
## AR-0889

Turn selected spike findings into an ASB-owned synthetic fixture/scenario contract while preserving strict replay as a separate recorded-response evidence class.

- 2026-09-09T08:15:55+00:00: Dependency AR-0888 is released done; promote the synthetic LLM
  fixture/scenario contract with strict evidence labels and fail-closed privacy bounds.

- 2026-09-09T08:15:58+00:00: Claimed by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:16:01+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:16:04+00:00: Recorded command exit 0; command argv SHA-256
  31ed81ee531312064c694654a7726d240d2987b6feba7aa0b71eba94585b65fc.

- 2026-09-09T08:19:41+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:19:51+00:00: Implemented synthetic scenario schema, canonical validator/hash,
  generated public fixture, and hostile tests. Enforces synthetic-only origin, closed fields,
  ordered/session/size bounds, loopback URLs, credential/private-data rejection, and preserves
  cassette separation. Six focused tests, Ruff, strict mypy, and diff-check pass.

- 2026-09-09T08:20:03+00:00: Recorded command exit 0; command argv SHA-256
  688dd0254ca55929282dc33ddb11b22c1bc07a192b868f0738f690e9d271e539.

- 2026-09-09T08:20:32+00:00: Recorded command exit 0; command argv SHA-256
  a3e01a00ba0176c71334c4d82c8aac02d831b7314ef58dcb31abf82bd8fb0924.

- 2026-09-09T08:20:51+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:20:55+00:00: Recorded command exit 8; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:21:50+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:21:53+00:00: Recorded command exit 8; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:22:10+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:22:45+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:22:49+00:00: Recorded command exit 8; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:23:08+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:23:44+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:23:59+00:00: Recorded command exit 8; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:24:07+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:24:55+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:24:58+00:00: Recorded command exit 8; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:25:15+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:25:57+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:26:01+00:00: Recorded command exit 0; command argv SHA-256
  bd587645fac4e8eda4cccb01ba8e60c376ac12d5bf5d15a56130fdbbdcdc80a7.

- 2026-09-09T08:26:16+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:26:30+00:00: Recorded command exit 0; command argv SHA-256
  b9da8151f2836d4bd32ff361f86316e57f3d66be5a1991a1cecd5a1b40aab0e7.

- 2026-09-09T08:26:48+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:26:52+00:00: Recorded command exit 0; command argv SHA-256
  c48082a9689122c4c8c8d71eced85407c967c57c0e71d4ca2b37727b17410af8.

- 2026-09-09T08:27:33+00:00: Heartbeat by codex-longrun-llm-fixture-contract-20260909.

- 2026-09-09T08:27:37+00:00: Recorded command exit 0; command argv SHA-256
  9aa0d3b96333e50ee716dbeda0e027159a59be9e392eb124c1ded276c2ffc982.
