# AR-1533 plan: AR-1308 unsigned-development QEMU fixture repair

1. Read AR-1308, AR-1528, AR-1530 and AR-1531 plus all referenced plans and inspect the protected-main state runner and validator.
2. Reproduce the current unsigned-development fixture path with generated local inputs. Classify failures as fixture, launcher, cleanup, resource preflight, or evidence-contract failures; never substitute them for formal qualification.
3. Repair the minimal state-owned code/config/docs. Keep QEMU/container use portable, offline, bounded and private-root confined; deny network and alternate egress; clean up on success, timeout and cancellation.
4. Add positive and negative tests proving generated-seed development success, clear rejection of formal claims without exact inputs, deterministic cleanup, and sanitized `qualification_authorized=false` evidence.
5. Run focused fixture tests and all applicable state gates, then perform independent exact-head diff review, vendor/privacy checks and hosted CI.
6. Publish/merge only from a clean exact tree. Verify protected main after merge and hand remaining formal blockers to AR-1531/AR-1522 without changing their gates.

Acceptance: unsigned-development is reproducible with generated local inputs and no reviewed seed/signing authority; missing formal inputs produce actionable diagnostics and cannot authorize formal/publication/release; VM/network/resource cleanup and evidence sanitization are tested on success and failure; no product, asb-tui, handoffctl, credential, telemetry or native-host-only requirement.

