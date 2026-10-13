# AR-1848 plan: graph extraction qualification

1. Run the complete extractor from a clean checkout and capture the DOT/SVG
   artifacts and deterministic registry counts.
2. Cross-check every configuration field, storage entity, command, option, and
   relation against the generated graph; investigate any omission as a product
   defect rather than adding a graph exception.
3. Run privacy scans and Graphviz/SVG structural validation, including the
   documented no-Graphviz path that preserves DOT output.
4. Add concise developer documentation and paired ASB/asb-tui consumption
   guidance, then obtain independent review and exact-head post-merge evidence.
