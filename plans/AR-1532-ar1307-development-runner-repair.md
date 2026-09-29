# AR-1532 plan: AR-1307 unsigned-development runner repair

1. Read AR-1307, AR-1528, AR-1530 and their plans, then inspect the exact protected-main state runner, schema, docs and tests.
2. Identify every development-path check that incorrectly requires reviewed formal seed bytes, a seed digest, signed bundle/provenance, publication evidence, or a native host. Preserve those checks for formal and release profiles.
3. Repair the smallest state-owned surface. Keep command execution bounded, argv-only, offline, private-root confined, cancellation-safe and free of retained subprocess output. Reject unknown profile/input fields.
4. Add generated documentation plus positive and negative tests for generated disposable seeds, missing formal inputs, profile separation, timeout/cleanup and sanitized non-qualifying evidence.
5. Run focused tests, the complete applicable state suite, format/lint/type, vendor and privacy gates. Independently review the complete diff and exact head.
6. Publish only from a clean exact tree through reviewed PR/CI. After merge, verify protected-main equality and record durable evidence. Do not claim AR-1307 formal qualification.

Acceptance: unsigned-development runs with generated local/mock inputs; formal/release profiles still fail closed on missing or mismatched exact inputs; tests cover allowed execution and forbidden qualification claims; no product, asb-tui, handoffctl, credential, telemetry or native-host change.

