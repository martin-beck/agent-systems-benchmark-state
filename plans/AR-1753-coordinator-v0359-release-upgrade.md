# AR-1753 — Coordinator v0.3.59 release upgrade and integrity repair

## Scope

Replace the current Coordinator v0.3.57 development vendor snapshot with the
official complete v0.3.59 release snapshot. The source must be a clean checkout
whose `HEAD` equals the exact release commit and whose tree/tag provenance has
been independently verified. Use the upstream release `sync` path, review the
entire add/change/remove set, and leave every vendored byte identical to the
release manifest.

Repair only ASB-owned integration surfaces exposed by the upgrade. This includes
downstream fixtures, allowlists, compatibility adapters, generated projections,
formal launch integration, and tests, but never an in-place edit of a vendored
file. Preserve existing task meaning, development-only warning semantics, and
all unrelated work.

## Acceptance

- `coordinator.vendor.json` is the canonical schema-v1 release manifest for
  `v0.3.59` and binds the exact upstream commit and complete vendored file
  digest set. The immutable receipt separately records and verifies the Git
  tree determined by that commit; do not add a noncanonical manifest field.
- Offline vendor verification and an independent source-to-vendor byte
  comparison pass with no untracked or locally patched vendored bytes.
- Task/schema validation, generated-view checks, privacy and source-header
  checks, strict Ruff and mypy, the complete state unit suite at the unchanged
  95% branch-aware coverage floor, and applicable formal/vendor gates pass.
- `handoffctl reconcile`, clean-tree verification, and `doctor --live` pass on
  the exact reviewed candidate and again after integration.
- Every failure caused by the update is either repaired in a downstream-owned
  file with regression coverage or recorded as a precise external blocker; no
  gate is lowered or bypassed.
- A different agent independently reviews the exact head/tree. Hosted CI passes
  before a signed+DCO exact-tree merge, and exact-main CI passes afterward.
