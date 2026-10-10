# AR-1781 plan: external workload acquisition catalog

1. Inventory canonical ASB workloads and every external workload claimed in
   documentation/adapters. Seed the development set with agentbench, agentdojo,
   agentops, ai-agents-that-matter, aider-polyglot, bigcodebench, core-bench,
   evalplus, exercism-tracks, hal, harbor, helm, inspect-ai, livecodebench,
   swe-bench, swe-bench-pro, swe-fficiency, swe-lancer, swe-mini, swe-perf,
   swe-rebench, tau-bench, and terminal-bench.
2. Define a versioned workload catalog schema covering official primary source,
   immutable identity, proof, license/terms, size/resources, preparation closure,
   adapter, and compatibility.
3. Add reviewed entries/fixtures for every listed suite. Development support
   means installable, selectable, and bounded-executable; retain genuine
   license/resource/compatibility negative examples, but do not use missing
   production authorization or qualification as an exclusion.
4. Define contributor admission, license/provenance review, update/revocation,
   and cache/offline rules without credentials or private paths.
5. Validate schema/inventory/provenance and obtain independent exact-head review.
