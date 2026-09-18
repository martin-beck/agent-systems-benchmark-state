---
{
  "branch": "feature/ar-1308-full-exhaustive-qemu-capacity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T15:47:05+00:00",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1308",
  "next_action": "Promote after AR-1304 review; provision disposable x86_64 QEMU capacity and qualify the exact AR-1307 full-exhaustive liveness run without changing its 3G/3G contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1308-qemu-capacity-20260918",
  "plan": "../plans/AR-1308.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide governed disposable capacity for exact full-exhaustive TLC liveness qualification.",
  "task_revision": 22,
  "title": "Full-exhaustive QEMU capacity qualification",
  "updated_at": "2026-09-18T14:00:16+00:00",
  "worktree_key": "agent-systems-benchmark-asb-ar-1308-full-exhaustive-qemu-capacity"
}
---

# AR-1308

AR-1307's exact-head full-exhaustive qualification reached approximately 45.77M generated and
37.99M distinct states, then failed because Java ran out of memory during liveness checking under
the existing 3G memory and 3G swap contract. This follow-on owns only the disposable capacity and
evidence needed to rerun that exact qualification truthfully; it must not weaken AR-1307's limits,
model, admission, or attestation gates.

The dependency on AR-1304 provides the reviewed required-tier QEMU runner and user-bus foundation.
The run must consume the exact signed AR-1307 head and pinned TLC/JDK/model inputs, without changing
source code or treating a capacity failure as a model result.


- 2026-09-18T13:45:32+00:00: AR-1304 is done; promote capacity follow-on to open for independent
  worker assignment. Preserve AR-1307 3G/3G contract and exact-head dependency.

- 2026-09-18T13:47:05+00:00: Claimed by codex-ar1308-qemu-capacity-20260918.

- 2026-09-18T13:47:23+00:00: Recorded command exit 128; command argv SHA-256
  3c23ab8c7aef5e69413a67148e540252a0be1c5f0afbf399d42a0b9fde7ef802.

- 2026-09-18T13:47:37+00:00: Recorded command exit 0; command argv SHA-256
  ae02b81cc87b547b19688a831039dc959be03909d2e8e8486319fe841ede01c3.

- 2026-09-18T13:51:59+00:00: Recorded command exit 0; command argv SHA-256
  9216f649f27dd4b7d9d0a6f363edd54f10a42e125b3802be7b1ef90da1e133d7.

- 2026-09-18T13:52:21+00:00: Recorded command exit 0; command argv SHA-256
  a1e22af43f312aca7eb94e3247acdcda3397b77489c6b756c25032889be42756.

- 2026-09-18T13:52:43+00:00: Recorded command exit 0; command argv SHA-256
  6788e083bb57e4638deb59f3ad667c37d7da4278328cc0b97dda64087b54d291.

- 2026-09-18T13:53:24+00:00: Recorded command exit 0; command argv SHA-256
  d47cc6663d902762ead98e64bc95b11888e9bae0a80a1b41e89586e488c7468f.

- 2026-09-18T13:54:16+00:00: Recorded command exit 0; command argv SHA-256
  087e8b4d4560b54bf6f050af48dae960159bde94f309fa84da4ac438c41e1ce4.

- 2026-09-18T13:54:27+00:00: Recorded command exit 0; command argv SHA-256
  09485738bdc509f7235ee90ba6fbe4f9976f846437a37a7fb65dd4bcddc472f8.

- 2026-09-18T13:55:49+00:00: Recorded command exit 0; command argv SHA-256
  1bcaa710b254d2cacd043de64e28c05c95e268f597892a361c5543d0cdf8ea61.

- 2026-09-18T13:56:01+00:00: Recorded command exit 0; command argv SHA-256
  4f9691df5cd21483d2cf25abb01c8bd13a3c26316d4c04ee70a777814164bd5b.

- 2026-09-18T13:56:16+00:00: Recorded command exit 0; command argv SHA-256
  44e5b46c4ba6f255e7da6353be6e542bf96670815399b816d90ab91de37a8011.

- 2026-09-18T13:56:33+00:00: Recorded command exit 1; command argv SHA-256
  672bc8b0e4b5dc6f601d619f56873dbf2ab9087c955c7d8adcba7b10d3cff76c.

- 2026-09-18T13:58:02+00:00: Recorded command exit 0; command argv SHA-256
  ee4145add4dfd9ecc477b588ee49d479dacaffee60ee2e0d08c4d4f60d994a04.

- 2026-09-18T13:58:48+00:00: Recorded command exit 0; command argv SHA-256
  3b341e11434d275c8731a357d340024fa55ade02c998b8e97c276190b39070a0.

- 2026-09-18T13:59:31+00:00: Recorded command exit 0; command argv SHA-256
  e85b09e8044353156f6d17fc343209531cd2b9ccea337f93689018e564631954.

- 2026-09-18T13:59:41+00:00: Recorded command exit 0; command argv SHA-256
  1040bf72dac6afd78bc6e6b8c39bff9885671f66d6b6996d82c81879b0ecaa8e.

- 2026-09-18T13:59:50+00:00: Recorded command exit 0; command argv SHA-256
  e58b3ac9a7f1d254c72c3070d26ed4d78b494ede3743ec7cc0fba31f1fd2b483.

- 2026-09-18T14:00:02+00:00: Recorded command exit 0; command argv SHA-256
  35f6e4bb709c55773c41df46b693e4d1341242518469522a99120c6c0258d776.

- 2026-09-18T14:00:16+00:00: Recorded command exit 0; command argv SHA-256
  746f25205abb8ea61c110b306bc9134d8c263b798b13b4c1763b02f588aa324d.
