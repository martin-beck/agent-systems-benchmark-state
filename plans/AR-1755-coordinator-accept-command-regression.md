# AR-1755 — Restore coordinator acceptance command after v0.3.59 upgrade

Restore the downstream-owned acceptance mutation that existed before the
v0.3.59 vendor upgrade but is absent from the current `handoffctl` CLI.

Scope is limited to `tools/handoffctl.py`, its tests, and coordinator usage
documentation. Vendored Coordinator files remain byte-identical to v0.3.59.

Acceptance requires:

- `handoffctl accept TASK` is parsed and dispatched;
- active owner, status, exact revision, task spec/ref revision, allowed
  evidence class, public evidence reference, and `sha256:` digest are checked;
- valid acceptance writes only the canonical `spec_acceptance` object;
- malformed, stale, mismatched, unknown, or unauthorised inputs fail without
  mutation;
- full state tests, coverage, privacy, vendor integrity, generated views,
  signed/DCO review, hosted CI, exact merge, and post-merge doctor pass.

After merge, use the restored command to attach acceptance to AR-1729 and
AR-1730 before releasing those dependency tasks.
