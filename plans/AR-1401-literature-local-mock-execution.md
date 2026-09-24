# AR-1401: Local deterministic execution for literature workloads

## Objective

Make the documented literature workload families runnable in development and
CI without external providers, credentials, network access, or native hosts.
Each family gets a bounded deterministic local fixture/mock evaluator that
exercises the same workload identity, prompt, attempt, scoring, cleanup, and
report contracts as a real evaluator without claiming official benchmark
results.

## Scope

- Cover repository repair (SWE-bench family, SWE-Lancer, SWE-rebench), terminal
  tasks (Terminal-Bench and AgentBench), code controls (Aider Polyglot,
  BigCodeBench, EvalPlus, LiveCodeBench), systems/performance (SWE-Perf,
  SWE-fficiency, CORE-Bench), and stateful/tool-use (tau-bench, AgentDojo,
  Harbor, Inspect AI, HAL-compatible tasks).
- Use local LiteLLM-compatible or in-process deterministic model doubles and
  fixture repositories/tasks; never require a live backend connection.
- Preserve official evaluator boundaries and label mock results as
  `development-mock`, never as benchmark qualification or leaderboard scores.

## Acceptance

- Every family has at least one positive mock and negative/failure-path test
  for malformed tasks, digest/license mismatch, timeout, reset, grader
  isolation, and denied egress.
- Runs remain bounded, offline after installation, privacy-safe, and carry
  source/revision, adaptation, evaluator, mock, workload, scorer, and result
  digests. Replays and reports distinguish mock from official results.
- No external API key, dataset, image, provider, or native architecture is a
  completion gate; missing real evidence remains explicitly unavailable.

