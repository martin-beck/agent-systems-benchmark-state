---
{
  "branch": "repair/ar-1438-hardened-trusted-runner-validation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T14:23:22+00:00",
  "depends_on": [
    "AR-0830"
  ],
  "id": "AR-1438",
  "next_action": "Promote and repair the trusted development-host validation so it passes under the approved NoNewPrivileges runner hardening without weakening isolation or skipping lifecycle checks.",
  "observed_branch": "repair/ar-1438-hardened-trusted-runner-validation",
  "observed_dirty": 0,
  "observed_head": "35d2b86e8eebcf318043a832ab3ea6e98aab3b7b",
  "owner": "ar1438_runner_validation_luna56",
  "plan": "../plans/AR-1438-hardened-trusted-runner-validation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make protected trusted-runner lifecycle validation compatible with hardened rootless execution.",
  "task_revision": 32,
  "title": "Hardened trusted-runner validation repair",
  "updated_at": "2026-09-25T12:23:22+00:00",
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

- 2026-09-25T12:10:13+00:00: Recorded command exit 0; command argv SHA-256
  9fd0e1d25ed0b077815a89b939f78e941e2586e12cd57ac45708f03c8c3b9013.

- 2026-09-25T12:14:02+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:14:16+00:00: Recorded command exit 0; command argv SHA-256
  08cf3e3844cc1e0ac21bad32519e4a93bd80e1254c6aa24014e5e4dcaf6f4c1c.

- 2026-09-25T12:14:37+00:00: Recorded command exit 0; command argv SHA-256
  1887872c61445b59c3bb8768f77ba7c2bf1dde5b73052e6d2f14009c1d5f8489.

- 2026-09-25T12:15:14+00:00: Recorded command exit 0; command argv SHA-256
  3eabbd6d1d4711e308886c1e8511c2cc319eddf76fd4526b55483dfa57511408.

- 2026-09-25T12:15:29+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:16:16+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:16:19+00:00: Recorded command exit 0; command argv SHA-256
  2cbbf7e3c61627bdb5fb15ca3f7bedf3ac9202cf79a910e9fd36865ef17b7c5a.

- 2026-09-25T12:16:50+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-25T12:17:09+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:17:17+00:00: Recorded command exit 0; command argv SHA-256
  d41ac12e68f75c59ee99849d679ad21d3964e292fbaa0c1ca2b14940164cf097.

- 2026-09-25T12:18:44+00:00: Recorded command exit 0; command argv SHA-256
  48e0f8154c7e0f300f83949b4b874ef98a26a6b62b4a9376233ae8dea47560a0.

- 2026-09-25T12:19:14+00:00: Recorded command exit 0; command argv SHA-256
  bb77e7b1b87a45936d84a8ae8b6b90abe2c77e24523d1233d27544bff180f94d.

- 2026-09-25T12:19:29+00:00: Recorded command exit 0; command argv SHA-256
  3eabbd6d1d4711e308886c1e8511c2cc319eddf76fd4526b55483dfa57511408.

- 2026-09-25T12:20:13+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:20:16+00:00: Recorded command exit 0; command argv SHA-256
  ab8734517a4b79055e8d85a8d8b0982326ceb622a2977baf18ef0dbceec35820.

- 2026-09-25T12:20:31+00:00: Recorded command exit 0; command argv SHA-256
  ffa27f93ad06927aff250785daec8ed1c1f9f33b28cf0592fb431eac5c0c1136.

- 2026-09-25T12:21:00+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:21:33+00:00: Recorded command exit 0; command argv SHA-256
  48e0f8154c7e0f300f83949b4b874ef98a26a6b62b4a9376233ae8dea47560a0.

- 2026-09-25T12:21:49+00:00: Recorded command exit 0; command argv SHA-256
  ac58baf1492e6f75253b33dee4969c791415748489cddadd21c2e6401ac66ea8.

- 2026-09-25T12:22:04+00:00: Heartbeat by ar1438_runner_validation_luna56.

- 2026-09-25T12:22:12+00:00: Recorded command exit 0; command argv SHA-256
  b986a1e80f3d43051792de30fb9ba357610b03978a31655bedae961196aa276f.

- 2026-09-25T12:23:02+00:00: Recorded command exit 0; command argv SHA-256
  fd3baf950ae1f3adb4c4b87ae9cabd0eaac63fe86d5d85099dd9d301e160262a.

- 2026-09-25T12:23:22+00:00: Heartbeat by ar1438_runner_validation_luna56.
