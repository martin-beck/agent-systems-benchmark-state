---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1733"
  ],
  "id": "AR-1736",
  "next_action": "Promote after AR-1733; inventory the canonical backend registry and implement catalog, selection, run, and sweep parity with exhaustive fixtures.",
  "owner": "",
  "plan": "../plans/AR-1736-backend-model-catalog-execution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "sha256:7adfb1d710f0aa5c02fe42edb23661c7f3b4c51810ae3cd1802b857cdf269731",
    "evidence_ref": "quality/AR-1736-postmerge-receipt.json",
    "spec_ref": "specs/AR-1736.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1736.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Make every supported model-bearing backend enumerate selectable models and carry the exact selection through complete run and sweep execution.",
  "task_revision": 31,
  "title": "Require model catalogs and execution parity for every backend",
  "updated_at": "2026-10-11T07:15:22+00:00",
  "worktree_key": ""
}
---

Establish one mechanically complete contract for every backend ASB advertises.
Each model-bearing backend must enumerate a bounded, generation/digest-bound
model catalog, allow only catalog-backed model selection, and preserve the exact
backend/model identity through plan, normal run, and bounded sweep results.
Backends that are intentionally model-less must declare that fact explicitly
and remain covered by the same registry completeness gate; they may not be
silently omitted. Development fixtures are authoritative for CI. Optional live
checks may add evidence but missing credentials, authentication, signatures, or
key services must not block this development AR.

- 2026-10-11T06:25:24+00:00: Dependency AR-1733 is durably done; promote for backend model catalog
  and execution parity implementation.

- 2026-10-11T06:25:27+00:00: Claimed by codex-asb-ar1736-catalog-luna56-20261011.

- 2026-10-11T06:26:12+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-11T06:26:37+00:00: Recorded command exit 0; command argv SHA-256
  eb3211a6e4a80eba2fbdf225d485899c73ab40da4c28324f6a333b592dbf6fbe.

- 2026-10-11T06:27:18+00:00: Recorded command exit 101; command argv SHA-256
  68f486ba58a0df23774e22d3cb2fad2b377c6a10db3ac77d8ef76bcca09266a7.

- 2026-10-11T06:27:44+00:00: Recorded command exit 0; command argv SHA-256
  5e452fff04ae080b5fca867c8dd2039011385cc762d0d00da578cd610b88e870.

- 2026-10-11T06:28:53+00:00: Recorded command exit 0; command argv SHA-256
  d54fab5b79a3fd68726bc6d51655bf31a639a2514ad705d9ee82e9fa22759dd5.

- 2026-10-11T06:29:02+00:00: Recorded command exit 0; command argv SHA-256
  891440837b6f605e3642d7c366f72a17a524c0887658ea4df4c2cb88116f2393.

- 2026-10-11T06:29:13+00:00: Recorded command exit 0; command argv SHA-256
  e5fa59dfe29169f475ea6ceedcb4a8c1102748353395d4c8e4a83c4f4073027b.

- 2026-10-11T06:29:39+00:00: Recorded command exit 0; command argv SHA-256
  4e458c96bb7efe091a5ed885a112a7f3e5cd0ab3970046ca6cdd4585a916e1c4.

- 2026-10-11T06:31:01+00:00: Recorded command exit 0; command argv SHA-256
  6d8c08127fde8f9757dcb102deb6c6c2ea671166cafc05949a586392fe6d51d0.

- 2026-10-11T06:31:32+00:00: Recorded command exit 0; command argv SHA-256
  7593ba38772c596d0492b4092fd2715464891b19554fdbe4c927f8ad08d74361.

- 2026-10-11T06:31:47+00:00: Recorded command exit 1; command argv SHA-256
  c06f35c71feeac4825551f25e7e2556c4985bd680effadf3f414f2b31c011978.

- 2026-10-11T06:32:04+00:00: Recorded command exit 0; command argv SHA-256
  8e248f74fb3415f2d8478a95d840169c8a06982dd54c9ee72e97e768076fffb5.

- 2026-10-11T06:43:05+00:00: Recorded command exit 0; command argv SHA-256
  8ceeacf1416d3db326ce0c731b72499c9584857f4018ebbdc9a55560a98ef63c.

- 2026-10-11T06:43:24+00:00: Recorded command exit 0; command argv SHA-256
  cf17815514e646449f195328e2d454335bc630a8f42c5e7dc7e69ae96964e11a.

- 2026-10-11T06:44:37+00:00: Recorded command exit 0; command argv SHA-256
  6d8c08127fde8f9757dcb102deb6c6c2ea671166cafc05949a586392fe6d51d0.

- 2026-10-11T06:58:25+00:00: Recorded command exit 0; command argv SHA-256
  77ce916d02df7248f70d7a03d673bff49d9abe25a23c850db0d253b64d170ffa.

- 2026-10-11T06:58:38+00:00: Recorded command exit 0; command argv SHA-256
  3500ab41a25eed50509129533bf6e71be6a5e59b19e0f35dcfdf9470f8c5aa7a.

- 2026-10-11T06:58:54+00:00: Recorded command exit 1; command argv SHA-256
  2b9053ae5a4ec35349a2057abcb4749b1e980e2f96006edf62ed616a36a9d653.

- 2026-10-11T06:59:09+00:00: Recorded command exit 1; command argv SHA-256
  88c353991e671a2d8c3fb7442674a44db5d7749bb9e71e44592347fa7e8eb77e.

- 2026-10-11T06:59:22+00:00: Recorded command exit 1; command argv SHA-256
  dcd91e2e733f39aacf127f59500f159756af3c7ab7bb672fd89021b5bdaad664.

- 2026-10-11T06:59:48+00:00: Recorded command exit 0; command argv SHA-256
  e7b711438b22f3310765642fae64b855140be719ebd1b6988c2a4591c4c55f28.

- 2026-10-11T07:12:53+00:00: Recorded command exit 0; command argv SHA-256
  34e90426d4374e2e769d2fac0c6e7131c8d38af31ea35694a76cf3588f1c3c20.

- 2026-10-11T07:13:12+00:00: Recorded command exit 0; command argv SHA-256
  681e0c4a35835fa120cef6ec116592767bfd7c1bb49d395a89744b42aab97abb.

- 2026-10-11T07:14:14+00:00: Recorded command exit 0; command argv SHA-256
  34e90426d4374e2e769d2fac0c6e7131c8d38af31ea35694a76cf3588f1c3c20.

- 2026-10-11T07:14:23+00:00: Recorded command exit 0; command argv SHA-256
  681e0c4a35835fa120cef6ec116592767bfd7c1bb49d395a89744b42aab97abb.

- 2026-10-11T07:14:54+00:00: Recorded command exit 0; command argv SHA-256
  274ac4b59c64c88b5b79bec6e4c137d31d8fbb9ff43d5ee16001881a9a0001b6.

- 2026-10-11T07:15:17+00:00: Accepted after protected merge 4cb87998; exact-main checkout
  verification passed the AR-1736 generation/digest/backend selection fixture, and all PR plus
  post-merge required workflows are green.

- 2026-10-11T07:15:22+00:00: Released after protected merge 4cb87998, exact-main verification, and
  all required PR/post-merge checks green.
