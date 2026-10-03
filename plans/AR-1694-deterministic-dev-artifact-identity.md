# AR-1694 Deterministic ASB development artifact identity

Make the ASB-owned development TUI materializer reproducible across disposable
workspace and cargo-home paths. Normalize build-path identity without weakening
trusted toolchain, source-head, manifest, executable digest, or warning-only
development authentication rules, and add a regression proving repeated
materializations produce the same executable digest and can consume the same
handoff manifest.
