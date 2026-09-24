# AR-1395: Literature workload adapter boundary

## Objective

Implement a versioned workload-adapter boundary that can acquire and normalize
approved literature benchmark tasks into ASB's `describe/acquire/prepare/
prompt/evaluate/cleanup` lifecycle without vendoring datasets or changing
official grading semantics.

## Workload families

- Repository repair: SWE-bench Lite/Verified, SWE-bench Pro, SWE-rebench,
  SWE-Lancer, SWE-Perf and SWE-fficiency.
- Terminal/system tasks: Terminal-Bench and AgentBench environments.
- Code-generation controls: Aider Polyglot, BigCodeBench, EvalPlus and
  LiveCodeBench.
- Stateful/tool-use tasks: tau-bench, AgentDojo, Harbor and Inspect AI
  scenarios; HAL is a harness interoperability boundary, not a workload.
- CORE-Bench and other docs-listed candidates remain explicit unsupported
  adapters until licensing, reset and evaluator evidence exists.

## Acceptance

- Adapters consume only registry-pinned explicit downloads or local test
  fixtures, with bounded size/time, digest checks, license gates and no network
  in default/CI paths.
- Every normalized task retains source ID/revision, split/window, evaluator
  identity, adaptation relation, contamination/exposure status, platform cell,
  and exact content digest; official scorers remain isolated from agent writes.
- Local deterministic mock tasks exercise every adapter family; missing
  evaluator/image/reset/native evidence returns unavailable rather than a score.
- Positive, malformed, digest, license, path, reset, grader-isolation, timeout,
  and no-network tests pass; generated schemas/docs update together.
