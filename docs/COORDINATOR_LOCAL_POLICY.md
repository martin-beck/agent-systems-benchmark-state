# State-repository coordinator policy

Development review identity is defined in
[`DEVELOPMENT_REVIEW_POLICY.md`](DEVELOPMENT_REVIEW_POLICY.md). An independent
technical review-worker remains mandatory, but a same-account GitHub approval
is sufficient for development integration after exact-head checks, signatures,
DCO, privacy, and post-merge assurance requirements pass. No separate
authorized-maintainer or second-account approval is required. Verified release
and provenance gates remain unchanged.

This file contains project-local policy; `docs/agent-workflow-coordinator.md` remains an
unaltered vendored coordinator release document.

Before merging, require exact-head tests, privacy checks, SSH signature/DCO validation and
independent review. Confirm the topic is based on current `main` and that the protected-main
merge tree equals the reviewed topic tree; rebase and requalify stale PRs before merging.
Merge a ready PR only through the repository's protected merge path; a green PR is not complete
until its immutable merge commit is identified.

Immediately after merging, watch every required post-merge assurance workflow for the exact
resulting main SHA until each reaches a terminal result. Record workflow names, run IDs,
conclusions, and failures or cancellations in the owning task; do not classify a merge as
released or usable while post-merge assurance is pending or failed.

Release to `done`, `open`, or `blocked` with the merge and post-merge evidence; reconcile and
run the live doctor.
