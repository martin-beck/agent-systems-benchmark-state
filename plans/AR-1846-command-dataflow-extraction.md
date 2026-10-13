# AR-1846 plan: command and option dataflow extraction

1. Discover the complete `asb` CLI command tree and option metadata from the
   authoritative parser/dispatch definitions, including aliases and JSON mode.
2. Connect commands and options to registry entities through shared relation
   APIs. Record creates, reads, updates, validation, process launch, and result
   emission, including conditional branches and remediation paths.
3. Generate a stable command-flow document with logical names, lifecycle order,
   relation kinds, and source ownership. Redact credential values and private
   paths while retaining enough identity for reproducibility.
4. Add a coverage test that fails when a command or option is added without a
   relation declaration or extractor hook.
5. Qualify the full setup-to-results route and obtain independent review.
