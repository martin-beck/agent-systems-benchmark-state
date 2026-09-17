---
{
  "branch": "feature/ar-1302-portable-tlc-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T08:58:11+00:00",
  "depends_on": [],
  "id": "AR-1302",
  "next_action": "Promote and provision a digest-pinned x86_64 container/VM runner with portable cgroup containment, bounded thread/memory/swap capacity, and owner-private evidence paths for AR-1293.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "coordinator-ar1302-full-20260917",
  "plan": "../plans/AR-1302.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision a clean portable TLC CI/VM runner for state formal admission.",
  "task_revision": 98,
  "title": "Portable TLC CI/VM runner",
  "updated_at": "2026-09-17T08:14:46+00:00",
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
