# AR-1725 — Two-agent OpenRouter/TUI tutorial and installation guide

## Scope

Add a beginner-oriented, credential-safe tutorial and dependency guide to ASB's
documentation. It must cover the CLI `easy` setup/run/sweep path, the explicit
live OpenRouter path, the explicit local/mock path, result/report/compare, and
the corresponding ASB TUI/asb-tui steps. It must link cleanly from the README
and existing quickstart/workflow indexes.

## Required content

1. Prerequisites and installation on each supported distribution family, using
   pinned toolchain and package names from `PLATFORMS.md`; distinguish required
   development tools, optional sandbox tools, and unsupported native claims.
2. A two-agent example using only catalog-advertised agents/models and a bounded
   workload. Keep API keys out of files, argv, screenshots, transcripts, and
   evidence; explain environment/key-reference setup without printing values.
3. ASB CLI and TUI command/step sequences, expected terminal states, result
   reporting/comparison, cancellation/recovery, and links to deeper workflows.
4. Screenshots or terminal-rendered images generated from a deterministic,
   privacy-safe runner, with Markdown alt text and text-only equivalents.

## Gates

- Run the tutorial-contract validator and executable command examples.
- Check links, generated schema/tutorial inventories, formatting, and docs tests.
- Review distribution commands against the pinned platform manifest.
- Verify all visual artifacts contain no secrets/private paths and retain text
  alternatives.
- Run focused and full applicable gates, independent review, exact-head hosted CI,
  and post-merge documentation verification.
