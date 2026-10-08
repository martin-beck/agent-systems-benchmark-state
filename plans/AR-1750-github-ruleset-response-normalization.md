# AR-1750 plan: ruleset response normalization and guarded completion

## Fixed starting point

- Product main is signed merge dc19bb1b758a60b4fe316021ab9fe751aaae361d.
- Repository ID 1359260742 is owned by the martin-beck User account.
- The only ruleset is active branch ruleset ID 24750310.
- Settings remain pre-apply: merge, squash, and rebase enabled; auto-merge and
  web signoff disabled.
- AR-1748 stopped before PATCH. Its response-only ID receipt is authoritative;
  ownership may be upgraded only by exact ID-bound readback.

## Policy model

Development review is durable independent-agent Coordinator evidence. The same
GitHub user may author and publish after that independent review, so GitHub
cannot require approval from a different account. Request
required_approving_review_count=0 and require_last_push_approval=false.
Independent review, exact-head CI, signed local merge, DCO, portable provenance,
merge-only admission, and resolved review threads remain mandatory.

## Implementation and gates

1. Claim AR-1750 from exact state/product main. Read-only audit repository ID,
   main head, capability, complete inventory, and exact ruleset ID 24750310.
2. Split request payload from strict response canonicalization. Pin a current
   immutable official GitHub REST OpenAPI commit/blob/full-file digest that
   includes required_reviewers; send explicit required_reviewers=[].
3. Accept only server-added
   require_extra_approval_for_unattributed_changes=true. Reject false,
   non-boolean values, every other unknown key, and nonempty or malformed
   required_reviewers. Preserve exact equality for every other policy field.
4. Bind every PUT and audit to expected ID 24750310. Missing/changed/duplicate
   IDs, same-name foreign ID, changed foreign inventory, repository identity,
   head, owner plan/capability, or policy fail before mutation. Never delete or
   recreate the ruleset.
5. Add hostile request/response fixtures for normalization values and unknown
   keys. Prove PATCH cannot occur until the PUT response and fresh complete
   ID-bound inventory/detail readback are canonical and exact. Keep typed,
   bounded, privacy-safe ID receipts on every partial path.
6. Document the development-review/account boundary, immutable ownership
   receipt, rollback and partial-effect rules, guarded PUT command, and audits.
7. Run focused hostile and full repository quality, privacy, headers, coverage,
   supply-chain, and workflow gates. Require signed+DCO commits, independent
   exact-head review, all PR checks, signed exact-tree local merge, and all
   exact-main post-merge workflows.
8. After post-merge green, run one guarded apply with expected ID 24750310.
   PATCH settings only after verified readback. Stop without retry on rejection
   or ambiguity. On success run two separate ID-bound read-only audits and
   independently review the durable receipt.

## Acceptance

- Official schema pin admits explicit empty required_reviewers while request
  and response shapes remain separate and closed.
- Only the observed true/empty normalization is accepted; hostile variants and
  unknown fields fail without PATCH.
- Ruleset ID 24750310 is updated in place; repository identity, main head,
  capability, and foreign inventory remain stable.
- Development policy remains representable with same-account independent-agent
  Coordinator review and the remaining protected-main gates intact.
- One guarded PUT/PATCH and two clean ID-bound audits produce a privacy-safe,
  independently reviewed receipt before AR-1748 can be unblocked.
