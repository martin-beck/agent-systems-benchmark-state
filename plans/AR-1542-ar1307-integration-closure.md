# AR-1542 plan: AR-1307 runner integration closure

1. Read AR-1307, AR-1308, AR-1532, AR-1534, AR-1540, AR-1541 and AR-1535
   completely, then verify the exact dependency heads and approved v0.3.50
   vendor snapshot.
2. Create one disposable clean worktree and run the AR-1307 runner,
   checkpoint/resume/recovery, privacy, vendor, lint, type and full-state gates
   with network disabled. Preserve bounded, sanitized failure classifications.
3. Repair only ASB-owned runner fixtures, session-aware tests, adapters or
   generated documentation. Do not edit handoffctl, coordinator source,
   formal validators, resource limits or signed-input policy.
4. Add positive and negative coverage for generated-seed development,
   missing-formal-input rejection, timeout/cancellation cleanup, stale session
   and checkpoint handling, done-admission evidence, and
   `qualification_authorized=false` separation.
5. Independently review the complete diff and signatures/DCO/privacy evidence;
   publish only a clean exact-head signed+DCO PR and wait for required checks.
6. Update AR-1307 and AR-1535 with the exact sanitized evidence, or leave a
   precise external formal-input blocker. Never claim formal qualification from
   this AR.

Success is a reproducibly green ASB-owned development path against the
approved vendor release plus a truthful formal handoff boundary.
