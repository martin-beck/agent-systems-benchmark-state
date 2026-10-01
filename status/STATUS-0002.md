<!-- This page is generated; the root STATUS.md index links the complete view. -->

| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Deliver the runtime-owned strict-replay launch authority required by the replay CLI contract. |
| Next action | Done via successor AR-1448: runtime-owned replay authority source merged and post-merge verified at f03d9e484d6ca73eacdbd5476980bf33ca737540. Preserve strict CLI-only fail-closed behavior and keep optional live capture AR-1330 separate. |

### AR-1332 — Record-live to replay-offline workflow

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the record-live then replay-offline end-to-end CLI workflow. |
| Next action | Monitor seven exact-main post-merge workflows for merge SHA ad4f96ab3f7e57916208406b2f56aa9ec4e54885; release only after all are green and post-merge verification is durable. |

### AR-1333 — Multi-agent by workload benchmark campaign

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run the multi-agent by workload benchmark campaign with per-tuple evidence and offline replay. |
| Next action | Keep AR-1333 as the optional production/live campaign successor; implement the mandatory credential-free local/mock campaign through AR-1456 and do not wait on AR-1329 for local qualification. |

### AR-1334 — OpenRouter free-model conformance and hostile qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the pinned OpenRouter free model under conformance and hostile fail-closed testing. |
| Next action | No further action; merged PR #255 and its exact qualification evidence are recorded. |

### AR-1335 — Credential-free CI stage for the benchmark path

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the required credential-free CI stage for the complete benchmark path. |
| Next action | Reconcile and doctor state; release AR-1335 done with PR, rerun, and eight post-merge workflow evidence. |

### AR-1336 — Live benchmark workflow documentation and support matrix

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Document the live benchmark workflow and publish the supported agent and provider matrix. |
| Next action | All eight post-merge workflows green; release AR-1336 done and reconcile/doctor. |

### AR-1337 — Repair protected-main merge-tree admission after OpenRouter merge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the protected-main merge-tree admission defect exposed after the OpenRouter provider merge. |
| Next action | Await remaining PR #252 exact-head checks and independent review; then merge only via signed integration procedure at the current protected target and verify post-merge workflows. |

### AR-1338 — Guided ASB command wrapper

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a catalog-driven friendly wrapper for setup, selection and benchmark workflows. |
| Next action | Run state reconcile and live doctor, then release AR-1338 done with exact post-merge workflow evidence. |

### AR-1339 — Runtime-owned live-provider egress backend

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the runtime-owned authenticated backend for explicit live provider egress. |
| Next action | AR-1339 backend merged and verified at protected main; AR-1340 owns namespace-bound child handoff and AR-1329 consumes it for final live CLI integration. |

### AR-1340 — Attested live-relay namespace and child handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bind the live provider relay to an attested child namespace and integrate it without weakening offline or replay denial. |
| Next action | SECURITY HOLD: AR-1341 must add runtime-observed child namespace attestation and copied/stale/mismatch denial before AR-1340 may be released or AR-1329 advanced. Do not release on green post-merge CI alone; continue collecting post-merge evidence for merge 3406faae. |

### AR-1341 — Runtime-observed namespace attestation repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair AR-1340 so live relay capabilities require runtime-observed child namespace agreement. |
| Next action | Monitor post-merge workflows for merge 2774b1d648b5c3bbda0e290e158dc352502d3768; after all seven exact-head workflows are green, release AR-1341 done with evidence and update AR-1340 security-hold transition. |

### AR-1342 — Runtime-owned live relay factory and CLI integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Create the runtime-owned relay factory and opaque launch context required for safe live CLI execution. |
| Next action | PR #259 merged at d24221731891fb39f56118be9c5ae51364824517; monitor all seven exact-head post-merge workflows and release AR-1342 done only after every one is green, then promote/advance AR-1329. |

### AR-1343 — Runtime live-provider relay service and CLI acquisition

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the runtime live-provider relay service and per-attempt opaque factory acquisition required by asb run and sweep. |
| Next action | BLOCKED on concrete missing primitives: asb-runtime has no production supervisor constructor for pinned SandboxBackend/live gate and no runtime-owned target/namespace provisioning; asb-agents ResolvedCredential transport is crate-private and cannot safely cross into runtime; no CLI service can acquire lease, credential, target, namespace, token, and relay atomically. Keep AR-1329 fail-closed. Coordinator must promote a narrowly scoped cross-crate runtime provisioning repair before AR-1343 can proceed. |

### AR-1344 — Runtime-owned CLI live acquisition contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the runtime-owned API and CLI integration needed for safe live-provider attempts. |
| Next action | Exact uncovered-line classification recorded: launch_factory misses include replay backend/authority alternate branches and LiveProviderAttempt lifecycle paths; live_relay misses are error conversion/display plus handoff/forwarding deadline branches; provider_egress misses are address-policy edge branches and relay timeout/error paths; live_namespace misses are gate/runtime observation and rebind branches; sandbox misses are live attestation/spawn/ownership teardown branches. Reachable negative/accessor branches have been covered; remaining live/sandbox branches are capability-gated or require a broad dedicated repair AR. Do not exclude files or weaken 90&#37;; PR remains unmergeable. |

### AR-1345 — Runtime live-provider coverage repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair runtime live-provider coverage without weakening the mandatory quality floor. |
| Next action | Monitor all seven post-merge workflows for exact SHA a336d6744b1a82f36a706ec606b847c92d49cfd3; release ARs only after all terminal success. |

### AR-1346 — Runtime supervisor provisioning boundary

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the production runtime supervisor boundary needed for safe live-provider CLI acquisition. |
| Next action | Cross-crate audit found the safe boundary is not yet implemented: asb-runtime cannot depend on asb-agents because asb-agents already depends on runtime; ResolvedCredential transport bytes are crate-private, while SandboxBackend::spawn_launch constructs the child command internally. Implement a new supervisor-owned composition boundary (likely dedicated crate or runtime credential injection trait) that keeps secret bytes opaque, then add CLI wiring/tests. Do not expose bytes or bypass NetworkPolicy::Deny. |

### AR-1347 — Neutral live-supervisor composition contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the dependency-safe opaque supervisor contract needed for live-provider acquisition. |
| Next action | BLOCKED pending successor runtime-acquisition AR: neutral credential injection is complete, but no production supervisor owns pinned SandboxBackend/live gate discovery, benchmark ResourceLease acquisition, concrete provider target DNS/allowlist, namespace handoff/rebind, launch token, or per-attempt relay. Existing LiveLaunchFactory::acquire requires caller-built authority inputs and cannot be wired safely. Keep AR-1329 fail-closed. |

### AR-1348 — Runtime-owned live acquisition service

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the runtime-owned supervisor that acquires every live-provider authority and tears it down safely. |
| Next action | Audit is complete and AR-1348 remains in_progress only as the verified lifecycle slice. Exact missing authority: no production-owned coordinator can resolve enrolled provider policy/credential, create NetworkPolicy::Deny SandboxLaunchInput, acquire benchmark ResourceLease, observe child NamespaceIdentity, issue launch token, construct LiveProviderNamespaceHandoff and LiveProviderRelay, and invoke asb-cli per attempt. CLI exposes only injected LiveProviderAttemptFactory seams; LiveLaunchFactory and RuntimeLiveBinding accept caller-built authority. Recommend coordinator create a narrowly scoped successor AR for LiveProviderRuntimeService atomic acquisition and CLI wiring; do not add a callback wrapper or synthetic authority. AR-1329 remains fail-closed. |

### AR-1349 — Production live-provider runtime service

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement production-owned atomic live-provider acquisition and wire it into asb run and sweep. |
| Next action | Opaque LiveProviderRuntimeHandle and public service acquire seam are now implemented without exposing policy/backend/path authority. Next wire the runtime enrollment layer to mint this handle and replace injected LiveProviderAttemptFactory in asb run/sweep; add CLI positive/negative dispatch tests and full gates. Do not expose bootstrap constructors. |

### AR-1350 — Sandbox-owned credential channel

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement a sandbox-owned sealed-FD credential channel for live provider children. |
| Next action | Fresh PR #261 exact head is f74b7d4f6f8290fcd39f47c1c65402cbbb088423. Hosted quality run 35903027712 failed narrowly at displayed 90.00&#37; (57954 total lines, 5796 missed), because strict fail-under-lines remained below 90&#37;; no gate weakening. Added deterministic launch metadata/accessor and backend probe coverage; local exact cargo llvm-cov --locked --workspace --all-targets --fail-under-lines 90 passes at 90.54&#37; (57982 lines, 5487 missed), with fmt check and clippy -D warnings green. Signed+DCO f74b7d4 verified and pushed. Monitor fresh PR-triggered exact-head checks and independent review; merge only after all required checks pass. AR-1349 expired-claim reconciliation remains a separate state issue. |

### AR-1351 — Runtime-owned live provisioning

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the private host/runtime provisioning seam for live acquisition. |
| Next action | Release AR-1351 done with merge and post-merge evidence; advance dependent AR-1349 while preserving its fail-closed gates. |

### AR-1352 — Runtime-owned live bootstrap

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add the private runtime-owned bootstrap source for live acquisition. |
| Next action | Release AR-1352 done with merge and post-merge evidence; advance dependent AR-1349 while keeping AR-1329 fail-closed. |

### AR-1353 — Runtime enrollment and CLI dispatch

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add runtime-owned enrollment and opaque live CLI dispatch. |
| Next action | Wire asb-cli run/sweep to acquire through LiveProviderRuntimeService::acquire_from_enrollment, using a runtime-only enrollment implementation that mints the opaque handle; remove the production requirement for caller-injected LiveProviderAttemptFactory. Add positive/negative dispatch and offline/replay tests, then run full gates. |

### AR-1354 — Runtime enrollment implementation

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement config-backed runtime-owned enrollment for live CLI dispatch. |
| Next action | BLOCKED on an attested runtime enrollment source: asb-runtime must receive an authority-free enrollment request and obtain concrete public target(s), pinned tool attestations, lease root, and relay root from a runtime/control-owned record; do not expose these asb-cli inputs. Add a signed/attested record transport or coordinator-owned runtime enrollment AR, then implement acquire_from_enrollment and CLI dispatch with positive/negative tests. |

### AR-1355 — Runtime-attested enrollment record transport

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Transport runtime-attested enrollment authority without exposing it to the CLI. |
| Next action | Implement the runtime/control-owned attested enrollment-record transport, validate target/tool/lease/relay authority inside asb-runtime, mint opaque handles, then consume them in asb run/sweep with positive and negative tests. |

### AR-1356 — Control/runtime enrollment attestation primitive

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Issue runtime-owned live enrollment capability from authenticated control attestation. |
| Next action | PR #264 merged at a6f1915aa5117f0296b1b8f4b9c4692a956b3d86. Monitor all seven post-merge workflows to terminal success; then release AR-1356 done with exact evidence and advance AR-1355 consumer. |

### AR-1357 — Runtime-attested enrollment record transport

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Transport authenticated enrollment records into runtime without exposing authority to the CLI. |
| Next action | PR #265 merged at 7862e3bb90a777e86e30d23b6af9639935671efe. Monitor all seven post-merge workflows at exact merge SHA; release AR-1357 only after every workflow terminal-success. |

### AR-1358 — Runtime enrollment CLI dispatch

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Consume runtime-attested enrollment records in asb run and sweep without exposing authority. |
| Next action | Promote after AR-1357 is done, then wire asb run/sweep through runtime-attested enrollment records with fail-closed positive and negative tests. |

### AR-1359 — Runtime/control enrollment bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bridge authenticated control enrollment into runtime-owned opaque live authority. |
| Next action | PR #266 exact head f511910 is published. Monitor every exact-head required check, repair any failures without weakening gates, then merge only after all green and independent review. |

### AR-1360 — Runtime CLI dispatch consumer

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Connect authenticated runtime enrollment receipts to asb run and sweep without exposing authority. |
| Next action | Promote after AR-1359 is done, then implement the production asb run/sweep consumer for authenticated runtime enrollment receipts with fail-closed tests. |

### AR-1361 — Runtime control receipt source

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide authenticated control receipt delivery and runtime-owned dispatch composition for CLI consumers. |
| Next action | Promote after AR-1359 is done, then add an authenticated control receipt source and runtime-owned dispatch factory without exposing authority to CLI. |

### AR-1362 — Runtime authority enrollment store

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Persist authenticated runtime authority enrollment required for receipt issuance without exposing secrets. |
| Next action | Run independent review, publish exact-head PR from clean signed head 7bf91f5, monitor required CI, repair failures without weakening gates, then merge only green and verify all seven post-merge workflows. |

### AR-1363 — Authenticated control receipt source

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Deliver authenticated runtime authority receipts through the versioned control boundary without exposing secrets or caller authority. |
| Next action | Release completed AR-1363 after exact protected-main verification; no further product action. |

### AR-1364 — Authenticated chain enrollment

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize authenticated certificate-chain authority for control-owned runtime receipt issuance. |
| Next action | Run full applicable gates, independently review the chain-enrollment boundary, then publish a clean exact-head PR and monitor all required checks. |

### AR-1365 — Control receipt source integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate authenticated chain and authority enrollment into the versioned control receipt source. |
| Next action | PR #269 merged as aa537f6a07ac3476a8c4d6443a8df3c42a1aebc1. Monitor seven post-merge workflows for exact merge SHA; release only after every workflow is terminal success. |

### AR-1366 — Runtime-owned dispatch consumer

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Connect runtime-owned authenticated receipt consumption to the benchmark dispatch path without exposing authority to CLI callers. |
| Next action | PR #270 merged as 0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c. Monitor seven post-merge workflows for exact merge SHA; release only after every workflow is terminal success. |

### AR-1367 — AR-1329 production dispatch integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Development asb run/sweep dispatch is qualified with local/mock and strict replay; deployment-owned live-provider materialization is optional future hardening. |
| Next action | No development action remains. Preserve the exact-main local/mock and strict-replay dispatch receipt; deployment-owned live-provider materialization is optional future hardening. |

### AR-1368 — Control receipt runtime source

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the authenticated runtime-owned ControlClient receipt source required by AR-1329 production dispatch. |
| Next action | Promote and claim the missing runtime-owned ControlClient receipt source, then add the authenticated control operation and production enrollment materialization without exposing authority. |

### AR-1369 — ControlBackend authority materialization

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize authenticated live-provider authority in ControlBackend for runtime receipt issuance. |
| Next action | Promote and claim the missing ControlBackend authority materialization, then persist authenticated chain/target/tool/lease/relay state for the receipt source. |

### AR-1370 — Runner authority materialization

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Superseded stale implementation successor; AR-1369 dependency was obsolete and current authority work is tracked by AR-1505/1513/1523. |
| Next action | No further action; superseded by merged AR-1505/1513 foundations and canonical AR-1523 live-authority integration. |

### AR-1371 — Runner authority injection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Inject existing authenticated certificate authority and runtime enrollment material into RunnerBackend/Catalog without synthetic authority. |
| Next action | PR #271 merged as 3f0b67638647dc016f7d5abd3e246baf3ae4ec29 after all 12 exact-head checks passed. Seven post-merge workflows are running; monitor all to terminal success before releasing AR. |

### AR-1372 — Protected merge topology repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair protected-main merge topology after AR-1371 without changing product behavior. |
| Next action | PR #272 merged with protected non-squash topology as 265b936d995148f8e40e36664cf68bf12affc20d. Seven post-merge workflows for exact merge are running; monitor all to terminal success, then release AR-1372 and reconcile AR-1371. |

### AR-1373 — Authenticated runtime receipt source

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the authenticated ControlBackend runtime receipt source for AR-1329 production dispatch. |
| Next action | PR #273 force-updated to exact head c623a006 after preserving historical v1 through v1.7 schemas. Monitor all required checks from the new head; repair any failure through handoffctl, merge only after independent review and all checks green, then verify seven post-merge workflows. |

### AR-1374 — Production live-provider dispatch

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Development ordinary run/sweep dispatch is qualified with local/mock and strict replay; deployment-owned live-provider authority is optional future hardening. |
| Next action | No development action remains. Preserve the exact-main local/mock and strict-replay receipt; deployment-owned live-provider authority is optional future hardening. |

### AR-1375 — Runtime-owned live control dispatch source

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Superseded duplicate: its dependency on AR-1374 formed a stale cycle; AR-1523 is canonical. |
| Next action | No further action; superseded by AR-1523, which owns the central-orchestrator live authority adapter. |

### AR-1376 — Runtime-owned live adapter

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize authenticated runtime receipts into opaque live dispatch attempts. |
| Next action | Audit blocker: ControlClient can issue RuntimeReceipt, but no runtime-owned authenticated chain store/source is available to validate the receipt. Do not synthesize a chain or accept caller authority. Create a successor for chain enrollment materialization before adapter implementation. |

### AR-1377 — Runtime-owned certificate-chain store

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Persist authenticated runtime certificate-chain material for live dispatch. |
| Next action | PR #274 force-updated to exact head 4163194 on current protected main 50acdcab after Repository quality base failure. Focused live_service rerun passes; monitor all required exact-head checks, repair failures, merge only green, then verify seven post-merge workflows. |

### AR-1378 — Authenticated live control adapter

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bind authenticated control receipts to runtime-owned live dispatch. |
| Next action | PR #275 is published at exact head 5f1902c. Monitor all required checks; repair failures through handoffctl, merge only after independent review and green exact-head CI, then verify seven post-merge workflows. |

### AR-1379 — Production live dispatch integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate authenticated runtime live dispatch into asb run and sweep. |
| Next action | Monitor rerun of post-merge Rust workflow and remaining six workflows at exact main SHA 1e2c591; release only after all seven terminal SUCCESS. |

### AR-1380 — Runtime scheduler composition for live dispatch

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Compose runtime-owned live attempts for production run and sweep scheduling. |
| Next action | PR #276 force-updated to exact head ab4e60c on protected main 16bca1f9 after policy/platform stale-base failure. Monitor fresh exact-head checks; repair any new failures, merge only green, then verify seven post-merge workflows. |

### AR-1381 — Runtime-owned live CLI scheduler wiring

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire runtime-owned live scheduler authority into production asb run and sweep. |
| Next action | PR #277 force-updated to exact head 4ba3085 after provenance fixture repair. Monitor fresh exact-head checks; repair any new failures, merge only green, then verify seven post-merge workflows. |

### AR-1382 — Authenticated live execution source

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize authenticated runtime-owned live execution for asb run and sweep. |
| Next action | Promote and claim this dependency-valid authenticated execution-source successor, then implement runtime-owned scheduler materialization. |

### AR-1383 — Runtime-owned authority profile materialization

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize runtime-owned live authority profile for authenticated execution. |
| Next action | Independent review complete; full runtime tests 114 passed/1 ignored, check and clippy -D warnings passed. Publish clean exact-head PR through handoffctl, then monitor required CI. |

### AR-1384 — Runtime-owned bootstrap materialization

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize the runtime-owned live bootstrap handle from authenticated authority. |
| Next action | Independent review complete; focused authority-profile tests (2), full asb-runtime tests (116 passed, 1 capability-gated ignored), fmt/check, and clippy -D warnings pass. Publish clean exact-head PR through handoffctl, then monitor exact-head CI. |

### AR-1385 — Authenticated runtime live dispatch source

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize the authenticated runtime-owned live dispatch source for production asb run and sweep. |
| Next action | PR #280 force-updated to signed+DCO exact head 02b79f3; monitor fresh required checks, repair only evidenced failures, then merge only after independent review and all checks green. |

### AR-1386 — Production live CLI dispatch integration

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate authenticated runtime live dispatch into production asb run and sweep. |
| Next action | Refresh the declared isolated worktree from protected main, integrate the authenticated runtime live dispatch source into production asb run and sweep, and add local provider-mock plus fail-closed egress/teardown tests. |

### AR-1387 — Authenticated runtime-control CLI bridge

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bridge authenticated runtime/control bootstrap state into the production CLI dispatch path. |
| Next action | Resume AR-1391 runtime-control bootstrap constructor; AR-1387 remains blocked pending that successor and has no safe in-scope product diff. |

### AR-1388 — Runtime authority receipt materializer

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize runtime-owned provider authority from authenticated receipt and chain state. |
| Next action | Done: original merge and AR-1389 replacement evidence verified; no further action remains. |

### AR-1389 — Formal fixture executable race repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the formal online-build fixture race that caused ETXTBSY after AR-1388 merge. |
| Next action | Done: atomic fixture repair merged at 10bffbf015bd7ca78d8c0d18f04cf0190195e933 and all seven post-merge workflows passed. |

### AR-1390 — Runtime live acquisition and CLI bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Development local/mock and strict-replay run/sweep bridge is actionable; deployment-owned authenticated live authority is optional future hardening, not a development blocker. |
| Next action | No development action remains. Preserve the local/mock and strict-replay receipt; any deployment-owned authenticated live authority is optional future hardening. |

### AR-1391 — Runtime control bootstrap constructor

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize authenticated runtime live authority into an opaque source without caller injection. |
| Next action | Claim the pre-bound isolated worktree, implement the runtime/control-owned authenticated bootstrap constructor, and publish a signed PR. |

### AR-1392 — Control-owned private authority materializer

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Resolve private live authority from authenticated control enrollment without caller injection. |
| Next action | Release done after exact main d59e6a7 verification; seven required workflows terminal green and remote main matches. |

### AR-1393 — Local provider authority provisioning

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provision a runtime-owned loopback mock authority so development never requires external provider access. |
| Next action | Publish signed+DCO PR from exact head 0a3817082d13f15187ea5efe4f5792664a50be99; monitor exact-head CI and independently review before merge. |

### AR-1394 — Literature workload registry expansion

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Catalog every documented literature benchmark with provenance and truthful qualification status. |
| Next action | Promote after the existing provenance ARs are verified, then add the strict literature workload inventory schema, entries, and generated docs. |

### AR-1395 — Literature workload adapter boundary

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Normalize approved literature tasks through bounded, non-vendored ASB workload adapters. |
| Next action | Exact merge post-merge Repository quality and Rust runs were cancelled by later main push c58b0b0a; after that main queue terminates, rerun both exact merge workflows and require success before release. |

### AR-1396 — Literature workload selection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make qualified literature workload families selectable beside built-in ASB software-engineering fixtures. |
| Next action | PR #288 exact head 58bc56f0b793c4f42e83cbe27515d63d22cfda51; fresh checks pending after CLI fail-closed validation repair. Review remaining OriginalWorkloads seams before merge. |

### AR-1397 — Protected-main post-merge concurrency and tree repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair protected-main merge-tree admission and serialize exact post-merge evidence across concurrent main pushes. |
| Next action | Preserve merge 123ba915d2732ee8a6c99fae301bfd64cf0aac4f and its seven successful post-merge runs as immutable evidence; it has exact tree/parents but GitHub-generated signature E and no matching Signed-off-by trailer. Create a signed descendant repair AR through the local merge path, then rerun exact-main gates before closing AR-1314/AR-1395/AR-1397. |

### AR-1398 — Signed protected-main recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Restore signed+DCO protected-main evidence after an unsigned GitHub-generated repair merge. |
| Next action | Watch all seven exact-main workflows for merge b63394b; after terminal success, record conclusions and release AR-1398 done. |

### AR-1399 — Literature workload registry completeness

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Represent every docs-listed literature workload family in the strict ASB registry. |
| Next action | Dependency branch e63a3c6 already contains complete six executable-candidate literature records and methodology-only AgentOps/HELM; focused validator/tests pass. Await parent integration decision; no duplicate product delta. |

### AR-1400 — Literature workload catalog activation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expose all documented literature workloads as truthful selectable candidates beside built-in fixtures. |
| Next action | Post-merge seven exact-main workflows for e0b15fc are running; release only after all terminal-success results and verify the merged catalog. |

### AR-1401 — Literature workload local mock execution

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide offline deterministic mock execution for every documented literature workload family. |
| Next action | Signed exact-base integration merge published as 0667f29 (base f213b296, head 6c397ce). Monitor seven exact-main post-merge workflows to terminal SUCCESS, verify exact tree/signature/DCO, then release AR-1401. |

### AR-1402 — Literature workload CLI dispatch integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate literature workload catalog and adapters through all ASB CLI execution and evidence paths. |
| Next action | Post-merge quality run 36004373951 failed only at optional analyzer download: curl exit 22 after repeated HTTP 500; product tests were not reached. Rerun the exact quality workflow after transient service recovery while monitoring the other six runs; release only after all seven terminal SUCCESS. |

### AR-1403 — Literature workload external qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add optional evidence-gated qualification for real literature workload sources and evaluators. |
| Next action | Execute signed exact-base integration merge PR #296 in isolated worktree; then verify seven post-merge workflows at merge commit. |

### AR-1404 — Literature workload documentation and matrix contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Rebased PR #295 onto current main 99a1af7; new exact-head checks running. |
| Next action | Wait for all 12 checks on rebased head 16c5b87, then merge exact base/head and run seven post-merge workflows. |

### AR-1405 — Open dependency PR reconciliation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Rebase, repair, verify, and truthfully resolve stale open dependency PRs. |
| Next action | Monitor seven post-merge workflows for exact SHA f213b296; after all green, close/supersede scoped stale PRs with exact evidence, then release AR done. Action PRs #235/#234/#148 require a future policy-pin migration AR; #147 requires separate sha2 compatibility AR. |

### AR-1406 — Action pin policy migration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify and merge remaining immutable GitHub action pin updates without weakening policy. |
| Next action | Monitor seven post-merge workflows for merge 8da098770e4a78e94f67cf7b13dbebbcd1c5bbac: 36023860491,36023860601,36023860551,36023860504,36023860525,36023860530,36023860510; release only after all terminal success, then close superseded PRs #235/#234/#148 with evidence. |

### AR-1407 — sha2 compatibility repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify or repair the closed sha2 0.11 dependency update without weakening crypto or MSRV contracts. |
| Next action | Keep current sha2 0.10.9 implementation authoritative; PR #147 sha2 0.11.0 remains superseded unless a separately reviewed compatibility migration addresses all digest formatting sites and proves exact parity. |

### AR-1408 — Literature workload inventory closure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | PR #293 merged at exact base; seven post-merge workflows running. |
| Next action | Wait for all seven post-merge workflows on merge 404ddde1 to reach terminal success, then release AR-1408 with evidence. |

### AR-1409 — Interactive literature workload adapters

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add offline-selectable interactive and tool-use literature workload adapters. |
| Next action | Monitor seven post-merge workflows for merge c2fe732b3b50ef38893c2e3513770939de04637f: 36021529638,36021529745,36021529796,36021529687,36021529643,36021529787,36021529768; release only after all terminal success. |

### AR-1410 — Literature selector completeness and parity

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Verify complete catalog, CLI, documentation, and evidence-state parity for literature workloads. |
| Next action | Monitor exact-main post-merge workflows 36034017499,36034017471,36034017528,36034017553,36034017539,36034017456,36034017548 until terminal success; verify merged tree then release AR-1410. |

### AR-1411 — Repository and terminal literature workload adapters

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add selectable, provenance-preserving repository-repair and terminal benchmark adapters. |
| Next action | PR #297 open; verify exact base fc74825cb86991bb3afac6854d8cb5048118ff8f/head 67129e7504dc28d8f8e02a6bbb955f6683917208/tree, wait for all required checks, independently review, then signed merge. |

### AR-1412 — Code-generation control workload adapters

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recovered an abandoned claim with malformed local-time expiry; branch/worktree are now coordinator-bound before the next claim. |
| Next action | Wait for fresh exact-head PR #298 checks on 0d94a2e rebased onto current main ea27dfb; independently review exact diff and merge only after all checks are green. |

### AR-1413 — Long-horizon and performance literature workload adapters

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Seven post-merge runs: four terminal success; aarch64, repository quality, and Rust remain actively executing on GitHub-hosted runners. |
| Next action | Continue monitoring post-merge IDs 36018871328/36018871323/36018871358; runner/job APIs show active in-progress steps, so do not rerun. Release only after all seven terminal success. |

### AR-1414 — Follow-up install-action pin qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the newer immutable install-action update reopened as PR #235. |
| Next action | Monitor seven post-merge workflows for merge 9d410f531bced0318df1ecc0614916488f62f4c5: 36026896292,36026896368,36026896414,36026896308,36026896341,36026896407,36026896374; release only after all terminal success. |

### AR-1415 — Total literature workload selector coverage

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the complete literature workload inventory selectable beside built-in software-engineering fixtures with truthful evidence gates. |
| Next action | Rerun exact failed post-merge workflow 36038241138 after three green isolated Goose reproductions; wait all seven terminal SUCCESS, verify main, then release. |

### AR-1416 — Literature workload local-mock cross-product

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prove end-to-end selectable literature workloads with deterministic local or LiteLLM-compatible mocks and no live provider dependency. |
| Next action | Monitor seven post-merge workflows for merge 0dcc717; release AR-1416 only after all seven terminal SUCCESS and exact-main verification. |

### AR-1417 — Interactive stateful literature workloads

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add selectable interactive and stateful literature workloads beside built-in software-engineering fixtures. |
| Next action | Keep open: protected-main Repository quality run 36048870322 failed because merge tree 5ddac12 differs from reviewed topic tree 666043f (base a2a6414 vs 0dcc717); await coordinator exact-main requalification or successor repair, never weaken gate. |

### AR-1418 — Tool-use reliability and safety workloads

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add selectable tool-use reliability and safety workloads from the literature with separate metrics. |
| Next action | Release: implementation is already merged in PR #300 at c2fe732b from 6f93076; focused interactive tests, all asb-workloads targets, and clippy -D warnings pass on exact current main 0dcc717. Preserve historical exact-head CI evidence and release without duplicate PR. |

### AR-1419 — Literature framework boundaries

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close literature documentation gaps and enforce benchmark-versus-framework selection boundaries. |
| Next action | Independent review, PR, exact-head CI, merge and seven post-merge assurance workflows; then release AR-1419. |

### AR-1420 — Literature workload campaign integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run the complete qualified literature workload matrix beside built-in software-engineering workloads. |
| Next action | Merge PR #350 normally; verify merge SHA and all exact-main post-merge workflows, then release AR-1420 done. |

### AR-1421 — Protected-main literature merge race repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair protected-main merge-tree requalification after a literature PR merges onto an advanced main. |
| Next action | Release AR-1421 done: merged tree equals reviewed topic tree e5d99b7; parents are 5ddac12 and 28e3560; topic passes SSH signature and DCO. Seven exact-main workflows all terminal SUCCESS. |

### AR-1422 — Stale agent-catalog PR cleanup

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close stale conflicting agent-catalog PR #306 through durable coordinator evidence. |
| Next action | Closure evidence complete. Re-run doctor --live after concurrent state-worker AR-1421 changes settle; then release AR-1422 done. Do not modify AR-1421 files. |

### AR-1423 — Exhaustive literature docs-to-registry reconciliation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reconcile all literature benchmark mentions with strict registry identities and framework boundaries. |
| Next action | Publish PR from exact clean head, obtain independent review and required CI, then merge and complete post-merge assurance workflows. |

### AR-1424 — Complete literature selector and local campaign matrix

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make all locally executable literature workloads selectable and campaignable beside built-in fixtures. |
| Next action | Monitor exact-main post-merge workflows for 6baa7ac; after all eight green, release AR-1424 done. |

### AR-1425 — Literature workload release-readiness gate

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Independently verify release readiness of the complete built-in and literature workload surface. |
| Next action | Release done after independent audit; no successor required. Future native/official qualification remains separately gated. |

### AR-1426 — Evolving literature workload window refresh

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Refresh evolving literature benchmark windows without stale or incomparable results. |
| Next action | Reconcile and doctor state, then release AR-1426 done. |

### AR-1427 — Protected-main merge-tree requalification repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair exact protected-main merge-tree requalification after sequential tutorial merges. |
| Next action | Promote and reproduce PR #310 merge f511645 versus reviewed topic 9d97e168; repair exact protected-main merge-tree requalification, then rerun AR-1215 post-merge evidence. |

### AR-1430 — Literature workload catalog gap closure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close documented literature workload identity and selector gaps without enabling live providers or external acquisition. |
| Next action | Run full local quality gates, publish exact-head PR, obtain independent review, merge, monitor seven post-merge workflows, then release. |

### AR-1431 — Protected-main stale-base merge requalification repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prevent stale-base sequential merges from passing review but failing protected-main merge-tree policy. |
| Next action | Monitor seven post-merge workflows for exact merge ed907603; release AR-1431 only after all seven terminal success, then coordinate AR-1216 release. |

### AR-1432 — Local OpenRouter execution bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify credential-free OpenRouter user execution through a deterministic loopback mock without external-provider access. |
| Next action | Local deterministic mock-attempt backend is delivered by AR-1433 (PR #325, merge 2872a31f) and is no longer blocked for development qualification. Preserve this AR&#x27;s remaining optional production live-bridge boundary: do not synthesize LiveProviderAttempt or weaken ProviderEgressTarget; runtime-owned relay/backend acquisition remains separately fail-closed. |

### AR-1433 — Runtime mock-attempt backend

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add an approved runtime mock-attempt backend for deterministic local run and sweep qualification. |
| Next action | Done: signed+DCO PR #325 merged as 2872a31f with all seven exact-main workflows green and post-merge local-mock verification complete. Preserve AR-1432&#x27;s separate optional production live-bridge blocker. |

### AR-1434 — Runtime local mock-attempt adapter

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add an approved runtime mock-attempt adapter for deterministic local run and sweep qualification. |
| Next action | Monitor exact merge 4736db727b13140364b8acd32cf77b7b375eeb17 until all seven post-merge workflows are terminal success: Fault assurance, Formal assurance, Repository quality, Emulated aarch64 portability, Rust verification, Hosted portability and native qualification, Huawei MIT source headers. Then run exact-main reconciliation and release only with durable evidence. |

### AR-1435 — Local mock CLI wiring

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire deterministic local mock attempts into asb run and sweep configuration qualification. |
| Next action | Monitor seven exact-main workflows for merge cc82333a53e03147ea95cc21ca697647dc27db1f to terminal success; verify exact tree/signature/DCO and release only afterward. |

### AR-1436 — Local guided CLI wrapper

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a catalog-driven guided CLI wrapper for deterministic local mock qualification. |
| Next action | No further action; PR #317 merged and the recorded post-merge qualification is complete. |

### AR-1437 — Local record/replay campaign qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify deterministic local record/replay and campaign journeys over the runtime mock. |
| Next action | No further action; PR #318 merged and the recorded seven-workflow qualification is complete. |

### AR-1438 — Hardened trusted-runner validation repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make protected trusted-runner lifecycle validation compatible with hardened rootless execution. |
| Next action | Promote and repair the trusted development-host validation so it passes under the approved NoNewPrivileges runner hardening without weakening isolation or skipping lifecycle checks. |

### AR-1440 — Refresh OpenRouter model pin and local measurements

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Refresh the stale OpenRouter free-model pin and qualify local-only benchmark measurements. |
| Next action | Release complete after PR #323 product head 8d2a99d and two-parent topology repair PR #324 merge 5871de7cad4ee7e496ffce1c5e1fe51862660bfc; seven exact-main workflows all green. GitHub has no independent review record for PR #324; preserved as an evidence gap, not fabricated. |

### AR-1441 — First-class install and bootstrap

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide a verified one-command install and first-run bootstrap for ASB CLI/runtime bundles. |
| Next action | Done: ASB-only bootstrap and lifecycle qualification passed against protected merge 2872a31f; preserve AR-0823 as the separate cross-repository/UI audit. |

### AR-1442 — Guided setup wizard orchestration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify ASB CLI first-run and reconfiguration of agents, providers, auth methods, models and defaults with a non-blocking development profile. |
| Next action | Done: ASB CLI setup/reconfiguration contract and full CLI qualification passed against protected merge 2872a31f; preserve standalone TUI wiring as separate downstream work. |

### AR-1443 — Guided benchmark capture and comparison

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make benchmark, offline capture/replay, and result comparison a single guided workflow with warning-only development prerequisites. |
| Next action | Done: ASB-only guided capture/replay/comparison qualification verified on protected merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec. CLI tests passed (107 unit, 12 capability, 3 CLI E2E, 5 guide, 2 setup, 4 lifecycle, 3 transcript); optional live capture and asb-tui remain separate. |

### AR-1444 — First-class journey qualification

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Optional cross-repository journey evidence; never an ASB release blocker. |
| Next action | Optional cross-repository qualification only: wait for external asb-tui AR-1327 to provide an exact pinned acceptance revision and credential-free journey transcript; this AR is not an ASB release or first-customer blocker. Do not modify asb-tui from this repository. |

### AR-1445 — Protected-main topology repair for OpenRouter refresh

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the single-parent protected-main merge produced for the OpenRouter model refresh. |
| Next action | PR #324 merged as two-parent 5871de7cad4ee7e496ffce1c5e1fe51862660bfc; monitor seven exact-main workflows 36145976341, 36145976337, 36145976326, 36145976266, 36145976239, 36145976238, 36145976223 to terminal success. Record that GitHub has no independent review record, then update/release AR-1440 only after all seven pass. |

### AR-1446 — First-customer production qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify ASB in a disposable first-customer production-like environment. |
| Next action | Done: ASB-only first-customer production-like qualification verified on protected merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec. Disposable bootstrap passed; CLI, runtime, and workspace-library gates passed, including literature/local-mock coverage. No live-provider or asb-tui dependency was required; AR-0903 and AR-1336 remain separate. |

### AR-1447 — ASB local campaign qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the complete credential-free ASB local campaign and replay journey. |
| Next action | Done: ASB-only local campaign qualification verified on protected merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec. Targeted guided-local and exact-campaign tests plus full asb-cli library tests (107/107) passed; AR-1338 remains a separate enhancement. |

### AR-1448 — Runtime replay authority source

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize runtime-owned strict replay authority for normal CLI replay. |
| Next action | Done: signed PR #326 merged as f03d9e484d6ca73eacdbd5476980bf33ca737540; all seven exact-main post-merge workflows and local runtime/CLI verification passed. |

### AR-1449 — Runtime-owned local replay CLI authority

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide fail-closed runtime-owned local replay authority for the guided CLI wrapper. |
| Next action | Blocked: AR-1448 exposes issuance only and requires caller-built sandbox, lease, backend and relay. A runtime-owned provisioning successor is required; no product change was published. |

### AR-1450 — Runtime-owned local replay acquisition factory

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Keep local replay authority acquisition inside the runtime boundary. |
| Next action | Release-ready: PR #328 head 2832912 passed exact-head checks and independent review; merge 452f3ca was repaired by AR-1454 merge a0bd63d3 with all seven post-merge workflows green. |

### AR-1451 — Central orchestration authority contract and ASB redesign

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Freeze one runtime-owned orchestration authority for every ASB run and attempt. |
| Next action | PR #329 merged as 071167d. Monitor seven exact-main post-merge workflows 36170798957, 36170798948, 36170798971, 36170798901, 36170798918, 36170798954, 36170798887 to terminal success; then release AR-1451 and promote AR-1452. |

### AR-1452 — Implement the runtime-owned ASB orchestration service

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement one service-owned authority for admission, attempts, resources, and teardown. |
| Next action | PR #330 merged at exact main a5eb7e6; wait for all seven post-merge workflows, then run exact-main verification and release AR-1452 done before promoting AR-1453. |

### AR-1453 — Route ASB frontends through central orchestration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make CLI and control use the central service for every run lifecycle. |
| Next action | Release AR-1453 complete after all seven exact-main post-merge workflows passed. |

### AR-1454 — Protected-main tree-equality repair for runtime replay

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the protected-main tree mismatch after the runtime replay merge. |
| Next action | Post-merge verification complete: all seven workflows succeeded; release AR-1454 and propagate repair evidence to AR-1450. |

### AR-1455 — Runtime-owned guided replay entrypoint

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the runtime-owned guided local replay entrypoint needed by AR-1338. |
| Next action | Run state reconcile and live doctor, then release AR-1455 done with exact post-merge workflow evidence. |

### AR-1456 — Local/mock multi-agent campaign successor

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Decouple mandatory local/mock multi-agent campaign qualification from optional live-provider execution. |
| Next action | No further action; PR #336 merged and all recorded exact-main post-merge workflows are green. |

### AR-1457 — Retire superseded AR-1453 pull request

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Retire the obsolete pre-repair AR-1453 pull request without changing product code. |
| Next action | No further action; obsolete PR #332 was closed and authoritative PR #333 remains verified. |

### AR-1458 — First-customer requalification after central orchestration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Requalify the first-customer production-like journey after central orchestration became authoritative. |
| Next action | Release done: exact protected-main requalification passed with credential-free local/mock and strict-replay evidence; no deterministic repair AR. |

### AR-1459 — Retire stale state-repository pull requests

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Retire obsolete state-repository pull requests without changing product or formal gates. |
| Next action | No further action; stale state PRs were closed and blocked formal PR #25 remains intentionally open. |

### AR-1460 — Current-main first-customer requalification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Requalify first-customer readiness after the latest local-mock campaign merge. |
| Next action | Release done: current protected-main first-customer qualification passed with credential-free local/mock and strict-replay evidence; no deterministic repair AR. |

### AR-1461 — First-customer release readiness and publication

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prepare and publish the first-customer ASB release from the currently qualified main. |
| Next action | No further action; v0.1.0 was published and fresh customer-consumption verification is recorded. |

### AR-1462 — Pinned release toolchain and first-customer bundle workflow

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Establish reproducible supply-chain checks and first-customer release bundle publication workflow. |
| Next action | No further action; PR #337 merged and all seven exact-main post-merge workflows are green. |

### AR-1463 — Current-main first-customer requalification after capture integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Exact protected main is requalified for first-customer production-like use: install/build, local/mock workloads, capture redaction and content-addressed sealing, strict offline replay, recovery/privacy/egress denial, coverage and deterministic/formal gates pass; existing v0.1.0 remains the verified release. |
| Next action | No new release publication; retain v0.1.0 as the verified customer release and repeat qualification only for a later protected-main revision. |

### AR-1464 — Formal capacity and signed-input provisioning repair

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Exact signed source, reviewed image, 64 GiB overlay, JDK/TLC/model and canonical lock are provisioned. Reclaimed the three stale AR-specific swap files and activated two fresh AR-specific swap files; repeated signed preflight now passes every gate except the unavailable exact seed digest. |
| Next action | Obtain or restore the reviewed full-exhaustive seed with SHA-256 b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28. Do not regenerate or substitute a different seed. Then rerun the signed preflight, hand inputs to AR-1308, and remove/revert only the temporary AR-specific swap after the runner lifecycle. |

### AR-1465 — Reviewed full-exhaustive seed archival recovery

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expanded archival audit found no exact reviewed seed in approved state/runner roots, Git objects, the ASB product tree, seed-named second-disk files, or available GitHub Actions artifacts. |
| Next action | External operator must supply reviewed immutable seed bytes with exact SHA-256 b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28 and provenance; independently verify them, bind them to AR-1308, and rerun signed preflight. Do not regenerate or substitute. |

### AR-1466 — State CI formatting repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | State CI repair is complete at exact protected-main head 932a91a: formatter/lint and schema compatibility repairs pass local gates, focused AR-1308 tests pass, and Coordination verification run 36274807110 succeeded. |
| Next action | No further action; AR-1466 is complete and exact-main state CI is green. |

### AR-1467 — Terminal AR metadata reconciliation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Remove stale historical next-action text from recently completed ASB AR records without changing implementation or gates. |
| Next action | No further action; terminal metadata was reconciled without changing implementation or gates. |

### AR-1468 — Control authority materialization successor

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the control-owned authority materializer without the superseded AR-1369 dependency deadlock. |
| Next action | Promote and claim the corrected-dependency successor, then implement the owner-checked control authority materializer through the reviewed workflow. |

### AR-1469 — AR-1392 protected-main topology repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the single-parent protected merge for AR-1392 without changing its reviewed implementation. |
| Next action | Reconcile and doctor state after seven green exact-main workflows; topology repair complete. |

### AR-1470 — Runtime certificate-chain enrollment materialization

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize runtime-owned certificate-chain enrollment authority for live dispatch. |
| Next action | Protected-main setup is not current: AR worktree is clean but 86 commits behind origin/main 7167e3d; refresh via handoffctl run, then implement the narrow runtime-owned authenticated enrollment source. Existing RuntimeAuthorityRecord holds only public digests/opaque chain metadata; no private bootstrap authority or caller-safe issuer is available. Do not fabricate authority. |

### AR-1471 — Control-to-runtime certificate-chain binding

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bind authenticated control enrollment to runtime certificate-chain storage and live dispatch. |
| Next action | Reconcile and doctor live state, then release AR-1471 done with merge and seven exact-main workflow evidence. |

### AR-1472 — Authenticated live-dispatch adapter

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Connect authenticated control receipts to runtime-owned CLI live dispatch without a dependency cycle. |
| Next action | Run reconcile and doctor --live, then release AR-1472 done with merge and seven-workflow evidence. |

### AR-1473 — Runtime-owned authenticated enrollment source

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Resolve authenticated control enrollment into an opaque runtime-owned source for normal ASB run and sweep. |
| Next action | Reconcile/doctor live state, then release AR-1473 done. |

### AR-1474 — Runtime-owned authority-input resolver

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Persist and resolve authenticated runtime authority inputs without caller-supplied or synthetic authority. |
| Next action | Release AR-1474 done; old PR coverage failure superseded by AR-1477 tests and AR-1478 topology repair. |

### AR-1475 — Repair asb-metrics evidence fixture classification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the deterministic ProbeRejected versus MalformedEvidence fixture failure blocking PR #345. |
| Next action | Release done after final reconcile; then rerun PR #345 exact-head validation. |

### AR-1476 — Repair workspace coverage floor

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Restore the enforced 90 percent workspace coverage floor blocking exact AR-1474 validation. |
| Next action | Rerun PR #345 exact-head validation against current protected main 1dada31c; no repair diff is required unless the current-base gate regresses. |

### AR-1477 — Cover authority resolver behavior

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Raise exact hosted coverage above the enforced 90 percent floor for the authority resolver. |
| Next action | Create a narrow protected-main topology repair successor for merge 67fa0d1; repository policy requires topic synchronization merge at tip. Preserve all six other post-merge results and do not waive policy. |

### AR-1478 — Repair topic synchronization topology

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair protected-main topic synchronization topology after AR-1477 merge policy failure. |
| Next action | Reconcile and doctor state; release AR-1478 done with complete merge and seven-workflow evidence. |

### AR-1479 — Rust CI timing and state-root flake repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the unrelated Rust state-root collision and malformed-ready-marker timing flakes blocking AR-1420 exact-head CI. |
| Next action | Monitor exact-main post-merge workflows for 1015a461; after all seven green, release AR-1479 and requalify AR-1420 PR #350 head 2884508. |

### AR-1480 — Runtime-control CLI composition

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch. |
| Next action | Run reconcile and doctor --live, then release AR-1480 done ownerless with complete merge/post-merge evidence. |

### AR-1481 — Runtime-owned CLI entry bootstrap

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire runtime-owned authenticated dispatch into the ordinary CLI entry path. |
| Next action | Promote and claim, then inspect the protected-main entrypoint and runtime/control bootstrap inputs. |

### AR-1482 — Control-runtime process bootstrap

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Compose authenticated control enrollment into the ordinary CLI process bootstrap. |
| Next action | Development qualification is not blocked: exercise process bootstrap with deterministic local/mock and strict-replay authority. A real deployment-owned authenticated provider/materializer is optional future production hardening; preserve fail-closed live behavior. |

### AR-1483 — Authenticated control process owner

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Own authenticated control session and lifecycle while minting opaque CLI dispatch sources. |
| Next action | Promote and claim, then audit whether the runtime/control owner contract can be implemented without caller authority. |

### AR-1484 — Runtime/control process-owner contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define stable runtime/control process-owner lifecycle and opaque handoff contract. |
| Next action | Reconcile/doctor, then release AR-1484 done ownerless with complete merge/post-merge evidence. |

### AR-1485 — Process-owner local/mock lifecycle

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement runtime-owned local/mock process lifecycle and opaque-source handoff. |
| Next action | Release complete; retain exact merge and eight workflow evidence. |

### AR-1486 — Runtime-owner CLI entry wiring

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire the runtime-owned local/mock process owner into ordinary CLI run and sweep. |
| Next action | Release complete; retain exact merge and eight workflow evidence. |

### AR-1487 — Owner-backed first-customer qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the owner-backed credential-free local/mock/replay first-customer journey. |
| Next action | Reconcile and doctor state projection; retain known generated WORKTREES/PROJECT_STATE caveat if reported. |

### AR-1488 — Owner-backed first-customer user journey

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the owner-backed first-customer install, operation, replay, evidence, and cleanup journey. |
| Next action | Reconcile and doctor state projection; retain known generated WORKTREES/PROJECT_STATE caveat if reported. |

### AR-1489 — First-customer package consumption

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Verify first-customer release package installation and owner-backed local/mock/replay consumption. |
| Next action | Reconcile and doctor state projection; retain known generated WORKTREES/PROJECT_STATE caveat if reported. |

### AR-1490 — Fresh package runtime acceptance

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run fresh package first-customer runtime acceptance and produce an explicit readiness report. |
| Next action | No further AR-1490 action. Development unsigned qualification is complete; any customer/release publication remains separately gated by a genuinely signed production bundle. |

### AR-1491 — Self-contained package qualification fixture

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add a self-contained non-production package qualification fixture using the offline verifier test-key pattern. |
| Next action | Reconcile and doctor state projection; retain generated WORKTREES/PROJECT_STATE caveat if reported. |

### AR-1492 — Customer bundle signing handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Stage a deterministic customer bundle and provide an explicit external signing handoff and verifier. |
| Next action | Run state reconcile and doctor, then release AR-1492 done ownerless with merge and eight-workflow evidence. |

### AR-1493 — Release-authority enrollment handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Define and validate the external release-authority enrollment and signed-bundle verification handoff. |
| Next action | Reconcile and doctor state, then release AR-1493 done ownerless with complete merge and post-merge evidence. |

### AR-1495 — Development-only unverified bundle profile

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add an explicit development-only unverified bundle profile without weakening production or customer-release verification. |
| Next action | Monitor PR #373 fresh exact signed+DCO head 4d63a66; merge only after all required checks and independent review are green. |

### AR-1496 — Runtime-owned provider capture and control activation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Complete runtime-owned provider capture, tuple cassette reconciliation and verified offline activation required by the setup wizard. |
| Next action | Done: PR #375 merged at protected main 8c53a4a62ecaa6fecc9eb195a105fc368a3395c8; independent review passed and all seven post-merge workflows succeeded. |

### AR-1497 — AR-1495 protected-main topology repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair AR-1495 protected-main synchronization topology without changing product semantics. |
| Next action | Monitor eight post-merge workflows for exact protected-main merge 45df6590; release AR-1497 only after all terminal SUCCESS. |

### AR-1498 — Authenticated lifecycle artifact executor

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | PR 376 merged at protected main exact merge commit |
| Next action | Verify origin/main contains merge 9231a660675d4b01277a60b75d838d69c6bba917, run post-merge applicable smoke/build checks, then release AR-1498 durably. |

### AR-1499 — Development credential enrollment contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair merged development credential selection binding |
| Next action | Released; no further AR-1499 action. PR #378 merged at protected main ee8ea15; exact main tree and post-merge smoke verified, and all eight post-merge workflows passed. |

### AR-1500 — Development credential/provider lifecycle fixture

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify generated development credentials through provider, capture and replay flows. |
| Next action | AR-1500 complete: PR #379 merged at exact checked head; post-merge main tree equality and offline fixture smoke passed. Continue dependent ARs. |

### AR-1501 — Production credential hardening follow-up

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P2 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Track production credential secrecy and authentication hardening after the prototype. |
| Next action | Monitor all seven active post-merge workflows for terminal success, verify remote merge signature/tree/parents and main tree, then release AR with durable evidence. |

### AR-1502 — Runtime-owned bootstrap authority

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Runtime-owned authenticated bootstrap authority merged and verified on main. |
| Next action | No further action; release AR-1502 after protected merge and exact-head post-merge workflows. |

### AR-1503 — Runtime/control process owner

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Own the authenticated control session and hand off only an opaque live dispatch source. |
| Next action | Diagnose unrelated full-workspace ASB test race, rerun serialized or focused affected gate; then independently review AR-1503 diff and decide whether platform-launcher seam is genuinely available. |

### AR-1504 — Runtime/platform launcher seam

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the real runtime/platform-owned launcher and authenticated session discovery for AR-1503. |
| Next action | Implement the missing runtime-owned platform adapter/session locator on protected main, with authenticated socket ownership/permissions, private input construction, opaque source handoff and lifecycle tests; do not copy AR-1503 façade. If platform authority contract cannot be established from existing control protocol, create a narrowly scoped successor AR for that protocol contract with exact symbols and keep this AR blocked. |

### AR-1505 — Control-plane platform authority/bootstrap protocol

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide an authenticated platform protocol that issues private runtime bootstrap inputs to ASB. |
| Next action | No further AR-1505 action; merge and post-merge assurance complete. |

### AR-1506 — Runtime platform launcher integration

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Connect the merged authenticated platform authority/bootstrap protocol to production ASB process startup and ordinary CLI dispatch. |
| Next action | Development qualification is not blocked: test the launcher integration with deterministic local/mock and strict-replay authority and no public injection. A runtime-owned deployment adapter from authenticated AR-1505 state is optional future production hardening; do not claim live support from mocks. |

### AR-1507 — Runtime-owned authority materialization

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Materialize private runtime launch authority from authenticated AR-1505 bootstrap state without caller or synthetic authority. |
| Next action | Promote after dependency verification; define and implement the runtime-owned authority materializer that maps authenticated bootstrap state to private roots, tools, policy, and opaque dispatch source. |

### AR-1508 — Platform-owned authority provider

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Lifecycle expiry fencing repaired and covered by seven focused plus 167 full asb-runtime tests; production platform authority callsite remains absent. |
| Next action | Development qualification is not blocked: retain the passing lifecycle-fencing tests and use deterministic local/mock and strict-replay authority for development. Route any non-test deployment source to optional future production hardening; do not make it a local qualification gate. |

### AR-1509 — Authenticated authority-provider receipt

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Replace the AR-1508 test façade with an authenticated production authority-provider receipt and lifecycle fence. |
| Next action | Blocked: implement a real runtime/control platform-authority adapter that obtains credential/enrollment/private roots from authenticated control state, emits a control-authenticated receipt, wires materialize_provisioner into live run/sweep, and rechecks restart/revocation/expiry at transitions; preserve this worktree for successor AR. |

### AR-1510 — Authenticated control source and production provider wiring

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provider boundary and expiry fencing are implemented and runtime/CLI tests mostly pass; ordinary production dispatch still lacks an authenticated non-test platform material source. |
| Next action | Development qualification is not blocked: wire and test the opaque source with deterministic local/mock and strict-replay authority through ordinary run/sweep. A platform-owned deployment adapter is optional future production hardening and must not gate local qualification. |

### AR-1511 — Runtime/control authority issuer and capability source

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the authenticated runtime/control authority issuer and opaque capability source required by production dispatch. |
| Next action | No further AR-1511 implementation: AR-1513 supplies the authenticated process-owner material source and ordinary run/sweep bridge on protected main 47329e35. Preserve AR-1513 merge and post-merge evidence; do not revive the old AR-1511 façade. |

### AR-1512 — Authenticated process-owner material contract

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the authenticated process-owner material source and ordinary CLI/control caller needed to consume runtime authority. |
| Next action | Independent exact-head review of a4064abf; create successor for authenticated lease-to-LiveProviderRuntimeHandle bridge, then publish exact-head PR/CI if review accepts provider-free boundary. |

### AR-1513 — Authenticated lease-to-live-dispatch bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Authenticate process-owner material, validate executable provenance, and connect leases to ordinary live dispatch. |
| Next action | PR #383 merged at 47329e35; monitor post-merge workflows 36550477933, 36550477996, 36550478002, 36550478037, 36550478039, 36550478042, 36550478232 to terminal success, then verify protected main and close AR. |

### AR-1514 — Reconciled development auth handoff runtime

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair ASB development-runtime reconciliation between digest-only enrollment and helper invocation. |
| Next action | Complete; PR #386 merged at bf89a45ddd71af96e6d4b6954320e199e147f83e. Protected main tree equals reviewed topic and post-merge auth-focused ASB tests pass. Paired asb-tui AR-1323 qualification remains external. |

### AR-1515 — AR-1307 runner CI repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Triage complete: AR-1307 runner admission and diagnostics are intact; remaining failure is workload capacity under the unchanged 3G/3G contract. |
| Next action | No runner source repair remains; AR-1309 owns the separately reviewed capacity/model-reduction decision. |

### AR-1516 — AR-1308 QEMU fixture repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Fixture repair passed boot/transient/JAR checks; full tier timed out at 1700s without attestation. |
| Next action | Close fixture repair; hand timeout to AR-1309 for capacity/model decision. |

### AR-1517 — AR-1309 capacity decision

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Select a reviewed AR-1309 capacity/model contract after runner failure. |
| Next action | Classify evidence and select AR-1309&#x27;s capacity/model contract. |

### AR-1518 — C

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Capacity profile boots and runs, but the 1700-second bounded QEMU attempt timed out without terminal TLC result or attestation. |
| Next action | Use AR-1519 for separately scoped reduced-model development; do not claim AR-1307 or AR-1308 formal qualification. |

### AR-1519 — AR-1307/1308 reduced-model development profile

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reduced development tier implemented with explicit 900s/1-worker/2G/2G/4G bounds and non-claiming attestation. |
| Next action | Independently review the exact head, then release this development-only repair; full AR-1307/1308 qualification remains separate. |

### AR-1520 — AR-1308 reduced-profile runtime qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reduced profile passes self-contained QEMU: transient admission, bounded models, sanitized non-claiming attestation, and clean poweroff. |
| Next action | Release after exact-head review; retain AR-1307/1308 formal qualification as separate blocked gates. |

### AR-1521 — AR-1307/1308 formal capacity repair implementation

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the reviewed successor contract that repairs the AR-1308 full-tier capacity failure while preserving AR-1307 qualification boundaries. |
| Next action | No further action: superseded by AR-1530, which owns the state-runner implementation. |

### AR-1522 — AR-1307/1308 formal qualification rerun

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run and independently verify the repaired AR-1307/1308 full-tier qualification, or leave a truthful classified blocker. |
| Next action | Formal-only blocker: wait for AR-1531 and the exact reviewed formal seed/input bundle before the one authorized terminal attempt. This does not block the completed unsigned-development/first-customer path. |

### AR-1523 — Platform authority deployment adapter

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the central orchestration path with deterministic local/mock and strict-replay authority; deployment-owned live authority is optional future hardening, not a development prerequisite. |
| Next action | Development path is unblocked: promote and claim this AR, qualify the existing central orchestrator with deterministic local/mock and strict-replay authority, and run exact-head gates. A deployment-owned authenticated source is optional future production hardening and must not block development qualification. |

### AR-1524 — Repair live-dispatch dependency graph

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the stale AR-1374/1375 dependency cycle and make AR-1523 the canonical live-dispatch successor. |
| Next action | Promote after dependency verification; supersede the stale AR-1375 cycle and route AR-1374 to AR-1523 without changing product code. |

### AR-1525 — Repair stale authority dependency graph

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P1 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Remove the obsolete AR-1370 dependency on superseded AR-1369 and preserve canonical authority evidence. |
| Next action | Promote after dependency verification; supersede stale AR-1370 and route remaining authority work through AR-1523. |

### AR-1526 — First-customer local/replay qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify the merged ASB production-shaped local/mock and strict-replay customer path with sanitized evidence. |
| Next action | No development action remains. Preserve the exact-main first-customer local/mock and strict-replay receipt; live-provider deployment remains optional future hardening. |

### AR-1527 — Normalize AR-1307/1308 development seed policy

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Remove reviewed seed and digest prerequisites from the AR-1307/1308 development path while preserving separate formal and release evidence gates. |
| Next action | Promote after state review; audit AR-1307/1308 and every active dependent for development-only seed/digest prerequisites, then normalize their task and plan language without changing formal gates. |

### AR-1528 — Rerun AR-1307/1308 development fixtures

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Run the repaired AR-1307/1308 unsigned-development fixture path and preserve separate formal qualification blockers. |
| Next action | No further action: development fixture rerun is complete; retain its non-qualifying evidence while formal work proceeds separately. |

### AR-1529 — AR-1307/1308 formal capacity decision successor

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Replace the stale AR-1309 dependency with a reviewed formal capacity/model decision grounded in the completed capacity and reduced-profile evidence. |
| Next action | No further action: the 8 GiB/8 GiB signed-capacity contract is recorded; AR-1530 owns implementation. |

### AR-1530 — State formal capacity profile for AR-1307/1308

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement the state-owned 8G/8G formal capacity profile selected by AR-1529 and route it to AR-1522. |
| Next action | No further action: merged PR #31 provides the signed-capacity-8g profile; AR-1531 owns disposable fixture provisioning. |

### AR-1531 — Provision signed 8G formal capacity fixture

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provision the missing 8G/8G disposable formal fixture and resource evidence required by AR-1522. |
| Next action | External operator must supply the exact reviewed formal seed and matching model/JDK/TLC/source inputs; preserve the provisioned 8 GiB/8 GiB fixture and do not run qualification before preflight passes. |

### AR-1532 — AR-1307 unsigned-development runner repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair and independently qualify the provider-free unsigned-development runner path associated with AR-1307 without changing formal limits or evidence gates. |
| Next action | Promote and claim; rerun the provider-free unsigned-development AR-1307 runner path on the v0.3.53-compatible state, then record non-qualifying evidence. |

### AR-1533 — AR-1308 unsigned-development QEMU fixture repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the provider-free unsigned-development QEMU fixture for AR-1308 and make its diagnostics, cleanup and non-qualification boundary reliable. |
| Next action | Promote and claim; rerun the provider-free unsigned-development AR-1308 QEMU fixture on the v0.3.53-compatible state and preserve qualification_authorized=false. |

### AR-1534 — Coordinator vendor integrity repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Immutable coordinator v0.3.53 vendor boundary and ASB lifecycle/session/SQLite compatibility are green; close with successor receipts. |
| Next action | Promote and close from AR-1547/AR-1549: v0.3.53 vendor verification and all compatibility gates are green; preserve the separate formal qualification boundary. |

### AR-1535 — AR-1307 formal-readiness handoff repair

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reconcile AR-1307&#x27;s repaired development runner with the formal qualification handoff after the approved vendor release. |
| Next action | Formal-only blocker: an authorized external operator must provide the exact reviewed AR-1307 seed and matching model/JDK/TLC/source bundle; do not substitute development fixtures. This does not block the completed unsigned-development path. Then AR-1545 audits the inputs for AR-1522. |

### AR-1536 — AR-1308 capacity and preflight handoff repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair AR-1308 capacity/preflight handoff after the unsigned-development fixture and approved vendor boundary are complete. |
| Next action | No development action remains. Preserve the unsigned-development handoff receipt; AR-1531 exact formal inputs remain separate optional formal work and cannot block development. |

### AR-1537 — Coordinator vendor bootstrap closure

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Allowlist closure is implemented and focused tests pass, but consuming v0.3.50 also changes ASB-owned formal/tests surfaces; AR-1538 owns that compatibility integration. |
| Next action | Remain blocked pending AR-1538 downstream integration. Preserve the repaired explicit allowlist and the mixed-snapshot failure; do not rerun sync until ASB-owned compatibility work is reviewed. |

### AR-1538 — Coordinator v0.3.50 downstream integration

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | v0.3.50 sync and immutable vendor verification pass, but the coordinator lifecycle/session contract is incompatible with ASB-owned tests and SQLite fence fixtures; a narrower compatibility successor is required. |
| Next action | Remain blocked pending AR-1539 compatibility repair. Preserve branch preserve/ar1538-v0350-mixed-snapshot and do not publish the failing integration. |

### AR-1539 — Coordinator v0.3.50 compatibility repair

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Compatibility audit reproduced the v0.3.50 failures and split them into AR-1540 session/lifecycle and AR-1541 SQLite fence repairs; no incompatible runtime is publishable. |
| Next action | Remain blocked pending AR-1540, AR-1541 and AR-1544. Preserve the exact v0.3.50 verifier result and the disposable failure evidence; resume AR-1534 only after all compatibility successors pass. |

### AR-1540 — Session and lifecycle contract compatibility

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Session/checkpoint/recovery compatibility is green against coordinator v0.3.53; close with AR-1549 evidence. |
| Next action | Promote and close from AR-1549&#x27;s v0.3.53 compatibility receipt; no additional ASB-owned session repair remains. |

### AR-1541 — SQLite fence compatibility and isolation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | SQLite/WAL fence compatibility is green against coordinator v0.3.53; close with AR-1549 evidence. |
| Next action | Promote and close from AR-1549&#x27;s v0.3.53 compatibility receipt; no additional ASB-owned SQLite repair remains. |

### AR-1542 — AR-1307 runner integration closure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close ASB-owned AR-1307 runner regressions after the coordinator v0.3.50 compatibility repairs and prepare the formal-readiness handoff. |
| Next action | Promote after AR-1532, AR-1534, AR-1540, AR-1541 and AR-1549 are done; run the exact v0.3.53 vendor-integrated AR-1307 runner gates and hand evidence to AR-1535. |

### AR-1543 — AR-1308 QEMU integration closure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Close ASB-owned AR-1308 QEMU and preflight regressions after coordinator v0.3.50 compatibility repairs and prepare the capacity handoff. |
| Next action | No development action remains. Preserve the unsigned-development diagnostic receipt; AR-1531/1536 exact formal-input work is separately scoped and fail-closed. |

### AR-1544 — State-worktree observation compatibility

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Historical v0.3.51 state-worktree blocker superseded by the verified v0.3.53 boundary and compatibility closure. |
| Next action | Historical blocker superseded by AR-1547 and AR-1549; preserve the rejected v0.3.51 evidence and do not resume this record. |

### AR-1545 — AR-1307 formal-input readiness repair

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Audit and repair the AR-1307 formal-input handoff after development runner integration, without executing qualification. |
| Next action | Formal-only work: after AR-1535 supplies reviewed inputs, inventory and independently verify every exact AR-1307 formal input for AR-1522. Do not block or alter the completed unsigned-development path. |

### AR-1546 — AR-1308 formal capacity-input readiness repair

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Audit and repair the AR-1308 capacity/input handoff after diagnostic QEMU integration, without executing qualification. |
| Next action | Formal-only work: after AR-1531 and AR-1536, verify the exact 8 GiB/8 GiB fixture and AR-1308 formal inputs for AR-1522. Do not block or alter the completed unsigned-development path. |

### AR-1547 — Coordinator v0.3.52 vendor adoption and compatibility rerun

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Adopt coordinator v0.3.52 and rerun the ASB state-worktree compatibility gates after the rejected v0.3.51 tag. |
| Next action | Promote and claim; record v0.3.52 vendor adoption, rerun AR-1540/AR-1541 compatibility and full state gates on the clean snapshot, then release AR-1544/AR-1534 successors with exact evidence. |

### AR-1548 — v0.3.52 formal and vendor fixture compatibility repair

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair ASB formal-tier and vendor-fixture compatibility defects found after adopting coordinator v0.3.52. |
| Next action | Promote after AR-1547; repair the ASB-owned formal-tier and vendor-fixture compatibility defects exposed by the v0.3.52 full state gate, then rerun focused and full gates. |

### AR-1549 — Coordinator v0.3.53 compatibility closure

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Rerun the compatibility gates previously blocked by the rejected coordinator vendor snapshots. |
| Next action | Promote and claim; rerun the state-worktree, session, SQLite and full compatibility gates against the verified v0.3.53 snapshot, then hand exact results to AR-1534/1542/1543. |

### AR-1550 — Compatibility blocker graph reconciliation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Reconcile stale compatibility blocker records after AR-1549 without claiming formal qualification. |
| Next action | Promote and claim; reconcile stale AR-1534/1540/1541/1544 blocker metadata with the verified v0.3.53 receipts, preserving historical failure evidence. |

### AR-1551 — First-customer platform authority deployment bootstrap

| Field | Value |
| --- | --- |
| Status | cancelled |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Optional future production-live platform authority bootstrap; not a development qualification requirement. |
| Next action | No development action: deployment-owned authenticated authority is optional future production hardening. If live-provider production is later authorized, create a separately scoped successor; local/mock authority is sufficient for development qualification. |

### AR-1552 — Dynamic workload-backed plan generation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Generate benchmark plans from the canonical supported-workload catalog, including workloads added later. |
| Next action | Implementation merged in ASB main; retain exact PR, provenance and hosted-check evidence. |

### AR-1553 — Plan creation CLI workflow

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expose dynamic workload plan creation through a simple ASB CLI command. |
| Next action | Implementation and qualification merged in ASB main; retain exact PR and test evidence. |

### AR-1554 — Global human-readable output mode

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make ASB commands human-readable by default and preserve JSON through a global --json flag. |
| Next action | Implementation merged in ASB main; retain exact PR, provenance and hosted-check evidence. |

### AR-1555 — Plan and output workflow qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify plan creation and output modes as one simple ASB user journey. |
| Next action | Release done: exact current main ce190124 qualifies dynamic plan creation, human/JSON output, local/mock run, report and compare workflow. |

### AR-1556 — Protected-main merge-topology gate repair

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair and verify the protected-main repository-quality gate after the plan/output merge series. |
| Next action | Promote after AR-1555 functional evidence; diagnose and repair the protected-main merge-topology gate for the plan/output series, then verify the exact current main checks. |

### AR-1557 — Protected-main receipt signature repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair protected-main signature evidence after the receipt PR rebase generated an unsigned topic commit. |
| Next action | Release done: signed forward repair 7aa09a0 passed exact protected-main policy and all required hosted checks. |

### AR-1558 — ASB plan/output release publication

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Publish the ASB release containing the dynamic plan and output-mode workflow after exact green-main verification. |
| Next action | Release done: signed tag asb-0.1.0-plan-output-ce190 published from exact green ce190124 and fresh checksum/doctor consumption passed. |

### AR-1559 — Machine consumer JSON opt-in repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the Rust workflow&#x27;s workload catalog JSON consumer after the human-output default change. |
| Next action | Release done: PR #395 merged at exact main ce190124 and all required hosted checks passed, including the rerun of Rust verification. |

### AR-1560 — State verification formatting repair

| Field | Value |
| --- | --- |
| Status | superseded |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the state repository formatting gate before publishing its coordination release. |
| Next action | Promote and format tests/test_handoffctl_vendor.py with the pinned Ruff tool; rerun exact state verification and record the repair. |

### AR-1561 — State strict-mypy repair

| Field | Value |
| --- | --- |
| Status | cancelled |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair strict mypy failures that prevent the changed coordination repository from reaching a releasable state. |
| Next action | Promote and resolve the latent strict-mypy import/typing failures after the formatter repair; preserve fail-closed optional authority boundaries and rerun hosted state verification. |

### AR-1562 — ASB TUI development release-channel contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add explicit ASB TUI release-channel selection with a development default. |
| Next action | Ready for independent review on exact rebased head c46be39 atop protected main 73029d9164808ca531713da9ff8fb575968f6d74; hosted PR #396 checks must verify channel-neutral lifecycle metadata and full quality gates before merge. |

### AR-1563 — ASB dev-channel clone/build materialization

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Clone and build the current asb-tui main head for the ASB dev channel. |
| Next action | Ready for independent re-review of PR #398 at exact head 46133cd. Verify live quota monitoring, concurrent bounded output drain, process-group descendant termination, staging cleanup preserving prior install, digest-bound atomic dev install, and unchanged stable channel. |

### AR-1564 — ASB development TUI lifecycle integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Integrate the dev-built TUI into the ASB lifecycle and launch path. |
| Next action | Ready for independent re-review of PR #399 at exact head 4a65476. Verify reversible marker/version trash transaction, injected final-delete failure restoration, dev lifecycle routing, stable isolation, and exact-current-main compatibility. |

### AR-1565 — ASB yanked dependency lock repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair the yanked dependency lock that blocks all protected ASB merges. |
| Next action | Run complete required ASB quality suite and obtain independent lockfile review; cargo-deny/cargo-audit binaries are absent on this host and must run in hosted/qualified environment. Then prepare exact-head PR from signed commit 54505f2. |

### AR-1566 — ASB development broker handoff integration

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire ASB development launch through the authenticated asb-tui broker handoff seam. |
| Next action | Remain blocked as historical evidence; the active real bridge work is tracked by TUI AR-1587 and ASB AR-1590, which must complete before this boundary can be closed. |

### AR-1567 — ASB development trusted toolchain discovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement trusted development cargo discovery |
| Next action | PR #401 is rebased onto current main 2eef71c at exact head bac495d0871c72b63bed9c55b2d2c557115a471d; hosted checks rerunning and independent review required before merge. |

### AR-1568 — ASB exact current-main identity binding

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Bind development metadata and broker descriptors to the exact ASB source identity. |
| Next action | Ready for independent review of PR #400 at exact head 665b6eb. Verify build-time exact checkout commit/tree derivation, required source headers, reproducible identity overrides, metadata/status/doctor identity validation, typed stale rejection, and unchanged stable behavior. |

### AR-1569 — ASB source-archive identity repair

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Repair merged identity generation so stable/source-archive ASB builds work without a Git checkout. |
| Next action | PR #402 is at exact head e05e7ff403ce6a1a91f4f05d5ea0c570eeb9d9d2; hosted checks rerunning after parent-git archive guard. Await independent review and green checks, then merge/release or repair. |

### AR-1570 — ASB dynamic development broker handoff

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Implement dynamic development broker handoff |
| Next action | Independent review and hosted green checks for PR #403 at f0b55e9f9e3056003b5bf949fc54ea7425c494ab |

### AR-1571 — ASB development broker channel transport handoff

| Field | Value |
| --- | --- |
| Status | blocked |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide the bounded broker channel transport that completes ASB to asb-tui launch handoff. |
| Next action | Remain blocked as historical evidence; the active exact inherited-fd qualification is tracked by ASB AR-1590 after TUI AR-1587 completes the real bridge. |

### AR-1572 — ASB approved development toolchain runner

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Private reproducible development toolchain runner hardened and proposed in PR #404. |
| Next action | Run hosted checks and obtain independent review for PR #404 at f423bca; then merge only after approval. |

### AR-1573 — ASB development control producer bridge

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expose the ASB-side development control producer bridge required by the asb-tui adopted stream. |
| Next action | Await all hosted gates and independent review of b4813cf; merge only identical green head, then release AR-1573 and promote AR-1574. |

### AR-1574 — ASB development control transport wiring

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Wire the ASB development launch transport to the producer control bridge. |
| Next action | Await AR-1578 workspace coverage recovery and hosted rerun; merge only identical green e2986e6 or later head, then release AR-1574. |

### AR-1576 — ASB development bootstrap projection

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make the development control backend satisfy the current asb-tui bootstrap projection without production credentials. |
| Next action | Promote and implement the development-only bootstrap projection contract required by current asb-tui startup. |

### AR-1577 — ASB interactive development supervision

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Keep successful development TUI sessions interactive while bounding handshake and cleanup failure paths. |
| Next action | Await hosted checks and independent review of PR #408 exact head e6f3d901dffba31845273fafd436f613d1485793; merge/release only identical green head. |

### AR-1578 — ASB workspace coverage recovery

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Recover the existing workspace coverage gate that currently blocks otherwise correct ASB transport changes. |
| Next action | Run exact workspace coverage gate on PR #407 using /srv/data target; continue only with concrete stable tests needed for 90&#37;, then merge/release or report measured blocker. |

### AR-1588 — ASB development-channel command surface

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Make ASB lifecycle commands consistently select and default the development release channel. |
| Next action | Promote after dependencies are released; implement and qualify consistent --channel selection with default dev across ASB lifecycle commands. |

### AR-1589 — ASB development-channel provenance and fault matrix

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify ASB development-channel identity, metadata integrity, and cleanup failure paths. |
| Next action | Promote after AR-1588; implement the development-channel provenance envelope and adversarial fault matrix without weakening stable verification. |

### AR-1590 — Inherited-fd cross-repository qualification

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Complete real ASB-to-asb-tui inherited-fd broker qualification after the PTY seam exists. |
| Next action | Obtain hosted execution and independent exact-head review for PR #416 at f439b35; only then reassess AR-1590 acceptance and release. |

### AR-1591 — Post-release fresh-clone ASB consumption

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Qualify fresh-clone consumption of the released development ASB journey. |
| Next action | Promote after the inherited-fd bridge and final cross-project qualification are released; run the fresh-clone post-release dev-channel journey and record exact evidence. |

### AR-1592 — ASB control catalog compatibility

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Add ASB control-protocol catalog compatibility required by the released asb-tui bootstrap journey. |
| Next action | Spec acceptance metadata is missing; coordinator must attach the required receipt/digest before done release can be admitted. PR #413 merged at f8c8d6b2c7b1476b91d0c93183864f23abadc488. |

### AR-1593 — Catalog protocol version alignment

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Align ASB and asb-tui catalog protocol versions so the real bootstrap can negotiate a common catalog-capable version. |
| Next action | Align the published BenchmarkCatalog version with the TUI common-version matrix, preserve older schema compatibility, and add cross-project negotiation evidence. |

### AR-1594 — Qualification coverage isolation

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Keep the real cross-repository qualification while preserving the enforced workspace coverage floor. |
| Next action | Release done after render and live doctor confirm the bound acceptance receipt. |

### AR-1595 — Development setup capability contract

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Expose provider, authentication, model, agent, and default-selection capabilities for the development wizard. |
| Next action | Rerun PR #415 hosted checks and obtain independent exact-head review at 25fe156c; do not merge until both approve. |

### AR-1596 — Cassette and offline lifecycle integration

| Field | Value |
| --- | --- |
| Status | done |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Provide deterministic cassette recording and provider-free replay for benchmark workloads. |
| Next action | Released: monitor downstream AR-1597 consumption of cassette/offline lifecycle. |

### AR-1597 — Fault matrix and deterministic runner

| Field | Value |
| --- | --- |
| Status | in_progress |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | ar1199-router-impl |
| Parent | None |
| Children | None |
| Summary | Exercise all setup, recording, replay, benchmark, and recovery failure paths with bounded evidence. |
| Next action | PR #420 exact head 32b5c514f3ca07eeaf18f3f0cb0c0b0b652f2bb0 is open; await hosted checks and independent review, then repair/merge only with green gates. |

### AR-1598 — Fresh-user development qualification

| Field | Value |
| --- | --- |
| Status | planned |
| Priority | P0 |
| Role | unassigned |
| Team | unassigned |
| Owner | Unclaimed |
| Parent | None |
| Children | None |
| Summary | Prove install-to-wizard-to-benchmark-to-offline-comparison works for a fresh development user. |
| Next action | Run the disposable fresh-user default-dev qualification after the fault-matrix runner is released. |


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
        AR_1449["AR-1449 - Blocked"]:::status_blocked
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
        AR_1589["AR-1589 - Planned"]:::status_planned
        AR_1590["AR-1590 - Done"]:::status_done
        AR_1591["AR-1591 - Planned"]:::status_planned
        AR_1592["AR-1592 - Done"]:::status_done
        AR_1593["AR-1593 - Done"]:::status_done
        AR_1594["AR-1594 - Done"]:::status_done
        AR_1595["AR-1595 - Done"]:::status_done
        AR_1596["AR-1596 - Done"]:::status_done
        AR_1597["AR-1597 - In progress"]:::status_in_progress
        AR_1598["AR-1598 - Planned"]:::status_planned
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
