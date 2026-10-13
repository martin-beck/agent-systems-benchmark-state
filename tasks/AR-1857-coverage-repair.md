---
{"branch":"codex/ar1857-coverage-repair","checkpoint_commit":"","claim_expires":"","depends_on":[],"id":"AR-1857","next_action":"Repair the recorded 94% full-gate coverage deficit without lowering the 95% threshold; preserve PR #145 unmerged until review and exact-head CI pass.","owner":"","plan":"../plans/AR-1857-coverage-repair.md","priority":"P0","schema_version":1,"spec_acceptance":{"evidence_class":"mechanical","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1857.json","spec_revision":1,"status":"pending"},"spec_ref":"specs/AR-1857.json","spec_revision":1,"status":"planned","summary":"Restore the full-gate coverage floor after the terminal 94% observation.","task_revision":1,"title":"Full-gate coverage floor repair","updated_at":"2026-10-13T17:10:00+00:00","worktree_key":"agent-systems-benchmark-state-ar-1857-coverage-repair"}
---

Successor to AR-1849 for the independent coverage seam. The terminal full run
passed 1,636/1,636 tests but measured 19,785 statements at 94%, below the
required 95% branch-aware floor. PR #145 remains unmerged. This task must not
modify AR-1841 or AR-1856 ownership and must not weaken formal/resource gates.

- 2026-10-13T17:10:00+00:00: Created as a narrowly scoped successor for the exact 94% versus 95% coverage blocker recorded by AR-1849.
