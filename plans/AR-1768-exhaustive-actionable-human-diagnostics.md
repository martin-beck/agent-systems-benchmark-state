# AR-1768 plan: exhaustive actionable human diagnostics

1. Define a concise sentence template for each cataloged diagnostic, not one
   template per broad class. State command outcome, precise cause, safe subject,
   mutation/retention result, and remediation.
2. Replace generic messages and code-to-spaces projections across all public
   families. Preserve distinct filesystem, configuration, provider/auth,
   network, runtime, tool/catalog, routed TUI, cancellation, timeout, partial,
   and reconciliation cases.
3. Render user-supplied or implicit local paths in a bounded unambiguous form.
   Name the exact parent/destination when it is the problem; never reveal secret
   values, raw provider bodies, internal temporary paths, or private evidence.
4. Validate next actions against parsed invocation and diagnostic context. Emit
   at most one copyable command when deterministic; otherwise give a concrete
   non-command correction and state whether retry is safe.
5. Add golden and semantic tests for every diagnostic variant: severity, cause,
   target, state change, recovery, wrapping, Unicode/control sanitization, shell
   safety, streams, exits, and JSON compatibility.
6. Update help, troubleshooting, setup, project/tool, live provider, execution,
   and record/replay guides with representative useful failures and warnings.

