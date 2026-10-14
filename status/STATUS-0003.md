<!-- This page is generated; the root STATUS.md index links the complete view. -->

| Next action | Run the exact-main comparison matrix for available, unavailable, asymmetric, and multi-candidate provider selections; record typed results without provider contact. |

### AR-1688 — Runner-owned cassette capture and replay qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify selected/all workload recording, complete cassette sealing, and strict offline replay from the runner-owned route. |
| Next action | No further action; exact post-merge runner-owned selected/all capture, sealing, generated-cassette strict replay, and denied-network evidence are recorded. |

### AR-1689 — Paired TUI fresh-user integration and receipt qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Independent review passed; exact paired receipt verified, pending final reconciliation/release |
| Next action | Reconcile generated projections and perform final exact-head/post-merge verification; then release AR-1689 done |

### AR-1690 — ASB development-channel current-main materializer

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the ASB dev-channel materializer that resolves the latest repository main heads, persists the selected channel, and emits a diagnostic manifest for the TUI handoff. |
| Next action | No further action; exact merged materializer and hosted evidence are recorded in quality/AR-1690-development-channel-materializer-receipt.txt. Continue AR-1691/AR-1693 paired lifecycle qualification. |

### AR-1691 — ASB default-dev fresh-user lifecycle gate

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the ASB clone-to-benchmark lifecycle with omitted dev selection, current-main provenance, recording, strict offline replay, comparison, and analysis. |
| Next action | A paired positive/negative journey receipt is recorded, but AR-1695 complete RunRequest wire-contract/backend qualification and AR-1696 TUI coverage repair remain required; after both, rerun the exact-head lifecycle and promote only with final receipt evidence. |

### AR-1692 — Paired development-channel handoff contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Publish and validate the ASB handoff that lets asb-tui consume the exact default-dev materialization without losing provenance or blocking on development credentials. |
| Next action | No further action; paired handoff implementation and hosted evidence are recorded in quality/AR-1692-paired-channel-handoff-receipt.txt. Final clean-room journey remains AR-1691/AR-1693. |

### AR-1693 — Default-dev quickstart qualification

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prove the smallest selection-driven ASB journey from clone and omitted dev channel through benchmark, recording, offline replay, comparison, and analysis. |
| Next action | The exact paired quickstart receipt is recorded, but AR-1695 complete RunRequest wire-contract/backend qualification and AR-1696 TUI coverage repair remain required; after both, rerun and promote only with final hosted/post-merge evidence. |

### AR-1694 — Deterministic development artifact identity

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make repeated ASB dev-channel TUI builds path-independent so content-addressed handoff manifests validate across clean-room materializations. |
| Next action | No further action; deterministic materialization and hosted evidence are recorded in quality/AR-1694-deterministic-artifact-receipt.txt. Final clean-room journey remains AR-1691/AR-1693. |

### AR-1695 — Fan-out RunRequest wire-contract conformance

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the paired TUI fan-out route emit and validate the complete ASB RunRequest schema against the live control contract. |
| Next action | Implement the paired contract fixture and real-backend acceptance checks for every required RunRequest field, bounded limits, digest/revision identity, and development-only warning behavior before the final lifecycle gates. |

### AR-1696 — Paired TUI trusted-main coverage and release-gate repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the TUI trusted-main coverage deficit after fan-out integration and requalify the paired release gate without weakening thresholds or development semantics. |
| Next action | Coordinate with TUI AR-1610 and add focused behavior coverage for changed fan-out, handoff, capture/replay, and comparison paths; rerun trusted-main coverage at the exact merged head and publish paired hosted evidence before AR-1691/AR-1693 closure. |

### AR-1697 — Channel specification and current-head qualification repair

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the missing authoritative channel specs and requalify ASB/TUI channel propagation, manifest provenance, compatibility, and default-dev quickstart at current main heads. |
| Next action | Complete valid AR-1674/1675-compatible state specifications, then run the current-head channel and quickstart matrix against ASB ad43609b and TUI 1cf4b43d without closing predecessor ARs from stale receipts. |

### AR-1698 — Current-head recording and strict offline qualification repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the existing ASB selected/all recording, cassette sealing, and strict offline replay implementation at the current merged ASB head so AR-1652 can be reconciled truthfully. |
| Next action | Run the current-head record, record-campaign, cassette integrity, strict offline replay, incomplete coverage, redaction, and network-denial matrix; publish a signed receipt without changing AR-1652 status from stale evidence. |

### AR-1699 — Development live-provider credential bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Connect the development setup and wizard configuration to a warning-only OpenRouter API-key reference and an explicit live-provider capability without requiring production attestation or key management. |
| Next action | No further action; retain the warning-only development setup boundary and require an operator API key only for an explicitly selected live run. |

### AR-1700 — Development live OpenRouter benchmark execution

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make &#96;asb run&#96; and benchmark/sweep routes execute real OpenRouter ChatCompletions for the selected agents and model in development mode, with bounded progress, errors, and cost/network reporting. |
| Next action | No further action; retain explicit live selection and typed operator-key/transport failures, with local/mock remaining an explicit alternative. |

### AR-1701 — Development live recording and comparison qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Record live OpenRouter responses for selected or all agents, seal a replayable cassette, and make the next run offline with comparison and analysis against the live baseline. |
| Next action | Add live-run capture selection, redaction and cassette sealing, then qualify strict offline replay, comparison, and analysis from the same benchmark manifest. |

### AR-1702 — Development live OpenRouter qualification

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run credential-backed online OpenRouter smoke and typed negative tests for the merged ASB live path without mock fallback. |
| Next action | Provide OPENROUTER_API_KEY only in the worker runtime environment, then rerun one bounded real OpenRouter request at exact ASB main 31ca7a481fca8b79bfbff126b92db6c6118beb7c and record only redacted provider/model/timing/outcome metadata; retain the already-green credential-free negative matrix. |

### AR-1703 — Current-main TUI live-control qualification

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify and repair the exact current asb-tui main PTY/control journey against ASB development live recording without pinning an older frontend or weakening live semantics. |
| Next action | Reproduce the current-main PTY action gap, repair the owning boundary, then run the exact paired live/offline journey with a real OpenRouter key when supplied and credential-free negative checks otherwise. |

### AR-1704 — Typed provider failures, model admission, and trusted curl discovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair and qualify ASB live-provider error propagation, provider/model compatibility admission, and bounded curl discovery without weakening development warning-only behavior. |
| Next action | Monitor all ten exact-main workflows for signed merge 2c6f3083504c3b2636f9e6da044a9a6f626f511c to terminal success; then record the post-merge receipt, accept/release AR-1704, reconcile durable state, and run doctor --live. |

### AR-1709 — Development live provider execution contract and credential injection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define and qualify the explicit development live provider boundary, runtime credential injection, and typed no-fallback failures. |
| Next action | PR #549 exact head 700b13b3a74401a42f9c5c1cae1a788641ac94a2 has fresh independent technical approval and all 15 exact-head checks green; merge only through signed protected-main procedure, then verify exact-main workflows. |

### AR-1710 — Wizard provider-model selection and warning-only readiness

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make provider, authentication mode, API-key readiness, agent defaults, and supported-model selection explicit and non-blocking in development setup. |
| Next action | Expose the connected provider/model catalog and readiness diagnostics to the setup/materialization boundary; qualify shared defaults, per-agent overrides, unavailable models, and warning-only development auth. |

### AR-1711 — Explicit live benchmark runner and typed failures

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide a simple explicit online benchmark command with selectable agents/workloads, typed failures, and no implicit mock or replay fallback. |
| Next action | Independent technical review accepted exact commit 653b91c09f146afc47f8b13f55d8eeeba8c794b7; await coordinator-authorized PR and hosted exact-head checks. No publication or merge is authorized by this receipt. |

### AR-1712 — Live result, recording, and comparison handoff contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define the ASB live-run result and selected/all recording handoff consumed by TUI for offline replay and comparison. |
| Next action | PR #484 merged at ASB 972a29f provides selected 2x2 and full 9x27 deterministic local-mock recording with offline_ready=true; still qualify strict network-denied replay, comparison, and paired TUI handoff before closure. |

### AR-1715 — Credential-backed development OpenRouter qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run the real OpenRouter selected/all live benchmark smoke and typed failure matrix with an operator API key, producing a privacy-safe exact-head receipt. |
| Next action | Run the post-AR-1785 CLI live qualification matrix on exact main: regenerate config-bound selection, exercise selected/all human and JSON, then complete credential-free typed negative cases without retaining the runtime key. |

### AR-1716 — Cassette provider-profile identity binding

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bind every recording index insertion to the selected provider profile identity and reject mismatched cassette metadata before mutation. |
| Next action | PR #566 rebased onto protected main 7e795589 at exact head 58a445a5; await fresh required checks green, then protected merge and exact-main verification. |

### AR-1717 — Comparison exact provider/settings/endpoint identity fences

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Require exact provider, model settings, and endpoint identity equality before comparison admits online/offline results. |
| Next action | Monitor PR #567 exact head c0e3f8f4 for fresh required CI; independent review, protected merge, postmerge verify, then accept/release. |

### AR-1718 — Portable fault-matrix network isolation repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the ASB fault matrix with explicitly validated loopback-only isolation backends and no host-network fallback. |
| Next action | Run current exact-main PR #490 post-merge fault-matrix qualification, publish the privacy-safe receipt, and independently review the evidence before releasing AR-1718. |

### AR-1719 — OpenRouter free-model catalog and wizard selection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Enumerate OpenRouter explicit :free models and free-router eligibility, normalize dynamic metadata/capabilities, and expose eligible models through provider catalog, provider-plan, and wizard selection. |
| Next action | Continue deterministic OpenRouter catalog normalization and fixtures; expose every eligible free model with typed unavailable/model-mismatch diagnostics and a credential-free/live smoke qualification path. |

### AR-1720 — Claimed-task identity and coordinator integrity

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prevent claimed AR identity and scope swaps, add auditable collision migration, and restore safe live reconciliation diagnostics. |
| Next action | Record the same-user independent-agent review of the exact isolated prototype head; no additional upstream authorization or merge is required for this development repair. |

### AR-1721 — ControlServer v1.15 dynamic OpenRouter bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expose ASB&#x27;s normalized dynamic OpenRouter provider catalog through an additive v1.15 ControlServer contract for paired TUI wizard selection. |
| Next action | Independent read-only reviewer: verify receipt b6072dfa3aefea82be76cd2444b2cc646e8cc80739558b78887343d94417d1f2 against exact current ASB 69bf9029a4976f14739cf4c25949428ff2fe0bb7 and asb-tui 60ab530dd1a09d6617514f9974217c9f08d48876, original PR #489/#296 provenance, focused test results, and all listed terminal-green hosted runs; approve or report findings before release. |

### AR-1722 — PR #487 protected-main requalification and merge-settings recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Requalify PR #487 after protected-main merge tree differed from the reviewed topic tree and recover the required merge settings without policy exceptions. |
| Next action | PR #490 exact head ac6557038 was independently reviewed and merged as 9b27d5d9. Verify post-merge ASB main, reconcile the corrected AR-1722 receipt, and release this incident only after exact-main post-merge evidence is recorded; do not require an authorized-maintainer review. |

### AR-1723 — Make the easy run default to online provider execution

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the shortest user-facing run use the configured live provider by default while keeping local mock explicit and development authentication warning-only. |
| Next action | Implement easy run default-online on the bound worktree; keep --local-mock explicit, add human/JSON positive and no-fallback negative coverage, then run focused/full gates and publish a reviewed PR. |

### AR-1724 — Make the easy sweep default to online provider execution

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Extend the simple default-online journey to bounded selected/all agent and workload sweeps with explicit mock and replay alternatives. |
| Next action | Promote after AR-1723 and recording/comparison dependencies are current; implement and qualify the bounded online sweep. |

### AR-1725 — Document two-agent OpenRouter and TUI quickstarts

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Publish a linked, executable tutorial for two-agent OpenRouter benchmarking, ASB TUI workflows, dependencies, and per-distribution installation. |
| Next action | Post-merge exact main verified at 7e795589fd4dbefecf17a7d4457623e1de33d2b4: tutorial freshness passes and broken link audit reports 0. Accept and release with protected merge evidence. |

### AR-1726 — Allow user-owned group-writable rustup shim in development

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make development asb tui installation accept a conventional user-owned 0775 rustup shim path with an explicit warning while preserving hard stable and production trust boundaries. |
| Next action | No further AR-1726 implementation action; signed main 736a65cd8904b8f4a6f1715fc86ae1c854fe2232 passed every required exact-main workflow after one documented successful rerun of the unrelated nondeterministic Goose symlink fixture. |

### AR-1727 — Repair development broker foreground-terminal handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Give the ASB development broker child correct foreground process-group ownership on the caller&#x27;s controlling terminal without weakening descendant cleanup. |
| Next action | No further implementation action; AR-1727 is merged on exact signed main 457317b21dbe300907ba7889ff68a16514fcd5c5 with terminal-green post-merge checks. Downstream asb-tui qualification may resume. |

### AR-1728 — Freeze development cli2key contract and bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define cli2key as a development-only loopback Codex OAuth bridge with an ephemeral local client key, then select and pin a qualifying implementation. |
| Next action | Release done, reconcile canonical state, and verify live doctor; dependent AR-1729 and AR-1730 may proceed from exact main 30286af46920b34096d3a48153e728f7319358a4. |

### AR-1729 — Supervise cli2key sidecar and ephemeral key

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a runtime-owned loopback sidecar lifecycle with a fresh per-invocation client key, private staging, bounded cleanup, and secret-safe evidence. |
| Next action | Construct and publish signed exact two-parent merge for PR #525; then verify post-merge workflows and close. |

### AR-1730 — Add cli2key provider and selection contracts

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a development cli2key provider profile, catalog and launch identity for loopback Responses without overstating official OpenAI support. |
| Next action | Promote after AR-1728; add protocol, control, catalog, selection, and launch contracts with fixture coverage. |

### AR-1731 — Connect Codex adapter to cli2key backend

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Project the runtime-owned cli2key endpoint, model, and ephemeral client credential into the existing Codex Responses adapter. |
| Next action | AR-1758 is repairing failed post-merge provenance for b3cb9b2; remain in progress and unaccepted until supported repair PR and exact-main checks are green. |

### AR-1732 — Integrate cli2key runs and sweeps

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make explicit cli2key selections executable through normal ASB run and sweep orchestration with bounded concurrency and typed live-development evidence. |
| Next action | PR #529 merged as signed merge 942c7b110045823c942e362e5247b6ce15027ec5; monitor all exact-main workflows, then reconcile/doctor and accept/release AR-1732 with post-merge evidence. |

### AR-1733 — Qualify and document cli2key development mode

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the complete cli2key setup, run, sweep, fault, cleanup, and privacy journey and document its development-only limits. |
| Next action | Credential-free qualification implementation committed at 12e28f8 and pushed. Run independent review, focused/full tests, open PR, exact-head CI, then merge through merge_pr.py. |

### AR-1734 — Propagate validated development tools to installed TUI

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the installed development TUI a minimal validated tool environment without inheriting ambient PATH or weakening stable launch. |
| Next action | Record spec acceptance for exact-main evidence, release done, reconcile, snapshot, and verify doctor --live. |

### AR-1735 — Harden Goose diagnostic fixture determinism

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the Goose diagnostic-and-symlink regression deterministic across native and emulated AArch64 runs. |
| Next action | Acceptance complete: preserve signed merge f3840f351c9da1657ad44af594cf2b6ae8b419c9 and receipt quality/AR-1735-goose-symlink-fixture-determinism-receipt.txt; no further implementation action. |

### AR-1736 — Require model catalogs and execution parity for every backend

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make every supported model-bearing backend enumerate selectable models and carry the exact selection through complete run and sweep execution. |
| Next action | Promote after AR-1733; inventory the canonical backend registry and implement catalog, selection, run, and sweep parity with exhaustive fixtures. |

### AR-1737 — Repair development TUI linker handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make env-cleared development TUI materialization pass the validated linker to every rustc link while retaining an empty ambient PATH. |
| Next action | Acceptance evidence is complete; publish the receipt, release AR-1737 done, reconcile, and run live doctor. |

### AR-1738 — Repair permissive development rustup permission acceptance

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Allow development rustup shim and RUSTUP_HOME permission/ownership findings with warnings instead of trusted_tool_invalid, while preserving path-shape and stable/production boundaries. |
| Next action | No further product action. PR #504 implementation and signed forward-only recovery PR #508 are complete on exact protected main bbe25d0; release AR-1738 after recording final evidence. |

### AR-1739 — Add easy channel build, install, update, and test lifecycle

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide a user-friendly native asb easy lifecycle for building, installing, updating a selected channel, testing, inspecting, rolling back, and removing ASB without cargo or Make commands. |
| Next action | Post-merge exact main 507559f workflows active; Repository quality is rerunning after transient analyzer HTTP 500 (run 37767084162), while remaining hosted workflows continue. Release only after every exact-main workflow is green. |

### AR-1740 — Add developer Makefile workflow

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add an optional ASB repository Makefile that checks prerequisites and safely wraps build, install, clean, update, and test workflows. |
| Next action | Released; preserve AR-1742 as the separate historical PR505 mismatch recovery. |

### AR-1741 — Signed protected-main recovery for AR-1738

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover signed protected-main provenance after the preserved GitHub-generated AR-1738 merge. |
| Next action | Monitor exact protected-main post-merge workflows for bbe25d0 (runs 37761614825, 37761614612, 37761614776, 37761614739, 37761614829, 37761614748, 37761614807); after all required workflows are green, release AR-1741 and update/release AR-1738 with exact signed-main evidence. |

### AR-1742 — PR #505 exact-tree recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover PR #505 protected-main exact-tree publication failure without rewriting history. |
| Next action | Released done after signed reviewed-tree PR #519 merge 5f9850c, ten successful exact-main workflows, and accepted receipt. |

### AR-1743 — Repair Make update lockfile handling

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair make update so dependency refresh never combines Cargo lockfile mutation with --locked and fails with cannot update the lock file. |
| Next action | Released; preserve the signed merge, receipt, and all-green protected-main evidence. |

### AR-1744 — Repair make test scratch-root isolation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Merged PR #511 and verified exact protected main; all required post-merge workflows are green. |
| Next action | Release AR-1744 done, reconcile state, and run doctor --live. |

### AR-1745 — Install ASB into the invoking user&#x27;s local bin

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make ASB development installation place the asb executable at the invoking user&#x27;s $HOME/.local/bin/asb by default, with a safe explicit prefix override. |
| Next action | Record completion receipt, release AR-1745 done, and reconcile live state. |

### AR-1746 — Enforce protected-main admission for AR-1722 recovery

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Apply and independently verify ASB&#x27;s merge-only protected-main settings and active exact-head ruleset so signed local integrations are enforced by GitHub. |
| Next action | Require all exact-main post-merge workflows for 2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb terminal-success, then invoke the merged typed settings apply once and audit normalized live state; stop on any rejected, partial, or ambiguous result. |

### AR-1747 — Adopt Coordinator unblock support for AR-1722

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt the official Coordinator development unblock capability in ASB state so AR-1722 can be reopened through a supported provenance-checked transition. |
| Next action | Release complete: canonical main already contains the stricter official Coordinator 113dc610 vendor adoption through reviewed PR #107/signed merge d6556e1; stale superseded PR #106 is closed unmerged and exact hosted/postmerge evidence is green. |

### AR-1748 — Portable protected-main provenance and capability admission

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Replace the unavailable Enterprise-only commit-metadata ruleset with a required portable provenance check while preserving Web Flow rejection and atomic protected-main admission. |
| Next action | Release AR-1748 done after attaching spec acceptance for independently approved PR #517/merge 31ca7a4/live-policy receipt; no further product or GitHub mutation is required. |

### AR-1749 — Bootstrap canonical Coordinator unblock vendor adoption

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bootstrap the reviewed Coordinator unblock and project evidence-policy vendor into ASB state without using an unreviewed topic-local lifecycle tool. |
| Next action | Rebuild the exact two signed implementation commits onto canonical main, publish repaired PR #107, require hosted Formal rerun and fresh independent exact-head review; do not merge stale PR #106. |

### AR-1750 — Canonicalize GitHub ruleset response and complete guarded admission

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair GitHub ruleset request/readback canonicalization and development-review admission after AR-1748 created owned ruleset 24750310 but stopped before repository-settings mutation. |
| Next action | Obtain independent receipt review of the exact AR-1750 live transaction and postmerge evidence. Do not release AR-1750 or unblock AR-1748 until that review accepts ruleset ID 24750310, merge 31ca7a48, final settings, two final audits, and exact-main workflows. |

### AR-1751 — Confine GCC linker-prefix trust after AR-1737

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Confine the PATH-free development linker handoff to validated linker material without trusting sibling GCC helpers or libraries. |
| Next action | Independent rereview of PR #518 at immutable head 2cda48c27ae99381a59dc0676126b34ec77d15ef and tree 5b75e55c7d4ee1e58df42b1e9989a96ab8994995, focusing on bounded continuous-output drain, process-group cleanup/reap, and CLOEXEC restoration. If approved, a different owner may merge and close AR-1751; this owner must not self-review or merge. |

### AR-1752 — Repair development broker v1.15 dynamic-catalog projection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Forward negotiated v1.15 provider-catalog projection through the read-only development broker so the installed public dynamic-catalog route works. |
| Next action | Release done, reconcile canonical state, and verify live doctor; parent AR-1721 may then requalify against exact main e21d6bc7 and TUI 60ab530d. |

### AR-1753 — Coordinator v0.3.59 release upgrade and integrity repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt the exact Agent Workflow Coordinator v0.3.59 release in ASB state and repair every downstream-owned integrity regression exposed by the upgrade. |
| Next action | Promote and claim; sync the exact v0.3.59 release into an isolated state worktree, repair only downstream-owned compatibility regressions, and run the complete integrity matrix before independent review. |

### AR-1754 — Make online execution the default across ASB workflows

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make configured online/live provider execution the default for canonical run, sweep, easy, recording/campaign, and TUI handoff paths while keeping local mock and strict replay explicit alternatives. |
| Next action | PR #558 now points to exact signed head 0dcd1472. The hosted Rust failure was a stale workflow provenance digest; it is repaired and the focused workflow-transcript gate passes locally. Independently review the complete diff, then wait for all 15 exact-head checks to reach terminal success. No GitHub Reviews API approval object is required; merge only through the documented signed protected-main procedure. |

### AR-1755 — Make ASB installation safely idempotent

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the ASB Make install path so rerunning plain &#96;make install&#96; replaces its existing ASB binary without advertising an invalid Make option. |
| Next action | Publish the privacy-safe acceptance receipt, reconcile stable exact-main observations, then release AR-1755 done. |

### AR-1756 — Coordinator v0.4.0 development vendor for supported acceptance

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt the exact upstream Coordinator main containing the supported spec-acceptance command as an explicitly development-only vendor so merged ASB ARs can be durably accepted. |
| Next action | Promote and claim; independently verify upstream main c2692d0 and the absence of a v0.4.0 tag, then sync it through sync-development in an isolated state worktree without patching vendored bytes. |

### AR-1757 — Human-first ASB command output

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make default ASB CLI output concise, command-aware, self-explanatory, and actionable while preserving stable machine-readable output. |
| Next action | Inventory every public ASB command outcome at exact current main, define the command-aware human presentation contract, and replace the generic JSON key/value renderer without changing explicit --json schemas. |

### AR-1758 — Repair AR-1731 protected-main merge provenance

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Restore a compliant protected-main publication after the AR-1731 local merge lacked a DCO trailer, without rewriting published history or weakening gates. |
| Next action | Protected main is repaired at exact signed+DCO merge 021ca1c39ff0199aa2c193026783712bc73bc51b; wait for remaining exact-main workflows, then record receipt and accept/release AR-1758 and AR-1731. |

### AR-1759 — ASB project and external-tool configuration schema

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define one versioned ASB project/tool inventory and catalog-selection configuration contract. |
| Next action | Wait for exact-main runs 37947479451, 37947479455, and 37947479450 to reach terminal success; then publish evidence and accept/release AR-1759. |

### AR-1760 — Initialize an ASB benchmark project workspace

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add an idempotent ASB project initializer containing config, results, and catalog areas. |
| Next action | Independent review has no blocking findings. Obtain separate GitHub approval, wait for all exact-head PR checks to finish, then merge via merge_pr.py. |

### AR-1761 — ASB external-tool installer and registry

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Install supported external ASB tools into a user/project-local root and persist validated records. |
| Next action | Monitor all post-merge workflows for exact main commit ae22d66b86060b8ee60b56ffd7ca0e31f7e50c54 (runs 37965524382, 37965524223, 37965524100, 37965524493, 37965524096, 37965524145, 37965523882, 37965523952). After terminal success, record post-merge receipt and accept/release AR-1761. |

### AR-1762 — Discover system and project ASB tools

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Auto-detect system-installed and project-configured ASB tools with deterministic diagnostics. |
| Next action | Monitor all exact-main CI for merge 3cab69a; after terminal green run post-merge verification, create receipt, then accept/release AR-1762. |

### AR-1763 — Generate and select ASB project catalogs

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Generate selectable agent/harness/benchmark/workload catalogs and persist their provenance. |
| Next action | PR #543 exact head 2e6a5d949e177599d6e78fec9488ad5e71cbe703 has independent technical review approval and terminal-green hosted checks. A distinct integration owner may now perform only the documented signed protected merge, then identify the immutable merge commit and record terminal exact-main assurance; do not treat this development approval as release evidence. |

### AR-1764 — Integrate project tools and catalogs with ASB runs

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make ASB benchmark commands consume initialized projects, discovered tools, and selected catalogs. |
| Next action | Wait for every post-merge workflow on exact main merge fd61b856570bf1d57e9dba4f8bee1da99b77189e to reach successful terminal status; then record receipt and accept/release. |

### AR-1765 — End-to-end qualification of ASB tool projects

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the complete fresh-user flow from project init through tool install/discovery/catalog selection and benchmark results. |
| Next action | Verify every exact-main workflow for signed merge a65ebb560cf26447858a1241ac80049c59a4bcbd reaches terminal success; then record the post-merge receipt, accept/release AR-1765, reconcile state, and run live doctor. |

### AR-1766 — Fine-grained human diagnostic contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define a fine-grained typed diagnostic catalog carrying the safe context needed for clear human errors, failures, warnings, and remediation. |
| Next action | Record post-merge receipt for merge 00840438 and all ten exact-main workflows, run doctor --live, accept spec, then release AR-1766 done. |

### AR-1767 — Safe automatic directory preparation with clear notice

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implementing safe directory preparation and notices for command-owned ASB outputs. |
| Next action | PR #539 now points to signed exact head f34830bb75ce919d43036b4f889afd4b9fa1375d; await rerun exact-head CI and review. AR-1770 is the durable successor for descriptor-safe race hardening and missing acceptance-matrix gates. |

### AR-1768 — Exhaustive actionable human diagnostics

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Give every human-visible ASB error, failure, partial result, and warning a precise cause, affected target, impact, and useful recovery. |
| Next action | All ten exact-main workflows for signed merge 5377317 are terminal-success. Receipt quality/AR-1768-postmerge-receipt.json is committed at db9b25237 with SHA-256 8323d99c0a426b67f6566c0696cfa12171f95fce4f33aec5024c4bbe56fe3c12. Accept that evidence and release AR-1768 done, then reconcile and run doctor --live. |

### AR-1769 — Human diagnostic completeness CI gate

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make CI reject uncataloged, overly generic, context-free, unactionable, or privacy-unsafe human diagnostics. |
| Next action | Obtain fresh independent exact-head review of 971a3a9afea18e6287541996699bab52e82ffafa; then wait for PR #542 exact-head CI before any merge. |

### AR-1770 — Descriptor-safe directory race hardening and acceptance matrix

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close remaining directory and atomic-publication replacement races and complete the AR-1767 acceptance matrix. |
| Next action | AR-1770 is done: merge dc67390494805693aef21d917319253b2e705da7 has all ten terminal-success post-merge workflows, tracked receipt quality/AR-1770-postmerge-receipt.json, and acceptance digest sha256:a1e98d92b0b6567f659590d21a105bbd0e79a4600bdade3af95cb9aa75245711. |

### AR-1771 — Human output, status, and quiet contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define one routed human-output vocabulary, levels, writers, and quiet contract without changing JSON or exit behavior. |
| Next action | Signed exact-base merge receipt accepted: protected main 3cd8ae24048d153a4928511b6b1e64a50213d5e0 has parents fd61b856570bf1d57e9dba4f8bee1da99b77189e and 4b86c4a7a0993de2a5f93a061505c1d819d4a2df, reviewed tree ef5ee164ac8753a30fd2b5b75c187a4e9ecb7620, verified signature and matching DCO. Await all exact-main hosted workflow results before release. |

### AR-1772 — Unified human step-progress reporter

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the sole status/progress reporter for delayed, terminal-safe, ETA-bearing human step output. |
| Next action | Implement the single human step reporter on the mandatory output router after its output, level, status, and quiet contracts are accepted. |

### AR-1773 — Universal command step instrumentation

| Field | Value |
| --- | --- |
| Status | open |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Route every eligible public ASB command step through the shared status/progress reporter with real work updates. |
| Next action | Repair the coordinator Bubblewrap runtime root to mount the approved pinned Cargo toolchain, compiler/linker support, complete workspace source, and required identity files through an authorized runner; then rerun exact-head focused and full tests through handoffctl. No product source repair is justified. |

### AR-1774 — Status and progress completeness CI

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make CI reject missing quiet support, status/progress bypasses, false estimates, and any human output in JSON mode. |
| Next action | Add required CI enforcement and controlled-defect tests for quiet, status, and progress completeness after universal instrumentation lands. |

### AR-1775 — Configurable output router and levels

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Independent PR #625 review complete; awaiting hosted required CI |
| Next action | Keep PR #625 pending; recheck exact-head hosted required checks and merge only after all are green |

### AR-1776 — Supported-tool acquisition catalog

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define pinned official acquisition and build recipes for every ASB-supported executable tool. |
| Next action | Define the authoritative supported executable-tool acquisition catalog, official primary sources, binary/source alternatives, verification identities, and build recipes. |

### AR-1777 — Verified prebuilt tool acquisition

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | PR #579 exact head d30079b7: credential-channel command construction is tested even when hosted bwrap is unavailable; source/archive validation remains hardened. |
| Next action | AR-1794 — protected-main merge-path repair must create the signed local forward merge after the web-merge provenance failure; then rerun exact-main workflows and close AR-1777 only after all post-merge gates pass. |

### AR-1778 — Pinned source builds and project dependencies

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Build supported tools from verified pinned source and materialize missing dependencies in a project-owned prefix. |
| Next action | Accept AR-1778 with exact-main postmerge evidence at d64ac90a; then release done after durable acceptance. |

### AR-1779 — Default usable tool-install command

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make default asb tool install produce and verify a usable project-local supported executable tool without manual source copying. |
| Next action | Current origin/main da0cbe0848a10e61a2cd0b9a3144217842a3369 is green across all 10 required workflows; AR-1825 is accepted on merged PR #622 with source-executable matrix and bounded adapter/rollback/smoke negative gates. Release AR-1779 from its owner with durable exact-main and post-merge evidence. Preserve AR-1826–1832. |

### AR-1780 — Installed tool and workload execution qualification

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | End-to-end qualify default-installed supported tools and workload bundles through actual ASB execution. |
| Next action | Qualify every development external workload, after installation and selection, through actual run, sweep, report, and comparison flows. |

### AR-1781 — External workload acquisition catalog

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | PR #578 merged at signed local merge 4a8f0925. |
| Next action | Wait for all exact-main workflows at 4a8f0925 to finish green, then post-merge verify and close AR-1781. |

### AR-1782 — Verified asb workload installation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement dedicated verified remote external workload installation and lifecycle through asb workload. |
| Next action | PR #584 rebased onto origin/main 24cb72d; exact remote head 96ea497a. Credential-free workload matrix, diagnostic contract, provenance, resolver, and clippy focused gates pass. Poll fresh exact-head CI; do not merge. |

### AR-1783 — Installed workload selection and execution

| Field | Value |
| --- | --- |
| Status | open |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implementation is integrated and workload matrix tests pass; qualification is blocked by current-main diagnostic catalog drift owned by AR-1863. |
| Next action | Await AR-1863 generated catalog repair, then rerun exact-head serialized coverage; do not duplicate workload/control tests or weaken the 90&#37; floor. |

### AR-1784 — Command dependency registry and preflight

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | PR #575 merged at signed local merge 14de8bce. |
| Next action | Wait for all exact-main workflows at 14de8bce to finish green, then perform post-merge verification and close AR-1784 with durable evidence. |

### AR-1785 — Repair OpenRouter configuration identity for live benchmark qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align persisted OpenRouter configuration, provider-plan selection identity, and benchmark-live selected/all execution. |
| Next action | Monitor exact-main post-merge workflows for daae06efa2d78b11acd6902c5ac6958091bfe546; after terminal success, run post-merge verification, accept, release, and requalify AR-1715. No GitHub Reviews API approval object required. |

### AR-1786 — Repair control state-root isolation race

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Eliminate control state-root ownership collisions in ordinary parallel workspace tests. |
| Next action | Continue monitoring PR #563 exact-head required CI at a5e58954; Rust verification, Repository quality, and Emulated aarch64 portability remain in progress, all completed checks are green. Merge only after terminal green. |

### AR-1787 — Repair control lock lifetime semantics

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Correct control lock descriptor lifetime and diagnostic identities after the AR-1786 review blocker. |
| Next action | Rebased candidate 573f3e631c9274829461fc051d461a383d994eb3 onto current protected main; PR #553 was closed for stale-base provenance. Release for fresh independent exact-head review before publishing a replacement PR. No GitHub Reviews API approval object is required. |

### AR-1788 — Make rustup path-replacement fixture deterministic

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair nondeterministic rustup path-replacement fixture failure exposed by AR-1787 review. |
| Next action | Wait for AR-1789 metrics fixture repair; then rerun focused tests and bounded repeated ordinary workspace gates on signed candidate eece088d66a30f310987e0ed238bc80227ff7d32. |

### AR-1789 — Make metrics malformed-configuration fixture deterministic

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair nondeterministic asb-metrics malformed-configuration fixture failure exposed by AR-1788 review. |
| Next action | Wait for AR-1790 retry-budget repair and independent review; then re-review combined candidate 2f1f08fb plus 97eb1e38 and publish exact-head CI only after all gates pass. |

### AR-1790 — Make metrics spawn retry budget effective

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the ineffective bounded metrics spawn retry guard found in AR-1789 review. |
| Next action | Repair the effective metrics WouldBlock retry guard and add retry-budget regression coverage in the bound worktree. |

### AR-1791 — Repair recurrent TUI fixture isolation failures

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the GCC descendant-marker and rustup descriptor-cleanup TUI fixtures deterministic under repeated ordinary workspace execution. |
| Next action | Inspect privacy/diff, then run another ordinary full workspace gate; release only if it passes and static/provenance gates remain green. |

### AR-1792 — Make development broker PTY fixture deterministic

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the intermittent development broker foreground/restore PTY fixture exposed by PR #555 coverage. |
| Next action | Release AR-1792 as done ownerless after independent review; no source changes. |

### AR-1793 — Repair human diagnostic output-parent contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the legacy human diagnostic output-parent wording contract exposed by the full ASB CLI suite. |
| Next action | Repair the legacy human diagnostic output-parent wording contract and add focused positive/negative coverage; do not publish AR-1784 until green. |

### AR-1794 — Protected-main merge-path repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the protected-main publication path after a GitHub web merge produced a rejected committer identity. |
| Next action | Keep open pending a clean signed local merge and green exact-main provenance receipt; do not use GitHub web merge. |

### AR-1795 — Coordinator v0.5.1 adoption

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt v0.5.1 with strict coverage repair. |
| Next action | Retry canonical publication-tier formal verification after the occupied shared admission lane clears; then independently review the exact state and release only with all required evidence. |

### AR-1796 — Concurrent integration liveness

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Keep autonomous development live during concurrent protected-main integration. |
| Next action | Reconcile the stale AR-1796 merge identity against current protected main, then obtain a fresh exact-head full-exhaustive formal attestation before any v0.5.2 release attempt. |

### AR-1797 — Wire cli2key sidecar into live benchmark execution

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair cli2key so an installed pinned bridge receives a runtime-issued sidecar launch and can execute a development ASB benchmark. |
| Next action | Wire the verified project-local cli2key bridge into the runtime-owned sidecar launch path, then qualify fake and opt-in live benchmark execution without exposing credentials. |

### AR-1798 — Pinned source-checkout acquisition

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Coverage margin repair pushed at c5303c05. |
| Next action | Monitor PR #585 exact-head CI at 55a78934; request independent re-review after hosted coverage passes. |

### AR-1799 — Repair asb tui install rustup/rustc trusted-tool rejection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the remaining current-main asb tui install trusted_tool_invalid failure for development rustup/rustc layouts and qualify the real installed entrypoint. |
| Next action | PR #613 (63ba8e7973545f65bd8dda56f3aa24d9d339bb16) is open; focused rustup tests, fmt, clippy, and independent review pass. Await remaining exact-head hosted checks, then merge and run post-merge installed-entrypoint qualification. |

### AR-1800 — Development channel warning-only trust contracts

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make development-channel trust, digest, and exact-version mismatches warning-only without weakening stable/production policy. |
| Next action | Release done after exact-main 74b391348fc5c1361034a14742f6afef747d72db verification: PR #615 merged, 13/13 exact-main checks green, focused trust tests and full locked workspace tests passed; perform final state reconciliation. |

### AR-1819 — Fail-closed expired-claim recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make expired-claim recovery fail closed when the exact current session snapshot is unavailable. |
| Next action | Implement fail-closed expired-claim recovery, add focused positive and negative coverage, then independently review and integrate the exact signed head. |

### AR-1820 — AR-1772 protected-main provenance and DCO requalification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Requalify AR-1772 protected-main provenance and DCO without rewriting PR #602 or weakening gates. |
| Next action | Await independent review of PR #614 exact head 7ebfd47a5ab6279779aa899ef83b27c6c4d86edd and the three remaining hosted checks; merge only through tools/integration/merge_pr.py after all green. |

### AR-1821 — AR-1817 PR #128 integration recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover the durable task record needed to integrate accepted AR-1817 PR #128 after its original task was removed from current generated state. |
| Next action | Claim this recovery task, verify accepted PR #128 exact head against current main, integrate through the signed local merge path, run exact-main post-merge checks, and close with durable evidence. |

### AR-1822 — Expired role assignment cleanup semantics

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Allow exact-revision roles.remove cleanup of explicitly named expired assignments while preserving fail-closed reads and admission. |
| Next action | Merged exact reviewed PR #140 at 4cea485091; stale assignment ar1774-pr612-review-ad7f1166 removed at role revision 22 to 23; verify roles list, doctor, and post-merge checks before acceptance and release. |

### AR-1823 — AR-1820 receipt publication cleanup

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Publish the already-verified AR-1820 provenance receipt and durable done state. |
| Next action | Publish the already-verified AR-1820 receipt and done transition from the durable current-main state; do not change product or historical PR evidence. |

### AR-1824 — cli2key public provider composition

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add public cli2key provider-plan/catalog construction and direct runtime-authority composition. |
| Next action | Implement the cli2key provider-plan/catalog and direct runtime-authority composition seam without reopening AR-1797. |

### AR-1825 — Bounded source-to-executable adapter/runtime contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement bounded source adapter contract |
| Next action | Post-merge exact-main workspace rerun completed with all tests passing, including source_checkout::tests::exact_fixture_checkout_is_returned_and_cleanup_is_explicit (443 asb-cli unit tests passed; workspace integration/doc tests passed). Initial 442/1 Unavailable was not reproducible and appears a one-time environmental/concurrency failure. Before acceptance, reconcile exact-main evidence and confirm required AArch64/Rust/repository-quality workflows terminal green; preserve AR-1779 expiry warning. |

### AR-1826 — Define explicit setup configuration and plan-binding contract

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define the explicit setup-file and config-bound plan contract that replaces implicit user configuration and provider-selection artifacts. |
| Next action | Supported repair unavailable in vendored handoffctl v0.7.5: bind-worktree rejects retained legacy worktree_key agent-systems-benchmark-ar-1826-explicit-setup-config-contract while branch is empty, and no coordinator command clears the pair. Add/use an explicitly reviewed coordinator repair version, then re-claim, bind codex/ar-1826-explicit-setup-contract to the exact non-overlapping worktree, and requalify reviewed e9d95999 onto current main d0e6a28. |

### AR-1827 — Author complete explicit benchmark configuration with asb setup

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make asb setup --output the complete authoring route for agents, live providers/models, workloads, monitors, measures, and bounded execution choices. |
| Next action | Implement the complete interactive and noninteractive setup authoring route against the explicit configuration contract. |

### AR-1828 — Retire legacy provider selection and implicit configuration surfaces

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Retire public config/catalog/provider-plan commands and all ProviderSelection artifacts in favor of setup-created explicit config. |
| Next action | Remove legacy public config, provider-catalog, provider-plan, and ProviderSelection surfaces after setup contains their user-facing selection responsibilities. |

### AR-1829 — Compile config-bound benchmark plans with explicit output

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make asb plan create compile a complete setup file into an explicit-output immutable benchmark plan with no provider-selection inputs. |
| Next action | Implement config-only benchmark plan compilation with mandatory --config and --output arguments. |

### AR-1830 — Execute config-bound live runs and sweeps

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make plan validation, run, and sweep require the setup config and safely execute complete live benchmark selections from config-bound plans. |
| Next action | Require explicit config validation for plan validation, live run, and live sweep, then wire bounded multi-agent execution. |

### AR-1831 — Align CLI, TUI handoff, and documentation to explicit config workflow

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make every CLI, TUI handoff, help page, completion, and example teach the explicit setup-output and plan-config workflow. |
| Next action | Align CLI help, human output, completions, TUI handoff, examples, and migration documentation to the explicit setup-config route. |

### AR-1832 — Qualify explicit setup-config benchmark workflow end-to-end

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify fresh-user setup-output through explicit config-bound plan creation, validation, live run, sweep, reporting, and legacy-surface absence. |
| Next action | Qualify the full fresh-user explicit-config route across supported selection matrices and live development execution. |

### AR-1833 — Repair AR-1689 receipt bytes

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Independent review passed: receipt newline repair preserves qualification content |
| Next action | Reconcile generated projections and release AR-1833 done after final state verification |

### AR-1834 — AR-1775 protected-main local identity recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover AR-1775 protected-main provenance with the established local signed integration identity without rewriting historical merge 356a669e |
| Next action | Monitor exact-main workflows for repaired merge da0cbe0848a10e61a2cd0b9a3144217842a3369b to terminal success; record post-merge receipt and release AR-1834 without touching unrelated ARs |

### AR-1835 — Authenticated control and live-isolation coverage repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the missing authenticated ControlClient/server and delegated live-isolation coverage seam without weakening AR-1783 gates. |
| Next action | Reconcile AR-1835 acceptance against signed protected-main merge 4a486e97 and receipt quality/AR-1837-postmerge-receipt.json; preserve AR-1783 in progress. |

### AR-1836 — Cross-repository Exact TUI qualification determinism

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the deterministic cross-repository Exact TUI inherited-fd/PTY qualification seam exposed by AR-1835 without weakening its assertions. |
| Next action | Promote after AR-1835 dependency resolution; reproduce the two hosted failures with complete workflow metadata, identify the owning workflow/asb-tui seam, and implement only a deterministic qualification repair without weakening the gate. |

### AR-1837 — PR #627 protected-main identity recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover current protected-main provenance after PR #627 was web-merged with a noreply committer, without rewriting history or weakening gates. |
| Next action | Await completion of exact-main rerun attempt 2 for Credential-free benchmark path plus remaining Rust, Repository quality, and Emulated AArch64 workflows; release only after all terminal-success and reconcile AR-1835 evidence. |

### AR-1838 — Repair reproducible source checkout fixture failure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the reproducible source_checkout exact-fixture test failure blocking protected-main post-merge quality. |
| Next action | Post-merge exact-main verification complete: merge d0e6a28a81b40a990e6b83b48a885e9ada96f0fd is remote main, signed+DCO verified, and all required post-merge check-runs terminal success; release AR-1838 done. |

### AR-1839 — Repair cross-process source fixture isolation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make source checkout test fixtures safe when independent cargo processes run concurrently. |
| Next action | Reproduce source_checkout fixture collisions across concurrent cargo processes, add process-safe isolation, then run focused/full gates and publish a reviewed repair. |

### AR-1840 — Persist AR-1839 review evidence

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Persist AR-1839 review evidence without bypassing handoffctl ownership rules. |
| Next action | Reconcile generated views and release AR-1840 with exact artifact digest and bounded doctor/auth evidence. |

### AR-1841 — Coordinator v0.5.3 adoption

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt Coordinator v0.7.4 with partial legacy worktree binding. |
| Next action | Wait for scoped v0.7.4 compatibility repairs AR-1851 (AR-1793), AR-1852 (roles), AR-1853 (complexity), and AR-1849 (formal admission/workspace) to merge; then rebase PR #142 onto protected main, rerun candidate-focused/full gates, obtain fresh exact-head independent review and CI. |

### AR-1842 — Name-first selection and internal identity resolution

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make logical names the only user-facing selection keys while ASB and asb-tui resolve and verify paths, hashes, versions, providers, and models internally. |
| Next action | Promote after AR-1832 is complete; inventory every user-facing selection and freeze the shared name-to-identity resolver contract before implementation. |

### AR-1843 — Hosted formal workspace permission repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair hosted formal TLC workspace permissions for the ASB state runner. |
| Next action | Verify PR #143 remains exact head 7bb995e65d, merge through handoffctl, then watch exact-main post-merge assurance workflows to terminal success. |

### AR-1844 — Extract the ASB data-model registry

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Generate a complete secret-free registry of ASB configuration options and individual settings from the authoritative data model. |
| Next action | Promote after AR-1842; inventory the authoritative ASB data model and define the generated field registry contract. |

### AR-1845 — Extract configuration entities and storage relations

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Extract where ASB settings are stored and transported across the complete configuration-to-results lifecycle. |
| Next action | Promote after AR-1844; enumerate storage entities and lifecycle relations from setup through benchmark results. |

### AR-1846 — Extract ASB command and option dataflows

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Extract all ASB commands and options and their relations to configuration entities across the complete workflow. |
| Next action | Promote after AR-1845; extract the authoritative &#96;asb&#96; command tree and connect every option to lifecycle entities. |

### AR-1847 — Export ASB configuration dataflows to Graphviz and SVG

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Write the ASB configuration/dataflow graph as Graphviz DOT and a developer-screen-readable SVG. |
| Next action | Promote after AR-1846; implement the extraction command and deterministic DOT/SVG graph artifacts with privacy checks. |

### AR-1848 — Qualify ASB dataflow graph extraction end to end

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify reproducible complete ASB dataflow extraction, DOT/SVG generation, privacy, and paired documentation. |
| Next action | Promote after AR-1847; run clean-checkout extraction and cross-check graph artifacts against all generated registries and CLI options. |

### AR-1849 — Formal admission environment repair

| Field | Value |
| --- | --- |
| Status | open |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair workflow-wide private TLC admission environment for formal CI. |
| Next action | Focused suites and TLC portable-smoke pass; full unittest 1,636/1,636 passes and formal portable-smoke passes with required admission/resource env, but terminal coverage is 94&#37; versus required 95&#37;. Preserve PR #145 unmerged; route the concrete coverage deficit to a scoped follow-up before independent review/CI publication. |

### AR-1850 — Repair development ASB TUI interactive lifetime

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Stop the development ASB launcher from killing a successfully admitted interactive TUI after its fixed 15-second lifetime deadline. |
| Next action | Do not release AR-1850. Reconcile the protected signed merge-path provenance failure with Coordinator; retain merge commit and evidence, then run authorized repair/requalification before post-merge PTY verification. |

### AR-1851 — AR-1793 v0.7.4 compatibility contracts

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align AR-1793 compatibility fixtures with Coordinator v0.7.4. |
| Next action | Obtain fresh independent review and terminal strict/formal CI at exact head 0d3693a24c; merge only when all required checks are green, then perform post-merge verification. |

### AR-1852 — Role-store v0.7.4 compatibility contracts

| Field | Value |
| --- | --- |
| Status | open |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align role-store authorization tests with Coordinator v0.7.4. |
| Next action | Blocked: direct exact-head role gate passes 10/10 using locked external v078 DCO venv; approved handoffctl sandbox cannot access /bin/true or external venv (bwrap execvp ENOENT), and direct full 2132-test gate has 8 baseline failures and 6 environment errors unrelated to role tests. Preserve PR148 7b46c6b076 and release owner. |

### AR-1853 — Complexity v0.7.4 compatibility contract

| Field | Value |
| --- | --- |
| Status | open |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align the complexity-budget contract with Coordinator v0.7.4. |
| Next action | Wait for AR-1851 and AR-1852 merged repairs, then rerun exact-head CI for approved PR #146 at 56371a22ad; preserve cross-repair failures as non-waived evidence. |

### AR-1854 — v0.7.4 compatibility integration qualification

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate and qualify the Coordinator v0.7.4 compatibility repairs. |
| Next action | Promote only after AR-1851, AR-1852 and AR-1853 merge; combine their exact reviewed heads and run the strict/formal integration gates. |

### AR-1855 — Repair AR-1850 coordination metadata schema

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the malformed observed_dirty coordination field on AR-1850 without changing its product scope. |
| Next action | Merge PR #149 at exact reviewed head 7fc186e48b after green required checks, then verify exact-main schema, focused tests, and live doctor. |

### AR-1856 — PR #631 protected-main identity recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover protected-main provenance after PR #631 was GitHub-web-merged with a non-local committer. |
| Next action | Keep AR-1856 claimed until every exact-main workflow for merge 870331be533ea1a0ba9645ddbb690df56af84935 is terminal-success; then record the post-merge receipt, accept the spec, release done, reconcile, and doctor --live. |

### AR-1857 — Full-gate coverage floor repair

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Restore the full-gate coverage floor after the terminal 94&#37; observation. |
| Next action | Analyze exact 94&#37; coverage artifact and add narrow tests for uncovered first-party paths; preserve 95&#37; threshold and PR #145 unmerged. |

### AR-1858 — v0.7.0 coverage floor repair

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the v0.7.0 coordinator coverage floor deficit. |
| Next action | AR-1859 is created and committed as the scoped successor for verify.sh TLC_WORK_ROOT validation, depends_on AR-1858, and is intentionally not promoted because handoffctl correctly rejects unfinished dependencies. Preserve AR-1858 evidence and PR145 unmerged until formal failures are repaired or explicitly scoped. |

### AR-1859 — v0.7.0 formal work-root validation

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reject non-absolute TLC work roots before formal execution. |
| Next action | Promote after validating the AR-1858 terminal evidence and bind the exact v0.7.0 formal worktree. |

### AR-1860 — Dependency-safe formal work-root repair adoption

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt and qualify the dependency-safe v0.7.0 formal work-root repair. |
| Next action | Merge PR #151 signed state-only coordination repair, run exact-main doctor/schema/post-merge assurance, then release AR-1860 with merged evidence. |

### AR-1861 — Adopt Coordinator AR-0034 legacy-binding repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt the merged Coordinator AR-0034 partial-legacy worktree repair needed to unblock ASB AR-1826. |
| Next action | Bind and accept the exact v0.7.8 vendor, quality, and advisory-role evidence, then release the verified adoption. |

### AR-1862 — Coordinator formal lifecycle inventory alignment

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align ASB formal lifecycle runtime/model inventories for Coordinator AR-0034 adoption. |
| Next action | Bind and accept exact v0.7.8 lifecycle-alignment evidence, then release this obsolete downstream repair successor. |

### AR-1863 — Repair control diagnostic catalog

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the eight current-main control.rs producer call sites missing from diagnostic_legacy_catalog_compact.rs after AR-1835 integration, without changing AR-1787 or diagnostic gates. |
| Next action | Implement the bounded control diagnostic catalog repair and record local acceptance evidence after the coordinator binds the reviewed source-write successor envelope; do not change AR-1787 or AR-1835. |

### AR-1864 — Align task-record schema vocabulary

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align task-record schema vocabulary for execution, retry, and standard task metadata without changing lifecycle semantics. |
| Next action | Align task-record schema execution/retry and standard metadata vocabulary; add positive and hostile fixtures and regenerate documentation. |

### AR-1865 — Repair expired role cleanup

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Restore the AR-1822 exact-revision roles.remove cleanup semantics lost when ASB adopted Coordinator v0.7.8, preserving fail-closed reads, admission, malformed-state checks, and unrelated coordinator behavior. |
| Next action | Obtain independent GitHub approval for PR #160 at exact head b0811a8802; merge via authorized signed path, then run post-merge verification and repaired roles.remove cleanup. Current gh pr review --approve is rejected because the available identity owns the PR. |

### AR-1866 — Correct vendor version docs

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Correct ASB public vendor documentation that still names Coordinator v0.3.5 after the checked-in coordinator.vendor.json adopted v0.7.8, without changing runtime or coordinator behavior. |
| Next action | Release AR-1866 after exact-main verification. |

### AR-1867 — Legacy reservation recovery

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a fail-closed ASB downstream handoffctl overlay path to recover expired bound execution reservations from pre-identity claims without direct state edits or weakened reservation structural checks. |
| Next action | PR #161 published at exact source head 7281ca87f5 plus signed overlay commit 5f7f247a39; obtain independent exact-head review and required CI before merge. Full unittest remains environment-blocked by bounded filesystem/jbd2 hang. |

### AR-1868 — Synchronize task schema vocabulary

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Update only schema/task-schema.json and generated validation fixtures so accepted modern task-record metadata is validated by ASB while unknown fields remain rejected; preserve ASB-specific lifecycle constraints. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1869 — Repair evidence ledger digests

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Refresh only the stale evidence-ledger candidate digests in AR-1861 and AR-1862 to the exact current coordinator.vendor.json bytes; preserve all predicates, evidence, and fail-closed validation. |
| Next action | Repair PR #164 scope at a fresh exact head: retain only the two AR-1861/AR-1862 evidence-ledger digest updates, restore/rebase away schema/task-record, checkpoint/session, and test changes; rerun focused/full gates and request fresh independent review. |

### AR-1870 — Repair ledger digests only

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Refresh only the stale evidence_ledger candidate and mechanical evidence digests in AR-1861 and AR-1862 to the exact current coordinator.vendor.json bytes, leaving schema, tests, checkpoints, sessions, predicates, and all other task fields unchanged. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1871 — Integrate schema ledger fix

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate independently reviewed AR-1868 schema vocabulary repair and AR-1870 ledger digest repair on current main, changing only schema/task-schema.json, tests/test_task_record_schema.py, and AR-1861/AR-1862 evidence_ledger blocks. This successor explicitly depends on AR-1868 and AR-1870 review evidence; do not include checkpoints, sessions, projections, runtime state, or unrelated files. |
| Next action | Publish exact-head signed integration PR; obtain independent review; run green CI; merge via handoffctl; post-merge verify schema and both evidence ledgers. |

### AR-1872 — Recover orphan reservations

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a narrowly scoped handoffctl recovery path for expired bound execution reservations whose original claim lacks worker PID/start-time identity, reusing only the AR-1867 legacy-recovery contract where explicit operator evidence, exact reservation/result matching, expiry, structural validation, and fail-closed identity checks remain mandatory. Do not edit AR-1871 state directly or force-clear reservations. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1873 — Abandon expired executions

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a fail-closed abandon-expired-execution transition clearing only expired bound reservations with no live identity; classify missing/mismatched results as failed, require exact owner/revision matches, non-empty operator evidence, and immutable audit. Reject live/non-expired, malformed, matching-success, wrong-owner/revision, and missing-evidence cases. No recovery/success authorization or direct edits to AR-1773/1852/1871. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1874 — Upgrade Coordinator v0.7.11

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt the exact signed upstream Agent Workflow Coordinator v0.7.11 release in the ASB state repository using the documented vendor sync path. Preserve ASB-owned overlays, task state, formal inventories, generated views, and fail-closed lifecycle behavior; do not patch vendored bytes or weaken existing gates. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1875 — Repair AR-1863 source-write envelope

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Create and bind a successor AR-1863 execution envelope that authorizes only the reviewed diagnostic-catalog source-write and publication paths, preserving the existing AR-1863 non-goals, path scope, fail-closed gates, and exact current-main review evidence. Do not modify AR-1787 or AR-1835. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1876 — Replace stale AR-1863 envelope

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide an explicit fail-closed coordinator transition for replacing AR-1863&#x27;s already-bound obsolete execution envelope with the reviewed successor AR-1863-e3, requiring exact task revision, active owner, no live execution reservation, immutable replacement evidence, and preserving all existing path and non-goal restrictions. |
| Next action | Implement the bounded scope and record local acceptance evidence. |

### AR-1877 — Adopt envelope replacement

| Field | Value |
| --- | --- |
| Status | in_progress |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | asb-ar1877-coordinator-adoption-20261014 |
| Parent | None |
| Children | None |
| Summary | Adopt the merged upstream Agent Workflow Coordinator successor-envelope replacement capability at commit c604e1dd82401a3000d9ec083e7b4fba22f6d513 using the documented vendor sync path. Update only coordinator vendor files and generated integrity evidence, preserve ASB overlays and task history, then validate AR-1863 envelope replacement without direct edits or gate weakening. |
| Next action | Implement the bounded scope and record local acceptance evidence. |


## Dependency graph

Arrows point from each prerequisite to the work that depends on it. Color is redundant
with the status text inside every node; the tables below are the complete text
alternative.

```mermaid
flowchart LR
    subgraph series_00["00 - Coordination foundation"]
        direction TB
        AR_0001["AR-0001 - Done"]:::status_done
        AR_0002["AR-0002 - Done"]:::status_done
        AR_0003["AR-0003 - Done"]:::status_done
        AR_0004["AR-0004 - Done"]:::status_done
        AR_0005["AR-0005 - Done"]:::status_done
    end
    subgraph series_01["01 - Contracts and runtime"]
        direction TB
        AR_0101["AR-0101 - Done"]:::status_done
        AR_0102["AR-0102 - Done"]:::status_done
        AR_0103["AR-0103 - Done"]:::status_done
        AR_0104["AR-0104 - Done"]:::status_done
        AR_0105["AR-0105 - Done"]:::status_done
    end
    subgraph series_02["02 - Analysis"]
        direction TB
        AR_0201["AR-0201 - Done"]:::status_done
        AR_0202["AR-0202 - Done"]:::status_done
        AR_0203["AR-0203 - Done"]:::status_done
        AR_0204["AR-0204 - Done"]:::status_done
    end
    subgraph series_03["03 - Adapters and workloads"]
        direction TB
        AR_0301["AR-0301 - Done"]:::status_done
        AR_0302["AR-0302 - Done"]:::status_done
        AR_0303["AR-0303 - Done"]:::status_done
        AR_0304["AR-0304 - Done"]:::status_done
        AR_0305["AR-0305 - Done"]:::status_done
        AR_0306["AR-0306 - Done"]:::status_done
        AR_0307["AR-0307 - Done"]:::status_done
        AR_0308["AR-0308 - Done"]:::status_done
        AR_0309["AR-0309 - Done"]:::status_done
        AR_0310["AR-0310 - Done"]:::status_done
        AR_0311["AR-0311 - Done"]:::status_done
        AR_0312["AR-0312 - Done"]:::status_done
        AR_0313["AR-0313 - Done"]:::status_done
        AR_0314["AR-0314 - Done"]:::status_done
        AR_0315["AR-0315 - Done"]:::status_done
        AR_0316["AR-0316 - Done"]:::status_done
        AR_0317["AR-0317 - Done"]:::status_done
        AR_0318["AR-0318 - Done"]:::status_done
        AR_0319["AR-0319 - Done"]:::status_done
        AR_0320["AR-0320 - Done"]:::status_done
    end
    subgraph series_04["04 - Live measurement"]
        direction TB
        AR_0401["AR-0401 - Done"]:::status_done
        AR_0402["AR-0402 - Done"]:::status_done
        AR_0403["AR-0403 - Done"]:::status_done
        AR_0404["AR-0404 - Done"]:::status_done
        AR_0405["AR-0405 - Done"]:::status_done
        AR_0406["AR-0406 - Done"]:::status_done
    end
    subgraph series_05["05 - Replay"]
        direction TB
        AR_0501["AR-0501 - Done"]:::status_done
        AR_0502["AR-0502 - Done"]:::status_done
        AR_0503["AR-0503 - Done"]:::status_done
        AR_0504["AR-0504 - Done"]:::status_done
        AR_0505["AR-0505 - Done"]:::status_done
        AR_0506["AR-0506 - Done"]:::status_done
        AR_0507["AR-0507 - Done"]:::status_done
        AR_0508["AR-0508 - Done"]:::status_done
        AR_0509["AR-0509 - Done"]:::status_done
        AR_0510["AR-0510 - Done"]:::status_done
        AR_0511["AR-0511 - Done"]:::status_done
        AR_0512["AR-0512 - Done"]:::status_done
        AR_0513["AR-0513 - Done"]:::status_done
        AR_0514["AR-0514 - Blocked"]:::status_blocked
        AR_0515["AR-0515 - Planned"]:::status_planned
        AR_0516["AR-0516 - Done"]:::status_done
        AR_0517["AR-0517 - Done"]:::status_done
        AR_0518["AR-0518 - Done"]:::status_done
        AR_0519["AR-0519 - Done"]:::status_done
        AR_0520["AR-0520 - Done"]:::status_done
        AR_0521["AR-0521 - Blocked"]:::status_blocked
    end
    subgraph series_06["06 - Metrics"]
        direction TB
        AR_0601["AR-0601 - Done"]:::status_done
        AR_0602["AR-0602 - Planned"]:::status_planned
        AR_0603["AR-0603 - Done"]:::status_done
        AR_0604["AR-0604 - Blocked"]:::status_blocked
    end
    subgraph series_07["07 - Platforms"]
        direction TB
        AR_0701["AR-0701 - Done"]:::status_done
        AR_0702["AR-0702 - Done"]:::status_done
        AR_0703["AR-0703 - Future"]:::status_future
        AR_0704["AR-0704 - Done"]:::status_done
        AR_0705["AR-0705 - Blocked"]:::status_blocked
        AR_0706["AR-0706 - Blocked"]:::status_blocked
        AR_0707["AR-0707 - Done"]:::status_done
    end
    subgraph series_08["08 - Interfaces"]
        direction TB
        AR_0801["AR-0801 - Done"]:::status_done
        AR_0802["AR-0802 - Done"]:::status_done
        AR_0803["AR-0803 - Done"]:::status_done
        AR_0804["AR-0804 - Done"]:::status_done
        AR_0805["AR-0805 - Done"]:::status_done
        AR_0806["AR-0806 - Done"]:::status_done
        AR_0807["AR-0807 - Planned"]:::status_planned
        AR_0808["AR-0808 - Planned"]:::status_planned
        AR_0809["AR-0809 - Planned"]:::status_planned
        AR_0810["AR-0810 - Planned"]:::status_planned
        AR_0811["AR-0811 - Planned"]:::status_planned
        AR_0812["AR-0812 - Done"]:::status_done
        AR_0813["AR-0813 - Done"]:::status_done
        AR_0814["AR-0814 - Blocked"]:::status_blocked
        AR_0815["AR-0815 - Planned"]:::status_planned
        AR_0816["AR-0816 - Planned"]:::status_planned
        AR_0817["AR-0817 - Planned"]:::status_planned
        AR_0818["AR-0818 - Planned"]:::status_planned
        AR_0819["AR-0819 - Done"]:::status_done
        AR_0820["AR-0820 - Done"]:::status_done
        AR_0821["AR-0821 - Done"]:::status_done
        AR_0822["AR-0822 - Done"]:::status_done
        AR_0823["AR-0823 - Planned"]:::status_planned
        AR_0830["AR-0830 - Done"]:::status_done
        AR_0831["AR-0831 - Done"]:::status_done
        AR_0832["AR-0832 - Blocked"]:::status_blocked
        AR_0833["AR-0833 - Planned"]:::status_planned
        AR_0834["AR-0834 - Done"]:::status_done
        AR_0835["AR-0835 - Done"]:::status_done
        AR_0836["AR-0836 - Blocked"]:::status_blocked
        AR_0837["AR-0837 - Planned"]:::status_planned
        AR_0840["AR-0840 - Done"]:::status_done
        AR_0841["AR-0841 - Done"]:::status_done
        AR_0842["AR-0842 - Done"]:::status_done
        AR_0843["AR-0843 - Done"]:::status_done
        AR_0844["AR-0844 - Done"]:::status_done
        AR_0845["AR-0845 - Done"]:::status_done
        AR_0846["AR-0846 - Planned"]:::status_planned
        AR_0847["AR-0847 - Done"]:::status_done
        AR_0848["AR-0848 - Done"]:::status_done
        AR_0849["AR-0849 - Done"]:::status_done
        AR_0850["AR-0850 - Done"]:::status_done
        AR_0851["AR-0851 - Done"]:::status_done
        AR_0852["AR-0852 - Done"]:::status_done
        AR_0853["AR-0853 - Done"]:::status_done
        AR_0854["AR-0854 - Done"]:::status_done
        AR_0855["AR-0855 - Done"]:::status_done
        AR_0856["AR-0856 - Planned"]:::status_planned
        AR_0857["AR-0857 - Done"]:::status_done
        AR_0858["AR-0858 - Done"]:::status_done
        AR_0859["AR-0859 - Done"]:::status_done
        AR_0860["AR-0860 - Done"]:::status_done
        AR_0861["AR-0861 - Blocked"]:::status_blocked
        AR_0862["AR-0862 - Planned"]:::status_planned
        AR_0863["AR-0863 - Blocked"]:::status_blocked
        AR_0864["AR-0864 - Planned"]:::status_planned
        AR_0865["AR-0865 - Planned"]:::status_planned
        AR_0866["AR-0866 - Planned"]:::status_planned
        AR_0867["AR-0867 - Planned"]:::status_planned
        AR_0868["AR-0868 - Planned"]:::status_planned
        AR_0869["AR-0869 - Done"]:::status_done
        AR_0870["AR-0870 - Done"]:::status_done
        AR_0871["AR-0871 - Done"]:::status_done
        AR_0872["AR-0872 - Done"]:::status_done
        AR_0873["AR-0873 - Planned"]:::status_planned
        AR_0874["AR-0874 - Planned"]:::status_planned
        AR_0875["AR-0875 - Done"]:::status_done
        AR_0876["AR-0876 - Done"]:::status_done
        AR_0877["AR-0877 - Done"]:::status_done
        AR_0878["AR-0878 - Done"]:::status_done
        AR_0879["AR-0879 - Done"]:::status_done
        AR_0880["AR-0880 - Done"]:::status_done
        AR_0888["AR-0888 - Done"]:::status_done
        AR_0889["AR-0889 - Done"]:::status_done
        AR_0890["AR-0890 - Blocked"]:::status_blocked
        AR_0891["AR-0891 - Done"]:::status_done
        AR_0892["AR-0892 - Planned"]:::status_planned
        AR_0893["AR-0893 - Planned"]:::status_planned
        AR_0894["AR-0894 - Planned"]:::status_planned
        AR_0895["AR-0895 - Done"]:::status_done
        AR_0896["AR-0896 - Blocked"]:::status_blocked
        AR_0897["AR-0897 - Done"]:::status_done
        AR_0898["AR-0898 - Done"]:::status_done
        AR_0899["AR-0899 - Done"]:::status_done
    end
    subgraph series_09["09 - Assurance"]
        direction TB
        AR_0901["AR-0901 - Done"]:::status_done
        AR_0902["AR-0902 - Done"]:::status_done
        AR_0903["AR-0903 - Planned"]:::status_planned
        AR_0904["AR-0904 - Done"]:::status_done
        AR_0905["AR-0905 - Done"]:::status_done
        AR_0906["AR-0906 - Done"]:::status_done
        AR_0907["AR-0907 - Done"]:::status_done
        AR_0908["AR-0908 - Done"]:::status_done
        AR_0909["AR-0909 - Done"]:::status_done
    end
    subgraph series_10["10 - Reliability and release"]
        direction TB
        AR_1001["AR-1001 - Done"]:::status_done
        AR_1002["AR-1002 - Done"]:::status_done
        AR_1003["AR-1003 - Done"]:::status_done
        AR_1004["AR-1004 - Done"]:::status_done
        AR_1005["AR-1005 - Done"]:::status_done
        AR_1006["AR-1006 - Done"]:::status_done
        AR_1007["AR-1007 - Done"]:::status_done
        AR_1008["AR-1008 - Done"]:::status_done
        AR_1010["AR-1010 - Done"]:::status_done
        AR_1011["AR-1011 - Planned"]:::status_planned
        AR_1012["AR-1012 - Planned"]:::status_planned
        AR_1013["AR-1013 - Done"]:::status_done
        AR_1014["AR-1014 - Planned"]:::status_planned
        AR_1015["AR-1015 - Planned"]:::status_planned
        AR_1016["AR-1016 - Planned"]:::status_planned
        AR_1017["AR-1017 - Done"]:::status_done
        AR_1018["AR-1018 - Done"]:::status_done
        AR_1019["AR-1019 - Done"]:::status_done
        AR_1020["AR-1020 - Done"]:::status_done
        AR_1021["AR-1021 - Done"]:::status_done
        AR_1022["AR-1022 - Done"]:::status_done
        AR_1023["AR-1023 - Done"]:::status_done
        AR_1024["AR-1024 - Blocked"]:::status_blocked
        AR_1025["AR-1025 - Blocked"]:::status_blocked
        AR_1026["AR-1026 - Planned"]:::status_planned
        AR_1027["AR-1027 - Planned"]:::status_planned
        AR_1028["AR-1028 - Done"]:::status_done
        AR_1029["AR-1029 - Planned"]:::status_planned
        AR_1030["AR-1030 - Done"]:::status_done
        AR_1031["AR-1031 - Planned"]:::status_planned
        AR_1032["AR-1032 - Planned"]:::status_planned
        AR_1033["AR-1033 - Planned"]:::status_planned
        AR_1034["AR-1034 - Planned"]:::status_planned
        AR_1035["AR-1035 - Planned"]:::status_planned
        AR_1036["AR-1036 - Done"]:::status_done
        AR_1037["AR-1037 - Done"]:::status_done
        AR_1038["AR-1038 - Done"]:::status_done
        AR_1039["AR-1039 - Done"]:::status_done
        AR_1040["AR-1040 - Done"]:::status_done
        AR_1041["AR-1041 - Done"]:::status_done
        AR_1042["AR-1042 - Done"]:::status_done
        AR_1043["AR-1043 - Done"]:::status_done
        AR_1044["AR-1044 - Done"]:::status_done
        AR_1045["AR-1045 - Done"]:::status_done
        AR_1046["AR-1046 - Superseded"]:::status_superseded
        AR_1047["AR-1047 - Done"]:::status_done
        AR_1048["AR-1048 - Superseded"]:::status_superseded
        AR_1049["AR-1049 - Superseded"]:::status_superseded
        AR_1050["AR-1050 - Superseded"]:::status_superseded
        AR_1051["AR-1051 - Done"]:::status_done
        AR_1052["AR-1052 - Superseded"]:::status_superseded
        AR_1053["AR-1053 - Done"]:::status_done
        AR_1054["AR-1054 - Superseded"]:::status_superseded
        AR_1055["AR-1055 - Done"]:::status_done
        AR_1056["AR-1056 - Superseded"]:::status_superseded
        AR_1057["AR-1057 - Done"]:::status_done
        AR_1058["AR-1058 - Superseded"]:::status_superseded
        AR_1059["AR-1059 - Done"]:::status_done
        AR_1060["AR-1060 - Done"]:::status_done
        AR_1061["AR-1061 - Superseded"]:::status_superseded
        AR_1062["AR-1062 - Done"]:::status_done
        AR_1064["AR-1064 - Done"]:::status_done
        AR_1065["AR-1065 - Done"]:::status_done
    end
    subgraph series_11["11 - Additional work"]
        direction TB
        AR_1100["AR-1100 - Done"]:::status_done
        AR_1110["AR-1110 - Done"]:::status_done
        AR_1120["AR-1120 - Done"]:::status_done
        AR_1130["AR-1130 - Done"]:::status_done
        AR_1140["AR-1140 - Done"]:::status_done
        AR_1150["AR-1150 - Done"]:::status_done
        AR_1151["AR-1151 - Done"]:::status_done
        AR_1160["AR-1160 - Blocked"]:::status_blocked
        AR_1170["AR-1170 - Planned"]:::status_planned
        AR_1180["AR-1180 - Planned"]:::status_planned
        AR_1181["AR-1181 - Blocked"]:::status_blocked
        AR_1190["AR-1190 - Done"]:::status_done
        AR_1191["AR-1191 - Done"]:::status_done
        AR_1196["AR-1196 - Done"]:::status_done
        AR_1197["AR-1197 - Done"]:::status_done
        AR_1198["AR-1198 - Done"]:::status_done
        AR_1199["AR-1199 - Blocked"]:::status_blocked
    end
    subgraph series_12["12 - Additional work"]
        direction TB
        AR_1200["AR-1200 - Done"]:::status_done
        AR_1210["AR-1210 - Done"]:::status_done
        AR_1211["AR-1211 - Done"]:::status_done
        AR_1212["AR-1212 - Done"]:::status_done
        AR_1213["AR-1213 - Done"]:::status_done
        AR_1214["AR-1214 - Done"]:::status_done
        AR_1215["AR-1215 - Done"]:::status_done
        AR_1216["AR-1216 - Done"]:::status_done
        AR_1226["AR-1226 - Done"]:::status_done
        AR_1227["AR-1227 - Planned"]:::status_planned
        AR_1228["AR-1228 - Done"]:::status_done
        AR_1229["AR-1229 - Done"]:::status_done
        AR_1230["AR-1230 - Done"]:::status_done
        AR_1231["AR-1231 - Done"]:::status_done
        AR_1232["AR-1232 - Done"]:::status_done
        AR_1233["AR-1233 - Done"]:::status_done
        AR_1234["AR-1234 - Done"]:::status_done
        AR_1235["AR-1235 - Done"]:::status_done
        AR_1236["AR-1236 - Done"]:::status_done
        AR_1237["AR-1237 - Done"]:::status_done
        AR_1238["AR-1238 - Done"]:::status_done
        AR_1239["AR-1239 - Done"]:::status_done
        AR_1240["AR-1240 - Done"]:::status_done
        AR_1241["AR-1241 - Done"]:::status_done
        AR_1242["AR-1242 - Done"]:::status_done
        AR_1243["AR-1243 - Done"]:::status_done
        AR_1244["AR-1244 - Done"]:::status_done
        AR_1245["AR-1245 - Done"]:::status_done
        AR_1246["AR-1246 - Done"]:::status_done
        AR_1247["AR-1247 - Done"]:::status_done
        AR_1248["AR-1248 - Blocked"]:::status_blocked
        AR_1249["AR-1249 - Blocked"]:::status_blocked
        AR_1250["AR-1250 - Blocked"]:::status_blocked
        AR_1251["AR-1251 - Blocked"]:::status_blocked
        AR_1252["AR-1252 - Done"]:::status_done
        AR_1253["AR-1253 - Done"]:::status_done
        AR_1254["AR-1254 - Blocked"]:::status_blocked
        AR_1255["AR-1255 - Planned"]:::status_planned
        AR_1256["AR-1256 - Blocked"]:::status_blocked
        AR_1257["AR-1257 - Planned"]:::status_planned
        AR_1258["AR-1258 - Blocked"]:::status_blocked
        AR_1259["AR-1259 - Done"]:::status_done
        AR_1260["AR-1260 - Blocked"]:::status_blocked
        AR_1261["AR-1261 - Blocked"]:::status_blocked
        AR_1262["AR-1262 - Blocked"]:::status_blocked
        AR_1263["AR-1263 - Done"]:::status_done
        AR_1264["AR-1264 - Done"]:::status_done
        AR_1265["AR-1265 - Blocked"]:::status_blocked
        AR_1266["AR-1266 - Blocked"]:::status_blocked
        AR_1267["AR-1267 - Blocked"]:::status_blocked
        AR_1268["AR-1268 - Blocked"]:::status_blocked
        AR_1269["AR-1269 - Blocked"]:::status_blocked
        AR_1270["AR-1270 - Blocked"]:::status_blocked
        AR_1271["AR-1271 - Blocked"]:::status_blocked
        AR_1272["AR-1272 - Blocked"]:::status_blocked
        AR_1273["AR-1273 - Blocked"]:::status_blocked
        AR_1274["AR-1274 - Blocked"]:::status_blocked
        AR_1275["AR-1275 - Blocked"]:::status_blocked
        AR_1276["AR-1276 - Blocked"]:::status_blocked
        AR_1277["AR-1277 - Blocked"]:::status_blocked
        AR_1278["AR-1278 - Blocked"]:::status_blocked
        AR_1279["AR-1279 - Blocked"]:::status_blocked
        AR_1280["AR-1280 - Blocked"]:::status_blocked
        AR_1281["AR-1281 - Blocked"]:::status_blocked
        AR_1282["AR-1282 - Done"]:::status_done
        AR_1283["AR-1283 - Blocked"]:::status_blocked
        AR_1284["AR-1284 - Blocked"]:::status_blocked
        AR_1285["AR-1285 - Done"]:::status_done
        AR_1286["AR-1286 - Done"]:::status_done
        AR_1287["AR-1287 - Done"]:::status_done
        AR_1288["AR-1288 - Done"]:::status_done
        AR_1289["AR-1289 - Done"]:::status_done
        AR_1290["AR-1290 - Done"]:::status_done
        AR_1291["AR-1291 - Done"]:::status_done
        AR_1292["AR-1292 - Blocked"]:::status_blocked
        AR_1293["AR-1293 - Blocked"]:::status_blocked
        AR_1294["AR-1294 - Superseded"]:::status_superseded
        AR_1295["AR-1295 - Done"]:::status_done
        AR_1296["AR-1296 - Done"]:::status_done
        AR_1297["AR-1297 - Done"]:::status_done
        AR_1298["AR-1298 - Done"]:::status_done
        AR_1299["AR-1299 - Done"]:::status_done
    end
    subgraph series_13["13 - Additional work"]
        direction TB
        AR_1300["AR-1300 - Done"]:::status_done
        AR_1301["AR-1301 - Superseded"]:::status_superseded
        AR_1302["AR-1302 - Done"]:::status_done
        AR_1303["AR-1303 - Done"]:::status_done
        AR_1304["AR-1304 - Done"]:::status_done
        AR_1305["AR-1305 - Done"]:::status_done
        AR_1306["AR-1306 - Done"]:::status_done
        AR_1307["AR-1307 - Blocked"]:::status_blocked
        AR_1308["AR-1308 - Blocked"]:::status_blocked
        AR_1309["AR-1309 - Superseded"]:::status_superseded
        AR_1310["AR-1310 - Done"]:::status_done
        AR_1311["AR-1311 - Done"]:::status_done
        AR_1312["AR-1312 - Done"]:::status_done
        AR_1313["AR-1313 - Done"]:::status_done
        AR_1314["AR-1314 - Done"]:::status_done
        AR_1315["AR-1315 - Done"]:::status_done
        AR_1316["AR-1316 - Done"]:::status_done
        AR_1319["AR-1319 - Done"]:::status_done
        AR_1320["AR-1320 - Done"]:::status_done
        AR_1322["AR-1322 - Done"]:::status_done
        AR_1324["AR-1324 - Done"]:::status_done
        AR_1325["AR-1325 - Done"]:::status_done
        AR_1326["AR-1326 - Done"]:::status_done
        AR_1327["AR-1327 - Done"]:::status_done
        AR_1328["AR-1328 - Done"]:::status_done
        AR_1329["AR-1329 - Done"]:::status_done
        AR_1330["AR-1330 - Done"]:::status_done
        AR_1331["AR-1331 - Done"]:::status_done
        AR_1332["AR-1332 - Done"]:::status_done
        AR_1333["AR-1333 - Superseded"]:::status_superseded
        AR_1334["AR-1334 - Done"]:::status_done
        AR_1335["AR-1335 - Done"]:::status_done
        AR_1336["AR-1336 - Done"]:::status_done
        AR_1337["AR-1337 - Done"]:::status_done
        AR_1338["AR-1338 - Done"]:::status_done
        AR_1339["AR-1339 - Done"]:::status_done
        AR_1340["AR-1340 - Done"]:::status_done
        AR_1341["AR-1341 - Done"]:::status_done
        AR_1342["AR-1342 - Done"]:::status_done
        AR_1343["AR-1343 - Superseded"]:::status_superseded
        AR_1344["AR-1344 - Done"]:::status_done
        AR_1345["AR-1345 - Done"]:::status_done
        AR_1346["AR-1346 - Superseded"]:::status_superseded
        AR_1347["AR-1347 - Done"]:::status_done
        AR_1348["AR-1348 - Superseded"]:::status_superseded
        AR_1349["AR-1349 - Superseded"]:::status_superseded
        AR_1350["AR-1350 - Done"]:::status_done
        AR_1351["AR-1351 - Done"]:::status_done
        AR_1352["AR-1352 - Done"]:::status_done
        AR_1353["AR-1353 - Superseded"]:::status_superseded
        AR_1354["AR-1354 - Blocked"]:::status_blocked
        AR_1355["AR-1355 - Blocked"]:::status_blocked
        AR_1356["AR-1356 - Done"]:::status_done
        AR_1357["AR-1357 - Done"]:::status_done
        AR_1358["AR-1358 - Blocked"]:::status_blocked
        AR_1359["AR-1359 - Done"]:::status_done
        AR_1360["AR-1360 - Blocked"]:::status_blocked
        AR_1361["AR-1361 - Blocked"]:::status_blocked
        AR_1362["AR-1362 - Done"]:::status_done
        AR_1363["AR-1363 - Done"]:::status_done
        AR_1364["AR-1364 - Done"]:::status_done
        AR_1365["AR-1365 - Done"]:::status_done
        AR_1366["AR-1366 - Done"]:::status_done
        AR_1367["AR-1367 - Done"]:::status_done
        AR_1368["AR-1368 - Blocked"]:::status_blocked
        AR_1369["AR-1369 - Superseded"]:::status_superseded
        AR_1370["AR-1370 - Superseded"]:::status_superseded
        AR_1371["AR-1371 - Done"]:::status_done
        AR_1372["AR-1372 - Done"]:::status_done
        AR_1373["AR-1373 - Done"]:::status_done
        AR_1374["AR-1374 - Done"]:::status_done
        AR_1375["AR-1375 - Superseded"]:::status_superseded
        AR_1376["AR-1376 - Blocked"]:::status_blocked
        AR_1377["AR-1377 - Done"]:::status_done
        AR_1378["AR-1378 - Done"]:::status_done
        AR_1379["AR-1379 - Done"]:::status_done
        AR_1380["AR-1380 - Done"]:::status_done
        AR_1381["AR-1381 - Done"]:::status_done
        AR_1382["AR-1382 - Blocked"]:::status_blocked
        AR_1383["AR-1383 - Done"]:::status_done
        AR_1384["AR-1384 - Done"]:::status_done
        AR_1385["AR-1385 - Done"]:::status_done
        AR_1386["AR-1386 - Blocked"]:::status_blocked
        AR_1387["AR-1387 - Blocked"]:::status_blocked
        AR_1388["AR-1388 - Done"]:::status_done
        AR_1389["AR-1389 - Done"]:::status_done
        AR_1390["AR-1390 - Done"]:::status_done
        AR_1391["AR-1391 - Blocked"]:::status_blocked
        AR_1392["AR-1392 - Done"]:::status_done
        AR_1393["AR-1393 - Done"]:::status_done
        AR_1394["AR-1394 - Done"]:::status_done
        AR_1395["AR-1395 - Done"]:::status_done
        AR_1396["AR-1396 - Done"]:::status_done
        AR_1397["AR-1397 - Done"]:::status_done
        AR_1398["AR-1398 - Done"]:::status_done
        AR_1399["AR-1399 - Done"]:::status_done
    end
    subgraph series_14["14 - Additional work"]
        direction TB
        AR_1400["AR-1400 - Done"]:::status_done
        AR_1401["AR-1401 - Done"]:::status_done
        AR_1402["AR-1402 - Done"]:::status_done
        AR_1403["AR-1403 - Done"]:::status_done
        AR_1404["AR-1404 - Done"]:::status_done
        AR_1405["AR-1405 - Done"]:::status_done
        AR_1406["AR-1406 - Done"]:::status_done
        AR_1407["AR-1407 - Done"]:::status_done
        AR_1408["AR-1408 - Done"]:::status_done
        AR_1409["AR-1409 - Done"]:::status_done
        AR_1410["AR-1410 - Done"]:::status_done
        AR_1411["AR-1411 - Done"]:::status_done
        AR_1412["AR-1412 - Done"]:::status_done
        AR_1413["AR-1413 - Done"]:::status_done
        AR_1414["AR-1414 - Done"]:::status_done
        AR_1415["AR-1415 - Done"]:::status_done
        AR_1416["AR-1416 - Done"]:::status_done
        AR_1417["AR-1417 - Done"]:::status_done
        AR_1418["AR-1418 - Done"]:::status_done
        AR_1419["AR-1419 - Done"]:::status_done
        AR_1420["AR-1420 - Done"]:::status_done
        AR_1421["AR-1421 - Done"]:::status_done
        AR_1422["AR-1422 - Done"]:::status_done
        AR_1423["AR-1423 - Done"]:::status_done
        AR_1424["AR-1424 - Done"]:::status_done
        AR_1425["AR-1425 - Done"]:::status_done
        AR_1426["AR-1426 - Done"]:::status_done
        AR_1427["AR-1427 - Done"]:::status_done
        AR_1430["AR-1430 - Done"]:::status_done
        AR_1431["AR-1431 - Done"]:::status_done
        AR_1432["AR-1432 - Done"]:::status_done
        AR_1433["AR-1433 - Done"]:::status_done
        AR_1434["AR-1434 - Done"]:::status_done
        AR_1435["AR-1435 - Done"]:::status_done
        AR_1436["AR-1436 - Done"]:::status_done
        AR_1437["AR-1437 - Done"]:::status_done
        AR_1438["AR-1438 - Done"]:::status_done
        AR_1440["AR-1440 - Done"]:::status_done
        AR_1441["AR-1441 - Done"]:::status_done
        AR_1442["AR-1442 - Done"]:::status_done
        AR_1443["AR-1443 - Done"]:::status_done
        AR_1444["AR-1444 - Blocked"]:::status_blocked
        AR_1445["AR-1445 - Done"]:::status_done
        AR_1446["AR-1446 - Done"]:::status_done
        AR_1447["AR-1447 - Done"]:::status_done
        AR_1448["AR-1448 - Done"]:::status_done
        AR_1449["AR-1449 - Done"]:::status_done
        AR_1450["AR-1450 - Done"]:::status_done
        AR_1451["AR-1451 - Done"]:::status_done
        AR_1452["AR-1452 - Done"]:::status_done
        AR_1453["AR-1453 - Done"]:::status_done
        AR_1454["AR-1454 - Done"]:::status_done
        AR_1455["AR-1455 - Done"]:::status_done
        AR_1456["AR-1456 - Done"]:::status_done
        AR_1457["AR-1457 - Done"]:::status_done
        AR_1458["AR-1458 - Done"]:::status_done
        AR_1459["AR-1459 - Done"]:::status_done
        AR_1460["AR-1460 - Done"]:::status_done
        AR_1461["AR-1461 - Done"]:::status_done
        AR_1462["AR-1462 - Done"]:::status_done
        AR_1463["AR-1463 - Done"]:::status_done
        AR_1464["AR-1464 - Superseded"]:::status_superseded
        AR_1465["AR-1465 - Superseded"]:::status_superseded
        AR_1466["AR-1466 - Done"]:::status_done
        AR_1467["AR-1467 - Done"]:::status_done
        AR_1468["AR-1468 - Superseded"]:::status_superseded
        AR_1469["AR-1469 - Done"]:::status_done
        AR_1470["AR-1470 - Blocked"]:::status_blocked
        AR_1471["AR-1471 - Done"]:::status_done
        AR_1472["AR-1472 - Done"]:::status_done
        AR_1473["AR-1473 - Done"]:::status_done
        AR_1474["AR-1474 - Done"]:::status_done
        AR_1475["AR-1475 - Done"]:::status_done
        AR_1476["AR-1476 - Done"]:::status_done
        AR_1477["AR-1477 - Done"]:::status_done
        AR_1478["AR-1478 - Done"]:::status_done
        AR_1479["AR-1479 - Done"]:::status_done
        AR_1480["AR-1480 - Done"]:::status_done
        AR_1481["AR-1481 - Blocked"]:::status_blocked
        AR_1482["AR-1482 - Blocked"]:::status_blocked
        AR_1483["AR-1483 - Blocked"]:::status_blocked
        AR_1484["AR-1484 - Done"]:::status_done
        AR_1485["AR-1485 - Done"]:::status_done
        AR_1486["AR-1486 - Done"]:::status_done
        AR_1487["AR-1487 - Done"]:::status_done
        AR_1488["AR-1488 - Done"]:::status_done
        AR_1489["AR-1489 - Done"]:::status_done
        AR_1490["AR-1490 - Done"]:::status_done
        AR_1491["AR-1491 - Done"]:::status_done
        AR_1492["AR-1492 - Done"]:::status_done
        AR_1493["AR-1493 - Done"]:::status_done
        AR_1495["AR-1495 - Done"]:::status_done
        AR_1496["AR-1496 - Done"]:::status_done
        AR_1497["AR-1497 - Done"]:::status_done
        AR_1498["AR-1498 - Done"]:::status_done
        AR_1499["AR-1499 - Done"]:::status_done
    end
    subgraph series_15["15 - Additional work"]
        direction TB
        AR_1500["AR-1500 - Done"]:::status_done
        AR_1501["AR-1501 - Done"]:::status_done
        AR_1502["AR-1502 - Done"]:::status_done
        AR_1503["AR-1503 - Superseded"]:::status_superseded
        AR_1504["AR-1504 - Superseded"]:::status_superseded
        AR_1505["AR-1505 - Done"]:::status_done
        AR_1506["AR-1506 - Blocked"]:::status_blocked
        AR_1507["AR-1507 - Blocked"]:::status_blocked
        AR_1508["AR-1508 - Blocked"]:::status_blocked
        AR_1509["AR-1509 - Blocked"]:::status_blocked
        AR_1510["AR-1510 - Blocked"]:::status_blocked
        AR_1511["AR-1511 - Superseded"]:::status_superseded
        AR_1512["AR-1512 - Blocked"]:::status_blocked
        AR_1513["AR-1513 - Done"]:::status_done
        AR_1514["AR-1514 - Done"]:::status_done
        AR_1515["AR-1515 - Done"]:::status_done
        AR_1516["AR-1516 - Done"]:::status_done
        AR_1517["AR-1517 - Done"]:::status_done
        AR_1518["AR-1518 - Blocked"]:::status_blocked
        AR_1519["AR-1519 - Done"]:::status_done
        AR_1520["AR-1520 - Done"]:::status_done
        AR_1521["AR-1521 - Superseded"]:::status_superseded
        AR_1522["AR-1522 - Blocked"]:::status_blocked
        AR_1523["AR-1523 - Done"]:::status_done
        AR_1524["AR-1524 - Done"]:::status_done
        AR_1525["AR-1525 - Done"]:::status_done
        AR_1526["AR-1526 - Done"]:::status_done
        AR_1527["AR-1527 - Done"]:::status_done
        AR_1528["AR-1528 - Done"]:::status_done
        AR_1529["AR-1529 - Done"]:::status_done
        AR_1530["AR-1530 - Done"]:::status_done
        AR_1531["AR-1531 - Blocked"]:::status_blocked
        AR_1532["AR-1532 - Done"]:::status_done
        AR_1533["AR-1533 - Done"]:::status_done
        AR_1534["AR-1534 - Done"]:::status_done
        AR_1535["AR-1535 - Blocked"]:::status_blocked
        AR_1536["AR-1536 - Done"]:::status_done
        AR_1537["AR-1537 - Blocked"]:::status_blocked
        AR_1538["AR-1538 - Blocked"]:::status_blocked
        AR_1539["AR-1539 - Blocked"]:::status_blocked
        AR_1540["AR-1540 - Done"]:::status_done
        AR_1541["AR-1541 - Done"]:::status_done
        AR_1542["AR-1542 - Done"]:::status_done
        AR_1543["AR-1543 - Done"]:::status_done
        AR_1544["AR-1544 - Superseded"]:::status_superseded
        AR_1545["AR-1545 - Planned"]:::status_planned
        AR_1546["AR-1546 - Planned"]:::status_planned
        AR_1547["AR-1547 - Done"]:::status_done
        AR_1548["AR-1548 - Superseded"]:::status_superseded
        AR_1549["AR-1549 - Done"]:::status_done
        AR_1550["AR-1550 - Done"]:::status_done
        AR_1551["AR-1551 - Cancelled"]:::status_cancelled
        AR_1552["AR-1552 - Done"]:::status_done
        AR_1553["AR-1553 - Done"]:::status_done
        AR_1554["AR-1554 - Done"]:::status_done
        AR_1555["AR-1555 - Done"]:::status_done
        AR_1556["AR-1556 - Superseded"]:::status_superseded
        AR_1557["AR-1557 - Done"]:::status_done
        AR_1558["AR-1558 - Done"]:::status_done
        AR_1559["AR-1559 - Done"]:::status_done
        AR_1560["AR-1560 - Superseded"]:::status_superseded
        AR_1561["AR-1561 - Cancelled"]:::status_cancelled
        AR_1562["AR-1562 - Done"]:::status_done
        AR_1563["AR-1563 - Done"]:::status_done
        AR_1564["AR-1564 - Done"]:::status_done
        AR_1565["AR-1565 - Done"]:::status_done
        AR_1566["AR-1566 - Blocked"]:::status_blocked
        AR_1567["AR-1567 - Done"]:::status_done
        AR_1568["AR-1568 - Done"]:::status_done
        AR_1569["AR-1569 - Done"]:::status_done
        AR_1570["AR-1570 - Done"]:::status_done
        AR_1571["AR-1571 - Blocked"]:::status_blocked
        AR_1572["AR-1572 - Done"]:::status_done
        AR_1573["AR-1573 - Done"]:::status_done
        AR_1574["AR-1574 - Done"]:::status_done
        AR_1576["AR-1576 - Done"]:::status_done
        AR_1577["AR-1577 - Done"]:::status_done
        AR_1578["AR-1578 - Done"]:::status_done
        AR_1588["AR-1588 - Done"]:::status_done
        AR_1589["AR-1589 - Done"]:::status_done
        AR_1590["AR-1590 - Done"]:::status_done
        AR_1591["AR-1591 - Done"]:::status_done
        AR_1592["AR-1592 - Done"]:::status_done
        AR_1593["AR-1593 - Done"]:::status_done
        AR_1594["AR-1594 - Done"]:::status_done
        AR_1595["AR-1595 - Done"]:::status_done
        AR_1596["AR-1596 - Done"]:::status_done
        AR_1597["AR-1597 - Done"]:::status_done
        AR_1598["AR-1598 - Done"]:::status_done
        AR_1599["AR-1599 - Done"]:::status_done
    end
    subgraph series_16["16 - Additional work"]
        direction TB
        AR_1600["AR-1600 - Done"]:::status_done
        AR_1601["AR-1601 - Done"]:::status_done
        AR_1602["AR-1602 - Done"]:::status_done
        AR_1603["AR-1603 - Done"]:::status_done
        AR_1604["AR-1604 - Done"]:::status_done
        AR_1605["AR-1605 - Done"]:::status_done
        AR_1606["AR-1606 - Done"]:::status_done
        AR_1607["AR-1607 - Done"]:::status_done
        AR_1608["AR-1608 - Done"]:::status_done
        AR_1609["AR-1609 - Done"]:::status_done
        AR_1611["AR-1611 - Done"]:::status_done
        AR_1612["AR-1612 - Done"]:::status_done
        AR_1613["AR-1613 - Blocked"]:::status_blocked
        AR_1614["AR-1614 - Done"]:::status_done
        AR_1615["AR-1615 - Done"]:::status_done
        AR_1617["AR-1617 - Done"]:::status_done
        AR_1618["AR-1618 - Done"]:::status_done
        AR_1619["AR-1619 - Done"]:::status_done
        AR_1620["AR-1620 - Done"]:::status_done
        AR_1621["AR-1621 - Done"]:::status_done
        AR_1622["AR-1622 - Planned"]:::status_planned
        AR_1623["AR-1623 - Planned"]:::status_planned
        AR_1624["AR-1624 - Planned"]:::status_planned
        AR_1625["AR-1625 - Done"]:::status_done
        AR_1626["AR-1626 - Done"]:::status_done
        AR_1627["AR-1627 - Done"]:::status_done
        AR_1628["AR-1628 - Done"]:::status_done
        AR_1629["AR-1629 - Done"]:::status_done
        AR_1630["AR-1630 - Done"]:::status_done
        AR_1631["AR-1631 - Done"]:::status_done
        AR_1632["AR-1632 - Done"]:::status_done
        AR_1633["AR-1633 - Done"]:::status_done
        AR_1634["AR-1634 - Done"]:::status_done
        AR_1635["AR-1635 - Done"]:::status_done
        AR_1636["AR-1636 - Done"]:::status_done
        AR_1637["AR-1637 - Done"]:::status_done
        AR_1638["AR-1638 - Done"]:::status_done
        AR_1639["AR-1639 - Done"]:::status_done
        AR_1640["AR-1640 - Done"]:::status_done
        AR_1641["AR-1641 - Done"]:::status_done
        AR_1642["AR-1642 - Done"]:::status_done
        AR_1643["AR-1643 - Planned"]:::status_planned
        AR_1644["AR-1644 - Done"]:::status_done
        AR_1645["AR-1645 - Done"]:::status_done
        AR_1646["AR-1646 - Done"]:::status_done
        AR_1647["AR-1647 - Done"]:::status_done
        AR_1648["AR-1648 - Done"]:::status_done
        AR_1649["AR-1649 - Done"]:::status_done
        AR_1650["AR-1650 - Done"]:::status_done
        AR_1651["AR-1651 - Done"]:::status_done
        AR_1652["AR-1652 - Done"]:::status_done
        AR_1653["AR-1653 - Planned"]:::status_planned
        AR_1654["AR-1654 - Planned"]:::status_planned
        AR_1655["AR-1655 - Planned"]:::status_planned
        AR_1656["AR-1656 - Done"]:::status_done
        AR_1657["AR-1657 - Done"]:::status_done
        AR_1658["AR-1658 - Planned"]:::status_planned
        AR_1659["AR-1659 - Planned"]:::status_planned
        AR_1660["AR-1660 - Planned"]:::status_planned
        AR_1661["AR-1661 - Done"]:::status_done
        AR_1663["AR-1663 - Planned"]:::status_planned
        AR_1665["AR-1665 - Planned"]:::status_planned
        AR_1666["AR-1666 - Planned"]:::status_planned
        AR_1667["AR-1667 - Planned"]:::status_planned
        AR_1668["AR-1668 - Planned"]:::status_planned
        AR_1670["AR-1670 - Planned"]:::status_planned
        AR_1671["AR-1671 - Planned"]:::status_planned
        AR_1674["AR-1674 - Planned"]:::status_planned
        AR_1675["AR-1675 - Planned"]:::status_planned
        AR_1676["AR-1676 - Planned"]:::status_planned
        AR_1677["AR-1677 - Planned"]:::status_planned
        AR_1678["AR-1678 - Done"]:::status_done
        AR_1679["AR-1679 - Planned"]:::status_planned
        AR_1680["AR-1680 - Planned"]:::status_planned
        AR_1681["AR-1681 - Planned"]:::status_planned
        AR_1682["AR-1682 - Planned"]:::status_planned
        AR_1683["AR-1683 - Planned"]:::status_planned
        AR_1684["AR-1684 - Planned"]:::status_planned
        AR_1685["AR-1685 - Done"]:::status_done
        AR_1686["AR-1686 - Done"]:::status_done
        AR_1687["AR-1687 - Done"]:::status_done
        AR_1688["AR-1688 - Done"]:::status_done
        AR_1689["AR-1689 - Done"]:::status_done
        AR_1690["AR-1690 - Done"]:::status_done
        AR_1691["AR-1691 - Planned"]:::status_planned
        AR_1692["AR-1692 - Done"]:::status_done
        AR_1693["AR-1693 - Planned"]:::status_planned
        AR_1694["AR-1694 - Done"]:::status_done
        AR_1695["AR-1695 - Done"]:::status_done
        AR_1696["AR-1696 - Done"]:::status_done
        AR_1697["AR-1697 - Planned"]:::status_planned
        AR_1698["AR-1698 - Done"]:::status_done
        AR_1699["AR-1699 - Done"]:::status_done
    end
    subgraph series_17["17 - Additional work"]
        direction TB
        AR_1700["AR-1700 - Done"]:::status_done
        AR_1701["AR-1701 - Done"]:::status_done
        AR_1702["AR-1702 - Blocked"]:::status_blocked
        AR_1703["AR-1703 - Planned"]:::status_planned
        AR_1704["AR-1704 - Done"]:::status_done
        AR_1709["AR-1709 - Done"]:::status_done
        AR_1710["AR-1710 - Done"]:::status_done
        AR_1711["AR-1711 - Done"]:::status_done
        AR_1712["AR-1712 - Done"]:::status_done
        AR_1715["AR-1715 - Done"]:::status_done
        AR_1716["AR-1716 - Done"]:::status_done
        AR_1717["AR-1717 - Done"]:::status_done
        AR_1718["AR-1718 - Done"]:::status_done
        AR_1719["AR-1719 - Done"]:::status_done
        AR_1720["AR-1720 - Done"]:::status_done
        AR_1721["AR-1721 - Done"]:::status_done
        AR_1722["AR-1722 - Done"]:::status_done
        AR_1723["AR-1723 - Done"]:::status_done
        AR_1724["AR-1724 - Done"]:::status_done
        AR_1725["AR-1725 - Done"]:::status_done
        AR_1726["AR-1726 - Done"]:::status_done
        AR_1727["AR-1727 - Done"]:::status_done
        AR_1728["AR-1728 - Done"]:::status_done
        AR_1729["AR-1729 - Done"]:::status_done
        AR_1730["AR-1730 - Done"]:::status_done
        AR_1731["AR-1731 - Done"]:::status_done
        AR_1732["AR-1732 - Done"]:::status_done
        AR_1733["AR-1733 - Done"]:::status_done
        AR_1734["AR-1734 - Done"]:::status_done
        AR_1735["AR-1735 - Done"]:::status_done
        AR_1736["AR-1736 - Done"]:::status_done
        AR_1737["AR-1737 - Done"]:::status_done
        AR_1738["AR-1738 - Done"]:::status_done
        AR_1739["AR-1739 - Done"]:::status_done
        AR_1740["AR-1740 - Done"]:::status_done
        AR_1741["AR-1741 - Done"]:::status_done
        AR_1742["AR-1742 - Done"]:::status_done
        AR_1743["AR-1743 - Done"]:::status_done
        AR_1744["AR-1744 - Done"]:::status_done
        AR_1745["AR-1745 - Done"]:::status_done
        AR_1746["AR-1746 - Blocked"]:::status_blocked
        AR_1747["AR-1747 - Done"]:::status_done
        AR_1748["AR-1748 - Done"]:::status_done
        AR_1749["AR-1749 - Done"]:::status_done
        AR_1750["AR-1750 - Done"]:::status_done
        AR_1751["AR-1751 - Done"]:::status_done
        AR_1752["AR-1752 - Done"]:::status_done
        AR_1753["AR-1753 - Done"]:::status_done
        AR_1754["AR-1754 - Done"]:::status_done
        AR_1755["AR-1755 - Done"]:::status_done
        AR_1756["AR-1756 - Done"]:::status_done
        AR_1757["AR-1757 - Done"]:::status_done
        AR_1758["AR-1758 - Done"]:::status_done
        AR_1759["AR-1759 - Done"]:::status_done
        AR_1760["AR-1760 - Done"]:::status_done
        AR_1761["AR-1761 - Done"]:::status_done
        AR_1762["AR-1762 - Done"]:::status_done
        AR_1763["AR-1763 - Done"]:::status_done
        AR_1764["AR-1764 - Done"]:::status_done
        AR_1765["AR-1765 - Done"]:::status_done
        AR_1766["AR-1766 - Done"]:::status_done
        AR_1767["AR-1767 - Done"]:::status_done
        AR_1768["AR-1768 - Done"]:::status_done
        AR_1769["AR-1769 - Done"]:::status_done
        AR_1770["AR-1770 - Done"]:::status_done
        AR_1771["AR-1771 - Done"]:::status_done
        AR_1772["AR-1772 - Done"]:::status_done
        AR_1773["AR-1773 - Open"]:::status_open
        AR_1774["AR-1774 - Planned"]:::status_planned
        AR_1775["AR-1775 - Done"]:::status_done
        AR_1776["AR-1776 - Done"]:::status_done
        AR_1777["AR-1777 - Done"]:::status_done
        AR_1778["AR-1778 - Done"]:::status_done
        AR_1779["AR-1779 - Done"]:::status_done
        AR_1780["AR-1780 - Planned"]:::status_planned
        AR_1781["AR-1781 - Done"]:::status_done
        AR_1782["AR-1782 - Done"]:::status_done
        AR_1783["AR-1783 - Open"]:::status_open
        AR_1784["AR-1784 - Done"]:::status_done
        AR_1785["AR-1785 - Done"]:::status_done
        AR_1786["AR-1786 - Done"]:::status_done
        AR_1787["AR-1787 - Done"]:::status_done
        AR_1788["AR-1788 - Done"]:::status_done
        AR_1789["AR-1789 - Done"]:::status_done
        AR_1790["AR-1790 - Done"]:::status_done
        AR_1791["AR-1791 - Done"]:::status_done
        AR_1792["AR-1792 - Done"]:::status_done
        AR_1793["AR-1793 - Done"]:::status_done
        AR_1794["AR-1794 - Done"]:::status_done
        AR_1795["AR-1795 - Done"]:::status_done
        AR_1796["AR-1796 - Blocked"]:::status_blocked
        AR_1797["AR-1797 - Done"]:::status_done
        AR_1798["AR-1798 - Done"]:::status_done
        AR_1799["AR-1799 - Done"]:::status_done
    end
    subgraph series_18["18 - Additional work"]
        direction TB
        AR_1800["AR-1800 - Done"]:::status_done
        AR_1819["AR-1819 - Done"]:::status_done
        AR_1820["AR-1820 - Done"]:::status_done
        AR_1821["AR-1821 - Done"]:::status_done
        AR_1822["AR-1822 - Done"]:::status_done
        AR_1823["AR-1823 - Done"]:::status_done
        AR_1824["AR-1824 - Done"]:::status_done
        AR_1825["AR-1825 - Done"]:::status_done
        AR_1826["AR-1826 - Blocked"]:::status_blocked
        AR_1827["AR-1827 - Planned"]:::status_planned
        AR_1828["AR-1828 - Planned"]:::status_planned
        AR_1829["AR-1829 - Planned"]:::status_planned
        AR_1830["AR-1830 - Planned"]:::status_planned
        AR_1831["AR-1831 - Planned"]:::status_planned
        AR_1832["AR-1832 - Planned"]:::status_planned
        AR_1833["AR-1833 - Done"]:::status_done
        AR_1834["AR-1834 - Done"]:::status_done
        AR_1835["AR-1835 - Done"]:::status_done
        AR_1836["AR-1836 - Blocked"]:::status_blocked
        AR_1837["AR-1837 - Done"]:::status_done
        AR_1838["AR-1838 - Done"]:::status_done
        AR_1839["AR-1839 - Done"]:::status_done
        AR_1840["AR-1840 - Done"]:::status_done
        AR_1841["AR-1841 - Blocked"]:::status_blocked
        AR_1842["AR-1842 - Planned"]:::status_planned
        AR_1843["AR-1843 - Done"]:::status_done
        AR_1844["AR-1844 - Planned"]:::status_planned
        AR_1845["AR-1845 - Planned"]:::status_planned
        AR_1846["AR-1846 - Planned"]:::status_planned
        AR_1847["AR-1847 - Planned"]:::status_planned
        AR_1848["AR-1848 - Planned"]:::status_planned
        AR_1849["AR-1849 - Open"]:::status_open
        AR_1850["AR-1850 - Done"]:::status_done
        AR_1851["AR-1851 - Blocked"]:::status_blocked
        AR_1852["AR-1852 - Open"]:::status_open
        AR_1853["AR-1853 - Open"]:::status_open
        AR_1854["AR-1854 - Planned"]:::status_planned
        AR_1855["AR-1855 - Done"]:::status_done
        AR_1856["AR-1856 - Done"]:::status_done
        AR_1857["AR-1857 - Blocked"]:::status_blocked
        AR_1858["AR-1858 - Blocked"]:::status_blocked
        AR_1859["AR-1859 - Planned"]:::status_planned
        AR_1860["AR-1860 - Done"]:::status_done
        AR_1861["AR-1861 - Done"]:::status_done
        AR_1862["AR-1862 - Done"]:::status_done
        AR_1863["AR-1863 - Blocked"]:::status_blocked
        AR_1864["AR-1864 - Done"]:::status_done
        AR_1865["AR-1865 - Done"]:::status_done
        AR_1866["AR-1866 - Done"]:::status_done
        AR_1867["AR-1867 - Superseded"]:::status_superseded
        AR_1868["AR-1868 - Done"]:::status_done
        AR_1869["AR-1869 - Superseded"]:::status_superseded
        AR_1870["AR-1870 - Done"]:::status_done
        AR_1871["AR-1871 - Done"]:::status_done
        AR_1872["AR-1872 - Done"]:::status_done
        AR_1873["AR-1873 - Done"]:::status_done
        AR_1874["AR-1874 - Superseded"]:::status_superseded
        AR_1875["AR-1875 - Blocked"]:::status_blocked
        AR_1876["AR-1876 - Blocked"]:::status_blocked
        AR_1877["AR-1877 - In progress"]:::status_in_progress
    end
    AR_0001 --> AR_0002
    AR_0001 --> AR_0003
    AR_0001 --> AR_0101
    AR_0001 --> AR_0501
    AR_0001 --> AR_0701
    AR_0002 --> AR_0004
    AR_0002 --> AR_0005
    AR_0002 --> AR_0830
    AR_0002 --> AR_0834
    AR_0002 --> AR_0895
    AR_0002 --> AR_0903
    AR_0003 --> AR_0830
    AR_0003 --> AR_0831
    AR_0003 --> AR_0845
    AR_0003 --> AR_0855
    AR_0003 --> AR_0877
    AR_0003 --> AR_0878
    AR_0003 --> AR_0895
    AR_0003 --> AR_0897
    AR_0003 --> AR_0898
    AR_0003 --> AR_0899
    AR_0003 --> AR_0903
    AR_0003 --> AR_0906
    AR_0003 --> AR_1235
    AR_0003 --> AR_1242
    AR_0003 --> AR_1252
    AR_0003 --> AR_1283
    AR_0004 --> AR_0005
    AR_0004 --> AR_0849
    AR_0101 --> AR_0102
    AR_0101 --> AR_0104
    AR_0101 --> AR_0201
    AR_0101 --> AR_0203
    AR_0101 --> AR_0301
    AR_0101 --> AR_0302
    AR_0101 --> AR_0303
    AR_0101 --> AR_0304
    AR_0101 --> AR_0305
    AR_0101 --> AR_0306
    AR_0101 --> AR_0307
    AR_0101 --> AR_0308
    AR_0101 --> AR_0309
    AR_0101 --> AR_0310
    AR_0101 --> AR_0317
    AR_0101 --> AR_0401
    AR_0101 --> AR_0502
    AR_0101 --> AR_0517
    AR_0101 --> AR_0601
    AR_0101 --> AR_0603
    AR_0101 --> AR_0801
    AR_0101 --> AR_0803
    AR_0101 --> AR_0840
    AR_0101 --> AR_0847
    AR_0101 --> AR_0857
    AR_0101 --> AR_0863
    AR_0101 --> AR_0875
    AR_0101 --> AR_0901
    AR_0101 --> AR_0904
    AR_0101 --> AR_0908
    AR_0101 --> AR_0909
    AR_0101 --> AR_1001
    AR_0101 --> AR_1003
    AR_0101 --> AR_1005
    AR_0101 --> AR_1013
    AR_0102 --> AR_0103
    AR_0102 --> AR_0201
    AR_0102 --> AR_0204
    AR_0102 --> AR_0301
    AR_0102 --> AR_0302
    AR_0102 --> AR_0303
    AR_0102 --> AR_0304
    AR_0102 --> AR_0305
    AR_0102 --> AR_0306
    AR_0102 --> AR_0307
    AR_0102 --> AR_0308
    AR_0102 --> AR_0309
    AR_0102 --> AR_0317
    AR_0102 --> AR_0318
    AR_0102 --> AR_0503
    AR_0102 --> AR_0601
    AR_0102 --> AR_0603
    AR_0102 --> AR_0857
    AR_0102 --> AR_0863
    AR_0102 --> AR_0875
    AR_0102 --> AR_0876
    AR_0102 --> AR_0901
    AR_0102 --> AR_0905
    AR_0102 --> AR_0908
    AR_0102 --> AR_0909
    AR_0103 --> AR_0105
    AR_0103 --> AR_0202
    AR_0103 --> AR_0204
    AR_0103 --> AR_0305
    AR_0103 --> AR_0306
    AR_0103 --> AR_0307
    AR_0103 --> AR_0308
    AR_0103 --> AR_0309
    AR_0103 --> AR_0401
    AR_0103 --> AR_0601
    AR_0103 --> AR_0603
    AR_0103 --> AR_0702
    AR_0103 --> AR_0703
    AR_0103 --> AR_0704
    AR_0103 --> AR_0707
    AR_0103 --> AR_0830
    AR_0103 --> AR_0848
    AR_0103 --> AR_0857
    AR_0103 --> AR_0863
    AR_0103 --> AR_0875
    AR_0103 --> AR_0876
    AR_0103 --> AR_0902
    AR_0103 --> AR_0908
    AR_0103 --> AR_0909
    AR_0103 --> AR_1002
    AR_0104 --> AR_0204
    AR_0104 --> AR_0314
    AR_0104 --> AR_0601
    AR_0104 --> AR_0603
    AR_0104 --> AR_0801
    AR_0104 --> AR_0803
    AR_0104 --> AR_0805
    AR_0104 --> AR_0806
    AR_0104 --> AR_0822
    AR_0104 --> AR_0841
    AR_0104 --> AR_0847
    AR_0104 --> AR_0902
    AR_0104 --> AR_0905
    AR_0104 --> AR_1002
    AR_0104 --> AR_1005
    AR_0104 --> AR_1037
    AR_0105 --> AR_0204
    AR_0201 --> AR_0202
    AR_0201 --> AR_0204
    AR_0201 --> AR_0504
    AR_0201 --> AR_0601
    AR_0201 --> AR_0602
    AR_0201 --> AR_0604
    AR_0201 --> AR_0702
    AR_0201 --> AR_0703
    AR_0201 --> AR_0705
    AR_0201 --> AR_0706
    AR_0201 --> AR_0848
    AR_0202 --> AR_0602
    AR_0202 --> AR_0604
    AR_0203 --> AR_0204
    AR_0203 --> AR_0806
    AR_0203 --> AR_0901
    AR_0203 --> AR_1001
    AR_0203 --> AR_1004
    AR_0204 --> AR_0801
    AR_0204 --> AR_0803
    AR_0204 --> AR_0805
    AR_0204 --> AR_0847
    AR_0204 --> AR_0903
    AR_0204 --> AR_0905
    AR_0204 --> AR_1004
    AR_0204 --> AR_1006
    AR_0301 --> AR_0311
    AR_0301 --> AR_0312
    AR_0301 --> AR_0315
    AR_0301 --> AR_0316
    AR_0301 --> AR_0505
    AR_0301 --> AR_0506
    AR_0301 --> AR_1003
    AR_0302 --> AR_0311
    AR_0302 --> AR_0312
    AR_0302 --> AR_0315
    AR_0302 --> AR_0316
    AR_0302 --> AR_0505
    AR_0302 --> AR_0507
    AR_0302 --> AR_0516
    AR_0302 --> AR_1003
    AR_0303 --> AR_0311
    AR_0303 --> AR_0312
    AR_0303 --> AR_0315
    AR_0303 --> AR_0316
    AR_0303 --> AR_0505
    AR_0303 --> AR_0508
    AR_0303 --> AR_0850
    AR_0303 --> AR_1003
    AR_0304 --> AR_0311
    AR_0304 --> AR_0312
    AR_0304 --> AR_0315
    AR_0304 --> AR_0316
    AR_0304 --> AR_0505
    AR_0304 --> AR_0509
    AR_0304 --> AR_1003
    AR_0305 --> AR_0311
    AR_0305 --> AR_0312
    AR_0305 --> AR_0315
    AR_0305 --> AR_0316
    AR_0305 --> AR_0510
    AR_0306 --> AR_0311
    AR_0306 --> AR_0312
    AR_0306 --> AR_0315
    AR_0306 --> AR_0316
    AR_0306 --> AR_0511
    AR_0307 --> AR_0311
    AR_0307 --> AR_0312
    AR_0307 --> AR_0315
    AR_0307 --> AR_0316
    AR_0307 --> AR_0512
    AR_0308 --> AR_0311
    AR_0308 --> AR_0312
    AR_0308 --> AR_0315
    AR_0308 --> AR_0316
    AR_0308 --> AR_0513
    AR_0308 --> AR_0909
    AR_0309 --> AR_0311
    AR_0309 --> AR_0312
    AR_0309 --> AR_0315
    AR_0309 --> AR_0316
    AR_0309 --> AR_0514
    AR_0309 --> AR_0521
    AR_0310 --> AR_0311
    AR_0310 --> AR_0312
    AR_0310 --> AR_0314
    AR_0310 --> AR_0318
    AR_0310 --> AR_0857
    AR_0310 --> AR_0863
    AR_0310 --> AR_1325
    AR_0311 --> AR_0313
    AR_0311 --> AR_0315
    AR_0312 --> AR_0313
    AR_0312 --> AR_0315
    AR_0312 --> AR_0879
    AR_0312 --> AR_0891
    AR_0313 --> AR_0314
    AR_0313 --> AR_0315
    AR_0313 --> AR_0804
    AR_0313 --> AR_0869
    AR_0313 --> AR_0876
    AR_0313 --> AR_0879
    AR_0313 --> AR_0891
    AR_0313 --> AR_1100
    AR_0313 --> AR_1326
    AR_0314 --> AR_0315
    AR_0314 --> AR_0804
    AR_0314 --> AR_0808
    AR_0314 --> AR_0871
    AR_0315 --> AR_0857
    AR_0315 --> AR_0863
    AR_0315 --> AR_0879
    AR_0315 --> AR_0891
    AR_0315 --> AR_0903
    AR_0315 --> AR_1110
    AR_0315 --> AR_1327
    AR_0316 --> AR_0876
    AR_0317 --> AR_0857
    AR_0317 --> AR_0863
    AR_0317 --> AR_0876
    AR_0318 --> AR_0314
    AR_0318 --> AR_0319
    AR_0318 --> AR_0320
    AR_0318 --> AR_0869
    AR_0318 --> AR_0876
    AR_0318 --> AR_1325
    AR_0319 --> AR_0876
    AR_0319 --> AR_1228
    AR_0319 --> AR_1230
    AR_0320 --> AR_0869
    AR_0320 --> AR_0876
    AR_0320 --> AR_1120
    AR_0320 --> AR_1228
    AR_0320 --> AR_1230
    AR_0401 --> AR_0402
    AR_0401 --> AR_0403
    AR_0401 --> AR_0405
    AR_0401 --> AR_0505
    AR_0401 --> AR_0506
    AR_0401 --> AR_0507
    AR_0401 --> AR_0508
    AR_0401 --> AR_0509
    AR_0401 --> AR_0510
    AR_0401 --> AR_0511
    AR_0401 --> AR_0512
    AR_0401 --> AR_0513
    AR_0401 --> AR_0514
    AR_0401 --> AR_0702
    AR_0401 --> AR_0703
    AR_0401 --> AR_0705
    AR_0401 --> AR_0706
    AR_0401 --> AR_0802
    AR_0401 --> AR_0808
    AR_0401 --> AR_0848
    AR_0401 --> AR_1002
    AR_0401 --> AR_1004
    AR_0401 --> AR_1007
    AR_0402 --> AR_0404
    AR_0402 --> AR_0406
    AR_0403 --> AR_0404
    AR_0404 --> AR_1394
    AR_0405 --> AR_1394
    AR_0406 --> AR_1394
    AR_0501 --> AR_0502
    AR_0501 --> AR_0879
    AR_0502 --> AR_0503
    AR_0502 --> AR_0516
    AR_0502 --> AR_0517
    AR_0502 --> AR_0518
    AR_0502 --> AR_0520
    AR_0502 --> AR_0871
    AR_0502 --> AR_0879
    AR_0502 --> AR_0901
    AR_0502 --> AR_1005
    AR_0502 --> AR_1330
    AR_0503 --> AR_0314
    AR_0503 --> AR_0504
    AR_0503 --> AR_0505
    AR_0503 --> AR_0506
    AR_0503 --> AR_0507
    AR_0503 --> AR_0508
    AR_0503 --> AR_0509
    AR_0503 --> AR_0510
    AR_0503 --> AR_0511
    AR_0503 --> AR_0512
    AR_0503 --> AR_0513
    AR_0503 --> AR_0514
    AR_0503 --> AR_0516
    AR_0503 --> AR_0517
    AR_0503 --> AR_0518
    AR_0503 --> AR_0520
    AR_0503 --> AR_0857
    AR_0503 --> AR_0863
    AR_0503 --> AR_0871
    AR_0503 --> AR_0879
    AR_0503 --> AR_0902
    AR_0503 --> AR_0905
    AR_0503 --> AR_1330
    AR_0504 --> AR_0314
    AR_0504 --> AR_0505
    AR_0504 --> AR_0506
    AR_0504 --> AR_0507
    AR_0504 --> AR_0508
    AR_0504 --> AR_0509
    AR_0504 --> AR_0510
    AR_0504 --> AR_0511
    AR_0504 --> AR_0512
    AR_0504 --> AR_0513
    AR_0504 --> AR_0514
    AR_0504 --> AR_0516
    AR_0504 --> AR_0517
    AR_0504 --> AR_0879
    AR_0505 --> AR_0315
    AR_0505 --> AR_0802
    AR_0505 --> AR_0808
    AR_0505 --> AR_0871
    AR_0505 --> AR_0879
    AR_0505 --> AR_0903
    AR_0505 --> AR_1151
    AR_0505 --> AR_1231
    AR_0505 --> AR_1232
    AR_0506 --> AR_0515
    AR_0507 --> AR_0515
    AR_0508 --> AR_0515
    AR_0508 --> AR_0850
    AR_0509 --> AR_0515
    AR_0510 --> AR_0515
    AR_0511 --> AR_0515
    AR_0512 --> AR_0515
    AR_0513 --> AR_0515
    AR_0514 --> AR_0515
    AR_0517 --> AR_0518
    AR_0517 --> AR_0520
    AR_0518 --> AR_0519
    AR_0601 --> AR_0405
    AR_0601 --> AR_0602
    AR_0601 --> AR_0604
    AR_0601 --> AR_1015
    AR_0602 --> AR_1015
    AR_0603 --> AR_0601
    AR_0604 --> AR_0602
    AR_0604 --> AR_1015
    AR_0701 --> AR_0317
    AR_0701 --> AR_0702
    AR_0701 --> AR_0703
    AR_0701 --> AR_0704
    AR_0701 --> AR_0707
    AR_0701 --> AR_0820
    AR_0701 --> AR_0848
    AR_0701 --> AR_1007
    AR_0702 --> AR_0807
    AR_0702 --> AR_0813
    AR_0702 --> AR_0816
    AR_0702 --> AR_0903
    AR_0702 --> AR_0907
    AR_0702 --> AR_1006
    AR_0704 --> AR_0705
    AR_0704 --> AR_0706
    AR_0801 --> AR_0802
    AR_0801 --> AR_0803
    AR_0801 --> AR_0808
    AR_0801 --> AR_0820
    AR_0801 --> AR_0840
    AR_0801 --> AR_0842
    AR_0801 --> AR_0847
    AR_0801 --> AR_0849
    AR_0801 --> AR_0869
    AR_0802 --> AR_0808
    AR_0802 --> AR_0809
    AR_0802 --> AR_0872
    AR_0802 --> AR_0903
    AR_0803 --> AR_0804
    AR_0803 --> AR_0805
    AR_0803 --> AR_0813
    AR_0803 --> AR_0819
    AR_0803 --> AR_0821
    AR_0803 --> AR_1010
    AR_0803 --> AR_1017
    AR_0803 --> AR_1023
    AR_0804 --> AR_0805
    AR_0804 --> AR_0807
    AR_0804 --> AR_0809
    AR_0804 --> AR_0812
    AR_0804 --> AR_0817
    AR_0804 --> AR_0819
    AR_0804 --> AR_0820
    AR_0804 --> AR_0821
    AR_0804 --> AR_0870
    AR_0804 --> AR_1010
    AR_0804 --> AR_1014
    AR_0804 --> AR_1017
    AR_0804 --> AR_1025
    AR_0805 --> AR_0806
    AR_0805 --> AR_0807
    AR_0805 --> AR_0809
    AR_0805 --> AR_0812
    AR_0805 --> AR_0815
    AR_0805 --> AR_0817
    AR_0805 --> AR_0821
    AR_0805 --> AR_0870
    AR_0805 --> AR_1010
    AR_0805 --> AR_1014
    AR_0805 --> AR_1017
    AR_0805 --> AR_1025
    AR_0806 --> AR_0807
    AR_0806 --> AR_0809
    AR_0806 --> AR_0812
    AR_0806 --> AR_0817
    AR_0806 --> AR_0875
    AR_0806 --> AR_1010
    AR_0806 --> AR_1017
    AR_0806 --> AR_1025
    AR_0807 --> AR_0809
    AR_0807 --> AR_0823
    AR_0807 --> AR_0873
    AR_0807 --> AR_0903
    AR_0807 --> AR_1012
    AR_0808 --> AR_0810
    AR_0808 --> AR_0811
    AR_0809 --> AR_0810
    AR_0809 --> AR_0811
    AR_0810 --> AR_0811
    AR_0811 --> AR_0903
    AR_0812 --> AR_0807
    AR_0812 --> AR_0820
    AR_0812 --> AR_1033
    AR_0813 --> AR_0814
    AR_0813 --> AR_0818
    AR_0813 --> AR_1288
    AR_0814 --> AR_0815
    AR_0814 --> AR_0818
    AR_0815 --> AR_0816
    AR_0815 --> AR_0817
    AR_0815 --> AR_0818
    AR_0816 --> AR_0817
    AR_0816 --> AR_0818
    AR_0817 --> AR_0809
    AR_0817 --> AR_0818
    AR_0818 --> AR_0903
    AR_0819 --> AR_0809
    AR_0819 --> AR_0815
    AR_0819 --> AR_0816
    AR_0819 --> AR_0817
    AR_0819 --> AR_0818
    AR_0820 --> AR_0821
    AR_0820 --> AR_0822
    AR_0820 --> AR_1024
    AR_0821 --> AR_0808
    AR_0821 --> AR_0809
    AR_0821 --> AR_0822
    AR_0821 --> AR_0823
    AR_0821 --> AR_1024
    AR_0821 --> AR_1441
    AR_0822 --> AR_0808
    AR_0822 --> AR_0809
    AR_0822 --> AR_0823
    AR_0822 --> AR_1024
    AR_0822 --> AR_1441
    AR_0823 --> AR_0903
    AR_0823 --> AR_1027
    AR_0830 --> AR_0831
    AR_0830 --> AR_0832
    AR_0830 --> AR_0833
    AR_0830 --> AR_0834
    AR_0830 --> AR_0835
    AR_0830 --> AR_0836
    AR_0830 --> AR_1438
    AR_0831 --> AR_0832
    AR_0831 --> AR_0835
    AR_0831 --> AR_0836
    AR_0831 --> AR_0845
    AR_0832 --> AR_0833
    AR_0835 --> AR_0837
    AR_0836 --> AR_0837
    AR_0840 --> AR_0841
    AR_0840 --> AR_0842
    AR_0840 --> AR_0843
    AR_0840 --> AR_0844
    AR_0840 --> AR_1023
    AR_0841 --> AR_0842
    AR_0841 --> AR_0843
    AR_0841 --> AR_0844
    AR_0841 --> AR_1023
    AR_0842 --> AR_0844
    AR_0842 --> AR_1023
    AR_0843 --> AR_0844
    AR_0843 --> AR_1023
    AR_0844 --> AR_0870
    AR_0844 --> AR_1023
    AR_0845 --> AR_0846
    AR_0848 --> AR_0907
    AR_0851 --> AR_1017
    AR_0855 --> AR_0857
    AR_0855 --> AR_0863
    AR_0857 --> AR_0858
    AR_0857 --> AR_0880
    AR_0858 --> AR_0859
    AR_0859 --> AR_0860
    AR_0860 --> AR_0861
    AR_0861 --> AR_0862
    AR_0862 --> AR_0856
    AR_0863 --> AR_0864
    AR_0864 --> AR_0865
    AR_0865 --> AR_0866
    AR_0866 --> AR_0867
    AR_0867 --> AR_0868
    AR_0868 --> AR_0856
    AR_0869 --> AR_0870
    AR_0869 --> AR_0871
    AR_0869 --> AR_0872
    AR_0869 --> AR_0876
    AR_0869 --> AR_0893
    AR_0870 --> AR_0871
    AR_0870 --> AR_0872
    AR_0870 --> AR_0894
    AR_0870 --> AR_1011
    AR_0870 --> AR_1025
    AR_0871 --> AR_0872
    AR_0871 --> AR_0879
    AR_0871 --> AR_0893
    AR_0871 --> AR_1011
    AR_0871 --> AR_1025
    AR_0871 --> AR_1150
    AR_0872 --> AR_0808
    AR_0872 --> AR_0809
    AR_0872 --> AR_0873
    AR_0872 --> AR_0893
    AR_0872 --> AR_1028
    AR_0873 --> AR_0808
    AR_0873 --> AR_0809
    AR_0873 --> AR_0874
    AR_0873 --> AR_0894
    AR_0873 --> AR_1012
    AR_0874 --> AR_0808
    AR_0874 --> AR_0809
    AR_0875 --> AR_0908
    AR_0875 --> AR_1031
    AR_0875 --> AR_1035
    AR_0876 --> AR_1130
    AR_0877 --> AR_1021
    AR_0878 --> AR_0906
    AR_0879 --> AR_0888
    AR_0879 --> AR_0891
    AR_0888 --> AR_0889
    AR_0888 --> AR_0890
    AR_0888 --> AR_0896
    AR_0888 --> AR_1249
    AR_0888 --> AR_1250
    AR_0888 --> AR_1251
    AR_0889 --> AR_0890
    AR_0889 --> AR_0896
    AR_0889 --> AR_1249
    AR_0889 --> AR_1250
    AR_0889 --> AR_1251
    AR_0890 --> AR_0892
    AR_0890 --> AR_0893
    AR_0891 --> AR_0892
    AR_0891 --> AR_0893
    AR_0892 --> AR_0893
    AR_0893 --> AR_0894
    AR_0897 --> AR_0898
    AR_0897 --> AR_0903
    AR_0897 --> AR_1242
    AR_0897 --> AR_1264
    AR_0898 --> AR_0899
    AR_0898 --> AR_0903
    AR_0899 --> AR_0903
    AR_0901 --> AR_0877
    AR_0901 --> AR_0878
    AR_0901 --> AR_0903
    AR_0901 --> AR_0906
    AR_0902 --> AR_0813
    AR_0902 --> AR_0877
    AR_0902 --> AR_0878
    AR_0902 --> AR_0903
    AR_0902 --> AR_0906
    AR_0902 --> AR_0909
    AR_0903 --> AR_0846
    AR_0903 --> AR_1027
    AR_0904 --> AR_1023
    AR_0906 --> AR_0877
    AR_0906 --> AR_1021
    AR_0907 --> AR_1303
    AR_1001 --> AR_0310
    AR_1001 --> AR_0806
    AR_1001 --> AR_0875
    AR_1001 --> AR_0904
    AR_1001 --> AR_1006
    AR_1001 --> AR_1007
    AR_1001 --> AR_1013
    AR_1002 --> AR_0405
    AR_1002 --> AR_1016
    AR_1007 --> AR_0405
    AR_1007 --> AR_0406
    AR_1007 --> AR_1016
    AR_1007 --> AR_1394
    AR_1008 --> AR_0898
    AR_1010 --> AR_1011
    AR_1010 --> AR_1012
    AR_1010 --> AR_1024
    AR_1010 --> AR_1025
    AR_1010 --> AR_1033
    AR_1011 --> AR_0807
    AR_1011 --> AR_1012
    AR_1011 --> AR_1026
    AR_1012 --> AR_0823
    AR_1012 --> AR_0903
    AR_1012 --> AR_1027
    AR_1013 --> AR_1014
    AR_1013 --> AR_1015
    AR_1013 --> AR_1036
    AR_1014 --> AR_1011
    AR_1014 --> AR_1016
    AR_1014 --> AR_1032
    AR_1014 --> AR_1034
    AR_1015 --> AR_1016
    AR_1017 --> AR_1018
    AR_1017 --> AR_1019
    AR_1017 --> AR_1021
    AR_1017 --> AR_1022
    AR_1017 --> AR_1030
    AR_1018 --> AR_1019
    AR_1018 --> AR_1021
    AR_1018 --> AR_1022
    AR_1018 --> AR_1199
    AR_1018 --> AR_1498
    AR_1019 --> AR_1020
    AR_1019 --> AR_1021
    AR_1019 --> AR_1022
    AR_1019 --> AR_1199
    AR_1019 --> AR_1498
    AR_1020 --> AR_1021
    AR_1020 --> AR_1022
    AR_1020 --> AR_1199
    AR_1020 --> AR_1498
    AR_1021 --> AR_1022
    AR_1022 --> AR_1024
    AR_1022 --> AR_1025
    AR_1022 --> AR_1060
    AR_1023 --> AR_1024
    AR_1023 --> AR_1025
    AR_1023 --> AR_1036
    AR_1023 --> AR_1038
    AR_1023 --> AR_1060
    AR_1024 --> AR_1026
    AR_1024 --> AR_1029
    AR_1025 --> AR_1014
    AR_1025 --> AR_1026
    AR_1025 --> AR_1029
    AR_1025 --> AR_1031
    AR_1025 --> AR_1033
    AR_1025 --> AR_1034
    AR_1025 --> AR_1035
    AR_1026 --> AR_0807
    AR_1026 --> AR_0823
    AR_1026 --> AR_1027
    AR_1026 --> AR_1180
    AR_1029 --> AR_0903
    AR_1029 --> AR_1026
    AR_1030 --> AR_1010
    AR_1031 --> AR_1011
    AR_1031 --> AR_1032
    AR_1032 --> AR_1011
    AR_1033 --> AR_1011
    AR_1033 --> AR_1014
    AR_1033 --> AR_1031
    AR_1033 --> AR_1034
    AR_1033 --> AR_1035
    AR_1034 --> AR_1011
    AR_1034 --> AR_1032
    AR_1034 --> AR_1170
    AR_1035 --> AR_1011
    AR_1035 --> AR_1032
    AR_1036 --> AR_1014
    AR_1036 --> AR_1037
    AR_1037 --> AR_1014
    AR_1037 --> AR_1024
    AR_1037 --> AR_1025
    AR_1040 --> AR_1043
    AR_1045 --> AR_1051
    AR_1052 --> AR_1010
    AR_1054 --> AR_1010
    AR_1056 --> AR_1010
    AR_1058 --> AR_1010
    AR_1060 --> AR_1024
    AR_1060 --> AR_1025
    AR_1060 --> AR_1160
    AR_1060 --> AR_1227
    AR_1060 --> AR_1310
    AR_1061 --> AR_1010
    AR_1062 --> AR_1010
    AR_1062 --> AR_1058
    AR_1062 --> AR_1061
    AR_1100 --> AR_1120
    AR_1100 --> AR_1228
    AR_1100 --> AR_1230
    AR_1100 --> AR_1231
    AR_1100 --> AR_1232
    AR_1100 --> AR_1233
    AR_1100 --> AR_1234
    AR_1100 --> AR_1236
    AR_1100 --> AR_1238
    AR_1100 --> AR_1328
    AR_1110 --> AR_1130
    AR_1120 --> AR_1110
    AR_1130 --> AR_1140
    AR_1130 --> AR_1150
    AR_1140 --> AR_0808
    AR_1140 --> AR_0823
    AR_1140 --> AR_1180
    AR_1150 --> AR_1151
    AR_1151 --> AR_0808
    AR_1151 --> AR_1160
    AR_1151 --> AR_1227
    AR_1151 --> AR_1310
    AR_1151 --> AR_1496
    AR_1160 --> AR_1034
    AR_1160 --> AR_1170
    AR_1160 --> AR_1227
    AR_1170 --> AR_0807
    AR_1170 --> AR_0809
    AR_1170 --> AR_0823
    AR_1170 --> AR_0873
    AR_1170 --> AR_1011
    AR_1170 --> AR_1026
    AR_1170 --> AR_1031
    AR_1170 --> AR_1032
    AR_1170 --> AR_1035
    AR_1170 --> AR_1180
    AR_1180 --> AR_0809
    AR_1190 --> AR_1191
    AR_1190 --> AR_1198
    AR_1190 --> AR_1199
    AR_1190 --> AR_1299
    AR_1190 --> AR_1316
    AR_1190 --> AR_1498
    AR_1191 --> AR_1199
    AR_1191 --> AR_1316
    AR_1191 --> AR_1498
    AR_1200 --> AR_1226
    AR_1200 --> AR_1475
    AR_1200 --> AR_1476
    AR_1200 --> AR_1477
    AR_1210 --> AR_1211
    AR_1210 --> AR_1216
    AR_1211 --> AR_1212
    AR_1211 --> AR_1216
    AR_1212 --> AR_1213
    AR_1212 --> AR_1216
    AR_1213 --> AR_1214
    AR_1213 --> AR_1215
    AR_1213 --> AR_1216
    AR_1214 --> AR_1216
    AR_1215 --> AR_1216
    AR_1226 --> AR_1337
    AR_1228 --> AR_1120
    AR_1228 --> AR_1229
    AR_1229 --> AR_1120
    AR_1230 --> AR_1120
    AR_1230 --> AR_1228
    AR_1230 --> AR_1229
    AR_1230 --> AR_1231
    AR_1230 --> AR_1232
    AR_1231 --> AR_1151
    AR_1231 --> AR_1233
    AR_1231 --> AR_1234
    AR_1231 --> AR_1236
    AR_1231 --> AR_1238
    AR_1231 --> AR_1248
    AR_1232 --> AR_1151
    AR_1232 --> AR_1244
    AR_1232 --> AR_1248
    AR_1233 --> AR_1232
    AR_1233 --> AR_1237
    AR_1233 --> AR_1257
    AR_1234 --> AR_1232
    AR_1236 --> AR_1233
    AR_1236 --> AR_1234
    AR_1236 --> AR_1237
    AR_1236 --> AR_1239
    AR_1237 --> AR_1232
    AR_1237 --> AR_1260
    AR_1237 --> AR_1261
    AR_1237 --> AR_1262
    AR_1237 --> AR_1265
    AR_1237 --> AR_1266
    AR_1237 --> AR_1267
    AR_1237 --> AR_1268
    AR_1237 --> AR_1269
    AR_1237 --> AR_1270
    AR_1237 --> AR_1271
    AR_1237 --> AR_1272
    AR_1237 --> AR_1273
    AR_1237 --> AR_1274
    AR_1237 --> AR_1275
    AR_1237 --> AR_1276
    AR_1237 --> AR_1277
    AR_1237 --> AR_1278
    AR_1237 --> AR_1279
    AR_1237 --> AR_1280
    AR_1237 --> AR_1281
    AR_1237 --> AR_1282
    AR_1237 --> AR_1284
    AR_1237 --> AR_1285
    AR_1237 --> AR_1286
    AR_1238 --> AR_1236
    AR_1238 --> AR_1240
    AR_1238 --> AR_1260
    AR_1238 --> AR_1261
    AR_1238 --> AR_1262
    AR_1238 --> AR_1263
    AR_1238 --> AR_1265
    AR_1238 --> AR_1266
    AR_1238 --> AR_1267
    AR_1238 --> AR_1268
    AR_1238 --> AR_1269
    AR_1238 --> AR_1270
    AR_1238 --> AR_1271
    AR_1238 --> AR_1272
    AR_1238 --> AR_1273
    AR_1238 --> AR_1274
    AR_1238 --> AR_1275
    AR_1238 --> AR_1276
    AR_1238 --> AR_1277
    AR_1238 --> AR_1278
    AR_1238 --> AR_1279
    AR_1238 --> AR_1280
    AR_1238 --> AR_1281
    AR_1238 --> AR_1282
    AR_1238 --> AR_1284
    AR_1238 --> AR_1285
    AR_1238 --> AR_1286
    AR_1239 --> AR_1240
    AR_1239 --> AR_1243
    AR_1239 --> AR_1260
    AR_1239 --> AR_1261
    AR_1239 --> AR_1262
    AR_1239 --> AR_1265
    AR_1239 --> AR_1266
    AR_1239 --> AR_1267
    AR_1239 --> AR_1268
    AR_1239 --> AR_1269
    AR_1239 --> AR_1270
    AR_1239 --> AR_1271
    AR_1239 --> AR_1272
    AR_1239 --> AR_1273
    AR_1239 --> AR_1274
    AR_1239 --> AR_1275
    AR_1239 --> AR_1276
    AR_1239 --> AR_1277
    AR_1239 --> AR_1278
    AR_1239 --> AR_1279
    AR_1239 --> AR_1280
    AR_1239 --> AR_1281
    AR_1239 --> AR_1282
    AR_1239 --> AR_1284
    AR_1239 --> AR_1285
    AR_1239 --> AR_1286
    AR_1240 --> AR_1241
    AR_1240 --> AR_1243
    AR_1241 --> AR_1243
    AR_1242 --> AR_1245
    AR_1242 --> AR_1246
    AR_1242 --> AR_1247
    AR_1242 --> AR_1259
    AR_1243 --> AR_1245
    AR_1245 --> AR_1246
    AR_1250 --> AR_1257
    AR_1251 --> AR_1257
    AR_1252 --> AR_1253
    AR_1252 --> AR_1254
    AR_1252 --> AR_1256
    AR_1252 --> AR_1303
    AR_1253 --> AR_1254
    AR_1253 --> AR_1255
    AR_1253 --> AR_1256
    AR_1254 --> AR_1255
    AR_1282 --> AR_1284
    AR_1282 --> AR_1285
    AR_1282 --> AR_1286
    AR_1282 --> AR_1300
    AR_1285 --> AR_1286
    AR_1285 --> AR_1300
    AR_1287 --> AR_1301
    AR_1287 --> AR_1306
    AR_1288 --> AR_1370
    AR_1288 --> AR_1371
    AR_1288 --> AR_1377
    AR_1288 --> AR_1468
    AR_1300 --> AR_1301
    AR_1300 --> AR_1306
    AR_1302 --> AR_1304
    AR_1302 --> AR_1305
    AR_1302 --> AR_1307
    AR_1302 --> AR_1515
    AR_1304 --> AR_1308
    AR_1304 --> AR_1516
    AR_1304 --> AR_1517
    AR_1304 --> AR_1519
    AR_1307 --> AR_1309
    AR_1308 --> AR_1309
    AR_1310 --> AR_1316
    AR_1310 --> AR_1319
    AR_1314 --> AR_1315
    AR_1314 --> AR_1495
    AR_1316 --> AR_1320
    AR_1316 --> AR_1422
    AR_1316 --> AR_1442
    AR_1319 --> AR_1316
    AR_1325 --> AR_1326
    AR_1325 --> AR_1327
    AR_1325 --> AR_1328
    AR_1326 --> AR_1327
    AR_1326 --> AR_1328
    AR_1327 --> AR_1329
    AR_1327 --> AR_1334
    AR_1327 --> AR_1342
    AR_1327 --> AR_1343
    AR_1327 --> AR_1346
    AR_1327 --> AR_1347
    AR_1327 --> AR_1348
    AR_1327 --> AR_1349
    AR_1327 --> AR_1432
    AR_1327 --> AR_1433
    AR_1328 --> AR_1329
    AR_1328 --> AR_1334
    AR_1328 --> AR_1339
    AR_1328 --> AR_1342
    AR_1328 --> AR_1343
    AR_1328 --> AR_1346
    AR_1328 --> AR_1347
    AR_1328 --> AR_1348
    AR_1328 --> AR_1349
    AR_1328 --> AR_1350
    AR_1328 --> AR_1367
    AR_1328 --> AR_1368
    AR_1328 --> AR_1374
    AR_1328 --> AR_1432
    AR_1328 --> AR_1433
    AR_1328 --> AR_1436
    AR_1328 --> AR_1437
    AR_1328 --> AR_1440
    AR_1328 --> AR_1442
    AR_1328 --> AR_1699
    AR_1329 --> AR_1330
    AR_1329 --> AR_1333
    AR_1329 --> AR_1700
    AR_1330 --> AR_1463
    AR_1330 --> AR_1496
    AR_1331 --> AR_1332
    AR_1331 --> AR_1338
    AR_1332 --> AR_1333
    AR_1332 --> AR_1456
    AR_1333 --> AR_1335
    AR_1333 --> AR_1336
    AR_1333 --> AR_1420
    AR_1334 --> AR_1335
    AR_1334 --> AR_1336
    AR_1335 --> AR_1336
    AR_1336 --> AR_1725
    AR_1337 --> AR_1397
    AR_1337 --> AR_1398
    AR_1338 --> AR_1526
    AR_1338 --> AR_1725
    AR_1338 --> AR_1757
    AR_1339 --> AR_1340
    AR_1339 --> AR_1341
    AR_1339 --> AR_1342
    AR_1339 --> AR_1343
    AR_1339 --> AR_1344
    AR_1339 --> AR_1345
    AR_1339 --> AR_1346
    AR_1339 --> AR_1347
    AR_1339 --> AR_1348
    AR_1339 --> AR_1349
    AR_1339 --> AR_1350
    AR_1339 --> AR_1351
    AR_1339 --> AR_1367
    AR_1339 --> AR_1368
    AR_1339 --> AR_1374
    AR_1339 --> AR_1390
    AR_1339 --> AR_1391
    AR_1339 --> AR_1392
    AR_1339 --> AR_1393
    AR_1340 --> AR_1329
    AR_1340 --> AR_1342
    AR_1340 --> AR_1343
    AR_1340 --> AR_1344
    AR_1340 --> AR_1345
    AR_1340 --> AR_1346
    AR_1340 --> AR_1347
    AR_1340 --> AR_1348
    AR_1340 --> AR_1349
    AR_1340 --> AR_1350
    AR_1340 --> AR_1351
    AR_1340 --> AR_1367
    AR_1340 --> AR_1368
    AR_1340 --> AR_1374
    AR_1340 --> AR_1390
    AR_1340 --> AR_1391
    AR_1340 --> AR_1392
    AR_1340 --> AR_1393
    AR_1341 --> AR_1390
    AR_1341 --> AR_1391
    AR_1341 --> AR_1392
    AR_1341 --> AR_1393
    AR_1341 --> AR_1432
    AR_1341 --> AR_1433
    AR_1341 --> AR_1434
    AR_1341 --> AR_1451
    AR_1342 --> AR_1344
    AR_1342 --> AR_1345
    AR_1342 --> AR_1390
    AR_1342 --> AR_1391
    AR_1342 --> AR_1392
    AR_1342 --> AR_1393
    AR_1342 --> AR_1432
    AR_1342 --> AR_1433
    AR_1342 --> AR_1434
    AR_1347 --> AR_1349
    AR_1347 --> AR_1350
    AR_1347 --> AR_1351
    AR_1350 --> AR_1349
    AR_1350 --> AR_1351
    AR_1351 --> AR_1352
    AR_1352 --> AR_1353
    AR_1352 --> AR_1354
    AR_1352 --> AR_1355
    AR_1352 --> AR_1356
    AR_1356 --> AR_1357
    AR_1357 --> AR_1358
    AR_1357 --> AR_1359
    AR_1357 --> AR_1451
    AR_1357 --> AR_1452
    AR_1357 --> AR_1470
    AR_1357 --> AR_1471
    AR_1359 --> AR_1360
    AR_1359 --> AR_1361
    AR_1359 --> AR_1362
    AR_1359 --> AR_1470
    AR_1359 --> AR_1471
    AR_1362 --> AR_1363
    AR_1362 --> AR_1364
    AR_1362 --> AR_1365
    AR_1362 --> AR_1366
    AR_1362 --> AR_1369
    AR_1362 --> AR_1376
    AR_1362 --> AR_1378
    AR_1362 --> AR_1379
    AR_1362 --> AR_1380
    AR_1362 --> AR_1381
    AR_1362 --> AR_1468
    AR_1362 --> AR_1470
    AR_1362 --> AR_1471
    AR_1362 --> AR_1474
    AR_1363 --> AR_1472
    AR_1364 --> AR_1365
    AR_1364 --> AR_1366
    AR_1364 --> AR_1369
    AR_1364 --> AR_1376
    AR_1364 --> AR_1377
    AR_1364 --> AR_1378
    AR_1364 --> AR_1379
    AR_1364 --> AR_1380
    AR_1364 --> AR_1381
    AR_1364 --> AR_1468
    AR_1365 --> AR_1366
    AR_1365 --> AR_1373
    AR_1366 --> AR_1367
    AR_1366 --> AR_1368
    AR_1366 --> AR_1369
    AR_1366 --> AR_1373
    AR_1366 --> AR_1376
    AR_1366 --> AR_1378
    AR_1366 --> AR_1379
    AR_1366 --> AR_1380
    AR_1366 --> AR_1381
    AR_1366 --> AR_1390
    AR_1366 --> AR_1391
    AR_1366 --> AR_1392
    AR_1366 --> AR_1393
    AR_1366 --> AR_1468
    AR_1369 --> AR_1370
    AR_1371 --> AR_1373
    AR_1373 --> AR_1374
    AR_1373 --> AR_1375
    AR_1373 --> AR_1376
    AR_1373 --> AR_1377
    AR_1373 --> AR_1381
    AR_1373 --> AR_1382
    AR_1373 --> AR_1383
    AR_1373 --> AR_1384
    AR_1373 --> AR_1385
    AR_1373 --> AR_1390
    AR_1373 --> AR_1391
    AR_1373 --> AR_1392
    AR_1373 --> AR_1393
    AR_1373 --> AR_1472
    AR_1373 --> AR_1524
    AR_1374 --> AR_1375
    AR_1377 --> AR_1378
    AR_1377 --> AR_1379
    AR_1377 --> AR_1380
    AR_1377 --> AR_1381
    AR_1377 --> AR_1382
    AR_1377 --> AR_1383
    AR_1377 --> AR_1384
    AR_1377 --> AR_1385
    AR_1377 --> AR_1386
    AR_1377 --> AR_1387
    AR_1377 --> AR_1388
    AR_1378 --> AR_1379
    AR_1378 --> AR_1380
    AR_1378 --> AR_1381
    AR_1378 --> AR_1382
    AR_1378 --> AR_1386
    AR_1378 --> AR_1387
    AR_1378 --> AR_1388
    AR_1379 --> AR_1473
    AR_1379 --> AR_1474
    AR_1379 --> AR_1475
    AR_1379 --> AR_1476
    AR_1379 --> AR_1477
    AR_1379 --> AR_1478
    AR_1380 --> AR_1381
    AR_1380 --> AR_1382
    AR_1380 --> AR_1383
    AR_1380 --> AR_1384
    AR_1380 --> AR_1385
    AR_1380 --> AR_1386
    AR_1381 --> AR_1382
    AR_1381 --> AR_1383
    AR_1381 --> AR_1384
    AR_1381 --> AR_1385
    AR_1381 --> AR_1386
    AR_1383 --> AR_1384
    AR_1384 --> AR_1385
    AR_1384 --> AR_1386
    AR_1384 --> AR_1387
    AR_1384 --> AR_1388
    AR_1384 --> AR_1389
    AR_1385 --> AR_1386
    AR_1385 --> AR_1387
    AR_1385 --> AR_1388
    AR_1385 --> AR_1390
    AR_1385 --> AR_1391
    AR_1385 --> AR_1392
    AR_1385 --> AR_1393
    AR_1385 --> AR_1432
    AR_1385 --> AR_1433
    AR_1385 --> AR_1434
    AR_1388 --> AR_1390
    AR_1388 --> AR_1391
    AR_1388 --> AR_1392
    AR_1388 --> AR_1393
    AR_1388 --> AR_1432
    AR_1388 --> AR_1433
    AR_1388 --> AR_1434
    AR_1393 --> AR_1432
    AR_1393 --> AR_1433
    AR_1393 --> AR_1434
    AR_1394 --> AR_1395
    AR_1394 --> AR_1399
    AR_1395 --> AR_1396
    AR_1395 --> AR_1401
    AR_1396 --> AR_1400
    AR_1397 --> AR_1495
    AR_1398 --> AR_1421
    AR_1399 --> AR_1396
    AR_1399 --> AR_1400
    AR_1399 --> AR_1408
    AR_1400 --> AR_1401
    AR_1400 --> AR_1404
    AR_1400 --> AR_1408
    AR_1401 --> AR_1402
    AR_1401 --> AR_1409
    AR_1401 --> AR_1411
    AR_1401 --> AR_1412
    AR_1401 --> AR_1413
    AR_1401 --> AR_1416
    AR_1402 --> AR_1403
    AR_1402 --> AR_1404
    AR_1402 --> AR_1410
    AR_1402 --> AR_1416
    AR_1403 --> AR_1423
    AR_1404 --> AR_1410
    AR_1405 --> AR_1406
    AR_1405 --> AR_1407
    AR_1406 --> AR_1414
    AR_1408 --> AR_1409
    AR_1408 --> AR_1411
    AR_1408 --> AR_1412
    AR_1408 --> AR_1413
    AR_1408 --> AR_1417
    AR_1408 --> AR_1418
    AR_1409 --> AR_1410
    AR_1410 --> AR_1415
    AR_1411 --> AR_1410
    AR_1412 --> AR_1410
    AR_1413 --> AR_1410
    AR_1414 --> AR_1415
    AR_1415 --> AR_1416
    AR_1415 --> AR_1423
    AR_1416 --> AR_1417
    AR_1416 --> AR_1418
    AR_1416 --> AR_1421
    AR_1416 --> AR_1424
    AR_1416 --> AR_1430
    AR_1417 --> AR_1419
    AR_1417 --> AR_1420
    AR_1417 --> AR_1425
    AR_1418 --> AR_1419
    AR_1418 --> AR_1420
    AR_1418 --> AR_1425
    AR_1419 --> AR_1420
    AR_1419 --> AR_1423
    AR_1420 --> AR_1424
    AR_1421 --> AR_1427
    AR_1423 --> AR_1424
    AR_1423 --> AR_1426
    AR_1423 --> AR_1430
    AR_1424 --> AR_1425
    AR_1425 --> AR_1426
    AR_1427 --> AR_1431
    AR_1427 --> AR_1722
    AR_1427 --> AR_1746
    AR_1427 --> AR_1750
    AR_1430 --> AR_1424
    AR_1431 --> AR_1722
    AR_1431 --> AR_1746
    AR_1431 --> AR_1750
    AR_1432 --> AR_1699
    AR_1433 --> AR_1446
    AR_1433 --> AR_1447
    AR_1433 --> AR_1451
    AR_1433 --> AR_1452
    AR_1433 --> AR_1456
    AR_1433 --> AR_1496
    AR_1433 --> AR_1700
    AR_1434 --> AR_1435
    AR_1435 --> AR_1436
    AR_1436 --> AR_1437
    AR_1436 --> AR_1440
    AR_1436 --> AR_1442
    AR_1437 --> AR_1440
    AR_1437 --> AR_1443
    AR_1437 --> AR_1447
    AR_1441 --> AR_1442
    AR_1441 --> AR_1446
    AR_1441 --> AR_1488
    AR_1442 --> AR_1338
    AR_1442 --> AR_1443
    AR_1442 --> AR_1446
    AR_1442 --> AR_1447
    AR_1442 --> AR_1488
    AR_1442 --> AR_1499
    AR_1443 --> AR_1331
    AR_1443 --> AR_1338
    AR_1443 --> AR_1444
    AR_1443 --> AR_1446
    AR_1443 --> AR_1448
    AR_1443 --> AR_1449
    AR_1443 --> AR_1500
    AR_1446 --> AR_1331
    AR_1446 --> AR_1338
    AR_1446 --> AR_1448
    AR_1446 --> AR_1458
    AR_1446 --> AR_1487
    AR_1447 --> AR_1443
    AR_1447 --> AR_1456
    AR_1447 --> AR_1496
    AR_1448 --> AR_1449
    AR_1448 --> AR_1450
    AR_1448 --> AR_1451
    AR_1448 --> AR_1452
    AR_1448 --> AR_1455
    AR_1450 --> AR_1455
    AR_1450 --> AR_1487
    AR_1450 --> AR_1488
    AR_1450 --> AR_1496
    AR_1451 --> AR_1452
    AR_1451 --> AR_1454
    AR_1452 --> AR_1453
    AR_1452 --> AR_1454
    AR_1453 --> AR_1455
    AR_1453 --> AR_1457
    AR_1453 --> AR_1458
    AR_1453 --> AR_1523
    AR_1453 --> AR_1524
    AR_1453 --> AR_1525
    AR_1453 --> AR_1526
    AR_1455 --> AR_1487
    AR_1455 --> AR_1488
    AR_1455 --> AR_1496
    AR_1455 --> AR_1526
    AR_1456 --> AR_1333
    AR_1456 --> AR_1458
    AR_1456 --> AR_1460
    AR_1456 --> AR_1461
    AR_1456 --> AR_1526
    AR_1457 --> AR_1459
    AR_1458 --> AR_1460
    AR_1460 --> AR_1461
    AR_1460 --> AR_1462
    AR_1461 --> AR_1463
    AR_1461 --> AR_1489
    AR_1461 --> AR_1490
    AR_1461 --> AR_1491
    AR_1461 --> AR_1492
    AR_1461 --> AR_1493
    AR_1462 --> AR_1489
    AR_1462 --> AR_1490
    AR_1462 --> AR_1491
    AR_1462 --> AR_1492
    AR_1462 --> AR_1493
    AR_1471 --> AR_1473
    AR_1471 --> AR_1474
    AR_1472 --> AR_1473
    AR_1472 --> AR_1474
    AR_1472 --> AR_1475
    AR_1472 --> AR_1476
    AR_1472 --> AR_1477
    AR_1472 --> AR_1480
    AR_1472 --> AR_1481
    AR_1472 --> AR_1482
    AR_1472 --> AR_1483
    AR_1472 --> AR_1484
    AR_1472 --> AR_1485
    AR_1473 --> AR_1480
    AR_1473 --> AR_1481
    AR_1473 --> AR_1482
    AR_1473 --> AR_1483
    AR_1473 --> AR_1484
    AR_1473 --> AR_1485
    AR_1473 --> AR_1502
    AR_1473 --> AR_1503
    AR_1473 --> AR_1504
    AR_1473 --> AR_1505
    AR_1473 --> AR_1506
    AR_1473 --> AR_1507
    AR_1473 --> AR_1508
    AR_1473 --> AR_1509
    AR_1474 --> AR_1502
    AR_1474 --> AR_1503
    AR_1474 --> AR_1504
    AR_1474 --> AR_1505
    AR_1474 --> AR_1506
    AR_1474 --> AR_1507
    AR_1474 --> AR_1508
    AR_1474 --> AR_1509
    AR_1475 --> AR_1478
    AR_1476 --> AR_1478
    AR_1480 --> AR_1481
    AR_1480 --> AR_1482
    AR_1480 --> AR_1483
    AR_1480 --> AR_1484
    AR_1480 --> AR_1485
    AR_1480 --> AR_1486
    AR_1480 --> AR_1502
    AR_1480 --> AR_1503
    AR_1480 --> AR_1504
    AR_1480 --> AR_1505
    AR_1480 --> AR_1506
    AR_1480 --> AR_1507
    AR_1480 --> AR_1508
    AR_1480 --> AR_1509
    AR_1484 --> AR_1485
    AR_1484 --> AR_1486
    AR_1484 --> AR_1503
    AR_1484 --> AR_1504
    AR_1484 --> AR_1505
    AR_1484 --> AR_1506
    AR_1484 --> AR_1507
    AR_1484 --> AR_1508
    AR_1484 --> AR_1509
    AR_1484 --> AR_1511
    AR_1484 --> AR_1512
    AR_1484 --> AR_1513
    AR_1485 --> AR_1486
    AR_1485 --> AR_1503
    AR_1485 --> AR_1504
    AR_1485 --> AR_1505
    AR_1485 --> AR_1506
    AR_1485 --> AR_1507
    AR_1485 --> AR_1508
    AR_1485 --> AR_1509
    AR_1486 --> AR_1487
    AR_1487 --> AR_1488
    AR_1488 --> AR_1489
    AR_1488 --> AR_1490
    AR_1488 --> AR_1491
    AR_1489 --> AR_1490
    AR_1489 --> AR_1491
    AR_1491 --> AR_1492
    AR_1491 --> AR_1493
    AR_1491 --> AR_1495
    AR_1492 --> AR_1493
    AR_1493 --> AR_1495
    AR_1493 --> AR_1497
    AR_1496 --> AR_1199
    AR_1496 --> AR_1498
    AR_1496 --> AR_1499
    AR_1498 --> AR_1199
    AR_1499 --> AR_1500
    AR_1499 --> AR_1501
    AR_1499 --> AR_1514
    AR_1500 --> AR_1501
    AR_1500 --> AR_1514
    AR_1501 --> AR_1502
    AR_1502 --> AR_1503
    AR_1502 --> AR_1504
    AR_1502 --> AR_1505
    AR_1502 --> AR_1506
    AR_1502 --> AR_1507
    AR_1502 --> AR_1508
    AR_1502 --> AR_1509
    AR_1502 --> AR_1511
    AR_1502 --> AR_1512
    AR_1502 --> AR_1513
    AR_1505 --> AR_1506
    AR_1505 --> AR_1507
    AR_1505 --> AR_1508
    AR_1505 --> AR_1509
    AR_1505 --> AR_1510
    AR_1505 --> AR_1523
    AR_1505 --> AR_1525
    AR_1505 --> AR_1551
    AR_1513 --> AR_1523
    AR_1513 --> AR_1551
    AR_1514 --> AR_1523
    AR_1514 --> AR_1526
    AR_1514 --> AR_1551
    AR_1517 --> AR_1518
    AR_1517 --> AR_1529
    AR_1519 --> AR_1520
    AR_1519 --> AR_1528
    AR_1520 --> AR_1521
    AR_1520 --> AR_1526
    AR_1520 --> AR_1528
    AR_1520 --> AR_1529
    AR_1520 --> AR_1530
    AR_1520 --> AR_1531
    AR_1527 --> AR_1528
    AR_1528 --> AR_1532
    AR_1528 --> AR_1533
    AR_1529 --> AR_1530
    AR_1530 --> AR_1521
    AR_1530 --> AR_1522
    AR_1530 --> AR_1531
    AR_1530 --> AR_1534
    AR_1530 --> AR_1537
    AR_1530 --> AR_1538
    AR_1530 --> AR_1539
    AR_1530 --> AR_1540
    AR_1530 --> AR_1541
    AR_1530 --> AR_1544
    AR_1531 --> AR_1546
    AR_1532 --> AR_1535
    AR_1532 --> AR_1542
    AR_1533 --> AR_1536
    AR_1533 --> AR_1543
    AR_1534 --> AR_1535
    AR_1534 --> AR_1536
    AR_1534 --> AR_1542
    AR_1534 --> AR_1543
    AR_1535 --> AR_1545
    AR_1536 --> AR_1546
    AR_1540 --> AR_1542
    AR_1540 --> AR_1543
    AR_1541 --> AR_1542
    AR_1541 --> AR_1543
    AR_1542 --> AR_1535
    AR_1543 --> AR_1536
    AR_1545 --> AR_1522
    AR_1546 --> AR_1522
    AR_1547 --> AR_1548
    AR_1547 --> AR_1549
    AR_1549 --> AR_1542
    AR_1549 --> AR_1543
    AR_1549 --> AR_1550
    AR_1552 --> AR_1553
    AR_1552 --> AR_1555
    AR_1553 --> AR_1555
    AR_1554 --> AR_1555
    AR_1554 --> AR_1559
    AR_1555 --> AR_1556
    AR_1555 --> AR_1558
    AR_1555 --> AR_1757
    AR_1557 --> AR_1558
    AR_1562 --> AR_1563
    AR_1562 --> AR_1564
    AR_1562 --> AR_1653
    AR_1562 --> AR_1658
    AR_1563 --> AR_1564
    AR_1563 --> AR_1567
    AR_1563 --> AR_1599
    AR_1563 --> AR_1631
    AR_1563 --> AR_1653
    AR_1563 --> AR_1658
    AR_1564 --> AR_1566
    AR_1564 --> AR_1568
    AR_1564 --> AR_1588
    AR_1564 --> AR_1599
    AR_1564 --> AR_1631
    AR_1564 --> AR_1653
    AR_1567 --> AR_1572
    AR_1567 --> AR_1634
    AR_1568 --> AR_1569
    AR_1568 --> AR_1570
    AR_1568 --> AR_1588
    AR_1568 --> AR_1599
    AR_1570 --> AR_1571
    AR_1570 --> AR_1573
    AR_1573 --> AR_1574
    AR_1573 --> AR_1576
    AR_1574 --> AR_1577
    AR_1576 --> AR_1588
    AR_1576 --> AR_1590
    AR_1576 --> AR_1592
    AR_1576 --> AR_1594
    AR_1588 --> AR_1589
    AR_1588 --> AR_1598
    AR_1588 --> AR_1599
    AR_1588 --> AR_1631
    AR_1589 --> AR_1591
    AR_1589 --> AR_1598
    AR_1590 --> AR_1591
    AR_1590 --> AR_1596
    AR_1590 --> AR_1727
    AR_1591 --> AR_1598
    AR_1591 --> AR_1606
    AR_1592 --> AR_1590
    AR_1592 --> AR_1593
    AR_1592 --> AR_1595
    AR_1593 --> AR_1590
    AR_1593 --> AR_1595
    AR_1594 --> AR_1590
    AR_1595 --> AR_1596
    AR_1595 --> AR_1602
    AR_1595 --> AR_1607
    AR_1596 --> AR_1597
    AR_1596 --> AR_1602
    AR_1597 --> AR_1598
    AR_1597 --> AR_1600
    AR_1597 --> AR_1718
    AR_1598 --> AR_1603
    AR_1599 --> AR_1600
    AR_1599 --> AR_1601
    AR_1599 --> AR_1611
    AR_1600 --> AR_1601
    AR_1600 --> AR_1611
    AR_1601 --> AR_1603
    AR_1601 --> AR_1607
