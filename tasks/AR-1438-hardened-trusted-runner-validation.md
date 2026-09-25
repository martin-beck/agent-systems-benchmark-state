---
{
  "branch": "repair/ar-1438-hardened-trusted-runner-validation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T14:09:24+00:00",
  "depends_on": [
    "AR-0830"
  ],
  "id": "AR-1438",
  "next_action": "Promote and repair the trusted development-host validation so it passes under the approved NoNewPrivileges runner hardening without weakening isolation or skipping lifecycle checks.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1438_runner_validation_luna56",
  "plan": "../plans/AR-1438-hardened-trusted-runner-validation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make protected trusted-runner lifecycle validation compatible with hardened rootless execution.",
  "task_revision": 3,
  "title": "Hardened trusted-runner validation repair",
  "updated_at": "2026-09-25T12:09:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1438-hardened-trusted-runner-validation"
}
---

Repair the protected ASB trusted development-host validation exposed by run
36132910260. The approved runner service uses split identities and
`NoNewPrivileges`; the current lifecycle fixture unconditionally invokes sudo
and therefore fails before exercising its actual checks.

Preserve the exact label `asb-development-v1-x86_64-ubuntu2404`, split
operator/service identities, private procfs requirement, cleanup and
registration-failure checks, and all existing runner hardening. Do not grant
the GitHub runner broad sudo, remove `NoNewPrivileges`, weaken workflow guards,
or classify Ubuntu as Debian/openEuler. Make the fixture work rootlessly where
the kernel permits the existing private-procfs fixture, with an explicit
fail-closed diagnostic when the required capability is unavailable.

Add positive and negative tests, update development documentation if needed,
run focused and full applicable gates, publish a signed+DCO PR, wait for exact
head CI, merge only after green required checks, and verify the protected
trusted workflow on the exact merge commit.

- 2026-09-25T12:09:21+00:00: dependencies verified: AR-0830 done; begin hardened rootless runner
  validation repair

- 2026-09-25T12:09:24+00:00: Claimed by ar1438_runner_validation_luna56.
