---
{
  "branch": "feature/ar-1811-development-formal-workflow-separation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1811",
  "next_action": "Monitor PR #606 exact head d9972679899cf18c1c9ab87e694ad639a2c18786 until all required non-TLC checks are green; then obtain independent review, merge, exact-main post-merge verification, and durable closure.",
  "observed_branch": "feature/ar-1811-development-formal-workflow-separation",
  "observed_dirty": 0,
  "observed_head": "d9972679899cf18c1c9ab87e694ad639a2c18786",
  "owner": "",
  "plan": "../plans/AR-1811-development-formal-workflow-separation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:cac2dc603365a0d8499427a876e98f1a26f2eb656657c992f21cd91db4152219",
    "evidence_ref": "quality/AR-1811-postmerge-receipt.txt",
    "spec_ref": "specs/AR-1811.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1811.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Separate development CI from the single future final-delivery TLC gate without weakening Kani, Loom, policy, Rust, privacy, or release assurance.",
  "task_revision": 59,
  "title": "Development/formal workflow separation",
  "updated_at": "2026-10-12T10:38:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1811-development-formal-workflow-separation"
}
---


Implement a fail-closed workflow contract in which ordinary pull requests and
development pushes never invoke TLC/Alloy or require their result. Preserve
Kani, Loom, Rust, policy, privacy, fuzz, supply-chain, and platform checks.
Keep exactly one explicitly labelled final-delivery workflow path that invokes
TLC/Alloy, is not claimable as development work, and remains required only for
the finished-product delivery PR. Add positive and negative workflow-contract
tests and update the generated quality documentation.

- 2026-10-12T09:45:28+00:00: No dependencies; promote workflow separation to remove TLC from
  development CI while preserving final-delivery formal gate.

- 2026-10-12T09:46:15+00:00: Claimed by ar1811-formal-separation-luna56.

- 2026-10-12T09:46:27+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:46:57+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-12T09:47:21+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T09:48:12+00:00: Recorded command exit 0; command argv SHA-256
  046c0503ca59c590c18bd9ee7f8ae745744a0d24fb528ac7b48bd2f7be1a9447.

- 2026-10-12T09:48:34+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T09:48:55+00:00: Recorded command exit 0; command argv SHA-256
  ec62c79b228f7de760486bd74752568c5534a803fad538ace016b239037d50bb.

- 2026-10-12T09:49:02+00:00: Recorded command exit 0; command argv SHA-256
  24f496bc51708459a0d1eb7a46999509df26464e87b1aad90564d77869e0e019.

- 2026-10-12T09:49:23+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:49:33+00:00: Recorded command exit 0; command argv SHA-256
  37a902b766633d89a3fe82e64dfe47ad2b2e736573bbed9015dd677621568ba9.

- 2026-10-12T09:49:37+00:00: Recorded command exit 0; command argv SHA-256
  3edd81fbfb0f6e8c1fa3b6845bc219d4957726f4bc9913c211359cff0359cbeb.

- 2026-10-12T09:49:54+00:00: Recorded command exit 0; command argv SHA-256
  542d74b51c6a99d32ca08bb3859111a8be1b3e5b4da052b37818d4491a7ca19b.

- 2026-10-12T09:50:06+00:00: Recorded command exit 0; command argv SHA-256
  b8ed48420f139dcbf658b4282285a9753813070c85cd0b874ffb5a83b17cd07a.

- 2026-10-12T09:50:16+00:00: Recorded command exit 0; command argv SHA-256
  7ae4f1187d992d3fe3e48f28ed0fd94fe58d516b6ac92347a0ef892ccfd039e0.

- 2026-10-12T09:52:21+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:52:28+00:00: Recorded command exit 0; command argv SHA-256
  b157be7b3ec91247e741a0de6359ec0b2429133c65fcba2b1d29cba906666fe1.

- 2026-10-12T09:52:51+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T09:52:59+00:00: Recorded command exit 0; command argv SHA-256
  8e9cd44b17c841d20ffbf0f1c2fa4d9e36f79b91467d9bd1221511152e633d94.

- 2026-10-12T09:53:06+00:00: Recorded command exit 0; command argv SHA-256
  39cf5398131881d6bebfeb6940a170dba53287cbad205a984f34c80a6dbe58e7.

- 2026-10-12T09:53:27+00:00: Recorded command exit 0; command argv SHA-256
  ec4139c84d2ae71d929bef96d31edea3264aebcb788559f0f35f61ab804995a2.

- 2026-10-12T09:53:38+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:54:24+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:55:46+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:57:07+00:00: PR #606 exact-head repair da764cf74d70783eff73d6f0055a1ac3a0dfa221 adds
  separated-workflow pin assertions after initial Loom job failure. Initial failure was
  deterministic toolchain_pins expecting setup-java and temporal invocation in formal.yml; repaired
  test now binds Kani/Loom to development workflow and setup-java/temporal invocation to
  final-delivery workflow. Local toolchain_pins passed. TLC/model-check was not run. Current hosted
  checks: Kani, Loom, platform, retained faults, fuzz, credential-free, TUI, AWQ, provenance,
  headers and mutation checks green; Rust, policy, QEMU and remaining checks pending.

- 2026-10-12T09:57:44+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T10:01:59+00:00: Worker implementation complete; releasing claim for coordinator to
  reconcile PR #606 after main advanced. Preserve exact-head evidence and non-TLC development
  policy.

- 2026-10-12T10:02:02+00:00: Claimed by coordinator-ar1811-merge.

- 2026-10-12T10:02:05+00:00: Recorded command exit 0; command argv SHA-256
  4619c4673c4ba2378f12d94083f2241b828e5a32b32a306c18ddc06346c29ef8.

- 2026-10-12T10:02:15+00:00: Recorded command exit 0; command argv SHA-256
  b6341a02ea4be8e9e9e5984b373b91219153297ec7349c33ba5bf3d5fc2f21ea.

- 2026-10-12T10:02:39+00:00: Recorded command exit 0; command argv SHA-256
  f18a0eddcb9055b049eaf4ab099fe62010d68ce9e886a5700afefd490ba5c66e.

- 2026-10-12T10:02:50+00:00: Recorded command exit 0; command argv SHA-256
  1e89cfc3e9861df745b363d9d839cba4ebf3213e91b9c77468f912e7f67cb87f.

- 2026-10-12T10:08:02+00:00: Updated exact-head next action after rebasing PR #606 onto current
  main; development TLC remains excluded.

- 2026-10-12T10:16:21+00:00: Recorded open interaction gate role;
  event=sha256:f10a4f38f89d898180a30ebe9f3b2968de4c2b9f63b7443f58d29f91d03783c6.

- 2026-10-12T10:16:24+00:00: Recorded resolve interaction gate role;
  event=sha256:90cd1a09bd8a4d4165a746e1a99c16e1783e1b5b0ed57c697dcd1a7c3d014ceb.

- 2026-10-12T10:19:03+00:00: Recorded open interaction gate spec;
  event=sha256:10c54098babd9d7c94456bb8f2b192568fa688a6158ee0b93e675e72047a0c70.

- 2026-10-12T10:19:07+00:00: Recorded resolve interaction gate spec;
  event=sha256:7f0867bc0055b584f7103eada798e38afc5fad548a7f2d9daf5c344d3e7a5e6e.

- 2026-10-12T10:19:19+00:00: Recorded open interaction gate decision;
  event=sha256:b09bfcdd5e6c65771c25af05eb618dc916725a88ad1d3400a145ffe43ccb6718.

- 2026-10-12T10:19:22+00:00: Recorded resolve interaction gate decision;
  event=sha256:65f6550f65bd93bcbb061cf2fe9476628eb07d5033ff421a90b82f5c11b9a25f.

- 2026-10-12T10:19:26+00:00: Recorded command exit 2; command argv SHA-256
  f2bdcbf2bdd63e9ca7c7dc95337f57ca3ac597e19a8594e8f284c3ded096ffd3.

- 2026-10-12T10:19:34+00:00: Recorded command exit 1; command argv SHA-256
  235d9016055b6eeb0d4ec0e273d2a56cf87f6dc8fc4f7b5055047ec072a1624c.

- 2026-10-12T10:19:59+00:00: Recorded command exit 0; command argv SHA-256
  0a915f675c68a430ebd26211be9e51080e209cac500895d2035bae68855f7282.

- 2026-10-12T10:20:10+00:00: Recorded command exit 1; command argv SHA-256
  c64532d2240f0635cac81226cc4d98546ea999bf320f9358045a0a58b18f522e.

- 2026-10-12T10:20:22+00:00: Recorded command exit 1; command argv SHA-256
  26b3992d561988a3cabbbfbf7f7c01fa93ebc913047738aea55458add02017b6.

- 2026-10-12T10:20:44+00:00: PR #606 has green ordinary checks and independent state acceptance but
  GitHub branch policy rejects merge without an eligible non-author review; self-approval was
  rejected and no admin bypass used. Preserve exact-head evidence and resume only after external
  review policy is satisfied.

- 2026-10-12T10:25:02+00:00: AR-1814 removed only the stale TLC status from ruleset 24750310; PR
  #606 is now clean with all ordinary checks green and state independent review accepted. Resume
  merge transition without admin bypass.

- 2026-10-12T10:25:05+00:00: Claimed by coordinator-ar1811-merge.

- 2026-10-12T10:25:11+00:00: Recorded command exit 1; command argv SHA-256
  c64532d2240f0635cac81226cc4d98546ea999bf320f9358045a0a58b18f522e.

- 2026-10-12T10:38:20+00:00: Bound task spec specs/AR-1811.json revision 1.

- 2026-10-12T10:38:25+00:00: Exact reviewed PR #606 merged at 5a6c5477; all exact-main workflows
  terminal success after minimal AR-1814 ruleset repair; independent review and DCO/signature
  evidence retained.

- 2026-10-12T10:38:33+00:00: AR-1811 complete: PR #606 merged at exact protected-main commit
  5a6c5477; all exact-main workflows passed after AR-1814 minimal ruleset repair; acceptance receipt
  and independent review retained.


## Preserved oracle-gate evidence

```json
{
  "completed": [
    "role",
    "spec",
    "decision"
  ],
  "discussion_rounds": 0,
  "events": [
    {
      "action": "open",
      "after": [
        {
          "digest": "sha256:607625b5d8597e0ae25eca71b8e2608f6f08664ef9f12f06f5583cf5921a2f45",
          "ref": "review/candidate"
        }
      ],
      "before": [
        {
          "digest": "sha256:cc330f6cc2411e636d0434b5cceb13aa3da50412081d4e2307c858c0efe9ae4f",
          "ref": "review/base"
        }
      ],
      "disposition": "unresolved",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786",
      "recorded_at": "2026-10-12T10:16:21+00:00",
      "stage": "role",
      "task_id": "AR-1811",
      "task_revision": 41
    },
    {
      "action": "resolve",
      "after": [
        {
          "digest": "sha256:607625b5d8597e0ae25eca71b8e2608f6f08664ef9f12f06f5583cf5921a2f45",
          "ref": "review/accepted"
        }
      ],
      "before": [
        {
          "digest": "sha256:607625b5d8597e0ae25eca71b8e2608f6f08664ef9f12f06f5583cf5921a2f45",
          "ref": "review/candidate"
        }
      ],
      "disposition": "accepted",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786",
      "recorded_at": "2026-10-12T10:16:24+00:00",
      "stage": "role",
      "task_id": "AR-1811",
      "task_revision": 42
    },
    {
      "action": "open",
      "after": [
        {
          "digest": "sha256:88e12d0e567e6030f4aade22e82ff0870a9640e9e705b8f51c6e04ed17b1c633",
          "ref": "candidate-spec"
        }
      ],
      "before": [
        {
          "digest": "sha256:cc330f6cc2411e636d0434b5cceb13aa3da50412081d4e2307c858c0efe9ae4f",
          "ref": "base-spec"
        }
      ],
      "disposition": "unresolved",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786/spec",
      "recorded_at": "2026-10-12T10:19:03+00:00",
      "stage": "spec",
      "task_id": "AR-1811",
      "task_revision": 43
    },
    {
      "action": "resolve",
      "after": [
        {
          "digest": "sha256:88e12d0e567e6030f4aade22e82ff0870a9640e9e705b8f51c6e04ed17b1c633",
          "ref": "accepted-spec"
        }
      ],
      "before": [
        {
          "digest": "sha256:88e12d0e567e6030f4aade22e82ff0870a9640e9e705b8f51c6e04ed17b1c633",
          "ref": "candidate-spec"
        }
      ],
      "disposition": "accepted",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786/spec-accepted",
      "recorded_at": "2026-10-12T10:19:07+00:00",
      "stage": "spec",
      "task_id": "AR-1811",
      "task_revision": 44
    },
    {
      "action": "open",
      "after": [
        {
          "digest": "sha256:b678ee8b2515d49f7ba2137e1380f8719a08eb15b97c35efb4b2b8b8d6afe45d",
          "ref": "candidate-decision"
        }
      ],
      "before": [
        {
          "digest": "sha256:cc330f6cc2411e636d0434b5cceb13aa3da50412081d4e2307c858c0efe9ae4f",
          "ref": "base-decision"
        }
      ],
      "disposition": "unresolved",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786/decision",
      "recorded_at": "2026-10-12T10:19:19+00:00",
      "stage": "decision",
      "task_id": "AR-1811",
      "task_revision": 45
    },
    {
      "action": "resolve",
      "after": [
        {
          "digest": "sha256:b678ee8b2515d49f7ba2137e1380f8719a08eb15b97c35efb4b2b8b8d6afe45d",
          "ref": "accepted-decision"
        }
      ],
      "before": [
        {
          "digest": "sha256:b678ee8b2515d49f7ba2137e1380f8719a08eb15b97c35efb4b2b8b8d6afe45d",
          "ref": "candidate-decision"
        }
      ],
      "disposition": "accepted",
      "public_ref": "PR-606/d9972679899cf18c1c9ab87e694ad639a2c18786/decision-accepted",
      "recorded_at": "2026-10-12T10:19:22+00:00",
      "stage": "decision",
      "task_id": "AR-1811",
      "task_revision": 46
    }
  ],
  "open_stage": null,
  "reconciliation_required": false,
  "required": true,
  "stage_sequence": [
    "role",
    "spec",
    "decision"
  ]
}
```
