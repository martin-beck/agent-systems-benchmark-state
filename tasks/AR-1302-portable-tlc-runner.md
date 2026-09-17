---
{
  "branch": "feature/ar-1302-portable-tlc-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1302",
  "next_action": "Use run_lifecycle from signed commit 1fd5e31cf to create a fresh overlay, boot the UUID-serial data disk, run guest UUID/mount preflight, then execute f1931686c portable-smoke and capture sanitized terminal attestation. Do not claim qualification from container evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1302.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Provision a clean portable TLC CI/VM runner for state formal admission.",
  "task_revision": 432,
  "title": "Portable TLC CI/VM runner",
  "updated_at": "2026-09-17T13:37:31+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1302-portable-tlc-runner"
}
---

## AR-1302

Provision the clean, portable-containment runner required to unblock AR-1293. Keep all images,
VMs, caches, queues, locks and evidence under `/srv/data/projects`; use immutable provenance,
offline-after-install behavior, no network or host-mount access, bounded execution and sanitized
evidence. Native ARM64 is optional and must not be a gate. Do not modify ASB product code,
asb-tui, handoffctl, or unrelated root-owned admission locks.

- 2026-09-17T07:09:22+00:00: Create clean portable TLC runner to unblock AR-1293; no product or
  asb-tui dependency

- 2026-09-17T07:10:38+00:00: Claimed by codex-ar1302-runner-20260917.

- 2026-09-17T07:10:47+00:00: Recorded command exit 0; command argv SHA-256
  fd092032b6d14bf8b53313beae3931f4074a2111f503bc5021464a0c35121252.

- 2026-09-17T07:12:48+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:12:50+00:00: Recorded command exit 0; command argv SHA-256
  b08c2d8d2773a00d8520aab8910dc444e48ccf8febeb51d9c0d825ed3a02ea55.

- 2026-09-17T07:13:41+00:00: Recorded command exit 0; command argv SHA-256
  d667a58d27e6920c90524c55ecd81df13e4a8f3080dbe844aff3ae9d5990a50c.

- 2026-09-17T07:14:13+00:00: Recorded command exit 1; command argv SHA-256
  4cc5bdf8eaa7b6f8f07d5f475f5048c08e48dd4d61cf2c1832e5339c2e843ed5.

- 2026-09-17T07:14:29+00:00: Recorded command exit 0; command argv SHA-256
  e4f842cc5744a8aeed6e22075832459707a5c67223e513c61840f6ffdb7c8b73.

- 2026-09-17T07:14:55+00:00: Recorded command exit 1; command argv SHA-256
  2e4709a3c708405760e333d4bfc380cf00fcbbf909bfbc301dab89d1e04a3d98.

- 2026-09-17T07:15:14+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:15:17+00:00: Recorded command exit 0; command argv SHA-256
  ad5f47b3effc3f08ed5739f48bc671ee6415b7f8560428c48d2ee12cf66f70c4.

- 2026-09-17T07:15:35+00:00: Recorded command exit 0; command argv SHA-256
  a7a2f6aa7ccac8f2f0a28af0ecd73b9218200bf9ca3364855714e6629ab7f648.

- 2026-09-17T07:16:00+00:00: Recorded command exit 0; command argv SHA-256
  1fe621021f432f3527d8d1a285759370986c899b0d4436b8342a23072e9c5ec9.

- 2026-09-17T07:16:21+00:00: Recorded command exit 0; command argv SHA-256
  9581b362f978b75783a138af2132c2427bd7ed9b49089ffdcf046a27856aa83d.

- 2026-09-17T07:16:45+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:16:47+00:00: Recorded command exit 0; command argv SHA-256
  ef913d4b73a97ebe2a654958090c7cc3e195b7e40dcdcabb72079758865f9322.

- 2026-09-17T07:18:16+00:00: Recorded command exit 0; command argv SHA-256
  b780737a33f69de8ec896d32c0a3167f0922c97e3f133d71bffcfda7e4e4ce77.

- 2026-09-17T07:18:31+00:00: Recorded command exit 0; command argv SHA-256
  9d0d0a8797a21d98ca53d9a7853c6cd7a1ba82ed6a0eabfa067d221b31eb5c69.

- 2026-09-17T07:19:45+00:00: Recorded command exit 1; command argv SHA-256
  f8d97b2922f017a2e4a1e3bf3f78ee1ddd62208250598d59a5dd7cf02fc403ce.

- 2026-09-17T07:20:15+00:00: Recorded command exit 1; command argv SHA-256
  36af54164fe516f3936dacaaf372a2f1910e973ffca81526dcc2c1f3cd2b4dfc.

- 2026-09-17T07:20:34+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:20:39+00:00: Recorded command exit 0; command argv SHA-256
  70bfd50d43a629cdfdc5177f7ff409d2ff021f88bec732dbaf4f45b180e5aa37.

- 2026-09-17T07:21:07+00:00: Recorded command exit 0; command argv SHA-256
  eac9d0a9e7054ec96515070fd8345e5df91a5e9aecb3133fecd6fe74109cdea6.

- 2026-09-17T07:21:27+00:00: Recorded command exit 2; command argv SHA-256
  c4df7530be18deeff953553c261903c9a8268d5f723c4470022a36b77ba4cc14.

- 2026-09-17T07:21:51+00:00: Recorded command exit 2; command argv SHA-256
  85949d17f2ae95ec49925747fbf30e8396b5861676fa4b7fda9e0740d2dd8fe4.

- 2026-09-17T07:22:01+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:22:04+00:00: Recorded command exit 0; command argv SHA-256
  995ab4c467abf35f85b756575eca31607c231cbf492601fe5d1ee2e2b8030181.

- 2026-09-17T07:22:22+00:00: Recorded command exit 0; command argv SHA-256
  97864df6a1767b77f8bd974932d98502fcb72470a6f8bb16936b914ce43d825f.

- 2026-09-17T07:23:48+00:00: Recorded command exit 1; command argv SHA-256
  40fd5c2dc4500fd2f7c83e62e841f0fb4197dfd0382dccaf3e187c0414621543.

- 2026-09-17T07:24:03+00:00: Recorded command exit 0; command argv SHA-256
  40fd5c2dc4500fd2f7c83e62e841f0fb4197dfd0382dccaf3e187c0414621543.

- 2026-09-17T07:26:35+00:00: Recorded command exit 0; command argv SHA-256
  c78ce84f417df5b6e0eef6778b4455f02d88b60c943c0266f41e20f001910874.

- 2026-09-17T07:26:55+00:00: Recorded command exit 2; command argv SHA-256
  03374bc30c5107c464607bb27e48153cf07152866b3b92d724600cce30376dc6.

- 2026-09-17T07:27:18+00:00: Recorded command exit 0; command argv SHA-256
  dc88d82d04bc7db3f0db9fd08a4b853dfbc5689bedba5cac78f6d3647d2fec24.

- 2026-09-17T07:27:43+00:00: Recorded command exit 0; command argv SHA-256
  34420343697310b54f1488480975b328a86d9de66f254c83e335c0292bf07017.

- 2026-09-17T07:32:31+00:00: Worker stopped after no durable progress for approximately five
  minutes. Unsafe full-rootfs export was removed. Preserve only uncommitted minimal runner
  helper/docs for focused reassignment; tests, signed commit, and portable qualification remain
  outstanding.

- 2026-09-17T07:33:29+00:00: Claimed by codex-ar1302-recovery-20260917.

- 2026-09-17T07:34:12+00:00: Recorded command exit 141; command argv SHA-256
  b26857535769f0151e7df9d63e801e9b8c9850db82bffaa480580f3b62307bc6.

- 2026-09-17T07:34:33+00:00: Recorded command exit 0; command argv SHA-256
  b1c4016a92fa7187b5452c5a9f9cdc39ecd253348483ed7a86f2a4b066baa352.

- 2026-09-17T07:34:52+00:00: Recorded command exit 0; command argv SHA-256
  9b867ecea7d85e5d64957d9680a0ef64fc7c5e50010f7903c37fdcfdaf6c7b0f.

- 2026-09-17T07:35:14+00:00: Recorded command exit 0; command argv SHA-256
  7ad79c2e98f6e91f1b436e17bd7ee715dc9fbd178457cf6267c94b91ff16d05f.

- 2026-09-17T07:35:54+00:00: Recorded command exit 0; command argv SHA-256
  7c0a56de1958be0391f35c3abcf9fc92754f132a0081e72bea54cf349eabd0b8.

- 2026-09-17T07:37:36+00:00: Recorded command exit 1; command argv SHA-256
  d6e1dd341751ed7e466dccff06314d67e6e37f975c88dbcb34166b65a0add93f.

- 2026-09-17T07:38:45+00:00: Recorded command exit 0; command argv SHA-256
  52f7a59a938e19b963ba4cc99347d470cb9717b4519bc948c97c16192433542a.

- 2026-09-17T07:39:06+00:00: Recorded command exit 1; command argv SHA-256
  6042671193e133a30cf9268656ee0442eaf5c10382ebc86d6acfde0c4b82fd31.

- 2026-09-17T07:39:30+00:00: Recorded command exit 0; command argv SHA-256
  193c12f0caad1f65eadeb0d941a2daa988336c8580f4262bcc019034cb6b315c.

- 2026-09-17T07:39:49+00:00: Recorded command exit 1; command argv SHA-256
  76177692d5202624a12bc7d771a1a805302aca3f2a050b6a57a8ec4e17bcd3bd.

- 2026-09-17T07:40:07+00:00: Recorded command exit 0; command argv SHA-256
  99692400aa5e7fbcbaa8bfff7436253effe0e587c494fffbab744c44d4efa486.

- 2026-09-17T07:40:25+00:00: Recorded command exit 1; command argv SHA-256
  76177692d5202624a12bc7d771a1a805302aca3f2a050b6a57a8ec4e17bcd3bd.

- 2026-09-17T07:40:43+00:00: Recorded command exit 0; command argv SHA-256
  7a73ea9bd6e296ead8809d3dc6360194331468ccb04bdfbeed6cf4144c5d8f3e.

- 2026-09-17T07:41:02+00:00: Recorded command exit 0; command argv SHA-256
  76177692d5202624a12bc7d771a1a805302aca3f2a050b6a57a8ec4e17bcd3bd.

- 2026-09-17T07:41:21+00:00: Recorded command exit 1; command argv SHA-256
  7fe4928d112df3ad9d493bbad7c517392cdbd93fc3d1b39aa02acbfaffab3e95.

- 2026-09-17T07:41:43+00:00: Recorded command exit 0; command argv SHA-256
  1c815792e9cfe6679bc4770de94ab59e66d1fdb66c440bd5cac0680687ac71b3.

- 2026-09-17T07:42:03+00:00: Recorded command exit 2; command argv SHA-256
  fed942daff97a45fe7bbaa12785e71e31c8b3ac0bd344cd0d3880d17ff00bdcd.

- 2026-09-17T07:43:18+00:00: Recorded command exit 0; command argv SHA-256
  02480e544546027278e5568b1cae15ae7defc161c746e36e07ad0f45c6a35386.

- 2026-09-17T07:43:40+00:00: Recorded command exit 0; command argv SHA-256
  76177692d5202624a12bc7d771a1a805302aca3f2a050b6a57a8ec4e17bcd3bd.

- 2026-09-17T07:44:10+00:00: Recorded command exit 1; command argv SHA-256
  259fccc740f8520a3ec45346070564b0bcb51f928de5354b92d3fe77447a2340.

- 2026-09-17T07:44:37+00:00: Recorded command exit 0; command argv SHA-256
  62ec7adf933748b30162aaad77dc8a9e911b9e254cde9e5ce03fb353909e0500.

- 2026-09-17T07:44:54+00:00: Recorded command exit 0; command argv SHA-256
  3edcfd33f31f10782f76213bc54e0d28a2f3a37576ee48a38acb3fb57f51c3da.

- 2026-09-17T07:45:25+00:00: Recorded command exit 0; command argv SHA-256
  2e1a17375743d96bf790601d6deb5c9a2b6a73307818c870df0ae187a4746c17.

- 2026-09-17T07:46:02+00:00: Recorded command exit 2; command argv SHA-256
  f2bad9a03562ee4abed64e9611417087bd6a04b3fccc4bfcc9a8709ea8f334b6.

- 2026-09-17T07:46:32+00:00: Recorded command exit 0; command argv SHA-256
  a11b789865551a279b527b791566eccf8220f267926e4fa559cdf32fe6de80b0.

- 2026-09-17T07:46:59+00:00: Recorded command exit 1; command argv SHA-256
  11c3884a18b653cee944cf4584bfa8702861d17a6b8d1778072fc640f6976d4c.

- 2026-09-17T07:47:15+00:00: Recorded command exit 0; command argv SHA-256
  9c62cc91a9fb7b87bba58cda2289f7f312eeec5a35dcc0129b9a4f4e4bb6973f.

- 2026-09-17T07:47:40+00:00: Recorded command exit 0; command argv SHA-256
  e79c68837c99b7a31a61ed4aac6818e83cd4b064c6545deda09b1bbb6a3743cc.

- 2026-09-17T07:48:22+00:00: Heartbeat by codex-ar1302-recovery-20260917.

- 2026-09-17T07:48:54+00:00: Recorded command exit 2; command argv SHA-256
  f2bad9a03562ee4abed64e9611417087bd6a04b3fccc4bfcc9a8709ea8f334b6.

- 2026-09-17T07:49:15+00:00: Recorded command exit 0; command argv SHA-256
  8777590b37cc0336bc361ce2acbcb7e3728137ffa4fa13bfe29c4a482fcea105.

- 2026-09-17T07:49:52+00:00: Recorded command exit 2; command argv SHA-256
  f2bad9a03562ee4abed64e9611417087bd6a04b3fccc4bfcc9a8709ea8f334b6.

- 2026-09-17T07:50:31+00:00: Recorded command exit 0; command argv SHA-256
  f9e665637edca8c4194cd10d501b376d9bbc7954039ccaaba095eb32046f37cc.

- 2026-09-17T07:50:46+00:00: Recorded command exit 0; command argv SHA-256
  64813fbc09e7a082c6617c7f634537b3744081823e394b1dfa8474e41ca28d4a.

- 2026-09-17T07:50:57+00:00: Recorded command exit 1; command argv SHA-256
  d4626946b39c141289d286161e2b375153311471ee6ef285557e6936127b7d7d.

- 2026-09-17T07:51:19+00:00: Recorded command exit 0; command argv SHA-256
  dc3ea2ad2ef8d249e671313a6749f476b9fbf22761a7dc5cf9b8451a4ed88663.

- 2026-09-17T07:51:47+00:00: Recorded command exit 0; command argv SHA-256
  eff13c2332e4fa8ee86542554edbd88720f7c97eb90be8c521ec3391d2e23de2.

- 2026-09-17T07:52:50+00:00: Recorded command exit 1; command argv SHA-256
  f1a09521cb756f7b41a85f64e8432963f43182a847b2de811662253f58f6b17a.

- 2026-09-17T07:53:19+00:00: Recorded command exit 1; command argv SHA-256
  f1a09521cb756f7b41a85f64e8432963f43182a847b2de811662253f58f6b17a.

- 2026-09-17T07:53:46+00:00: Recorded command exit 0; command argv SHA-256
  9b1b911ce2740af020001d249c0dafdad74666162139577e2ddfacf2b4d20324.

- 2026-09-17T07:55:18+00:00: Recorded command exit 0; command argv SHA-256
  4bc1dc24ab2df6877e93255b3bd9552f6f1dd55c34b661b47ccbc8727d3caeb5.

- 2026-09-17T07:55:51+00:00: Preserved signed/DCO commit 01a3433bb adds the digest-pinned amd64
  Docker portable TLC runner, HandoffctlPR one-process fixture, argv-only sudo wrapper, private
  evidence enforcement, 3 GiB bounded tmpfs, and focused negative/positive tests. Source headers,
  schema/render checks, 7 focused tests, Ruff, and mypy pass. Actual sudo -n docker portable-smoke
  and pr-publication pass using image
  eclipse-temurin@sha256:c0d1549d1e0f5fa5b83622ec0033b00456107e0b1d0cfcce4c1d831532ce621e and TLC
  SHA-256 936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88. Initial full tier
  reached 1,683,316 states then exhausted the old 256 MiB tmpfs; runner changed to bounded 3 GiB
  tmpfs but exact post-fix full qualification is pending. Current doctor is blocked by unrelated
  expired AR-1299 claim. Next action: repair AR-1299 lease/state, rerun full-exhaustive once on
  clean exact head, record evidence, then resume AR-1302 for independent review/publication and
  update AR-1293.

- 2026-09-17T07:58:08+00:00: AR-1299 stale claim recovered and PR #213 merged as 6c694f8; resume
  exact full-tier requalification of signed runner 01a3433bb.

- 2026-09-17T07:58:11+00:00: Claimed by coordinator-ar1302-full-20260917.

- 2026-09-17T08:00:30+00:00: Recorded command exit 2; command argv SHA-256
  833842e3742991924309b636552bb68c9f4ec4ab046a92d8d59f13e308948f63.

- 2026-09-17T08:02:41+00:00: Recorded command exit 1; command argv SHA-256
  b29c498d9de692bead8f546e371631817083fc260e8b811a776cc7537dc96355.

- 2026-09-17T08:02:59+00:00: Recorded command exit 0; command argv SHA-256
  a4012b6f1d5e85570326e75e753e797876e9198df3c7e2843758f1758bc10b2b.

- 2026-09-17T08:03:13+00:00: Recorded command exit 0; command argv SHA-256
  6e60da292de6b23a07172e043b45a1e892e007329cf682c5366735137f908937.

- 2026-09-17T08:03:22+00:00: Recorded command exit 0; command argv SHA-256
  be3afb050f28b294306cd34fb6226f0b72ac36828536ed70132bab4f0316b31e.

- 2026-09-17T08:03:38+00:00: Recorded command exit 2; command argv SHA-256
  eb0586184b2d2a3484d378562d135a8c3a088ccfc368cadeed823f567ddfa390.

- 2026-09-17T08:04:23+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:04:44+00:00: Recorded command exit 0; command argv SHA-256
  db5e2086cebd7382ba78c70beec9c4ccc558b8792f7977db0663c9a4c34d9ce9.

- 2026-09-17T08:04:59+00:00: Recorded command exit 0; command argv SHA-256
  a4012b6f1d5e85570326e75e753e797876e9198df3c7e2843758f1758bc10b2b.

- 2026-09-17T08:06:54+00:00: Recorded command exit 2; command argv SHA-256
  cbc781cd5be7656d2528f35bd964fad4ee02c8b2f777a59f671cd857ccde63fb.

- 2026-09-17T08:07:22+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:07:32+00:00: Recorded command exit 0; command argv SHA-256
  67f3cce0ee4e5c0bc17b87565866fde381a06281cd8ce0c56440da4629b6ab6e.

- 2026-09-17T08:10:12+00:00: Recorded command exit 2; command argv SHA-256
  242e50ba6f2e9af6202f099939d899ba2726726f56a50523472a804a3d0a4d3d.

- 2026-09-17T08:10:46+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:11:00+00:00: Recorded command exit 0; command argv SHA-256
  0176ecd4b67a0214d221d4fcc7281682442b161367d5881b71d161b1437b8658.

- 2026-09-17T08:13:40+00:00: Recorded command exit 2; command argv SHA-256
  eebc45d32f05eba229f19efababa31e9df40713489f954b3f9b863f70e3efe7e.

- 2026-09-17T08:14:46+00:00: Recorded command exit 1; command argv SHA-256
  4f26b706ae94bcd5bc869143bd3f48bd4b9d87748229a1770a665a79b336b571.

- 2026-09-17T08:15:03+00:00: Recorded command exit 0; command argv SHA-256
  3654042bb6dc5ad805d41592f7bfb14211d1608cf1d74979e86fa246825655ef.

- 2026-09-17T08:15:18+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:15:27+00:00: Recorded command exit 0; command argv SHA-256
  739e0e2e468fd18437b4d55df64d71844e71e742082f7a65cc85fb7de653dd89.

- 2026-09-17T08:15:50+00:00: Recorded command exit 2; command argv SHA-256
  ee85c260527980593939b5a545dea2200adcf3fa494810a63dd5aebb12bc4524.

- 2026-09-17T08:16:16+00:00: Recorded command exit 0; command argv SHA-256
  6e60da292de6b23a07172e043b45a1e892e007329cf682c5366735137f908937.

- 2026-09-17T08:16:26+00:00: Recorded command exit 0; command argv SHA-256
  dd669b7d1dac35300001dfdd615f970bf917919ce87e7c8524dbbed4e9c4569a.

- 2026-09-17T08:19:07+00:00: Recorded command exit 2; command argv SHA-256
  f4b478a5a493709573ae7fe1ef4f63e2b8d57a3acfcacc37409cbca51f9ec46c.

- 2026-09-17T08:19:53+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:20:02+00:00: Recorded command exit 0; command argv SHA-256
  89122c6e2c9ecf261f43fc0ada78bc57216a6c93a60fe0571a32ee7b5dea215d.

- 2026-09-17T08:22:43+00:00: Recorded command exit 2; command argv SHA-256
  4f3b61bbb27ee6df312d3307109c578fefd30ec9d097c0987b1e82e861ca1b10.

- 2026-09-17T08:23:14+00:00: Recorded command exit 0; command argv SHA-256
  992f1c3606101b67fa2bf316acde03b29373471b70686eaf77cba456a83ace9d.

- 2026-09-17T08:23:30+00:00: Recorded command exit 0; command argv SHA-256
  952d4849e7d45427a27a2446be63490948571b1191e748403489804787aa0069.

- 2026-09-17T08:24:03+00:00: Recorded command exit 0; command argv SHA-256
  5357b1f8ede7d144d8ade1ae7b2ce2cc41a30de474f46a8b49feeffa52ed235b.

- 2026-09-17T08:24:13+00:00: Recorded command exit 0; command argv SHA-256
  930afbed057f4360dfb918d9cef255ab072d9b395683f4e85411af68656e1acf.

- 2026-09-17T08:24:29+00:00: Portable runner implementation is clean, signed, and passes
  portable-smoke plus pr-publication using digest-pinned linux/amd64 Docker image, no network/host
  mounts, read-only rootfs, ALL capabilities dropped, no-new-privileges, 2 CPUs, 64 PIDs, ephemeral
  Docker state volume, and an explicit 20 GiB/20 GiB memory profile matching the host cgroup.
  Full-exhaustive Handoffctl repeatedly reaches about 9 million states and is OOM-killed (exit 137);
  host memory.max is 25769803776 bytes (24 GiB), so further full-tier execution requires a clean
  runner/VM with at least 32 GiB effective cgroup memory. No gate was weakened; AR-1293 remains
  blocked pending that capacity.

- 2026-09-17T08:25:11+00:00: Temporarily reopen only to correct durable next_action after
  capacity-block release.

- 2026-09-17T08:25:14+00:00: Claimed by coordinator-ar1302-statefix-20260917.

- 2026-09-17T08:25:39+00:00: Corrected stale next_action after release. Full-tier capacity blocker
  and passing lower-tier evidence remain durable.

- 2026-09-17T08:25:42+00:00: Released ownerless after correcting next_action; no implementation or
  gate change.

- 2026-09-17T09:50:54+00:00: Provisioned runner receipt b1457b809 is now available; reclaiming to
  run required full-exhaustive gate and finish exact evidence.

- 2026-09-17T09:50:56+00:00: Claimed by codex-ar1302-runner-20260917-vm.

- 2026-09-17T09:51:06+00:00: Recorded command exit 0; command argv SHA-256
  ae385cb86a166410520cd47386337eed25f1c4aded48b8839a4e8221b23bdd53.

- 2026-09-17T09:51:43+00:00: Recorded command exit 0; command argv SHA-256
  ae385cb86a166410520cd47386337eed25f1c4aded48b8839a4e8221b23bdd53.

- 2026-09-17T09:52:08+00:00: Recorded command exit 0; command argv SHA-256
  6efb367638825b4bf33ee2e8d0468bd52b4c0619b0107cceec6ffed19568ee28.

- 2026-09-17T09:52:37+00:00: Recorded command exit 0; command argv SHA-256
  ae385cb86a166410520cd47386337eed25f1c4aded48b8839a4e8221b23bdd53.

- 2026-09-17T09:53:23+00:00: Recorded command exit 0; command argv SHA-256
  aab3aacca8368ff6656cfe51db3530a1770d013282b79a4462a0c7dd7ae5bbb0.

- 2026-09-17T09:53:33+00:00: Recorded command exit 0; command argv SHA-256
  2a3458227066644829fce3ea2f081ceaad7b4cb27f0557b21d5c6270834a5e86.

- 2026-09-17T09:54:46+00:00: Recorded command exit 1; command argv SHA-256
  e6b34fb534eb12c9e4837b3aaa0bd240e032207e1ee7c529fdc9c1f5928b97c3.

- 2026-09-17T09:55:07+00:00: Recorded command exit 0; command argv SHA-256
  839d0eda4745c69378b585429242c77a2858716c2323936b952a1c1b9b0de2fa.

- 2026-09-17T09:55:29+00:00: Recorded command exit 0; command argv SHA-256
  d153553ca7bd9e727a75a668e5a8595548d09ad2310189e71f3e694436a53fa6.

- 2026-09-17T09:55:57+00:00: Recorded command exit 0; command argv SHA-256
  40c4728529119eb049b8334eff5102e1e4ccef7bc37b986ed3c94dc56a0dfcbf.

- 2026-09-17T09:56:07+00:00: Recorded command exit 0; command argv SHA-256
  64f77d36f8ea0b6b001699fa5315cda72137c4780e45eb4dff683e33bbb352d3.

- 2026-09-17T09:56:55+00:00: Recorded command exit 0; command argv SHA-256
  22712b4195565fbe8c845b9e6a5bbd57381df39124a363d86470db4b575030ee.

- 2026-09-17T09:57:16+00:00: Recorded command exit 0; command argv SHA-256
  2ebd0baf471e213d06530704b931a8d16f78c88e6b88e51ab717d6324ee784b1.

- 2026-09-17T09:57:46+00:00: Recorded command exit 0; command argv SHA-256
  f9d9d8819a2a2ec4d60276e8862248abb3f856c0ddce224f87520da8a188a937.

- 2026-09-17T09:58:07+00:00: Recorded command exit 0; command argv SHA-256
  40c4728529119eb049b8334eff5102e1e4ccef7bc37b986ed3c94dc56a0dfcbf.

- 2026-09-17T09:58:32+00:00: Recorded command exit 0; command argv SHA-256
  6ab5062cdbc3bb50ce9cdd30f4ef0e9067039c704576b48faeef45f6fd67488b.

- 2026-09-17T09:58:52+00:00: Recorded command exit 0; command argv SHA-256
  d3bb4f2739eeef0704e62e7153d0b5bff7c84b7a7a46ec67b6ba4a9546dc0a02.

- 2026-09-17T09:59:09+00:00: Recorded command exit 1; command argv SHA-256
  f3d25adfb78b156cba73ba9645dba38106eecc35385199f994f0626cee50a50b.

- 2026-09-17T09:59:36+00:00: Recorded command exit 0; command argv SHA-256
  53947e2b3d22d3583103a9447d1b228eee540be89d4917c7c35e691e164cc975.

- 2026-09-17T10:00:12+00:00: Recorded command exit 0; command argv SHA-256
  612d510ef1d313e2d853f40e6f56903be45e398bd12d537c8b0a73fcc68e9ae6.

- 2026-09-17T10:00:37+00:00: Recorded command exit 0; command argv SHA-256
  0bef41a398f28f1d99ec9667f39a99324cbd496effad587ba6a5219db3ab69f0.

- 2026-09-17T10:01:09+00:00: Recorded command exit 0; command argv SHA-256
  b909e840ac3ddb386e525f6d227dbdc0ad66f2f670e05eb7c4d60bd8b08b476d.

- 2026-09-17T10:01:38+00:00: Recorded command exit 0; command argv SHA-256
  457ebcf10172903bd1adf699113658ed82f3a8e43ce3bf88565d2a4b524899d0.

- 2026-09-17T10:01:59+00:00: Heartbeat by codex-ar1302-runner-20260917-vm.

- 2026-09-17T10:02:02+00:00: Recorded command exit 0; command argv SHA-256
  c1848c8a44a5478de9f7f37ccc0aa3ee0f72001cc1736ac7899a5cd94d976e63.

- 2026-09-17T10:02:19+00:00: Heartbeat by codex-ar1302-runner-20260917-vm.

- 2026-09-17T10:02:50+00:00: Recorded command exit 0; command argv SHA-256
  ed80f60aea6e69beefba503f542fc88d9dd487e2e44de61c3a03455aef2866bf.

- 2026-09-17T10:03:20+00:00: Runner definition commit 7a6f7fd94 and focused 7-test/ruff/mypy/header
  gates pass. VM receipt b1457b809 is available under /srv/data/projects/asb-state-tlc-vm-32g with
  32 GiB RAM, 16 GiB guest swap, 8 vCPU, no network and no host mounts. Shared VM PR attempt
  correctly failed closed at curl exit 6 because the pinned JAR was not yet staged; no formal pass
  claimed.

- 2026-09-17T10:04:14+00:00: Recorded command exit 0; command argv SHA-256
  95aa305bd5c8118360ec4549859c1606fe943659dd4f263c36c9fb6c5d124c31.

- 2026-09-17T10:12:26+00:00: Heartbeat by codex-ar1302-runner-20260917-vm.

- 2026-09-17T10:13:30+00:00: Heartbeat by codex-ar1302-runner-20260917-vm.

- 2026-09-17T10:14:16+00:00: 2026-09-17T10:13:55Z checkpoint: full-exhaustive is not yet runnable.
  The provisioned 32 GiB VM is live (QEMU pid 1928184) with runner-data-f16d2cb41.raw attached
  read-only; its data disk lacks tla2tools.jar. The active console/socat is owned by the AR-1293
  worker (codex-ar1293-clean-vm-20260917), and its prior guest attempt correctly failed before TLC
  with curl exit 6 because network=none. Do not stop or overlap that worker. Exact next action:
  after AR-1293 releases the VM, create a private offline copy of the data disk, inject the pinned
  JAR SHA-256 936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88, boot a distinct
  disposable VM/data path, then run full-exhaustive and capture terminal attestation.

- 2026-09-17T10:14:19+00:00: Recorded command exit 0; command argv SHA-256
  6c217499234d05165d24394a8558bcfbd8ed092cc12ff2fd2e71493de479e39a.

- 2026-09-17T10:14:47+00:00: Recorded command exit 0; command argv SHA-256
  f7a8fca9ebcc253b5beed1057ad651e56d25b9866b535cbcd73ffdb11f7f5e40.

- 2026-09-17T10:14:56+00:00: Recorded command exit 0; command argv SHA-256
  331f6bc67aefd85664cd8e2972b14e4da48f83a46787d87084abfc7071f08772.

- 2026-09-17T10:15:06+00:00: Recorded command exit 0; command argv SHA-256
  c8b79a01032b09234419e353202cfdf87dd6509b2b429bb33bdcb49d7328887b.

- 2026-09-17T10:15:28+00:00: Recorded command exit 0; command argv SHA-256
  ca9ac8deb26466c4ddda1b6135d7b815549495514c911af1454fdbc178dc0340.

- 2026-09-17T10:15:38+00:00: Recorded command exit 0; command argv SHA-256
  e2b1f358eed72138369e4559e00dc4150c5812168d5f22e3ab851e4d4427a28a.

- 2026-09-17T10:15:57+00:00: Recorded command exit 0; command argv SHA-256
  eef78d304e9e3eab5dea41a6c462d01baba35d8c86ca7d8b05b3ff4d206c3b67.

- 2026-09-17T10:16:07+00:00: Recorded command exit 0; command argv SHA-256
  3f060ca1b7423b754bbb1b6b80aa9c7f3a9d0000b40d110d363d7a93bdc77c18.

- 2026-09-17T10:16:39+00:00: Recorded command exit 0; command argv SHA-256
  543c4a3f3434fecb5e59d02578f13960e5c08d3519a3ed12807575483aa57385.

- 2026-09-17T10:16:49+00:00: Recorded command exit 0; command argv SHA-256
  e376d4097435802a894735e9ecaf4627e86154b6bf369a5d61f876d59176bc6c.

- 2026-09-17T10:17:12+00:00: Recorded command exit 0; command argv SHA-256
  7558636338a89ff9e8c3d60b9a266d5b6df7dfe17ff6dc171a2a59cbe477138b.

- 2026-09-17T10:17:27+00:00: Recorded command exit 0; command argv SHA-256
  4641aab1f8fee013aee0d4fe99e429fd1055284fc1d0455ca6a39232fa4b785a.

- 2026-09-17T10:17:37+00:00: Recorded command exit 0; command argv SHA-256
  7558636338a89ff9e8c3d60b9a266d5b6df7dfe17ff6dc171a2a59cbe477138b.

- 2026-09-17T10:17:58+00:00: Recorded command exit 0; command argv SHA-256
  a01830478165cda0dd12a6750919a9c2db7b3f4363dc6032573c4f66b827891f.

- 2026-09-17T10:18:08+00:00: Recorded command exit 0; command argv SHA-256
  4f14b42df13c4f2c98d500c33501d38c98f7801d6cfacb51aa473dce07635644.

- 2026-09-17T10:18:34+00:00: Recorded command exit 0; command argv SHA-256
  827f5c54c0c02d4f00a0a683321f8c0f64a6fb756038922bedde2cce7cbf3e12.

- 2026-09-17T10:18:44+00:00: Recorded command exit 0; command argv SHA-256
  4f14b42df13c4f2c98d500c33501d38c98f7801d6cfacb51aa473dce07635644.

- 2026-09-17T10:19:05+00:00: Recorded command exit 0; command argv SHA-256
  ae62335a1bbd63c1a4b35d88f8ae4f669ee50a4749a9a926278c9d4886c85475.

- 2026-09-17T10:19:26+00:00: Recorded command exit 0; command argv SHA-256
  7bd84028740fc1463d780a2e545559d4be4f074f21de63c18b41580f16595ed8.

- 2026-09-17T10:19:35+00:00: Recorded command exit 0; command argv SHA-256
  1081a90c322f490b39ea90c424d48ca0450f2aa9e77d70599b14673a6a285fbf.

- 2026-09-17T10:19:59+00:00: Recorded command exit 0; command argv SHA-256
  916f844ae1b024ec1ffaf40d2e76b83e71cedecbfef2067b101f1c67f4e85de0.

- 2026-09-17T10:20:14+00:00: Recorded command exit 0; command argv SHA-256
  f3450297cb02602c85f017cc4f11f49428da794a4b639d6ba13587b19570dfc1.

- 2026-09-17T10:20:27+00:00: Recorded command exit 0; command argv SHA-256
  916f844ae1b024ec1ffaf40d2e76b83e71cedecbfef2067b101f1c67f4e85de0.

- 2026-09-17T10:21:02+00:00: Recorded command exit 0; command argv SHA-256
  4823e9d12380f05abc992131ceca1c6984dfdf73e234ecd9c49d9522e48a6480.

- 2026-09-17T10:21:13+00:00: Recorded command exit 0; command argv SHA-256
  a4ad79bc0c29f153e05a82f0b4b1f773dc5bc87200c64c6b5a3b8ed9b25816e9.

- 2026-09-17T10:21:35+00:00: Recorded command exit 0; command argv SHA-256
  4ea9d35ad6f2fa5b8b2806c17b51bfb169116efccf4d0c9cd9ee3f5c358d5b0e.

- 2026-09-17T10:21:47+00:00: Recorded command exit 0; command argv SHA-256
  c5b5053c45893561a465b03fcb6ce97aedc2f716a7f5570593eec56b1ac14c5e.

- 2026-09-17T10:21:56+00:00: Recorded command exit 0; command argv SHA-256
  9140505b59a4255772e641ef1c120154592caf0f07a3db28f1a324323f3db597.

- 2026-09-17T10:22:05+00:00: Recorded command exit 0; command argv SHA-256
  4ea9d35ad6f2fa5b8b2806c17b51bfb169116efccf4d0c9cd9ee3f5c358d5b0e.

- 2026-09-17T10:22:15+00:00: Recorded command exit 0; command argv SHA-256
  e949b5740e34e0f36d81ab3f51ac15be8e904c4065c931ab0eb2a5b28730d989.

- 2026-09-17T10:22:24+00:00: Recorded command exit 0; command argv SHA-256
  916f844ae1b024ec1ffaf40d2e76b83e71cedecbfef2067b101f1c67f4e85de0.

- 2026-09-17T10:22:33+00:00: Recorded command exit 0; command argv SHA-256
  a7d55e10c626a1599d6877403cfb81cd9bf19d83c331a98dfddd1fd65ca129a1.

- 2026-09-17T10:22:57+00:00: Recorded command exit 1; command argv SHA-256
  2a96a7a0cb17bfcefae562a80c6550b22d06b480798309894fd7e8bbec81cb35.

- 2026-09-17T10:23:07+00:00: Recorded command exit 1; command argv SHA-256
  bdbecf5fe3bc573bfc3a16a136ab4c3ba813d452320e49fc1b96cb53e3a0015f.

- 2026-09-17T10:23:27+00:00: Recorded command exit 1; command argv SHA-256
  691ab4aca03bafcc9b61f91ab7332b9471df69007c8b44df3bb80285342d4723.

- 2026-09-17T10:24:03+00:00: Recorded command exit 0; command argv SHA-256
  2db4f77e783d7f23a602a27f1afacdbdec9fb4aea8116f704969024d61120af8.

- 2026-09-17T10:24:21+00:00: Recorded command exit 0; command argv SHA-256
  8de604639bbfb024644c64294a0f2e107d53b59ae6e8c5ba195a6ac67a70a803.

- 2026-09-17T10:24:34+00:00: Recorded command exit 0; command argv SHA-256
  5cc69f7590df8001d25a30fdb0695422b1a71e4f877a5ae3ba4f9f3f8e11b9c3.

- 2026-09-17T10:25:41+00:00: Recorded command exit 0; command argv SHA-256
  8d1d5514fae8d67f92d4f5a42ae6cfb8b25c9c7f80cfc76dfac11e59ff7381c4.

- 2026-09-17T10:25:59+00:00: Recorded command exit 0; command argv SHA-256
  bde4da8bb17fc5235d03ed29ffd87f91761366ac4403c9e9135f4296cd3a8d16.

- 2026-09-17T10:26:11+00:00: Recorded command exit 0; command argv SHA-256
  2f6bbee5189f20e619dd0db87af2695c5e5de4688611051db9aa67cb89e3d64b.

- 2026-09-17T10:27:24+00:00: Recorded command exit 0; command argv SHA-256
  b3c43079db6e3597a6ad7e87ba570a67e4dfcffe4ed381cf59c94bd5e138882e.

- 2026-09-17T10:27:42+00:00: Recorded command exit 0; command argv SHA-256
  422e96aec48f94364b2c922f6800b75653f4cdb66867ce5a9478e4f5b8da0650.

- 2026-09-17T10:28:54+00:00: Recorded command exit 0; command argv SHA-256
  6c9c1023849aebb6178bf9bc0759796601b5b5c6e6333639dbdde5d07e4290dc.

- 2026-09-17T10:29:03+00:00: Recorded command exit 0; command argv SHA-256
  9c6186df4972bec7828bd4001e408771438d7b5c0cac926c484bd2fbfb60a51f.

- 2026-09-17T10:30:29+00:00: Recorded command exit 0; command argv SHA-256
  c19100b9130503fb59b219f769eedb9f44eecb906a47753ed1e2caa226d7c1e6.

- 2026-09-17T10:30:48+00:00: Recorded command exit 0; command argv SHA-256
  38071a961d9940164e53a9732670a0bf305e3e0363ca89eaa344d9e8f33dc2bd.

- 2026-09-17T10:31:53+00:00: Recorded command exit 0; command argv SHA-256
  2482c356ad6ae99919c08ffe70a5980217e6e7667995a872a2e9e3524180c1fd.

- 2026-09-17T10:32:02+00:00: Recorded command exit 1; command argv SHA-256
  1e5ee6af3582ecc52e652008c622fb21c983bfe86248c110fffaef9342c69196.

- 2026-09-17T10:32:34+00:00: Recorded command exit 0; command argv SHA-256
  c4690393037cb626f03d5464b2dcca2f4cccad0d215f1b9934ce29b39377d152.

- 2026-09-17T10:32:44+00:00: Recorded command exit 0; command argv SHA-256
  0670c0dc3b4cbe91acd1c2943a95d702c69b8dc69ae0b661d0a210e1e6ef46a1.

- 2026-09-17T10:32:56+00:00: Recorded command exit 1; command argv SHA-256
  23196033275888b8386b330db30943eb50c35aaf938263d624e54428b3c207bd.

- 2026-09-17T10:33:58+00:00: Recorded command exit 0; command argv SHA-256
  63b1154cbd955cb9e300bdf3ba62cbe83ff4580e5ff902342035702c760711ac.

- 2026-09-17T10:34:17+00:00: Recorded command exit 0; command argv SHA-256
  23196033275888b8386b330db30943eb50c35aaf938263d624e54428b3c207bd.

- 2026-09-17T10:36:25+00:00: Heartbeat by codex-ar1302-runner-20260917-vm.

- 2026-09-17T10:36:48+00:00: Recorded command exit 0; command argv SHA-256
  144e3f370dc88e9510cef4ff4b8d1ce7ff6ea2aa47769b004b1b1a9ab4738bad.

- 2026-09-17T10:37:00+00:00: Recorded command exit 0; command argv SHA-256
  b255935de3959a274ae588747148d454b462c677dd848c77c962d8f25f3b2f40.

- 2026-09-17T10:37:09+00:00: Recorded command exit 0; command argv SHA-256
  650d6105d7eace3f33b9cae820a2e8660d41defe6d173149a68e9f1c82936623.

- 2026-09-17T10:39:12+00:00: Recorded command exit 0; command argv SHA-256
  4b1c60847f71d3d266af8cbce1f7be0c18a6e6c0b3199e21852d09c6a9abf045.

- 2026-09-17T10:39:22+00:00: Recorded command exit 0; command argv SHA-256
  29846031b507f1b1490c865e2320bab2fd1553dd3aaa1bfe9bd50002227d1d97.

- 2026-09-17T10:39:32+00:00: Recorded command exit 0; command argv SHA-256
  9521a5db2a60435b2007c17c99ad5331f66134e3ca0d8c2cae7650bd8bfaccad.

- 2026-09-17T10:40:45+00:00: 2026-09-17T10:40:10Z: AR-1293 released the original VM; AR-1302 now
  owns a distinct offline data copy with pinned JAR SHA-256
  936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88. v7 reached TLC but failed native
  allocation under portable prlimit AS=3G (ASB_RC=1), no attestation. v8 correctly used
  TLC_CGROUP_MODE=required but systemd-run --user failed with Failed to connect to bus: No medium
  found (ASB_RC=1), no attestation. No gate was weakened or success claimed.

- 2026-09-17T10:40:48+00:00: Recorded command exit 0; command argv SHA-256
  a82f0a38438752ac4bc778c60f2794fc9d262db1da45b6546bffacc2cecbe15c.

- 2026-09-17T10:41:19+00:00: Recorded command exit 0; command argv SHA-256
  2f23755f4b25d6fbd467aff4d0f1e13725de70fb400541be07741605a2efb54b.

- 2026-09-17T10:41:30+00:00: Recorded command exit 0; command argv SHA-256
  535bbb1dc92d5f690ecf4e4802b778c59920906b26210a982c31fc57f62e508b.

- 2026-09-17T10:41:39+00:00: Recorded command exit 0; command argv SHA-256
  d39be40074558f4ac48a15b8acbb9b5210c94fa6421b162d12dc0d51cf556f71.

- 2026-09-17T10:42:51+00:00: 2026-09-17T10:42:10Z: v9 retained required systemd containment and set
  XDG_RUNTIME_DIR/DBUS_SESSION_BUS_ADDRESS, but root cloud-init invocation failed with Failed to
  start transient service unit: Transport endpoint is not connected (ASB_RC=1), no attestation. The
  runner/data/JAR remain isolated and no full gate success is claimed. Next fix is to invoke verify
  as the guest asb UID through runuser so the active user manager owns the systemd transient unit.

- 2026-09-17T10:42:53+00:00: Recorded command exit 0; command argv SHA-256
  530902de1650337b7e9bea9464323481f1e0b6c8a94aa0392fc2691854f219a0.

- 2026-09-17T10:43:32+00:00: Recorded command exit 0; command argv SHA-256
  e995df4fcea08ed71b0344df47ea59a2d82a2b73022fe5428dc1d35ea58d1378.

- 2026-09-17T10:43:41+00:00: Recorded command exit 0; command argv SHA-256
  fecaa66bf9a4bc0764750f14551d13f000ab3d08e37a6bf803d464fb74cdd3e6.

- 2026-09-17T10:43:51+00:00: Recorded command exit 0; command argv SHA-256
  2fe8b0155814d43435ad3375dd681254a115999c120443323df35d8d3d880c10.

- 2026-09-17T10:44:02+00:00: Recorded command exit 0; command argv SHA-256
  4d106b9d6ff6475f98ed755b1c0fbf0ba3c9911fe6da24625f9880135a24b7a6.

- 2026-09-17T10:45:17+00:00: Recorded command exit 0; command argv SHA-256
  1b7575e9f74ad48cce919abaaf45ca8fb92ea4fd4680333eba2e71c3d4e04f79.

- 2026-09-17T10:45:26+00:00: Recorded command exit 0; command argv SHA-256
  1fa9d8f25791c10aed46bed9833926d0ab6ea7967b33fd77634480c1455bb7a1.

- 2026-09-17T10:45:36+00:00: Recorded command exit 0; command argv SHA-256
  4648c3693953ab7fcefc97153e91ca925ea793f70b122fb5d3b902bd43d20ab8.

- 2026-09-17T10:46:46+00:00: 2026-09-17T10:46:20Z: Released ownerless blocked after bounded v11
  attempt. Distinct 32 GiB QEMU/KVM runner, offline pinned JAR, private data disk, no network/host
  mounts, and cloud-init execution all functioned. Terminal full-exhaustive results: v7 reached TLC
  but native allocation failed under portable prlimit AS=3G; v8 required mode failed systemd-run
  --user with No medium; v9 failed Transport endpoint is not connected; v10 failed same plus asb
  evidence permission; v11 fixed evidence ownership and started a guest session bus, but systemd-run
  required containment failed with Process org.freedesktop.systemd1 exited with status 1. No
  terminal attestation was emitted, so no full-exhaustive success is claimed. Exact next action:
  provision/repair a guest user systemd manager that accepts transient units for asb, or extend the
  approved runner launcher with a documented system-scope cgroup path while preserving
  TLC_CGROUP_MODE=required; rerun from fresh exact candidate f16d2cb41 and capture attestation.
  Implementation branch remains clean at signed commit 7a6f7fd94 plus prior runner commits.

- 2026-09-17T10:47:46+00:00: Reclaiming AR-1302 to repair guest user-systemd transient-unit
  admission and rerun required full-exhaustive.

- 2026-09-17T10:47:49+00:00: Claimed by codex-ar1302-runner-20260917-vm2.

- 2026-09-17T10:48:25+00:00: Recorded command exit 0; command argv SHA-256
  d15d07c2976fbcedfc16e35ca647ff04afbf6a1d3f51fea11e46755251755f03.

- 2026-09-17T10:48:35+00:00: Recorded command exit 0; command argv SHA-256
  71a6eac4133f1a9b7562589d3630351e73df20f883a21570723202202617374d.

- 2026-09-17T10:48:45+00:00: Recorded command exit 0; command argv SHA-256
  d14d5c13d1cc1906add66de9401faf7086efed553d50663d5e659b3d7ff67f5a.

- 2026-09-17T10:50:03+00:00: Recorded command exit 0; command argv SHA-256
  ac7359bf39e80a938a039f9dfc2494a3edca734148d196d4680c20b7a297f843.

- 2026-09-17T10:50:13+00:00: Recorded command exit 0; command argv SHA-256
  ecf0edfbfd1bc5c23b7dd14f925a6df39fba7b9ea8f5b1d7cc27dbf6941d1628.

- 2026-09-17T10:50:22+00:00: Recorded command exit 0; command argv SHA-256
  1d95f1ffd809a68a8c013f9d1f132cbc5ebae493ac3ca39e0439ecba2ac72b5c.

- 2026-09-17T10:51:36+00:00: Recorded command exit 0; command argv SHA-256
  9690d291841ef48f574336896f3b996818687b8addab081812b43fd22f201f61.

- 2026-09-17T10:51:46+00:00: Recorded command exit 0; command argv SHA-256
  c5ae60edff7d2f6cfe6e66debcb2950c3bf1583a3764528b213877b4fa365891.

- 2026-09-17T10:51:55+00:00: Recorded command exit 0; command argv SHA-256
  ea49140b1f99035b77ad39aa45f4b5cf7b6aef5806acd933a2036195e8c863f8.

- 2026-09-17T10:52:54+00:00: Recorded command exit 0; command argv SHA-256
  97f37aa4496652a003374ffccadd9273f9398d19cc68c87c6d470b9a9a7bf1b7.

- 2026-09-17T10:53:04+00:00: Recorded command exit 0; command argv SHA-256
  5591fc8459119e1840f55a15fed5dae6666f34d9728c9243e44b36a12dfaca3a.

- 2026-09-17T10:53:13+00:00: Recorded command exit 1; command argv SHA-256
  2d20f180bec765419d20b7810b1745336bcd8fb1de360e06c1af68eebf954f52.

- 2026-09-17T10:53:28+00:00: Recorded command exit 1; command argv SHA-256
  c787648a6b4ff5268996eedca8b691ae6d7bd25ba6586208c97f71ccc5fe3a96.

- 2026-09-17T10:53:42+00:00: Recorded command exit 0; command argv SHA-256
  2d20f180bec765419d20b7810b1745336bcd8fb1de360e06c1af68eebf954f52.

- 2026-09-17T10:54:17+00:00: Recorded command exit 0; command argv SHA-256
  d96a30d18ff198e46e6da939fa8ee17070da2f328da8fb347cd51b9104f7eb75.

- 2026-09-17T10:54:27+00:00: Recorded command exit 0; command argv SHA-256
  3ca22dc20af8d327b2b5558da757881d8ee5e487674ed208da68551d86df7fea.

- 2026-09-17T10:54:37+00:00: Recorded command exit 0; command argv SHA-256
  fb62352af99e01d94cd32ac616678f5fcc5747490e5a859a4a37bbb3af20d8a4.

- 2026-09-17T10:55:52+00:00: Recorded command exit 0; command argv SHA-256
  ae4c14feed12b7de75a255b81b8688d7e9d4920194008d8031756cdfa6cef455.

- 2026-09-17T10:56:01+00:00: Recorded command exit 0; command argv SHA-256
  cede6d91aca058671ee364ab7c918271cd5b6670001b37a5db25ef1795db1a9f.

- 2026-09-17T10:56:11+00:00: Recorded command exit 0; command argv SHA-256
  6561e14c372d37730724cd3b635a70ce5a28546772a66442dec1d40ac39cb8d8.

- 2026-09-17T10:57:24+00:00: Recorded command exit 0; command argv SHA-256
  73f63084361142ef03384dc9eba8b78662404d11f766e46821aabe363659dd97.

- 2026-09-17T10:57:34+00:00: Recorded command exit 0; command argv SHA-256
  351f71998341c354fd6e302c6f9ce3b19d0fd1d88ae06214819e292eb032372e.

- 2026-09-17T10:57:43+00:00: Recorded command exit 1; command argv SHA-256
  207a70a66dd7d6d15211f20664743a7c3f9d0a2ae83085a371d06103236bfda2.

- 2026-09-17T10:58:36+00:00: Recorded command exit 0; command argv SHA-256
  45a58d224fba9858c02464e743e22739afc4429636193c2f5c0ffa153e36d314.

- 2026-09-17T10:58:56+00:00: Recorded command exit 0; command argv SHA-256
  207a70a66dd7d6d15211f20664743a7c3f9d0a2ae83085a371d06103236bfda2.

- 2026-09-17T10:59:55+00:00: Recorded command exit 0; command argv SHA-256
  03cf819f023ce3e61eb165fea0988051e7afb94062dfaa86490edad88357b612.

- 2026-09-17T11:00:08+00:00: Recorded command exit 0; command argv SHA-256
  cc34fd573959de5bf2db35519c9753278c23e0a92d63d65355d363cfbafbe677.

- 2026-09-17T11:00:18+00:00: Recorded command exit 0; command argv SHA-256
  f33412d5e85fe98bde22210dae1d7088e5b9cba6cb7a1a1be906b0636ef2840c.

- 2026-09-17T11:00:27+00:00: Recorded command exit 0; command argv SHA-256
  329d515d2188a04dab0dc823abf28a5dcc1640faafc33dadbcfd145419bd830e.

- 2026-09-17T11:00:36+00:00: Recorded command exit 0; command argv SHA-256
  ecc355baefed7c0d2e6d482779a4d55a21842ddda5c5d9cc4bd9492971653f13.

- 2026-09-17T11:00:45+00:00: Recorded command exit 0; command argv SHA-256
  ecc355baefed7c0d2e6d482779a4d55a21842ddda5c5d9cc4bd9492971653f13.

- 2026-09-17T11:00:56+00:00: Recorded command exit 0; command argv SHA-256
  c263992ab66aa46a295cd283fa11d2bcacf99e001c75379ffbcaa8693f4573f9.

- 2026-09-17T11:01:05+00:00: Recorded command exit 0; command argv SHA-256
  ea1bc87c9480f153af2546271a259b9a40bd9e244865d6ea718a0c787f410120.

- 2026-09-17T11:02:54+00:00: Recorded command exit 0; command argv SHA-256
  9dad6bc4c0eea631e9be6dfbede001d550321295790aa603a39fde8c4ab608c0.

- 2026-09-17T11:03:07+00:00: Recorded command exit 0; command argv SHA-256
  1ec7123185021ce85e9205f357b3c829594243934f748e96a886913a336e4dd9.

- 2026-09-17T11:03:16+00:00: Recorded command exit 0; command argv SHA-256
  7467aa8d72774ae29df9ac09c7c91466f9aa2d7c972a89eac4d51fe87b6e8069.

- 2026-09-17T11:03:26+00:00: Recorded command exit 0; command argv SHA-256
  0639a61fa7d263f959db5a027d9954259e26f23af62328b98e41797904ba7439.

- 2026-09-17T11:03:35+00:00: Recorded command exit 0; command argv SHA-256
  ad1d54167407f289aa4f1e0bb6703f90bd75a26f88f183937fc9c203cd86a6bc.

- 2026-09-17T11:03:45+00:00: Recorded command exit 0; command argv SHA-256
  6dae8326db929e47c232533243e96e0002801758a6a94b0bc0e7f34d0fd9af1f.

- 2026-09-17T11:03:54+00:00: Recorded command exit 0; command argv SHA-256
  992c8f08c7ff8d756274ff63f41e67cd8bb4d814133d3c21233bf5a87206e03b.

- 2026-09-17T11:05:14+00:00: Recorded command exit 0; command argv SHA-256
  a07959e0362405f145632c10856fff5ab0a0a61057e7a90d0855e18b2460b478.

- 2026-09-17T11:05:49+00:00: Recorded command exit 0; command argv SHA-256
  885f60fd2ffd2a88f9ae625db8bbab460945c6b6b46cf7d972d9e73cd3f520fe.

- 2026-09-17T11:05:59+00:00: Recorded command exit 0; command argv SHA-256
  aeabbe345327fb45fc24f592786831c3e3b6e19ce2525944e16895a3de1ef1fa.

- 2026-09-17T11:06:09+00:00: Recorded command exit 0; command argv SHA-256
  9e1e56ad00e71523b6463e2cd6694aa76d0ee693d92bc3fcb4aabef00ad8b2fc.

- 2026-09-17T11:07:39+00:00: Recorded command exit 0; command argv SHA-256
  074e679debc66266e3d3c5bc31207e7c3084bb3d2927c713902824e512541602.

- 2026-09-17T11:07:57+00:00: 2026-09-17T11:08:10Z: Reclaimed AR-1302 and repaired several runner
  layers. v14 proved guest user-systemd required containment can start, then failed only for 8 GiB
  root capacity. Enlarged clean offline data disk to 16 GiB; v15/v16 exposed and fixed evidence/temp
  ownership issues. Fresh v17/v18/v19/v20 retries were bounded and stopped after cloud-init
  preflight stalled before verify; the guest user-systemd bus/transient-unit path is not reliably
  usable from noninteractive cloud-init. No terminal full-exhaustive attestation exists. Exact next
  action: provision a guest image with user-systemd/dbus preconfigured at boot (bus socket and
  user@1000 ready before cloud-final) or an approved system-scope cgroup launcher accepted by the
  unchanged required attestation; then run exact candidate f16d2cb41 once on a clean 16 GiB+ data
  disk and capture all model outcomes plus attestation. No gate was weakened.

- 2026-09-17T11:09:00+00:00: Concrete image repair: add a boot-enabled systemd unit requiring
  user-runtime-dir@1000 and starting the asb session bus before cloud-final; then make one clean
  required full-exhaustive attempt.

- 2026-09-17T11:09:03+00:00: Claimed by codex-ar1302-runner-20260917-imagebus.

- 2026-09-17T11:09:26+00:00: Recorded command exit 0; command argv SHA-256
  9434a114e09eeb3104c8e555bccdeecb595f3988a21b3bc244ecaf02f47120e2.

- 2026-09-17T11:09:36+00:00: Recorded command exit 0; command argv SHA-256
  1126533269a0a342f9d5fd92c36c3d5be60a7fd0ff9234591112b569a3343d55.

- 2026-09-17T11:09:57+00:00: Recorded command exit 0; command argv SHA-256
  a529fde896ebcb4b9d0f8a98c7ab14f505d791404609b0be00f42af602c55f2c.

- 2026-09-17T11:10:24+00:00: Recorded command exit 0; command argv SHA-256
  9a68e2b1c9c8b3442d4a38df0025c31c43aaa42fa461ada7d52b7db2b22bbbbb.

- 2026-09-17T11:10:46+00:00: Recorded command exit 0; command argv SHA-256
  be2b10f53088e32a701c1118b4f63b46b532cb4cce4a9b3883d81d7fdd422f86.

- 2026-09-17T11:11:05+00:00: Recorded command exit 0; command argv SHA-256
  43a958575dec316c2d275c1fde751a6c7c6669f546af016803c1ec5825c7cace.

- 2026-09-17T11:11:15+00:00: Recorded command exit 0; command argv SHA-256
  e930c0a045775d68a75622a6aae0bb1294716fbe21199a5fcee272fe9b450104.

- 2026-09-17T11:11:24+00:00: Recorded command exit 0; command argv SHA-256
  19a2bcbca5abbb2415c86a9185e9941f55bccc437b1852143fe4e079f6bad739.

- 2026-09-17T11:11:33+00:00: Recorded command exit 0; command argv SHA-256
  e8a8228d17464b2622c4957e5fd40bc9c0c2369df0b04a014471797c50abbde5.

- 2026-09-17T11:11:50+00:00: Recorded command exit 0; command argv SHA-256
  106032ae92be995b7e51eb6c49ba39e4356b0ee2292fe4b96834119a9b313863.

- 2026-09-17T11:12:00+00:00: Recorded command exit 0; command argv SHA-256
  06b21c0ddc2ecc78d8c00d7fd421b4b02a9c9d459a0dba5d5142c13a70334e16.

- 2026-09-17T11:16:30+00:00: Recorded command exit 0; command argv SHA-256
  37cef7c3579fd1569c966c71976a880ed82e0d27c472082bfea5357bebdae871.

- 2026-09-17T11:17:07+00:00: Recorded command exit 1; command argv SHA-256
  19a2bcbca5abbb2415c86a9185e9941f55bccc437b1852143fe4e079f6bad739.

- 2026-09-17T11:17:33+00:00: 2026-09-17T11:18:00Z: Fresh image-level repair added a boot-enabled
  asb-session-bus.service requiring user-runtime-dir@1000 and ordered before cloud-final; fresh 16
  GiB data disk and 32 GiB/16 GiB VM were used with no network or host mounts. The bounded v22
  attempt reached user@1000 and high QEMU CPU but was stopped before cloud-final produced runner
  evidence; after offline fsck repair, the data disk contained no full-exhaustive.log or
  attestation, so no verify terminal result can be claimed. The image-level bus path remains an
  infrastructure blocker: one clean future attempt must capture systemd unit status/bus socket and
  terminal attestation without cloud-init shell retries. Runner is stopped and AR is ownerless
  blocked.

- 2026-09-17T11:29:18+00:00: One bounded qualification attempt using the existing image-level
  systemd bus unit, fresh 16 GiB data disk, and exact f16d2cb41 candidate.

- 2026-09-17T11:29:22+00:00: Claimed by codex-ar1302-runner-20260917-final.

- 2026-09-17T11:29:48+00:00: Recorded command exit 0; command argv SHA-256
  446e8ef4c49a04374996deaa2fa12b0f8210af51574b7039896cbc1ff1f3c7cf.

- 2026-09-17T11:29:59+00:00: Recorded command exit 0; command argv SHA-256
  e40b9e008bacc0a814e7d69957cb975134d0648486dc6eafd63f36ecd9b3dbc1.

- 2026-09-17T11:30:09+00:00: Recorded command exit 0; command argv SHA-256
  8147a1378d67bfdaa94f1b68a58dd34e5c80f0b8d5f98cec920fafff927b1bf7.

- 2026-09-17T11:30:19+00:00: Recorded command exit 0; command argv SHA-256
  8ca08155a4baec633f1f53d50e3b31c42d3f856e243a9e32f123e6ac781fcbd6.

- 2026-09-17T11:30:38+00:00: Recorded command exit 0; command argv SHA-256
  4f82822067516572c8abc20e3f573d65dcfc3bf6abb1438f24a119226c5c786d.

- 2026-09-17T11:30:47+00:00: Recorded command exit 0; command argv SHA-256
  4f82822067516572c8abc20e3f573d65dcfc3bf6abb1438f24a119226c5c786d.

- 2026-09-17T11:30:56+00:00: Recorded command exit 0; command argv SHA-256
  18e5122b2600a72221ad64ff4388df99ee1b2f9aa1f8e93f3ce20e88198d0108.

- 2026-09-17T11:31:07+00:00: Recorded command exit 0; command argv SHA-256
  18e5122b2600a72221ad64ff4388df99ee1b2f9aa1f8e93f3ce20e88198d0108.

- 2026-09-17T11:31:26+00:00: Recorded command exit 0; command argv SHA-256
  ae724897313e5d69b087f3f930096167f3cc8d5ab9d21dd244cf3173e9ef2b7e.

- 2026-09-17T11:33:24+00:00: Recorded command exit 0; command argv SHA-256
  5175266eead4eafd6c90f7df78c385a0f8b0701c7f48ce04ef123daefd23f5ea.

- 2026-09-17T11:33:45+00:00: 2026-09-17T11:34:00Z: Final bounded qualification attempt used a fresh
  image copy with image-level asb-session-bus.service, fresh 16 GiB data disk, 32 GiB RAM/16 GiB
  swap, no network/host mounts, pinned JAR, and exact f16d2cb41 state. Boot evidence is explicit:
  systemd started user@1000 but asb-session-bus.service failed before cloud-final; serial lines
  812-816 show service start then FAILED. QEMU consumed CPU while cloud-final attempted verify, but
  no full-exhaustive.log or attestation was produced. Runner was stopped through handoffctl. AR-1302
  remains infrastructure-blocked; no release gate was weakened and no success is claimed. Next
  action requires fixing unit ordering/activation so the session bus is active before cloud-final,
  then one terminal-attested run.

- 2026-09-17T12:10:54+00:00: Refreshing stale next_action to the final image-level bus activation
  blocker; no rerun.

- 2026-09-17T12:10:57+00:00: Claimed by codex-ar1302-diagnosis.

- 2026-09-17T12:11:12+00:00: Recorded command exit 0; command argv SHA-256
  4a558995c70694f9aa845fc2546212a09840f0125b3843a9ed68ebe53c517d07.

- 2026-09-17T12:11:39+00:00: Diagnosis: final serial evidence shows user-runtime-dir@1000 finished,
  then asb-session-bus.service started concurrently with user@1000 and failed before cloud-final;
  user@1000 later succeeded. The image unit is ordered only After=user-runtime-dir@1000, not
  After=user@1000, and uses runuser plus a forking session dbus daemon from a system oneshot; this
  race/activation design is the concrete likely failure. Offline mount inspection was unavailable
  because the boot-tested qcow2 remained dirty, so no additional image mutation was made. Stale
  ownerless AR-1293 QEMU cleanup was performed by coordinator.

- 2026-09-17T12:11:42+00:00: Recorded command exit 0; command argv SHA-256
  d37a24e5d17105ef564a0d77bc26084c9317d844667cab5290c38a64f6065b6a.

- 2026-09-17T12:12:03+00:00: Diagnosis complete and ownerless release: final serial proves the bus
  unit raced user@1000 (user-runtime-dir finished; bus unit failed; user@1000 succeeded afterward).
  Current exact next_action records the image-level repair: order After/Requires user@1000, use
  non-forking Type=simple dbus daemon, bounded readiness check, then one terminal-attested run. No
  further rerun or gate weakening performed.

- 2026-09-17T12:12:43+00:00: A concrete image-level repair is now identified: the final serial log
  shows user-runtime-dir@1000 finished, then asb-session-bus.service raced user@1000 and failed.
  Resume for one bounded image repair only: order after user@1000, use Type=simple bus daemon with
  bounded readiness, then one clean full-exhaustive attempt.

- 2026-09-17T12:12:45+00:00: Claimed by ar1302_image_repair.

- 2026-09-17T12:13:19+00:00: Recorded command exit 0; command argv SHA-256
  f8833dfcb418801003825c960c32ab88cad1d7fd94dc4b1a312bad75374aa59f.

- 2026-09-17T12:13:30+00:00: Recorded command exit 0; command argv SHA-256
  db79b5390a2018bfbe5cdfae17792e37b93d5651b81bac10cedaebc24b93bd49.

- 2026-09-17T12:13:46+00:00: Recorded command exit 0; command argv SHA-256
  3040c55127d5f5b7db668abdefb017f73f6921d542a85575f8bcbc888cb509a9.

- 2026-09-17T12:13:56+00:00: Recorded command exit 0; command argv SHA-256
  cfb5f69fe35e01f15cf85ced4038d5cedb66cdc49eff02c102d3c9f048c0f5df.

- 2026-09-17T12:14:06+00:00: Recorded command exit 0; command argv SHA-256
  8df02f7a1be27a5889e726f588d15a1302a2071f785c4aea086e31c33088cce0.

- 2026-09-17T12:14:20+00:00: Recorded command exit 0; command argv SHA-256
  8e094cde8eb9868bef060ede4a4c6b7b019d12ea76a5f70310da5afc1945883d.

- 2026-09-17T12:14:38+00:00: Recorded command exit 0; command argv SHA-256
  8e094cde8eb9868bef060ede4a4c6b7b019d12ea76a5f70310da5afc1945883d.

- 2026-09-17T12:14:57+00:00: Recorded command exit 0; command argv SHA-256
  9d7e53ca50f647969f4c67fc85b8d42f1ac3efd963d40ff00f74b4ce4930012f.

- 2026-09-17T12:16:07+00:00: 2026-09-17T12:16:00Z: Concrete image repair applied and one clean
  attempt completed. Fresh image unit now has Requires=user@1000.service, After=user@1000.service,
  Type=simple, User=asb, non-forking dbus-daemon, and 10s startup bound; serial confirms user@1000
  and asb-session-bus.service both started successfully before cloud-final. Fresh 16 GiB data disk,
  32 GiB RAM, 8 vCPU, 16 GiB swap, no network/host mounts, pinned JAR and exact candidate were used.
  Terminal result from data evidence: JAR hash verified, then Failed to start transient service
  unit: Process org.freedesktop.systemd1 exited with status 1; ASB_RC=1; no attestation. Runner
  powered off cleanly and fsck completed. Remaining blocker is the guest systemd user manager
  refusing the TLC transient unit despite the session bus being active; no gate was weakened or
  success claimed.

- 2026-09-17T12:17:46+00:00: Final image repair completed: user@1000 and asb-session-bus started
  before cloud-final, but the exact required transient systemd containment still failed with Process
  org.freedesktop.systemd1 status 1 and no attestation. Keep blocked; no blind rerun.

- 2026-09-17T12:17:49+00:00: Claimed by coordinator_state_cleanup.

- 2026-09-17T12:18:26+00:00: Final AR-1302 evidence is durable in 64a9f6dc7: session-bus activation
  race repaired, but required transient systemd containment still fails. Runner powered off, fsck
  completed, no QEMU remains; keep blocked.

- 2026-09-17T12:18:28+00:00: Released after reconciling final image repair and transient containment
  blocker; ownerless blocked.

- 2026-09-17T12:29:52+00:00: Evidence review only; no rerun. The image-level dbus service starts,
  but it creates a standalone session bus that is not the bus owned by user@1000; required
  systemd-run --user then exits status 1. A distinct repair must provision the native user-manager
  bus (dbus-user-session/libpam-systemd and linger in the immutable guest image) and pass a bounded
  transient-unit preflight before launching TLC.

- 2026-09-17T12:29:55+00:00: Claimed by codex-ar1302-preflight-diagnosis.

- 2026-09-17T12:30:24+00:00: Distinct safe repair proposed from completed evidence; no TLC rerun.
  The bus service was standalone, not the native user-manager bus. Required guest image properties:
  immutable offline image with dbus-user-session/libpam-systemd provenance, lingering asb user@1000,
  32 GiB RAM, 8 vCPU, 16 GiB swap, separate >=16 GiB data disk, no network or host mounts. Before
  any verify command, run as asb with XDG_RUNTIME_DIR=/run/user/1000 and
  DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus: systemctl --user is-system-running; then
  systemd-run --user --wait --pipe --collect --property=MemoryMax=3G --property=MemorySwapMax=3G
  --property=CPUQuota=200% --property=TasksMax=64 /usr/bin/true. Both must exit 0 and bus ownership
  must identify user@1000; otherwise fail closed without launching TLC. Only after positive
  admission should exact f16d2cb41 full-exhaustive run.

- 2026-09-17T12:30:37+00:00: Recorded command exit 0; command argv SHA-256
  f3b19139c55a1adfd4799226f94a4277369efdf361b4a8778f667503f037b7f0.

- 2026-09-17T12:32:11+00:00: Heartbeat by codex-ar1302-preflight-diagnosis.

- 2026-09-17T12:32:52+00:00: Recorded command exit 0; command argv SHA-256
  862e43e9c54a5c31defa5a3cdf6c6c842d40026382868b589d6d6cd9c68828dc.

- 2026-09-17T12:33:35+00:00: Recorded command exit 0; command argv SHA-256
  5fc6d8becc213b72e56c9ade381a16275521ef4d44f619756fe17db0b0e2e9ca.

- 2026-09-17T12:34:49+00:00: Recorded command exit 0; command argv SHA-256
  862e43e9c54a5c31defa5a3cdf6c6c842d40026382868b589d6d6cd9c68828dc.

- 2026-09-17T12:35:33+00:00: Recorded command exit 0; command argv SHA-256
  b73e3735bd47af48fe4d1fcafda23a4d934974ffbec716e132daf14a79c7b87e.

- 2026-09-17T12:36:21+00:00: Recorded command exit 0; command argv SHA-256
  137230a5d609610b30c9a5a58a316f39e1dd72c09412833599078e32ab5e9160.

- 2026-09-17T12:37:13+00:00: Recorded command exit 0; command argv SHA-256
  fa3438aef1b80cd2498029fc2a46a2fb4a29282c67f0744f8a8b5bf936b8253e.

- 2026-09-17T12:39:34+00:00: Heartbeat by codex-ar1302-preflight-diagnosis.

- 2026-09-17T12:43:28+00:00: Sanitized checkpoint: fresh repair image used 32 GiB RAM, 8 vCPU, 30
  GiB usable root after resize, 8 GiB guest swap, no network/host mounts, and pinned f16d2cb41 data
  disk. Exact required preflight passed through handoffctl: user@1000 active, user systemd running,
  /run/user/1000/bus present, systemd-run --user /bin/true exit 0 with MemoryMax=3G,
  MemorySwapMax=3G, CPUQuota=200%, TasksMax=64, RuntimeMaxSec=1800. Portable-smoke then passed for
  f16d2cb41721bf8f17aa5aa75ab01520aeb91eb8 with TLC no-error and success attestation. A subsequent
  required-pr helper failed before verify because /mnt/asb-data mount point/device was absent in
  that boot; this is runner data-disk wiring, not TLC. Full-exhaustive was started only after the
  exact preflight, but manually interrupted during Handoffctl liveness exploration (~9.3M distinct
  states); no full attestation or qualification. QEMU repair process was stopped cleanly and no
  socat remains.

- 2026-09-17T12:43:40+00:00: Ownerless blocked after exact preflight and portable-smoke evidence;
  required-pr failed on missing /mnt/asb-data wiring, full-exhaustive was interrupted and has no
  qualification. Next action is fresh virtio data-disk UUID/fstab/boot-mount repair, then exact
  preflight and portable-smoke through handoffctl.

- 2026-09-17T12:45:02+00:00: Resume distinct runner repair: fix virtio data-disk UUID/fstab boot
  mount, then rerun exact containment and portable-smoke; full-exhaustive remains gated.

- 2026-09-17T12:45:09+00:00: Claimed by codex-ar1302-data-mount-repair.

- 2026-09-17T12:45:50+00:00: Recorded command exit 0; command argv SHA-256
  d7a5f8493c5c52feaa2c04132e918a7b1e04b5fa3c56bd1c9fb690e6da2f6931.

- 2026-09-17T12:46:02+00:00: Recorded command exit 0; command argv SHA-256
  09b621166ae51173c21a0498634e493cd640fb6aaa6d9dda3ca3ed0f97bb8b17.

- 2026-09-17T12:46:11+00:00: Recorded command exit 0; command argv SHA-256
  111750c83d2f820db75eca1d6a59fc2a052d81f77c14b849d4a3dc3e1b7bb8b1.

- 2026-09-17T12:46:21+00:00: Recorded command exit 0; command argv SHA-256
  ead89d2d53b94c11957b4984dff3e1212a5cb52e4124c20b30db35b10dba4f15.

- 2026-09-17T12:46:30+00:00: Recorded command exit 0; command argv SHA-256
  2251b687b7c7a373590248ed4c1184ee7f3a73708d2a762e2c74c777378e76fa.

- 2026-09-17T12:46:39+00:00: Recorded command exit 1; command argv SHA-256
  bdbd7d7ab0416dde104c6423ae406e44dd66e707310d5969444eec6fe59cc540.

- 2026-09-17T12:46:49+00:00: Recorded command exit 0; command argv SHA-256
  bdbd7d7ab0416dde104c6423ae406e44dd66e707310d5969444eec6fe59cc540.

- 2026-09-17T12:46:58+00:00: Recorded command exit 0; command argv SHA-256
  2251b687b7c7a373590248ed4c1184ee7f3a73708d2a762e2c74c777378e76fa.

- 2026-09-17T12:47:08+00:00: Recorded command exit 0; command argv SHA-256
  bdbd7d7ab0416dde104c6423ae406e44dd66e707310d5969444eec6fe59cc540.

- 2026-09-17T12:47:42+00:00: Recorded command exit 0; command argv SHA-256
  a14dddee9359722086d76ffbd2c865cfdf94d8b0654cf1c3b2b66d21aaa1e6d0.

- 2026-09-17T12:48:02+00:00: Recorded command exit 0; command argv SHA-256
  a402e04c8c70c1fab77f294175fafa8f292dd10cd55729668da41271854da77e.

- 2026-09-17T12:48:53+00:00: Recorded command exit 1; command argv SHA-256
  c14b5f828f87cb214fecae8cc1ae7b034e3708cc335400f2d9687eab84164fb7.

- 2026-09-17T12:49:18+00:00: 2026-09-17T12:49:20Z: Fresh UUID-wired VM/data run completed mount
  preflight successfully. The guest mounted the recorded ext4 data-disk UUID at /mnt/asb-data,
  verified the pinned JAR SHA-256, and started TLC portable-smoke. TLC failed before model
  completion with native JVM allocation failure under portable prlimit AS=3G (AllocateHeap 16
  bytes), ASB_RC=1; no attestation. Required-pr was correctly not launched because smoke did not
  pass. Runner powered off and data fsck completed.

- 2026-09-17T12:49:21+00:00: Recorded command exit 0; command argv SHA-256
  d2d0ad76bf84a0d8480eae80cf11b1c9aadf63dd417c845be05fb83bb06c963c.

- 2026-09-17T12:49:38+00:00: Mountrepair checkpoint complete: boot mount succeeded and UUID-wired
  data path was usable; portable-smoke reached TLC but failed native JVM allocation under AS=3G
  prlimit, with no attestation. Required-pr/full-exhaustive was not launched. Runner is stopped;
  next action is a capacity-safe portable containment repair followed by successful portable-smoke
  evidence.

- 2026-09-17T12:50:20+00:00: Resume distinct capacity repair: preserve bounded portable containment
  but eliminate JVM native allocation failure; rerun exact preflight and portable-smoke before any
  required/full tier.

- 2026-09-17T12:50:23+00:00: Claimed by codex-ar1302-capacity-repair.

- 2026-09-17T12:50:58+00:00: Capacity diagnosis: portable runner invokes prlimit --as equal to the
  attested 3G memory_max. On the clean 32 GiB/16 GiB-swap UUID-wired VM, TLC portable-smoke verified
  the pinned JAR then failed JVM native allocation (AllocateHeap 16 bytes) under AS=3G. Increasing
  AS ad hoc would decouple enforcement from the attested contract and weaken the gate; increasing
  guest RAM does not fix RLIMIT_AS. No rerun performed.

- 2026-09-17T12:51:01+00:00: Recorded command exit 0; command argv SHA-256
  d709e5a449886c08660b0495f04fac85fef8ecde7d64346771b5f2dd8e74c358.

- 2026-09-17T12:52:00+00:00: 2026-09-17T12:51:30Z: Capacity repair review complete. The portable
  Docker helper already provides a 20 GiB address-space bound, but the VM portable-smoke path
  executes the reviewed AR-1293 tools/tlc_runner.py, whose portable mode sets RLIMIT_AS equal to the
  attested 3 GiB memory_max. The clean UUID-wired VM proved mount/JAR/TLC startup but failed native
  JVM allocation under that ceiling. Raising AS ad hoc or changing tier evidence would
  weaken/circumvent the reviewed contract; no source or gate change was made.

- 2026-09-17T12:52:03+00:00: Recorded command exit 0; command argv SHA-256
  4e2a95a82c38486469748dbfc1df62aad08e49ea335a15c425bb128a75bd75d4.

- 2026-09-17T12:52:22+00:00: No repair commit was made because the required change belongs to the
  reviewed AR-1293/state TLC runner contract, not VM provisioning. UUID mount and portable-smoke
  evidence are complete; the VM path fails native JVM allocation with RLIMIT_AS=3G. Raising that
  limit ad hoc would violate attested containment. AR-1302 is released ownerless blocked pending a
  reviewed separate virtual-address-space bound with tests/evidence.

- 2026-09-17T13:14:05+00:00: AR-1293 contract repair is reviewed at f1931686c: portable launcher now
  separates bounded 8G address space from 3G physical/swap. Requalify fresh UUID-wired VM exact
  preflight and portable-smoke; no required/full until attestation succeeds.

- 2026-09-17T13:14:08+00:00: Claimed by codex-ar1302-requalify-address-space.

- 2026-09-17T13:15:06+00:00: Recorded command exit 0; command argv SHA-256
  7ecf66fc70bcbbe8a6ba5ec2a3c095d2af57f61b8d0def97de5d8ae3d6a66c06.

- 2026-09-17T13:15:39+00:00: Container requalification passed at
  /srv/data/projects/.asb-ar1302/evidence/portable-smoke-address-space.json: immutable linux/amd64
  digest c0d1549d1e0f5fa5b83622ec0033b00456107e0b1d0cfcce4c1d831532ce621e, no network or host
  mounts, read-only root, dropped capabilities, no-new-privileges, 2 CPUs, 20 GiB memory/swap, 64
  PIDs; HandoffctlBinding exit 0 in 0.818s. This does not qualify the requested UUID-wired VM yet.

- 2026-09-17T13:16:14+00:00: Heartbeat by codex-ar1302-requalify-address-space.

- 2026-09-17T13:16:32+00:00: Container portable-smoke passed in portable-smoke-address-space.json
  under pinned amd64 Docker containment. VM qualification is blocked: no reusable reviewed
  UUID-wired VM launch helper exists; only historical private seeds/raw disks remain, so exact
  f1931686c source/JAR injection cannot safely proceed without stale-disk or overlap risk. No VM
  attestation, pr-publication, or full-exhaustive claim.

- 2026-09-17T13:17:27+00:00: Create a reviewed reusable UUID-wired VM launcher under the state
  runner worktree, with pinned image, 32G/8vCPU/16G swap, no network/host mounts, boot mount
  preflight, and sanitized serial evidence. Then run f1931686c portable-smoke.

- 2026-09-17T13:17:30+00:00: Claimed by codex-ar1302-vm-launcher.

- 2026-09-17T13:19:01+00:00: Recorded command exit 1; command argv SHA-256
  fe2d5a04a0305d2ae85fc449ea519d5529c872a0e938adf7e961ef784c13bcc1.

- 2026-09-17T13:19:17+00:00: Recorded command exit 1; command argv SHA-256
  bfcb52ab5d410f86f1a5df19a04148648e398b4ed4418072e0097e433be4c25f.

- 2026-09-17T13:19:28+00:00: Recorded command exit 1; command argv SHA-256
  ec49453acf45fa227dfb791daeb8614c81609a9c2d86cc7c707836e188492e13.

- 2026-09-17T13:19:37+00:00: Recorded command exit 1; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:19:55+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:20:05+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:20:15+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:20:55+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:21:06+00:00: Recorded command exit 1; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:21:16+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:21:40+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:21:57+00:00: Recorded command exit 0; command argv SHA-256
  7b1ce8f18cbe65b517165db452fc17ec25bb1cba0a1c3a4dbb02c5f616a116dc.

- 2026-09-17T13:22:09+00:00: Recorded command exit 0; command argv SHA-256
  1509d5694a3759fd1c0be33c5f6c2756670c6d9d7febc72f2a712d4f408f8619.

- 2026-09-17T13:22:29+00:00: Recorded command exit 0; command argv SHA-256
  a0c6696c02e57f3a531e676ba6eb0c67d1f793c3e011c6f691760aacfc960698.

- 2026-09-17T13:23:05+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:23:14+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:23:24+00:00: Recorded command exit 1; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:24:19+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:24:28+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:24:38+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:24:53+00:00: Recorded command exit 0; command argv SHA-256
  7b1ce8f18cbe65b517165db452fc17ec25bb1cba0a1c3a4dbb02c5f616a116dc.

- 2026-09-17T13:25:03+00:00: Recorded command exit 0; command argv SHA-256
  f87f3f65f41f03a11edf874320cbac3bf5973a0bae633d312af42950df2c3a97.

- 2026-09-17T13:25:34+00:00: Launcher implementation is signed/DCO at 6907c558a. It validates
  project-local non-symlink root/data/serial paths and reviewed qemu-system-x86_64, requires fresh
  non-existing overlay, creates root-backed qcow2 overlays, assigns the reviewed data UUID as virtio
  serial, uses -net none, 32G RAM, 8 vCPUs, bounded timeout, and cleanup. Five focused tests plus
  Ruff pass. VM execution/guest preflight/attestation remain outstanding.

- 2026-09-17T13:26:03+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:26:13+00:00: Recorded command exit 1; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:26:23+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:26:44+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:26:59+00:00: Recorded command exit 0; command argv SHA-256
  7b1ce8f18cbe65b517165db452fc17ec25bb1cba0a1c3a4dbb02c5f616a116dc.

- 2026-09-17T13:27:09+00:00: Recorded command exit 0; command argv SHA-256
  2f19866966241bfcbebe068b88f884a8a45aa065c71bd73a0f0c3a74da050c87.

- 2026-09-17T13:27:29+00:00: Lifecycle hardening is signed/DCO at 1fd5e31cf: run_lifecycle creates
  the overlay, builds the bounded offline QEMU argv, runs with a strict timeout, and always cleans
  the run overlay and serial artifact. Six focused tests pass. VM execution and guest
  preflight/attestation remain outstanding.

- 2026-09-17T13:28:01+00:00: Recorded command exit 1; command argv SHA-256
  94b99e667bf18d7639c2e7952be5b6fdf7c870b6aae811e3b47c1c2709d35950.

- 2026-09-17T13:28:25+00:00: Recorded command exit 0; command argv SHA-256
  ae4b185f2d8a97cf266a30385056440baae3e4b8fb2f1a09d892f36564f5d9e7.

- 2026-09-17T13:28:35+00:00: Recorded command exit 0; command argv SHA-256
  40850b86ed85bf508f6d37e90216635a99a7df9bed10f45d5a6940b1605c4b49.

- 2026-09-17T13:28:45+00:00: Recorded command exit 0; command argv SHA-256
  48bab4c210616f9d7476387ddeba7192eadde15aca80efb1bb86da5552ec4710.

- 2026-09-17T13:29:01+00:00: Recorded command exit 1; command argv SHA-256
  6e33b36a57c19722d7d1b2a064d172b86a203ab859c1f2620f0578b34ee2f7f1.

- 2026-09-17T13:29:27+00:00: Recorded command exit 0; command argv SHA-256
  ae4b185f2d8a97cf266a30385056440baae3e4b8fb2f1a09d892f36564f5d9e7.

- 2026-09-17T13:29:37+00:00: Recorded command exit 0; command argv SHA-256
  31841db4f05deea6b79c2597856bcec203bbb51fd562b1cd6b0c339c29d1fa2d.

- 2026-09-17T13:30:42+00:00: Recorded command exit 0; command argv SHA-256
  e8b2b173bc2a746397c8c320dc8c1e349414ad6c004cae64ad364f289f6f9cd1.

- 2026-09-17T13:31:00+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:31:10+00:00: Recorded command exit 1; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:31:19+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:31:29+00:00: Heartbeat by codex-ar1302-vm-launcher.

- 2026-09-17T13:31:43+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:31:53+00:00: Recorded command exit 0; command argv SHA-256
  94bc8295a401cc3c4c58f044d83e0c82d46ca97caac771426b331c08492ccae3.

- 2026-09-17T13:32:02+00:00: Recorded command exit 0; command argv SHA-256
  e8ae288056e98090654cc08b718b5a4536da3fd442af5d8e3b07f5434cd8a6e4.

- 2026-09-17T13:32:18+00:00: Signed launcher commits 1fd5e31cf, 37dbbee0b, and 973ea8a67 provide
  bounded lifecycle, root-backed overlay creation, virtio UUID serial, no-network argv, timeout
  cleanup, and 6/6 focused tests with Ruff green. Actual fresh VM boot failed closed: SeaBIOS
  reported Boot failed: not a bootable disk / No bootable device using the pinned Ubuntu root path
  with the current -nodefaults/virtio launch. The VM was terminated and disposable overlay/serial
  cleanup completed. Next action: repair boot-device/image wiring in a reviewed launcher change,
  then rerun guest UUID/mount preflight and f1931686c portable-smoke; no VM attestation or
  qualification claimed.

- 2026-09-17T13:32:59+00:00: Repair reviewed boot-device/image wiring after pinned Ubuntu SeaBIOS
  no-boot failure; preserve no-network/no-host-mount/bounded UUID runner properties, then rerun
  fresh VM preflight and exact f1931686c portable-smoke.

- 2026-09-17T13:33:19+00:00: Claimed by codex-ar1302-boot-repair.

- 2026-09-17T13:33:29+00:00: Recorded command exit 0; command argv SHA-256
  0b5a103d792f3993be7e299d2c4bcf744f96b5a2c58dcf9fa4b16aa71a0765aa.

- 2026-09-17T13:33:39+00:00: Recorded command exit 0; command argv SHA-256
  c4460cd790804a2a7b2c3ca14816b53f6ab1b5aed6730b736ba3aa461d3ebb83.

- 2026-09-17T13:33:49+00:00: Recorded command exit 0; command argv SHA-256
  96701017e485b9df3234ac745e38edbd4ce843805a9c15350db23d54bc4ea2ee.

- 2026-09-17T13:33:59+00:00: Recorded command exit 0; command argv SHA-256
  7543b6b57350961bf59cde635bdd84c40877e131a35a2d8dc28429672b20a17d.

- 2026-09-17T13:34:15+00:00: Recorded command exit 0; command argv SHA-256
  ae4b185f2d8a97cf266a30385056440baae3e4b8fb2f1a09d892f36564f5d9e7.

- 2026-09-17T13:34:24+00:00: Recorded command exit 0; command argv SHA-256
  2a5fe4dcdeb879174b8e13362994084259291362a9f540f3ef39cdb8dcee22a8.

- 2026-09-17T13:36:01+00:00: Recorded command exit 0; command argv SHA-256
  37b8d76ed51bd0133160661acb0bd5afc82655ad0a8a24461e01c80a92f70468.

- 2026-09-17T13:36:11+00:00: Recorded command exit 143; command argv SHA-256
  24707341df6e1924a3441e23752f646be90cc44ba85c9d26765998760231086c.

- 2026-09-17T13:36:21+00:00: Recorded command exit 0; command argv SHA-256
  c741fd8ef5e0593c6388cd75ff8651a3ea6c353954f820bff1522bce64e840a4.

- 2026-09-17T13:36:36+00:00: Boot wiring repair signed at 9174db1c7; focused 6/6 tests and Ruff
  pass. Fresh VM now boots the root image successfully, but with -net none the guest stalls
  indefinitely on systemd-networkd-wait-online before cloud-init/UUID mount preflight; bounded
  lifecycle was terminated and cleanup performed. The attempt therefore produced no guest mount
  proof or f1931686c portable-smoke attestation. Next action: use the receipt-approved prepared root
  overlay image (not the base cloud image), add a boot-time offline seed/service that disables only
  the guest wait-online dependency without enabling networking, then rerun preflight and smoke.

- 2026-09-17T13:36:41+00:00: Use receipt-approved prepared bootable root_overlay, verify provenance,
  and add offline guest seed/service only if state-owned and preserves -net none; rerun UUID mount
  preflight and exact f1931686c portable-smoke with bounded cleanup.

- 2026-09-17T13:36:56+00:00: Claimed by codex-ar1302-prepared-root.

- 2026-09-17T13:37:31+00:00: Prepared-root repair could not safely proceed. Receipt SHA256SUMS
  authorizes only the base Ubuntu image digest 612b2c0c...; the prepared root overlay
  /srv/data/projects/asb-state-tlc-vm-32g/asb-state-tlc-32g.qcow2 has observed SHA256 49d5d97c...
  but no matching receipt provenance. Existing exact-preflight and qemu scripts are private
  historical artifacts and cannot be reused as the reviewed launcher/seed. No VM UUID/mount evidence
  or f1931686c portable-smoke attestation was produced. Next action: create a reviewed seed/receipt
  that records the prepared root hash and offline mount service, then rerun with -net none.
