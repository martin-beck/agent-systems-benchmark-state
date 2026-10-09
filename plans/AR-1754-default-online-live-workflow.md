# AR-1754 plan: default-online ASB workflow

## Scope

Inventory and normalize all user-facing benchmark entry points that currently
require an optional online/live switch or force local mock. The configured
provider path becomes the default in development; mock and strict replay remain
explicit alternatives.

## Required behavior

- `run` and `sweep` use the configured provider by default; `--local-mock` is
  explicit and labeled development-only.
- `easy run` and `easy sweep` follow the same default and offer a clear mock
  override; setup remains warning-only when credentials are absent.
- Recording/campaign commands default to online only where they create provider
  effects; `--local-mock` and offline replay are explicit and never implicit.
- TUI/control handoff carries the same mode and selection contract without
  making the frontend an authority or changing the separate asb-tui source.
- Missing credentials, transport errors, unsupported selections, and absent
  runtime authority produce actionable typed errors; there is no silent mode
  fallback.

## Dependencies and boundaries

AR-1699/1700 provide the development credential/live boundary. AR-1723/1724
provide the narrower easy-run/easy-sweep work and must be current before this
integration AR is promoted. Production-owned runtime authority remains a
separate optional hardening path and must not be weakened or made implicit.

## Evidence and gates

Add positive and negative CLI, easy, and TUI-contract tests; verify credential
redaction, mode identity, provider/model/agent/workload binding, bounded output,
network/cost warnings, and no-fallback behavior. Run focused and full locked
Rust gates, exact-head hosted checks, independent review, and post-merge exact
main verification. Record a concise operator quickstart update and a durable
acceptance receipt.
