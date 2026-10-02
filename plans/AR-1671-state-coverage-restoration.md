# AR-1671 — Restore ASB state coverage floor after Coordinator vendoring

Establish exact-base and exact-v0.3.53 coverage receipts, inventory every
uncovered restored module, and port the authoritative Coordinator behavior and
negative tests needed to reach the unchanged 95% branch/line gate. Cover
barrier admission, repository identity, staged commit/rollback, WAL/SHM
recovery, roles, upgrade identity, and lifecycle failure paths. Run the full
state workflow and independent review; do not use exclusions or threshold
changes.
