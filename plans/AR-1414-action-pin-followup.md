# AR-1414: Follow-up install-action pin qualification

## Objective

Qualify the newly reopened PR #235, which updates `taiki-e/install-action` from
the already merged v2.87.12 pin to v2.87.14. Preserve immutable commit pins,
policy coverage, exact-head review, and all required CI gates.

## Constraints

- Do not weaken repository policy or replace immutable SHAs with floating refs.
- Verify the requested upstream release identity and record provenance.
- Use a clean isolated worktree with SSH-signed, DCO-certified commits.
- Merge only through handoffctl after independent review and green exact-head CI.
- Live providers and native hosts are not prerequisites.

## Acceptance

PR #235 is merged or truthfully closed as superseded with exact evidence; any
repair has focused/full tests, all required checks, and seven post-merge gates.
