# AR-1394: Literature workload registry expansion

## Objective

Turn every established workload benchmark named in `docs/WORKLOADS.md`,
`docs/RELATED_WORK.md`, and the existing AR-0404/0405/0406 provenance records
into an explicit, machine-readable workload candidate inventory. The registry
must distinguish executable workloads from methodology/scoring systems and
must never imply qualification merely because a source is listed.

## Scope

Inventory SWE-bench Lite/Verified, Terminal-Bench, Aider Polyglot, SWE-bench
Pro, BigCodeBench, HumanEval+/MBPP+ (EvalPlus), LiveCodeBench, SWE-Lancer,
SWE-rebench, SWE-Perf, SWE-fficiency, CORE-Bench, AgentBench, tau-bench,
AgentDojo, Harbor task definitions, Inspect AI scenarios, HAL harness tasks,
and any additional benchmark source explicitly cited by the current docs.
Record each source's role, official locator, code/data licenses separately,
revision/window, evaluator identity, acquisition mode, adaptation policy,
contamination/exposure risk, platform requirements, and status (`planned`,
`available`, `unsupported`, or `qualified`).

## Acceptance

- Strict versioned schema and generated documentation cover every listed
  source, with stable IDs and no unknown fields.
- No dataset, evaluator, image, credential, prompt, transcript, or private
  path is vendored; sources remain explicit-download/non-vendored until
  separately qualified.
- Methodology-only systems are classified as scoring/runner references and
  cannot be selected as executable workloads.
- Positive/negative schema, license, duplicate, stale-revision, and
  unsupported-platform tests pass offline; missing evidence remains planned.
