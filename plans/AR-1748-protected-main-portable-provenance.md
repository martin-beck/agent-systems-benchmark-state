# AR-1748 plan: portable protected-main provenance and capability admission

## Incident and boundary

AR-1746's reviewed product repair merged as
`2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb`; all nine exact-main workflows
passed. Its only live apply was rejected before mutation with GitHub HTTP 422,
and two normalized audits observed the unchanged pre-state. The exact rejected
payload included `committer_email_pattern`, a metadata restriction documented
for Enterprise organizations, while `martin-beck/agent-systems-benchmark` is a
public user-owned GitHub Free repository. The checked-in sanitizer retained the
status and safe top-level message but discarded the validation field, so this
classification is high-confidence rather than a claim about unseen response
bytes.

This AR owns the product-side portable enforcement, capability preflight,
bounded diagnostics, independent review, signed local merge, hosted
qualification, and one subsequent live settings transaction. It must not
rewrite history, delete foreign rulesets, expose authentication material,
require Enterprise or a second GitHub account, weaken signature/DCO/review
requirements, or touch ASB runtime/provider/TUI behavior.

## Portable provenance contract

1. Add a deterministic required CI job whose stable context is included in
   `REQUIRED_CHECKS`. On a pull request, examine the exact base-to-head commit
   range and fail unless every in-scope commit has an accepted GitHub
   verification result, an allowed signing-key identity under the existing
   signing policy, and a matching DCO trailer. Reject GitHub Web Flow and
   `noreply@github.com` author/committer identities, unexpected parent shapes,
   stale/missing commit data, truncated pagination, API ambiguity, and a
   mismatch between checked head and event head.
2. On push to `main`, additionally prove that the new integration commit is a
   signed two-parent merge, its first parent is the previous main, its second
   parent is the reviewed PR head, its tree equals the reviewed candidate tree,
   and its DCO/signing identity is accepted. Bind any API-derived PR identity
   unambiguously; reject zero, multiple, closed-without-merge, stale, or
   mismatched candidates. Preserve a safe bootstrap path for the AR's own
   post-merge run without creating an unenforced interval.
3. Keep the enforcement implementation bounded, offline-testable, and
   privacy-safe. Untrusted Git metadata and API fields are data, never shell
   syntax. Bound response size, item count, pagination, time, and diagnostics.
   Never print tokens, headers, email addresses outside the allowlisted policy,
   raw authenticated responses, host paths, or unrelated commit history.
4. Test hostile histories: unsigned/unknown/bad signatures, missing or
   mismatched DCO, Web Flow identities in author and committer positions,
   deceptive display names, Unicode/control input, single-parent/squash,
   octopus merges, wrong first/second parent, tree mismatch, stale refs,
   ambiguous PR association, pagination truncation, API failure/timeout, and
   malicious commit messages. Include valid local SSH-signed two-parent merge
   fixtures using the repository's documented integration path.

## Capability-aware settings admission

5. Split the ruleset model into generally available core enforcement and
   optional capability-gated metadata restrictions. Fetch and validate bounded
   repository owner type, visibility, plan/capability evidence, repository ID,
   and current rulesets before POST/PATCH. Never infer Enterprise capability
   merely because an OpenAPI schema includes the rule.
6. For the current public user-owned repository, omit the unavailable metadata
   rule only after the portable provenance context is present and successful on
   exact main and is included as a strict required status check. The auditor
   must reject a core-only ruleset when the portable check is absent, stale,
   optional, skipped, or not required.
7. On a capability that truthfully supports metadata restrictions, retain the
   stronger rule as defense in depth. Unknown owner/plan/capability evidence
   fails before mutation. Pin and test the official OpenAPI structural schema,
   but keep backend capability admission separate from structural validity.
8. Preserve privacy-safe diagnostic details sufficient to classify future 422
   responses: allowlist bounded `errors[].resource`, `field`, and `code` values
   or map them to stable internal enums. Do not echo arbitrary response
   messages, request URLs, authenticated payloads, or secrets. Tests must prove
   sanitizer behavior for hostile nested responses and oversized output.
9. Model settings apply as an observed transaction. Record the normalized
   pre-state, apply repository merge-method/signoff settings and one exact
   main-targeted ruleset, then re-read all relevant state. A rejection before
   mutation, partial mutation, server ambiguity, changed repository identity,
   duplicate/foreign ruleset, or post-read mismatch fails closed and records
   the exact recovery boundary. Never delete or rewrite an unrelated ruleset.

## Review, merge, and live completion

10. Run focused provenance/settings tests, full project quality and privacy
    suites, source/header checks, signature+DCO verification, and all applicable
    exact-head hosted workflows. Use an isolated exact-main worktree and keep
    the topic tree clean.
11. Obtain a separate independent technical-worker review bound to the exact
    candidate commit and tree. Same-account GitHub approval is sufficient for
    this development integration; no authorized-maintainer or second-account
    gate may be introduced.
12. Merge only through the documented signed local two-parent procedure after
    exact-head checks pass. Verify remote readback, parents, reviewed tree,
    accepted SSH signature, and matching DCO. Watch every exact-main
    post-merge workflow to terminal success, including the new provenance job.
13. Only then perform one bounded live settings apply. Immediately audit the
    normalized repository settings and ruleset twice, obtain independent review
    of the privacy-safe receipt, and record exact rule/check identities. Do not
    blindly retry a rejected, partial, or ambiguous external effect.

## Acceptance and handoff

AR-1748 is done only when the current repository exposes merge commit as the
sole PR merge method, disables squash/rebase/auto-merge, requires web signoff,
and has one active `main` ruleset enforcing PR review, resolved threads, strict
required checks (including portable provenance), accepted signatures,
merge-only integration, deletion prevention, and non-fast-forward prevention.
Two consecutive audits and an independent worker must accept the live receipt.
AR-1722 may count the external-settings blocker cleared only from this evidence;
Coordinator vendor/unblock adoption remains separately owned by AR-1747.
