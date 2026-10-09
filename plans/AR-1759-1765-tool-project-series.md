# ASB external-tool and project workspace AR series

This series makes a fresh ASB checkout usable with a small, discoverable
workflow: initialize a project, install or detect tools, select generated
catalogs, and run benchmarks with results kept in that project. It extends the
existing ASB CLI/config/catalog contracts; it does not create a second config
authority and it does not modify ASB-TUI in this series.

Dependency order:

`AR-1759 -> AR-1760 -> {AR-1761, AR-1762} -> AR-1763 -> AR-1764 -> AR-1765`

`AR-1761` and `AR-1762` may proceed in parallel after the project/schema
contract is merged. Existing provider/model and TUI ARs remain owners of their
specific integrations; these ARs own the generic external-tool inventory,
project layout, installer/discovery contract, and catalog selection metadata.

All commands retain human-readable output by default and accept `--json` for
machine-readable output. Development mode is warning-only for missing
authentication, signatures, and key management; no new security prerequisite
may block local installation, discovery, catalog generation, or test fixtures.
Credentials and secret values must never be written to project state.
