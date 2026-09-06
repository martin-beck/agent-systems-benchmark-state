# Agent Systems Benchmark current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0302](tasks/AR-0302-agent-opendesk.md): Implement OpenDesk client adapter | Support the bitclub OpenDesk CLI with its own dialect and compatibility record. | Inspect @bitclub.ai/opendesk-cli commands and protocol version. | root-coordination-20260906 |
| P1 | [AR-0401](tasks/AR-0401-engineering-workloads.md): Implement original engineering workloads | Deliver bug fix, feature addition, refactoring, test generation, dependency migration, build repair and repository navigation fixtures via extension API. | Run complete isolated quality/privacy/supply gates, then prepare focused signed candidate without root workspace/lock/schema edits. | replay-20260906 |
| P1 | [AR-1001](tasks/AR-1001-experiment-comparability.md): Define experiment identity and comparability | Make every comparison content-addressed and explicit about agent, model, workload and platform confounders. | Await coordinator immutable local review of signed candidate d051c5e; repair findings before any publication. Cargo workspace/lock and experiment-schema fence remains held by AR-1001. | quality-20260906 |

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0105](tasks/AR-0105-sandbox-test-portability.md): Repair sandbox test target portability | Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work. | Promote after confirming AR-0103 remains done, then repair the isolated-target fixture before resuming blocked full-tree gates. | - |

## Blocked

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0204](tasks/AR-0204-capacity-sweeps.md): Implement capacity sweeps and arrival scheduling | Run repeated closed-loop and open-loop experiments with bounded concurrency. | Await isolated-CARGO_TARGET_DIR sandbox fixture repair, then rerun full workspace tests/coverage and submit b0b2ae1 successor for review. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-0303](tasks/AR-0303-agent-aider.md): Implement aider client adapter | Support unattended aider editing with bounded input, output and repository changes. | Inspect aider batch invocation and editing lifecycle. | - |
| P1 | [AR-0304](tasks/AR-0304-agent-codex.md): Implement Codex client adapter | Use Codex noninteractive structured events or app-server with declared capability boundaries. | Inspect installed Codex help/schema and official provider configuration. | - |
| P1 | [AR-0305](tasks/AR-0305-agent-gemini.md): Implement Gemini CLI client adapter | Run pinned Gemini CLI through noninteractive JSON events. | Inspect the current official stable release, transition constraints, stream-JSON contract and provider override. | - |
| P1 | [AR-0306](tasks/AR-0306-agent-qwen-code.md): Implement Qwen Code client adapter | Run pinned Qwen Code through isolated headless stream-JSON. | Inspect the current stable release, stream-JSON contract, provider override and ambient context loading. | - |
| P1 | [AR-0307](tasks/AR-0307-agent-goose.md): Implement goose client adapter | Run pinned AAIF goose in no-session structured mode. | Inspect current release assets, structured run mode, provider configuration and extension failure behavior. | - |
| P1 | [AR-0505](tasks/AR-0505-agent-replay-conformance.md): Prove real-agent replay conformance | Test each actual client through recording and offline replay of engineering tasks. | Build production-boundary integration matrix using synthetic upstream service. | - |
| P1 | [AR-0702](tasks/AR-0702-native-platforms.md): Validate native Linux kernels and architectures | Exercise native x86_64 and aarch64 including booted openEuler kernels. | Provision disposable native test environments with isolated benchmark resources. | - |
| P1 | [AR-0801](tasks/AR-0801-terminal-interface.md): Implement terminal and automation interfaces | Provide doctor, plan, run, sweep, compare and report with stable JSON output. | Build planned commands around public library interfaces. | - |
| P1 | [AR-0902](tasks/AR-0902-fault-assurance.md): Add fuzz mutation and lifecycle fault campaigns | Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection. | Build bounded campaigns and counterexample retention. | - |
| P1 | [AR-0904](tasks/AR-0904-contract-consistency.md): Machine-check protocol and artifact consistency | Make schemas, Rust types, protocol examples, CLI capability output and documentation mechanically agree. | Define canonical sources and generated/artifact-diff gates before extension implementations fan out. | - |
| P1 | [AR-0905](tasks/AR-0905-recovery-models.md): Model execution recovery and worker fencing | Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects. | Translate Agent Relay's TLA+/Alloy/executable-model pattern to ASB run and replay domains. | - |
| P1 | [AR-1002](tasks/AR-1002-verifier-integrity.md): Protect verifiers and support offline rescoring | Separate immutable graders from agent work and version scoring independently of execution. | Design the immutable observation and score-revision contract using Inspect and Harbor concepts. | - |
| P1 | [AR-1003](tasks/AR-1003-execution-budgets.md): Enforce cost token and action budgets | Bound and report wall time, actions, tokens and monetary cost without treating unavailable telemetry as zero. | Specify budget capabilities and normalize provider usage with explicit uncertainty. | - |
| P1 | [AR-1004](tasks/AR-1004-reliability-fairness.md): Measure reliability and mixed-workload fairness | Report repeated-attempt reliability and prevent aggregate results from hiding starvation or hard strata. | Add trial/epoch aggregation following tau-bench and Inspect concepts. | - |
| P1 | [AR-1007](tasks/AR-1007-benchmark-validity.md): Maintain benchmark validity and portability registry | Track dataset provenance, contamination risk, grader validity and native portability per workload revision. | Implement registry schema and validation for built-in and imported workloads. | - |
| P2 | [AR-0202](tasks/AR-0202-kernel-diagnostics.md): Add optional kernel diagnostics | Integrate perf and optional eBPF diagnostics without making privileged tools mandatory. | Design capability probes and bounded diagnostics profiles. | - |
| P2 | [AR-0308](tasks/AR-0308-agent-mini-swe.md): Implement mini-SWE-agent client adapter | Run pinned mini-SWE-agent as a bounded batch engineering agent. | Inspect the current package, trajectory contract, LiteLLM override and environment isolation. | - |
| P2 | [AR-0309](tasks/AR-0309-agent-openhands.md): Implement maintained OpenHands SDK client adapter | Run a maintained MIT OpenHands SDK or canonical headless client. | Resolve the maintained SDK/client boundary and exclude retired or enterprise-licensed components. | - |
| P2 | [AR-0402](tasks/AR-0402-external-code-workloads.md): Integrate SWE-bench and Aider Polyglot | Add versioned external workload adapters without vendoring datasets. | Pin datasets/evaluators and evaluate image architecture parity. | - |
| P2 | [AR-0403](tasks/AR-0403-terminal-workloads.md): Integrate Terminal-Bench workloads | Import terminal tasks through an adapter to the published harness or task format. | Assess Harbor/Terminal-Bench integration contract before implementing. | - |
| P2 | [AR-0405](tasks/AR-0405-performance-workloads.md): Add performance and reproducibility workloads | Assess SWE-Perf, SWE-fficiency and CORE-Bench for correctness-preserving optimization and reproducibility. | Run compatibility spikes and accept only workload subsets with stable independent oracles. | - |
| P2 | [AR-0601](tasks/AR-0601-csb-integration.md): Prototype optional CSB integration | Reuse CSB application execution and monitoring where contracts fit ASB. | Audit bm-runner interfaces and compare subprocess integration with direct execution. | - |
| P2 | [AR-0802](tasks/AR-0802-executable-guides.md): Deliver runnable user and extension guides | Publish executable offline quickstart, workload/agent extension guide and reproducibility guide. | Capture actual CLI workflows after commands are implemented. | - |
| P2 | [AR-0903](tasks/AR-0903-release-qualification.md): Package and qualify the first release | Deliver reproducible native release artifacts with complete support and evidence statements. | Audit milestone completeness and run isolated release qualification. | - |
| P2 | [AR-1005](tasks/AR-1005-trace-interoperability.md): Export interoperable privacy-safe traces | Expose stable causal ASB events and optional standards-based telemetry without binding storage to an evolving convention. | Define stable internal trace schema and a version-pinned optional OTLP projection. | - |
| P3 | [AR-0404](tasks/AR-0404-extended-workloads.md): Expand established benchmark catalogue | Evaluate SWE-bench Pro, BigCodeBench, EvalPlus and LiveCodeBench as optional suites. | Rank suites by additional coverage and maintenance cost. | - |
| P3 | [AR-0406](tasks/AR-0406-evolving-workloads.md): Add evolving long-horizon workload sources | Assess SWE-Lancer and SWE-rebench for feature/proposal and contamination-aware evaluation. | Evaluate maintenance, licenses and reproducibility before integration. | - |
| P3 | [AR-1006](tasks/AR-1006-distributed-workers.md): Coordinate distributed experiment workers | Schedule trials across native-capability workers while preserving per-host capacity meaning. | Specify distributed control semantics after single-host measurement is stable. | - |

## Done

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001-repository-bootstrap.md): Bootstrap public repositories | Establish both public MIT repositories, Rust workspace, coordination reuse and evidence-backed plans. | No action; foundation verified. Begin AR-0002, AR-0003, AR-0101, AR-0501 or AR-0701 through the coordinator. | - |
| P1 | [AR-0002](tasks/AR-0002-coordination-assurance.md): Harden reusable coordination framework | Adapt generic coordination tooling for public ASB workers without importing private state. | Wait for AR-0003 to repair product PR DCO merge-context checks; then revalidate and integrate documentation PR before final AR-0002 release. | - |
| P1 | [AR-0003](tasks/AR-0003-quality-gates.md): Enforce Rust and repository quality gates | Install pinned analysis, coverage, workflow, documentation and supply-chain gates. | Await independent immutable-head review and coordinator integration of product PR #2; then run post-merge gates. | - |
| P1 | [AR-0004](tasks/AR-0004-ar-status-document.md): Generate the visual AR status document | Render every AR, status, and dependency as an accessible visual state document. | Await independent immutable-head review of state PR 3 at eedd311; repair findings before coordinator integration. | - |
| P1 | [AR-0005](tasks/AR-0005-transactional-promotion.md): Add transactional AR promotion | Make planned-to-open promotion a transactional handoffctl operation. | Await immutable independent review of exact state PR #4 head 4e56e83 and integrate only after verified green CI. | - |
| P1 | [AR-0101](tasks/AR-0101-extension-contracts.md): Freeze versioned extension and result contracts | Specify typed agent, workload, collector, runtime and result contracts before parallel implementations. | Await independent immutable-head delta review and coordinator integration of exact green PR #3 head 9e90c6a6; then run post-merge verification. | - |
| P1 | [AR-0102](tasks/AR-0102-process-runtime.md): Implement process execution and cancellation | Run real client processes with bounded I/O, monotonic deadlines and process-tree ownership. | Release done after successful reviewed integration, exact-main local/hosted checks, synchronized refs and live state doctor. | - |
| P1 | [AR-0103](tasks/AR-0103-sandbox-runtime.md): Implement isolated execution and resource leases | Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets. | Release AR-0103 done after exact-main local and hosted post-merge verification. | - |
| P1 | [AR-0104](tasks/AR-0104-durable-results.md): Implement durable run storage and recovery | Persist manifests, event streams, artifact hashes and recoverable execution intentions. | Await exact-head PR 6 CI and independent immutable-head review; repair findings before coordinator integration. | - |
| P1 | [AR-0201](tasks/AR-0201-portable-metrics.md): Collect portable system and session metrics | Collect procfs and cgroup v2 CPU, memory, I/O, faults, pressure and throttling. | Run final state reconcile/live doctor/full validation, then release AR-0201 done and explicitly return the Cargo workspace/lock fence. | - |
| P1 | [AR-0203](tasks/AR-0203-statistical-analysis.md): Implement statistical and SLO assessment | Compute latency distributions, quality/throughput intervals and evidence-aware SLO results. | Create and push reviewed signed+DCO no-ff merge of exact head 3bcfd85; verify PR merge identity, then run exact-main local and hosted post-merge checks. | - |
| P1 | [AR-0301](tasks/AR-0301-agent-opencode.md): Implement OpenCode client adapter | Run pinned OpenCode through its structured supported interfaces. | Await exact PR #13 head dfb0d54 hosted CI and immutable independent review; integrate only if both are green. | - |
| P1 | [AR-0501](tasks/AR-0501-replay-evaluation.md): Evaluate replay literature and reusable tools | Compare literature and record/replay implementations using identical synthetic conformance cases. | Await independent immutable-head review and coordinator integration of product PR #4; then run exact-main post-merge verification before release. | - |
| P1 | [AR-0502](tasks/AR-0502-replay-cassettes.md): Implement immutable response cassette format | Store versioned provider requests, event streams, causal IDs and integrity metadata. | Run full coordination validation, reconcile/snapshot/live doctor, verify clean synchronized repositories, then release AR-0502 done and return Cargo fence. | - |
| P1 | [AR-0503](tasks/AR-0503-strict-replay.md): Implement strict provider response replay | Serve local recorded responses while real agent and tools execute. | Run live coordination reconciliation/doctor and complete state validation; release AR-0503 done only if clean synchronized evidence remains exact. | - |
| P1 | [AR-0504](tasks/AR-0504-replay-pacing.md): Implement pacing and replay overhead assessment | Support immediate, fixed-latency, original-paced and seeded synthetic scenarios. | Run live coordination doctor/reconciliation, then release AR-0504 done with exact postmerge evidence. | - |
| P1 | [AR-0701](tasks/AR-0701-platform-manifests.md): Pin distribution and architecture support matrix | Define Ubuntu, Debian, Fedora, enterprise, openSUSE, Arch, Alpine and openEuler target manifests. | Run final coordination repository validation and live doctor, then release AR-0701 done if state and all product worktrees remain consistent. | - |
| P1 | [AR-0901](tasks/AR-0901-formal-assurance.md): Prove critical state and concurrency invariants | Use bounded proofs and model tests for safety-critical domain logic. | Await independent immutable-head review of PR 14 at 2a495a99; repair any findings without merging or releasing. | - |
