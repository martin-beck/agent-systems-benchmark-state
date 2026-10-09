# AR-1762 plan: system and project discovery

1. Define the adapter probe interface and precedence between project records,
   project-local installs, and PATH tools without changing configured pins.
2. Implement bounded, deterministic discovery and typed availability/error
   diagnostics; avoid arbitrary execution during a scan.
3. Add `asb tool discover/list` human and `--json` output and fixtures for PATH,
   project roots, duplicate versions, missing binaries, unsafe symlinks, and
   stale records.
4. Prove repeated scans are stable and never modify project configuration.
