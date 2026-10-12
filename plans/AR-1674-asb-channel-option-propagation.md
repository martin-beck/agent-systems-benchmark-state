# AR-1674 implementation plan

## Scope

- Extend the versioned project configuration schema with a typed channel field.
  `asb project init` writes `dev` for every new project; compatible legacy
  channel-less configuration resolves to `dev` through an explicit migration
  path rather than an invisible per-command fallback.
- Establish one resolver with deterministic precedence: an explicit
  invocation `--channel` overrides the project value for that invocation only;
  otherwise the project value is used; a fresh or compatible legacy project
  resolves to `dev`. Unknown, malformed, or unavailable values return a typed
  diagnostic and never select another channel.
- Construct command context once after command parsing and pass the resolved
  channel through every executable command family: project/config, catalog and
  discovery, provider/agent/model, tool/workload, plan/run/sweep,
  report/compare, record/replay, easy, control/serve, and TUI lifecycle and
  launch. A family that has no current channel behavior still receives the
  context so no later behavior can bypass the contract.
- Keep `--help`, `--version`, and shell completion pure: they remain available
  outside a project and do not create, rewrite, or require project config.
- Report the resolved channel in human output and `--json` where it affects the
  operation, selection, artifact, or diagnostic. Retain visible but
  non-blocking development warnings for authentication, signature, and key
  material on `dev`.

## Validation

- Unit tests for schema serialization, fresh-init default, legacy compatibility,
  parsing, precedence, persistence, and typed unavailable values.
- Subprocess/table-driven command-surface tests proving every executable public
  command family obtains the same resolved project channel, including commands
  which currently only pass it through.
- Tests showing an explicit override does not rewrite project configuration,
  while a deliberate configuration update persists across a fresh process.
- Human and `--json` output tests for channel-aware success and failure paths,
  plus help/version/completion tests outside a project.
- Exact-current-main provenance for the `dev` artifact path.
