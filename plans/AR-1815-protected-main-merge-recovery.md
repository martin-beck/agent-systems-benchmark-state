# AR-1815 plan

Create a forward-only, local signed integration recovery for the preserved
GitHub merge `15c80511` after exact-main policy, DCO, and portable provenance
checks rejected its `GitHub <noreply@github.com>` committer identity.

The worker must declare a dedicated branch/worktree, read the complete
development documentation, use `tools/integration/merge_pr.py`, preserve the
historical merge and reviewed tree, and never rewrite or force-update main.
Run focused policy/provenance checks, obtain independent exact-head review,
publish only from a clean signed DCO tree, wait for required CI, then verify
all exact-main workflows and record a bounded receipt. This is a development
repair; no TLC/model-check or live-provider run is required.
