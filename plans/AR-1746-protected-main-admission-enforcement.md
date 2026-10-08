# AR-1746 plan: protected-main admission enforcement

## Incident and ownership

ASB AR-1722 preserved the PR #487 reviewed-tree/merge-tree failure and added
the checked-in settings auditor and signed local merge procedure. The product
repair is already present, but GitHub's live repository configuration still
permits merge, squash, and rebase, has web signoff disabled, exposes no active
ruleset, and reports no classic branch protection for `main`. This AR owns only
the live `martin-beck/agent-systems-benchmark` admission configuration and its
privacy-safe evidence. It must not modify ASB runtime behavior, rewrite product
history, or conflate later PR #505/AR-1742 recovery.

## Required implementation

1. Record a fresh bounded pre-change snapshot using the checked-in
   `tools/integration/repository_settings.py` auditor and direct GitHub API
   reads. Bind the observation to the exact auditor commit and repository ID;
   do not record tokens, headers, raw authenticated payloads, host paths, or
   unrelated repository settings.
2. Review the exact apply payload before mutation. It must leave merge commits
   as GitHub's sole enabled pull-request method, disable squash, rebase, and
   auto-merge, require web signoff, and create or update one active ruleset
   targeting only `main`.
3. The ruleset must require pull requests, one fresh approval that may come
   from the same GitHub account after an independent technical-worker review,
   resolved conversations, strict exact-head required checks, verified
   signatures, and merge commits. It must reject GitHub Web Flow commits and
   prevent deletion and non-fast-forward updates. It must not require a second
   account, an authorized-maintainer review, production credentials, or a
   verified-release attestation for development integration.
4. Apply through the checked-in bounded tool. Treat partial mutation,
   permission failure, API ambiguity, a changed repository identity, or an
   unexpected existing ruleset as a failed transaction requiring a fresh
   read/audit; never guess success or delete unrelated rulesets.
5. Run the auditor again and independently compare the normalized live
   settings and ruleset with the repository contract. Exercise local fixture
   tests for missing permissions, partial apply, duplicate/foreign rulesets,
   stale required contexts, Web Flow rejection, and idempotent re-application.
6. Prove the existing `merge_pr.py` path remains compatible: a clean isolated
   fixture must construct an SSH-signed, DCO-bearing two-parent merge whose
   parents and tree match the exact reviewed base/head/tree, reject stale refs
   and mismatched trees, and use a target-ref lease. Do not publish a no-op
   product commit merely to manufacture evidence.
7. Obtain independent technical review of the exact live contract and receipt.
   Record only normalized settings, ruleset identity, exact auditor/product
   commits, fixture results, and relevant GitHub request/run identifiers.
8. Release only when the live audit is green and repeatable. If GitHub denies
   the required mutation, leave this AR blocked with the exact typed failure;
   do not weaken the contract or classify development authentication policy as
   a functional blocker.

## Acceptance and handoff

AR-1746 is done when two consecutive bounded audits observe the required live
contract, the failure/partial-apply and signed-integration fixtures pass, and an
independent worker accepts the privacy-safe receipt. Completion removes the
external-settings half of AR-1722's blocker. AR-1722 may be reopened only after
AR-1747 also supplies a supported Coordinator `unblock` transition.
