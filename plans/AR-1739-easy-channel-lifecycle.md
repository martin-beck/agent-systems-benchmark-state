# AR-1739 plan: easy channel lifecycle

1. Extend the existing native `asb easy` command family with a guided,
   human-readable lifecycle for `build`, `install`, `update`, `test`, `status`, and
   `remove`; do not introduce Make, Just, Python, shell, or another runtime
   dependency for end users.
2. Reuse the existing channel-manifest, install-root, active-channel,
   rollback, and diagnostic contracts. Support an explicit channel selector
   (`dev`, `stable`, `nightly`, or `experimental` where available), preserve
   the active channel when omitted, and reject unavailable or ambiguous
   selections before mutation. In development qualification, `--channel stable`
   is a local mock fixture only: it must not fetch, require, or imply the future
   public stable channel and must be visibly labelled as mock.
3. Make the guided path safe and scriptable: show a concise next-step prompt
   or confirmation for mutating operations, provide `--yes`/`--dry-run`, emit
   the versioned JSON envelope with `--json`, preserve bounded diagnostics,
   and never print credentials or private host paths.
4. Define `test` as a bounded channel smoke/lifecycle check that exercises
   install/status/launch/upgrade/remove prerequisites without contacting a
   provider unless an explicit live test is separately requested. Include
   rollback and interrupted-operation recovery guidance. The stable mock must
   exercise the same lifecycle shape without creating public-release evidence.
5. Define `build` as a bounded reproducible artifact build for the selected
   channel/profile, with clear output paths, digest reporting, dry-run/JSON
   support, and no implicit publication or channel promotion.
6. Add positive and negative CLI/contract tests, shell completions and
   operator documentation with examples for first install, switching or
   updating a specific channel, dry runs, testing, rollback, and removal.
   Requalify exact current-main lifecycle behavior and required hosted gates.
