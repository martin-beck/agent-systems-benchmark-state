---
{
  "branch": "feature/interaction-aware-redaction",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T23:07:49+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0517"
  ],
  "id": "AR-0520",
  "next_action": "Independent immutable review of exact 867861c95c192659102d07f0093a69b58d281513; publish only after approval, then require exact-head x86_64/aarch64 CI.",
  "observed_branch": "feature/interaction-aware-redaction",
  "observed_dirty": 0,
  "observed_head": "867861c95c192659102d07f0093a69b58d281513",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0520.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Support per-interaction request redaction policies for mixed catalog and private requests.",
  "task_revision": 80,
  "title": "Interaction-aware request redaction",
  "updated_at": "2026-09-07T21:08:53+00:00",
  "worktree_key": "agent-systems-benchmark-interaction-aware-redaction"
}
---
## AR-0520

Repair the cassette-global request-body redaction limitation exposed by Goose: catalog GET interactions must have null selectors while private POST message bodies retain bounded selectors and remain strictly replayable. Add interaction/method-aware policy representation, schema/roundtrip/strict-match support, missing-selector and marker-injection negatives, and full privacy/formal/platform gates.

- 2026-09-07T20:07:46+00:00: Promote interaction-aware redaction repair after confirmed Goose mixed
  GET/POST privacy blocker; serialize shared replay changes.

- 2026-09-07T20:07:49+00:00: Claimed by quality_20260906.

- 2026-09-07T20:09:42+00:00: Recorded command exit 0; command argv SHA-256
  5efc72697a98df829c65f8a4ee308763dec5ae70e9f2d2a898adc983a40735e9.

- 2026-09-07T20:12:05+00:00: Recorded command exit 0; command argv SHA-256
  b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b.

- 2026-09-07T20:12:22+00:00: Process deviation recorded: the initial two-file struct patch was
  applied by the workspace patch tool before entering handoffctl run. No mutation was repeated or
  reverted; a subsequent wrapped no-op reconciled the exact dirty effect (cassette.rs and lib.rs) at
  observed head 1963364e. All further product/build/test/Git mutations use the AR wrapper.

- 2026-09-07T20:14:10+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-07T20:17:59+00:00: Recorded command exit 0; command argv SHA-256
  25129675616e8700c212b0b326cccaa2408785fd10008254d4db3ccac5ba0847.

- 2026-09-07T20:18:18+00:00: Recorded command exit 101; command argv SHA-256
  7b050f7967ab45e7634a5f82616916975535a5b4d80c376e8fde79e59f45e29b.

- 2026-09-07T20:18:42+00:00: Recorded command exit 0; command argv SHA-256
  d2926918c598a6aa3756a7e8b500894c33e5531a5cc28baea4ae4d485b9b4ea5.

- 2026-09-07T20:18:58+00:00: Recorded command exit 0; command argv SHA-256
  7b050f7967ab45e7634a5f82616916975535a5b4d80c376e8fde79e59f45e29b.

- 2026-09-07T20:21:03+00:00: Recorded command exit 1; command argv SHA-256
  2ee96d19048e2fcee3b4c74f3c3f05f61c4b9d2ea4791dd27e6cd6e433cd8ba4.

- 2026-09-07T20:21:54+00:00: Recorded command exit 0; command argv SHA-256
  e705094d3d50c16469c8d34246471fd6ca4b967baf218dc0329c53b82c59a4fd.

- 2026-09-07T20:22:14+00:00: Recorded command exit 101; command argv SHA-256
  957fa16e8ea0a66a3b36100fc185724aacf82a7ab39971eb74b3a8a26c7540c5.

- 2026-09-07T20:22:55+00:00: Recorded command exit 0; command argv SHA-256
  e4e6b6a1b5a4ad0114151d38036bd312d03fc34efb044fbad0b8106083ec14a2.

- 2026-09-07T20:23:11+00:00: Recorded command exit 0; command argv SHA-256
  957fa16e8ea0a66a3b36100fc185724aacf82a7ab39971eb74b3a8a26c7540c5.

- 2026-09-07T20:24:45+00:00: Recorded command exit 0; command argv SHA-256
  d2ab710264276d53aece1c41a68cbc477ed517ee31e7948339fa4912229bf72a.

- 2026-09-07T20:25:01+00:00: Recorded command exit 101; command argv SHA-256
  effe24ac782acfdcddb913b84d00edd8e52bee3e76326e2c5285ba9b5fe08b53.

- 2026-09-07T20:25:23+00:00: Recorded command exit 0; command argv SHA-256
  7ae1608b87f0d3d9f9534f7399056cec41495734d0d4163c459139037cc35be8.

- 2026-09-07T20:25:39+00:00: Recorded command exit 101; command argv SHA-256
  effe24ac782acfdcddb913b84d00edd8e52bee3e76326e2c5285ba9b5fe08b53.

- 2026-09-07T20:25:59+00:00: Recorded command exit 0; command argv SHA-256
  c5cf81d3cf7419ece6878dbe24871b3f4c52b803ac9fc82bf5c8e1e76eccf461.

- 2026-09-07T20:26:15+00:00: Recorded command exit 0; command argv SHA-256
  effe24ac782acfdcddb913b84d00edd8e52bee3e76326e2c5285ba9b5fe08b53.

- 2026-09-07T20:26:49+00:00: Recorded command exit 101; command argv SHA-256
  fa825c9778ac5b5824c2e0a11e77a2f8bfe71dc2d10d70fb2b3b9800f18dace6.

- 2026-09-07T20:27:31+00:00: Recorded command exit 0; command argv SHA-256
  0d6dc014fb613cc8c23507e5bfb6070d25ee2a766548e53ea61d558fbc7c9ebe.

- 2026-09-07T20:27:48+00:00: Recorded command exit 0; command argv SHA-256
  fa825c9778ac5b5824c2e0a11e77a2f8bfe71dc2d10d70fb2b3b9800f18dace6.

- 2026-09-07T20:28:41+00:00: Recorded command exit 1; command argv SHA-256
  9c46186d6131b5c9b4331000e1e72ff5d544aea8d18a2603ce543a2e39421fc8.

- 2026-09-07T20:29:36+00:00: Recorded command exit 1; command argv SHA-256
  d50b8ff34ffd8881c80812d8b91f1998d9f36dcf752bae8ffac3517c34ace317.

- 2026-09-07T20:30:23+00:00: Recorded command exit 0; command argv SHA-256
  358c53d19bfd368de2393f74ff1e5e257801bfacd0b73c43d5443fd7fcc2e4ce.

- 2026-09-07T20:30:57+00:00: Recorded command exit 0; command argv SHA-256
  95d8ea34e3af7723adaf6477d73a8f552824c14e68d7e5d8d812e4e71a5ccebb.

- 2026-09-07T20:31:03+00:00: Recorded command exit 0; command argv SHA-256
  b309c91d916dc9d999d7589c41704395e12efa348dbc4831a51d74b23fa781b3.

- 2026-09-07T20:32:00+00:00: Recorded command exit 0; command argv SHA-256
  ab5b01f8215ccc36179e7e63ca00861ca2374b8a987c7f965eb64592b5692fe8.

- 2026-09-07T20:32:21+00:00: Recorded command exit 0; command argv SHA-256
  bc68d1c0d1cf3924e87bc8292a136ed411a94e15d460c23bf8e07f56b99b0b6d.

- 2026-09-07T20:32:49+00:00: Recorded command exit 101; command argv SHA-256
  a836b6c0d444e42ea0b84226539e82291da87b305e3ac49a02d9a914f81e30cf.

- 2026-09-07T20:33:12+00:00: Recorded command exit 0; command argv SHA-256
  4a99fba61c82aba287925c9e311d6fb5434b8d27a7013a7b4557d31b82bb8caf.

- 2026-09-07T20:33:28+00:00: Recorded command exit 101; command argv SHA-256
  a836b6c0d444e42ea0b84226539e82291da87b305e3ac49a02d9a914f81e30cf.

- 2026-09-07T20:34:04+00:00: Recorded command exit 0; command argv SHA-256
  383f3d056021a21c5ff3bd0f1262c4618f85ad85fe6989434b6153dfb0bf4406.

- 2026-09-07T20:34:23+00:00: Recorded command exit 0; command argv SHA-256
  95d8ea34e3af7723adaf6477d73a8f552824c14e68d7e5d8d812e4e71a5ccebb.

- 2026-09-07T20:34:29+00:00: Recorded command exit 0; command argv SHA-256
  a836b6c0d444e42ea0b84226539e82291da87b305e3ac49a02d9a914f81e30cf.

- 2026-09-07T20:35:00+00:00: Recorded command exit 0; command argv SHA-256
  8a7f3564653cafacaa034dc2ec4b3baacab7d1c683ce993587bf015f6b028b28.

- 2026-09-07T20:35:23+00:00: Recorded command exit 0; command argv SHA-256
  29d1a5b2b72190fb7d7bb2ca27b0310215adaaefc536979816cac35017fed308.

- 2026-09-07T20:36:13+00:00: Recorded command exit 0; command argv SHA-256
  2fd9dcdc9662f4b4ec0d852a05ceeeb210069287b9a8926bcba455f4e9c7e8de.

- 2026-09-07T20:37:18+00:00: Recorded command exit 0; command argv SHA-256
  f59be74f2c390ad0d4a45522721cb270403fd2ae965f9a9eebbeb65bca004b23.

- 2026-09-07T20:38:08+00:00: Recorded command exit 0; command argv SHA-256
  ed16369866a7f0a208eee694fd0762401670e5f5eaee29753483b4508c4ffe53.

- 2026-09-07T20:38:26+00:00: Recorded command exit 0; command argv SHA-256
  1bdfca613a51b906fc889ba18556ef21213760b0c5e2cb0e21a1312e29b1f8ae.

- 2026-09-07T20:40:41+00:00: Recorded command exit 1; command argv SHA-256
  78b6fc1abd97c64de9bfff7f02a29c86a0a2b0f86eca592560a1349d9591f9e0.

- 2026-09-07T20:41:02+00:00: Recorded command exit 1; command argv SHA-256
  a25c9ff29a34f2a0726815e3d061a23f514323b7693a493e6be5f50a1db44e44.

- 2026-09-07T20:41:54+00:00: Recorded command exit 0; command argv SHA-256
  c0c775850092add085998d8c2b13329c890439d0fbf53aa3416f2a278a12b814.

- 2026-09-07T20:42:52+00:00: Recorded command exit 101; command argv SHA-256
  84ae6d58822666102f8bfa336a4941fc009b41873115e4d363d431ef70305c47.

- 2026-09-07T20:46:09+00:00: Recorded command exit 1; command argv SHA-256
  65e33f1b54b2fbc64274ce2d7ac435ec61e374b1b9a6acbef3de8fd56dad0df7.

- 2026-09-07T20:46:36+00:00: Recorded command exit 0; command argv SHA-256
  021886f154eb6e627365b653ef995a7dae475cc08c61b5f3e7a76e4dd94bfc45.

- 2026-09-07T20:47:26+00:00: Recorded command exit 0; command argv SHA-256
  f3f039d98149e1648c3a2c1ba6f51149ff443f881ddb6bcd2151367a9f24641e.

- 2026-09-07T20:49:25+00:00: Assurance completion: bounded pinned cargo-fuzz completed
  protocol_jsonrpc, cassette_decode, replay_sse, and store_paths at 256 runs each after coordinated
  completed-AR cache reclamation. The fuzz command returned 1 only on its final cleanliness
  assertion because cargo-fuzz created four empty workspace artifact directories despite an external
  artifact prefix; exact empty directories were audited and removed with rmdir through the wrapper,
  with no source-diff change. Mutation sentinels caught 7/7 at
  /srv/data/projects/.asb-local/artifacts/ar0520-mutants-QmNb9o. Earlier ENOSPC and
  missing-toolchain-path attempts were environmental/preflight failures and were not repeated
  unchanged.

- 2026-09-07T20:49:50+00:00: Recorded command exit 1; command argv SHA-256
  80dd344be6238c3276ab60e22ca79959ce329af8bc7ff06250efeb5dc68f4892.

- 2026-09-07T20:50:15+00:00: Recorded command exit 1; command argv SHA-256
  88bcaea01987169bf08efc8d3069d7eaafdea41a6c0166f1f6eb9eb3a5797092.

- 2026-09-07T20:51:07+00:00: Recorded command exit 0; command argv SHA-256
  e733928428a36e51a15661b368e4bc040a309d73d74cb4a0b1414b7167c2ee85.

- 2026-09-07T20:51:37+00:00: Recorded command exit 1; command argv SHA-256
  78eaa4de134f6734fde7828920e906c509c3f4d7b5a1120e36945b5109d0ed10.

- 2026-09-07T20:52:07+00:00: Recorded command exit 0; command argv SHA-256
  2eb5a0472aa322e4bfc1836ffa11d2bc18737a3d22b096aab1bb4d4656dbb3d2.

- 2026-09-07T20:53:22+00:00: Recorded command exit 0; command argv SHA-256
  0ad9f617e207c9f8c2c56d652f345af06483d524dad6f691ec5022b8323340cc.

- 2026-09-07T20:54:07+00:00: Recorded command exit 0; command argv SHA-256
  0b31386d6219e83170647117fd3d6637906f981e9dbd511e9c66a05170919f35.

- 2026-09-07T20:55:15+00:00: Recorded command exit 0; command argv SHA-256
  3954f4e9dffe07a9e0572f01d18280f2b1af11939c24d540a013ce83872edf5c.

- 2026-09-07T20:55:51+00:00: Recorded command exit 2; command argv SHA-256
  05ffb42ad6cedac4693cec2c35bb4bfeb9c33245950ccde83efffa0ca0a13ab9.

- 2026-09-07T20:56:33+00:00: Recorded command exit 0; command argv SHA-256
  efa9def34af7032b0dfcd20334c52e2fdfaca084961a8af0a86405f3a7f1662e.

- 2026-09-07T20:57:02+00:00: Immutable candidate ready for independent review: signed+DCO head
  867861c95c192659102d07f0093a69b58d281513, tree ea068837cd8dbcf763f0f00a911fd44d0b987015, exact
  base d62add5f815ceb32a920eaa5fc46248b82c2525c. Range-diff from pre-rebase b61aaf58 is equal;
  intervening main delta is the disjoint mini-SWE replay test only. Exact-tree replay/full
  workspace/clippy/formal/Kani 6-of-6 plus deliberate
  negative/coverage/platform/policy/DCO/signature/Gitleaks/privacy/scope gates pass. Workspace line
  coverage is 94.74 percent and asb-replay 97.63 percent. Initial exact-policy command used
  positional DCO arguments and stopped at argparse; corrected owner-wrapped invocation passed
  without product mutation.

- 2026-09-07T21:03:49+00:00: Recorded command exit 0; command argv SHA-256
  9d16ae9898536a7ba2761a4876a1581c16f771fe929f3f968ed16a5665105050.

- 2026-09-07T21:07:54+00:00: Recorded command exit 0; command argv SHA-256
  f2914572f738c84398ca884d7586a60d4d3253f19f2f7f88c99f2815172f8e96.

- 2026-09-07T21:08:29+00:00: Recorded command exit 0; command argv SHA-256
  d8ec6ebf6ef484f99e31d6ae74ee26ffe8414a88b73968ea4466c54fc2cd1637.

- 2026-09-07T21:08:53+00:00: Recorded command exit 0; command argv SHA-256
  a24f605ae17896ac10e937a6d506fd92d21c0cbaed7d73d7e8070f13e7d940af.
