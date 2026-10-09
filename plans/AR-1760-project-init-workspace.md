# AR-1760 plan: project initialization

1. Reconcile the existing ASB workspace/result conventions with AR-1759 and
   select the canonical project root (defaulting to the current directory).
2. Add `asb project init [PATH]` with atomic directory/config creation,
   idempotent reruns, explicit refusal of conflicting files, and safe
   symlink/traversal handling.
3. Add human-first and `--json` output, including paths and next actions but no
   credentials or private host details.
4. Test fresh, repeated, partially-created, read-only, symlink, and nested
   project cases in disposable directories.
