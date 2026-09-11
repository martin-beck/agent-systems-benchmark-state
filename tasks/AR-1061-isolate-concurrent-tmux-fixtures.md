---
{
  "branch": "fix/tmux-live-fixture-isolation",
  "checkpoint_commit": "17f8b3bc26cfa35b1f8ecb8a2e2e5c11d756dae1",
  "claim_expires": "2026-09-11T07:07:48+00:00",
  "depends_on": [],
  "id": "AR-1061",
  "next_action": "Freeze exact signed test-only checkpoint 17f8b3bc/e4777aef for immutable review; publish only after approval, then require exact-head and exact-main trusted CI.",
  "owner": "codex-ar1061-tmux-fixture-isolation-20260911",
  "plan": "../plans/AR-1061.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Diagnose and isolate concurrent trusted tmux fixture contention.",
  "task_revision": 23,
  "title": "Isolate concurrent trusted tmux fixtures",
  "updated_at": "2026-09-11T05:48:19+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-live-fixture-isolation"
}
---

Exact-main Trusted run `34565894753` failed all five live tmux fixtures under the default-parallel
test binary after AR-1058 exposed `socket_connect_rejected` and `server_before_unavailable` stages.
Test process-local serialization is the next bounded experiment. Authentication, cleanup and all
product/UI behavior remain unchanged.

- 2026-09-11T05:37:46+00:00: Detailed test-only recovery plan approved by root after exact-main run
  34565894753 localized failures to concurrent live tmux fixtures; AR-1061 is dependency-ready.

- 2026-09-11T05:37:48+00:00: Claimed by codex-ar1061-tmux-fixture-isolation-20260911.

- 2026-09-11T05:38:16+00:00: Recorded command exit 0; command argv SHA-256
  88c9af6c736f41f3d7ca06988d2aa000f4682ca0f5fd03b9a4be193cc01416f1.

- 2026-09-11T05:39:20+00:00: Recorded command exit 0; command argv SHA-256
  d684d1d312d115d8b9341c231cbcf69e99bf079b18bbb62e01a2bcd975fcf50e.

- 2026-09-11T05:39:47+00:00: Recorded command exit 0; command argv SHA-256
  83fff7c494d5870840be1e9574db8b83db9606cc7b7763671f17aac085fd16d2.

- 2026-09-11T05:40:07+00:00: Recorded command exit 101; command argv SHA-256
  589e86e963c640e7858174384e0e7f7c8bed2580eaaa0b5c203a63370a736ddd.

- 2026-09-11T05:41:08+00:00: Recorded command exit 0; command argv SHA-256
  b9ac6cac17ef8d7be65caafdf32bc70b442a12df9c68f608f3666831d0ea4e11.

- 2026-09-11T05:41:20+00:00: Recorded command exit 0; command argv SHA-256
  841483e12d94002e5ba5d379b8f1234bb7c9aecde9274b9c0de6458610dc6ced.

- 2026-09-11T05:41:55+00:00: Recorded command exit 0; command argv SHA-256
  0983053a68865425677867d571631a20b69df2230e525a7d7281c452ca1b5bc6.

- 2026-09-11T05:42:28+00:00: Recorded command exit 0; command argv SHA-256
  13f830ea755053672fe2bcd27b8760a865f866d36f8f695b5514d4e76c396ba2.

- 2026-09-11T05:43:03+00:00: Recorded command exit 0; command argv SHA-256
  a601c5fb52327ac2ef68814cc83e972086465940a759b67c1887452c66658fd9.

- 2026-09-11T05:43:44+00:00: Recorded command exit 1; command argv SHA-256
  58b79e23d665745aafab4fd2914555b969ea6cceff3011c916898ce50adc63d2.

- 2026-09-11T05:43:58+00:00: Recorded command exit 1; command argv SHA-256
  12688130a96d74f80d55a8c9004a5f813651585eef26613b86bfa97527f62203.

- 2026-09-11T05:44:16+00:00: Recorded command exit 0; command argv SHA-256
  19b487308625fe61d8077f6a093deb90581971f2c15f29da1dadaf993fe81d08.

- 2026-09-11T05:44:57+00:00: Recorded command exit 0; command argv SHA-256
  12688130a96d74f80d55a8c9004a5f813651585eef26613b86bfa97527f62203.

- 2026-09-11T05:45:14+00:00: Recorded command exit 2; command argv SHA-256
  940a2f97caf53f8ed0c9f36b3d498780e7954544122533732b0307dc5d8d4fbd.

- 2026-09-11T05:45:37+00:00: Recorded command exit 0; command argv SHA-256
  1c2790cf053b31c03972c18f9f7b6c640c37c28e145231fb1ad785dace3f71b4.

- 2026-09-11T05:45:57+00:00: Recorded command exit 0; command argv SHA-256
  2429f5505e7e4ee51e5770030c9166aeb80251c5ce99a65ff9fe27284f0431b8.

- 2026-09-11T05:46:20+00:00: Frozen signed product checkpoint
  17f8b3bc26cfa35b1f8ecb8a2e2e5c11d756dae1, tree e4777aef699520acd74780a215ba85963f980604, base
  69fecc01. One test file adds process-local complete-lifetime exclusion for five live tmux fixtures
  and an injected two-way mutex proof; authentication and cleanup authority are unchanged. Gates:
  focused PASS; five default-parallel terminal passes 155/155; two serial passes 62/62; full locked
  PASS; fmt, all-target Clippy, rustdoc, release, deny, audit, coverage 91.44%, shell/workflow,
  schema/publication/channel validators, ASB isolation and promoted self-test PASS; scoped process
  audit zero. Classified first exit-101 as code-local nondeterminism in the new proof because it
  competed on the global fixture mutex; repaired using an injected local mutex, repeated parallel
  gates green. Classified two later exit-1 coverage attempts as clean-tree precondition failures
  because coverage was invoked before the product checkpoint commit; the same coverage gate passed
  after commit. Classified exit-2 combined-script attempt as invocation-only missing required
  ASB_PRODUCT_ROOT for prove-asb-isolation; rerun with the exact ASB root passed.

- 2026-09-11T05:47:49+00:00: Recorded command exit 0; command argv SHA-256
  58fb224d2a3004186148c639e3773c5f4df8c66bdf113b0882efdd11898e5824.

- 2026-09-11T05:48:06+00:00: Recorded command exit 0; command argv SHA-256
  322d0cdde750cafe9ac07c6a113f0398d356a126c8a9a7387c465d6c2d309d46.

- 2026-09-11T05:48:19+00:00: Recorded command exit 0; command argv SHA-256
  d437a46a5ac5dc6886f6e01e8880577ed952d8418c8068e07f9d6e21781d8fa9.
