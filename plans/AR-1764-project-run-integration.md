# AR-1764 plan: project-aware benchmark execution

1. Audit all current setup/run/sweep/compare/report entry points and wire them
   to the canonical project resolver, inventory, and selected catalog.
2. Add readiness validation and actionable install/discover/select diagnostics;
   keep result paths project-bounded and preserve existing live/offline modes.
3. Add command-level tests for valid selections, missing/stale tools,
   incompatible catalogs, multiple agents, and human/JSON output.
4. Run the existing benchmark workflow tests and applicable locked gates.
