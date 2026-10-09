# AR-1765 plan: end-to-end qualification

1. Create disposable HOME, PATH, project, and user-local tool roots; never use
   real credentials or mutate an existing project.
2. Execute the complete init -> install -> discover -> generate/select ->
   readiness -> benchmark -> results/report journey for every tool kind.
3. Exercise repeat, interruption, missing/unsafe/stale tools, incompatible
   catalogs, live/offline/mock boundaries, and human/JSON output.
4. Run focused, full applicable locked tests and hosted exact-head CI; publish
   the evidence receipt and concise fresh-user command sequence.
