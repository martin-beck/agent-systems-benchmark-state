# AR-1761 plan: external-tool installation

1. Inventory ASB adapters and existing user-local install/channel conventions;
   define the supported installer registry and artifact source vocabulary.
2. Implement bounded per-kind installers with explicit version/source/platform
   selection, staging, digesting, atomic publication, and rollback on failure.
3. Persist only the AR-1759 installation record after successful verification;
   make repeated installs deterministic and safe.
4. Add human-first, `--json`, dry-run/status, unsupported-source, offline, and
   partial-failure tests using disposable roots and fixture tools.
