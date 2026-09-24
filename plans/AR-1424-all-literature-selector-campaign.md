# AR-1424: Complete literature selector and local campaign matrix

## Objective

Extend the unified workload selector and multi-agent campaign so every
literature workload that is locally executable through deterministic fixtures
or a LiteLLM-compatible loopback mock can be selected beside the built-in
software-engineering workloads.  Every other literature record remains visible
with its precise unavailable reason and fails closed before network, provider,
privileged-host, or dataset acquisition activity.

The campaign matrix must preserve each benchmark's semantics: repository and
terminal repair, multilingual editing, function-level correctness, time
windows, interactive/tool-use utility and safety, long-horizon repair,
performance/correctness, and computational reproducibility.  Incompatible
scores must never be collapsed into one ranking.

The selector matrix must explicitly cover SWE-bench Lite/Verified/Pro,
Terminal-Bench, Aider Polyglot, Exercism, BigCodeBench, EvalPlus
(HumanEval+/MBPP+), LiveCodeBench, SWE-Lancer, SWE-rebench, SWE-Perf,
SWE-fficiency, CORE-Bench, AgentBench, tau-bench, and AgentDojo, in addition
to all seven `original.*` fixtures.  Harbor, Inspect AI, HAL, AgentOps, and
HELM remain visible methodology/framework records and are rejected as runnable
workloads unless a later AR supplies a task protocol and independent grader.

## Dependencies

- AR-1423 (exhaustive docs-to-registry reconciliation)
- AR-1430 (complete stable literature identity/catalog and selector boundary)
- AR-1420 (literature campaign integration)
- AR-1416 (local-mock cross-product)

## Acceptance

- `doctor`, plan validation, CLI selection, recording, replay, comparison,
  reporting, and campaign planning emit one deterministic inventory containing
  all seven built-ins and every reconciled literature identity.
- Each locally executable family has bounded local fixture coverage for
  prepare, run, grade, timeout/reset, malformed output, record, replay, and
  report; a loopback LiteLLM-compatible mock is the only model/provider path in
  development and CI.
- Unavailable, provenance-only, missing-license, mutable-window, missing-image,
  or unsupported-platform records are selectable for inspection only and fail
  closed with a stable reason before any external side effect.
- Campaign output retains per-family metrics and evidence states, rejects
  unknown/duplicate/stale IDs, and refuses to claim official, native, timing,
  or evaluator qualification from mock/container evidence.
- Positive and negative tests cover every family in the reconciled matrix,
  including the complete code-generation controls and performance suites.
- Selector output is deterministic and namespaced; a user can select any
  locally executable family by stable ID and can inspect, but not execute,
  every provenance-only or framework-only record with its stable boundary
  reason.

## Verification

Run focused selector/campaign/mock tests, privacy and formal checks, generated
catalog parity, full workspace quality, exact-head CI, independent review, and
all required post-merge assurance workflows.
