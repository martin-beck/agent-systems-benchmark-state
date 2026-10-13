# AR-1847 plan: Graphviz and SVG export

1. Add a documented developer command (or script subcommand) that runs the
   model/entity/command extractors and writes a DOT artifact to an explicit
   output directory.
2. Build clustered graph sections for settings/model fields, storage entities,
   commands/options, and lifecycle phases. Use stable IDs, readable logical
   labels, edge relation labels, and rank/layout settings suited to a normal
   developer screen without dropping detail.
3. Invoke Graphviz `dot` to produce SVG beside the DOT file. Keep the DOT file
   when Graphviz is absent and report a copyable installation/remediation
   message; do not make normal ASB execution depend on Graphviz.
4. Add deterministic snapshots/structural checks for node and edge counts,
   privacy redaction, valid DOT, valid SVG, and stable output ordering.
5. Document how to inspect, regenerate, and compare the graph, then obtain
   independent review and exact-head evidence.
