# AR-1635 — Control-state ownership test isolation

Repair the ASB production-backend idempotency test and temporary control-state
root lifecycle so the hosted suite is deterministic under parallel execution.
Preserve real ownership and recovery semantics; do not weaken locking, lower
coverage gates, or delete shared state broadly.

Acceptance:

- Reproduce or explain the hosted failure with bounded evidence.
- A signed repair passes focused control tests repeatedly and the full workspace suite.
- Required hosted checks pass on the exact reviewed head.
- Paired AR-1632 and AR-1615 qualification runs without cross-test state collisions.
- Development-only missing authentication, signatures, and key management remain warning-only.
