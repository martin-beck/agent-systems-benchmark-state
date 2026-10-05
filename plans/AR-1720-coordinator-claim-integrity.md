# AR-1720 — claimed-task identity and coordinator integrity

## Scope

Repair the ASB state coordinator so a claimed AR cannot be silently reused,
renumbered, or have its scope/owner/dependencies replaced by a concurrent
state writer. Preserve the existing task history, claims, leases, and generated
views; migrations must be explicit, append-only, and auditable.

## Required work

1. Add immutable task identity and claim-fingerprint validation covering the AR
   id, title, summary, dependencies, plan, spec reference, owner, claim lease,
   and task revision. A mutation must fail closed unless it presents the exact
   expected revision and active claim owner where ownership is required.
2. Add a coordinator-mediated migration operation for collision repair. It must
   preserve the old task record, lease, owner, and scope in an append-only
   migration record, allocate a fresh id, and reject identity changes to an
   active claim through ordinary update/reconcile paths.
3. Add duplicate-id, claimed-identity-change, stale-revision, concurrent
   migration, and migration-replay tests. Generated CURRENT/STATUS views must
   be derived only after the source transaction passes validation.
4. Repair stale worktree/replica diagnostics so `doctor --live` reports a typed
   recoverable condition instead of aborting on a missing worker checkout.
5. Reconcile the current remote state without overwriting unrelated dirty local
   files, record the AR-1718/AR-1719 collision as historical evidence, and
   verify that both surviving ARs retain their intended scope and leases.

## Acceptance and safety

- Existing claimed ARs are unchanged except through an explicit signed
  migration record.
- Two concurrent writers cannot both mutate or migrate one claimed task.
- A replayed/stale mutation is rejected without changing tasks or projections.
- Full coordinator tests, schema validation, generated-view checks, signed
  exact-head CI, and live doctor pass after reconciliation.
- No task, status projection, private runtime file, credential, or unrelated
  worker worktree is deleted or force-updated.

## Non-goals

- Do not close, release, or reassign AR-1718 or AR-1719 as part of this repair.
- Do not rewrite existing Git history or repair the collision by editing the
  historical commits.
