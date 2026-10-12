# AR-1822 implementation plan

1. Reconcile current state `main`, inspect the role assignment validator,
   `roles.remove`, CLI dispatch, and existing role tests. Preserve the existing
   schema, registry, evidence, and exact-revision contracts.
2. Change only removal's validation path so cleanup can validate the explicit
   target's structure and registry references without treating expiry as an
   admission/read check. Validate all non-temporal safety properties and reject
   malformed state, malformed target, unknown roles, duplicate roles, invalid
   evidence, missing target, and stale revision.
3. Add focused positive tests for removing an expired target and for removing
   an expired target while an unrelated assignment is also expired. Add
   negative tests proving list/check/admission still reject expiry and remove
   still rejects malformed, missing, and stale inputs. Document the distinction
   between cleanup mutation and authorization/admission.
4. Run focused role tests, the applicable handoffctl suite, schema/generated
   view/vendor/privacy checks, and bounded product gates. Commit with SSH
   signature and DCO, publish a clean PR, obtain independent exact-head review
   and CI, then perform signed local integration and post-merge verification.
   Do not run TLC for this development AR and do not edit roles.json directly.
