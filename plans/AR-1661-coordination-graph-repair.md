# AR-1661 — coordination graph repair

Use the Git-backed coordinator to inventory malformed task front matter,
missing dependency records, and dependency cycles. Repair historical metadata
with evidence-preserving changes, establish an acyclic dependency graph for
active ARs, regenerate `CURRENT.md`/`STATUS.md`, and prove the result with the
coordinator schema and render checks. Do not close or promote product ARs as a
side effect.
