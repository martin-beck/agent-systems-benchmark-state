# AR-1537 plan: close the downstream vendor bootstrap allowlist

1. Read the ASB vendor contract, `tools/handoffctl_vendor.py`, AR-1534 and
   the exact coordinator v0.3.50 source manifest. Reproduce the failure in a
   disposable target: the installed helper imports modules absent from the
   target because the pre-v0.3.50 allowlist is incomplete.
2. Expand only the allowlisted coordinator snapshot paths required by the
   released v0.3.50 runtime, schemas, formal evidence and vendor tests. Keep
   source paths and destination paths explicit; reject unknown files,
   symlinks, path escapes and incomplete staging.
3. Add positive and negative tests proving a clean v0.3.50 sync leaves a
   self-contained verifier and that missing source files or post-install
   verification failures restore the prior snapshot. Do not modify
   `tools/handoffctl.py`, extract it, rewrite the manifest, or weaken digest
   verification.
4. Run vendor-focused tests, the complete ASB state suite, strict lint/type/
   format/privacy/schema/generated-view gates and independent diff/signature
   review. Publish through the normal reviewed workflow.

Acceptance: the existing ASB state tool remains usable before and after the
upgrade, a clean coordinator v0.3.50 sync installs every declared dependency,
and the installed verifier passes on the exact immutable snapshot.
