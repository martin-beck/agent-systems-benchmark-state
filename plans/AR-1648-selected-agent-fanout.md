# AR-1648 — Selected-agent/workload fan-out

Add a bounded typed request that fans out the persisted selected agents and
workloads into durable plan/run references, with idempotency, cancellation, and
reconciliation. Offline fan-out must bind each tuple to its cassette digest and
runtime replay authority without provider fallback.
