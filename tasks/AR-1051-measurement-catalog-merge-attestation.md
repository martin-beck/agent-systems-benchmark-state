---
{
  "branch": "docs/measurement-catalog-merge-attestation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:31:24+00:00",
  "depends_on": [
    "AR-1045"
  ],
  "id": "AR-1051",
  "next_action": "Push exact approved head 7b3ef113d2b77c3982748f16c540d0e556252464, open the protected-merge PR, and require all exact-head checks before merge.",
  "observed_branch": "docs/measurement-catalog-merge-attestation",
  "observed_dirty": 0,
  "observed_head": "7b3ef113d2b77c3982748f16c540d0e556252464",
  "owner": "codex-ar1051-measurement-catalog-attestation-20260911",
  "plan": "../plans/AR-1051.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Record the exact reviewed measurement-catalog merge and its non-compliant GitHub-authored DCO identity without rewriting history.",
  "task_revision": 64,
  "title": "Attest the measurement catalog merge boundary",
  "updated_at": "2026-09-11T04:11:06+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-catalog-merge-attestation"
}
---

PR #140 passed all 12 exact-head checks and merged the reviewed catalog tree, but protected-main
quality run 34557143666 correctly rejected merge `252f746e903555c2dc626fadfa1a75bb76913144`:
the GitHub author is `martin-beck <martin.beck2@gmx.de>` while its trailer names `Martin Beck`.
Do not rewrite or retroactively call that merge compliant. Publish only bounded, reproducible
attestation evidence and a corrective future merge recipe using the exact GitHub author identity.


- 2026-09-11T03:31:21+00:00: AR-1045 is done at protected-main merge 1a19b692 with all postmerge
  workflows green; PR #140 historical attestation is dependency-ready.

- 2026-09-11T03:31:24+00:00: Claimed by codex-ar1051-measurement-catalog-attestation-20260911.

- 2026-09-11T03:31:34+00:00: Recorded command exit 0; command argv SHA-256
  0bb4def436152f367f4fa7116ee3cfb548e90e591a39a802a958d67aba426670.

- 2026-09-11T03:32:34+00:00: Recorded command exit 0; command argv SHA-256
  8b5f438fc7d30b21bfe653d3cabac1c3f2b60f41b4e1cd9a77a5dd3c627fa5be.

- 2026-09-11T03:32:48+00:00: Recorded command exit 0; command argv SHA-256
  619402b9a12255f06dd13d71aa157db6b35edcf8450890f0654051caa48d89e2.

- 2026-09-11T03:33:08+00:00: Recorded command exit 0; command argv SHA-256
  e0c1e229dc528046d86d06050a9c8c83e7d60a602856ec4b9a82aea94e8143e6.

- 2026-09-11T03:33:30+00:00: Recorded command exit 0; command argv SHA-256
  92ba3ab0e9a0496eaf7e904bee5271a8e1c8b39713e33fae1599c4476baf7ba4.

- 2026-09-11T03:33:47+00:00: Recorded command exit 0; command argv SHA-256
  155bc0ddccdc50c63c37d4881a236e8ea6d50500648713d1f29c0f05c10b0b19.

- 2026-09-11T03:34:06+00:00: Recorded command exit 0; command argv SHA-256
  7e3698fdd6ac736994ca22686d230bf7a2f2f283823aeb141927a450198396b2.

- 2026-09-11T03:34:22+00:00: Recorded command exit 0; command argv SHA-256
  998c1d6fe71ea61a69635e65fc74903fe84b2da41a68237d5d4e3ecf03207efd.

- 2026-09-11T03:34:39+00:00: Recorded command exit 0; command argv SHA-256
  0531edea64e8ac055163b07d900c3a12bd3dfb3af7198f169022db01eca46851.

- 2026-09-11T03:35:46+00:00: Recorded command exit 0; command argv SHA-256
  796b3c4ae27b72210a97401d23a4a7a894040a65c36084fbd9e4348a1a452391.

- 2026-09-11T03:37:48+00:00: Recorded command exit 0; command argv SHA-256
  89d0f8a91cb08f2a85edc2ebaf64768a3da86ae6a106a7eeea3ec8e6d6123424.

- 2026-09-11T03:38:14+00:00: Recorded command exit 0; command argv SHA-256
  d69c325b88e94ea458d955f7222afec7194c35ccb5ef2a67fe7cde7e903003e6.

- 2026-09-11T03:38:28+00:00: Recorded command exit 127; command argv SHA-256
  0177c7f298b9557d14d47a62050dcb3281c530d0065de703b3d407ece7b3773e.

- 2026-09-11T03:39:05+00:00: Classified focused gate exit 127: governed shell PATH did not contain
  cargo, so no Rust test executed. Rerun uses the fully qualified Rust tool; four-file
  attestation/docs/test-only scope remains intact.

- 2026-09-11T03:39:13+00:00: Recorded command exit 127; command argv SHA-256
  d2ece22636714739d9278b85c67e625d30f3515e0730e82058cde155a25f48f4.

- 2026-09-11T03:39:40+00:00: Recorded command exit 1; command argv SHA-256
  d64a0f877dd75219210f14aaa1690c74e3086691c018e29ac3ba9c5135bfbfab.

- 2026-09-11T03:40:13+00:00: Recorded command exit 0; command argv SHA-256
  53ca2a6c8c04b1cad78627d2384b23d5e025f6e03b05e122ae0ae42f0e21d73d.

- 2026-09-11T03:40:41+00:00: Recorded command exit 0; command argv SHA-256
  ce7d53afc7439272dff8ff02789b7ec1e90bb86231e1f669eae531f79bff8d1d.

- 2026-09-11T03:41:04+00:00: Recorded command exit 0; command argv SHA-256
  8b4d637086eefd99a68aef35a53f1de3128eb0900b0b9a086d04547245a1be7d.

- 2026-09-11T03:42:51+00:00: Recorded command exit 0; command argv SHA-256
  c3b577d0126575e6247eb8121a0df139884400499902b910e7dd0b08e4f05c18.

- 2026-09-11T03:43:25+00:00: Recorded command exit 101; command argv SHA-256
  5ddbd902cd91fb73086370347410da33302796a87d09fdbd2fbd177a06925559.

- 2026-09-11T03:43:46+00:00: Recorded command exit 0; command argv SHA-256
  3e31afe946b07f3847f89009dc621cf1e5ddc9c5e8b00e5dcfd2f7b8a24acea4.

- 2026-09-11T03:46:03+00:00: Recorded command exit 0; command argv SHA-256
  cb64b347404a09f63fc4e386cdd4126ab6caeb279a984824572b042616b5957c.

- 2026-09-11T03:46:22+00:00: Recorded command exit 0; command argv SHA-256
  af0d87f42fcc7392f1044d92b24aa698bc45389b141a81905b077c98bdf85e68.

- 2026-09-11T03:46:36+00:00: Recorded command exit 0; command argv SHA-256
  3805ba161f3d717d363bec42baa80505e1fad45a957900c535d349c843771586.

- 2026-09-11T03:47:03+00:00: Implemented exact PR140 attestation fixture, closed-schema bounded
  historical catalog validator, corrective merge-message adversaries, and publication/quality
  documentation in exactly four files. Focused test passed 10/10 and Clippy passed. Full workspace
  fmt, Clippy, tests, rustdoc and release build passed; deny, audit, formal, contract, failure-path,
  signature, artifact, platform, actionlint, zizmor, gitleaks and coverage gates passed. Coverage
  line total was 97.84%. Classified non-code failures: two exit 127 invocations used absent cargo
  paths; one exit 1 was the expected fmt-check diff before formatting; formal fixture hit one
  transient ETXTBSY, then passed exact test 10/10 and full formal rerun; one exit 1 came from
  malformed audit-only awk quoting and the corrected exact-scope assertion passed.

- 2026-09-11T03:47:22+00:00: Recorded command exit 0; command argv SHA-256
  5b77f9aa909afd87a60713d4097618442e96583256599e42eb6da4a451454935.

- 2026-09-11T03:47:58+00:00: Recorded command exit 0; command argv SHA-256
  e1cf755495d5bf9c991f6810bed5ad39c2c884614bb10a7790465ed2b0c7c804.

- 2026-09-11T03:48:17+00:00: Frozen clean signed+DCO single-parent AR-1051 candidate
  7b3ef113d2b77c3982748f16c540d0e556252464, tree 2430f369bd110e4560b38ea1ca3ad8e7b003c348, parent
  1a19b692d724fd5ba1996470daccbfed06171a0a. Exact four-file scope: two attestation/docs additions
  and no production, protocol behavior, catalog schema, or TUI changes. Postcommit focused tests,
  Clippy, repository policy, contract consistency, gitleaks, signature and DCO passed; prior full
  gates and failure classifications are recorded. Candidate remains unpushed pending independent
  review.

- 2026-09-11T03:51:30+00:00: Recorded command exit 0; command argv SHA-256
  ace8fc3144f4c668df9caf91543dae2d271b40c1afeeb600f60dbff1e3c04b67.

- 2026-09-11T03:51:50+00:00: Recorded command exit 0; command argv SHA-256
  560a2e07a6236b2c0353ab695e558065245f8fbe931a6aa2a3d8831f815d9aa9.

- 2026-09-11T03:53:34+00:00: Recorded command exit 127; command argv SHA-256
  bfcbfd2b2a89bcc54f822615b0ebc955fe6a5ed6ddc1e20a9766a2a748d5ce5a.

- 2026-09-11T03:55:14+00:00: Recorded command exit 0; command argv SHA-256
  aa6d55b92e505e58bd4040b05b661267b4d948283e3b980fe055a71cfd2ef5f5.

- 2026-09-11T03:56:33+00:00: Recorded command exit 0; command argv SHA-256
  5533be3b7cd20dc7f13578b9bde4c16bbfb8960530a2a2e193ace309f8072651.

- 2026-09-11T03:56:50+00:00: Different-agent immutable review APPROVED exact head
  7b3ef113d2b77c3982748f16c540d0e556252464 and tree 2430f369bd110e4560b38ea1ca3ad8e7b003c348. Fresh
  origin/main remains exact parent 1a19b692d724fd5ba1996470daccbfed06171a0a, so no rebase or byte
  change is required.

- 2026-09-11T03:57:07+00:00: Recorded command exit 0; command argv SHA-256
  e04d92562e4ebfed5b913e962e815bb57d2fc07eb39ef414e1ea7359f4b39e6d.

- 2026-09-11T03:57:28+00:00: Recorded command exit 0; command argv SHA-256
  c873ac9d692ba9f110cd885681d4a2b9943b4ff9c93becadcf6c748f301f0327.

- 2026-09-11T03:57:47+00:00: Recorded command exit 0; command argv SHA-256
  0333933628487e1ff1f69ace3d9319f92157f908fe8aa12f590f9b02bacc45f8.

- 2026-09-11T04:00:07+00:00: Recorded command exit 8; command argv SHA-256
  3ca22a2c60d46a7cd591ac4953896102b373f1f19d3781b4a1feec07f09ad934.

- 2026-09-11T04:00:56+00:00: Recorded command exit 8; command argv SHA-256
  a0c810520463140329da6c744a5a9d0ae210e7819302fb3656867f0090e0120b.

- 2026-09-11T04:01:42+00:00: Recorded command exit 8; command argv SHA-256
  db9b09057e4b2e783acf73fb543eef8aa43f28b9135dca25817e5196f0071fa1.

- 2026-09-11T04:01:57+00:00: Recorded command exit 0; command argv SHA-256
  d895ec4b9252c8870fbd610656797b07b9fb0fa4c9186239f67cce55fb5e26c4.

- 2026-09-11T04:02:07+00:00: Recorded command exit 0; command argv SHA-256
  44fd9551a57f8fd1bee6c206a759aa4af631050d4510d08b1e6efa516620e893.

- 2026-09-11T04:02:15+00:00: Recorded command exit 0; command argv SHA-256
  5dee03dcff9dcbfe9ceb4fdffd0bbe4f9b3664b665d88c1ee17493ca153067fd.

- 2026-09-11T04:03:07+00:00: Recorded command exit 8; command argv SHA-256
  5d97b0a2d247617fba44927b2f2ecf821905142dacdfb11c94c25ecbd456efa8.

- 2026-09-11T04:04:05+00:00: Recorded command exit 0; command argv SHA-256
  a0011f75239d7d13c1b2b2339650c89a35e256c0031b50f5a2daa200d94a1606.

- 2026-09-11T04:04:32+00:00: Recorded command exit 0; command argv SHA-256
  a482b7ddd4a157c21f9c5cad6e03069c177d74f1b3825c96ab7c5681612e3f27.

- 2026-09-11T04:04:53+00:00: Recorded command exit 0; command argv SHA-256
  2fd985bcc0997cccdb602ef21a598d0412783e4c9eb4f2dffa55b3e1b8d5f53c.

- 2026-09-11T04:05:09+00:00: Recorded command exit 0; command argv SHA-256
  f41ba75a0b71a5edd1c19bb0c0d100fb71186f361b0029f86fc9f9a4c04681f7.

- 2026-09-11T04:06:14+00:00: Recorded command exit 0; command argv SHA-256
  ebe91f691f7f032b01ba5d517469a322aaf7189bf498d50167b595f1bf9fe8e1.

- 2026-09-11T04:07:11+00:00: Recorded command exit 0; command argv SHA-256
  ebe91f691f7f032b01ba5d517469a322aaf7189bf498d50167b595f1bf9fe8e1.

- 2026-09-11T04:08:20+00:00: Recorded command exit 0; command argv SHA-256
  cfe3def20a22a22d3b86805ea73baa57e99e9f4c0524f9a84e9e549ed24a4b4e.

- 2026-09-11T04:09:21+00:00: Recorded command exit 0; command argv SHA-256
  ebe91f691f7f032b01ba5d517469a322aaf7189bf498d50167b595f1bf9fe8e1.

- 2026-09-11T04:10:14+00:00: Recorded command exit 0; command argv SHA-256
  ebe91f691f7f032b01ba5d517469a322aaf7189bf498d50167b595f1bf9fe8e1.

- 2026-09-11T04:11:06+00:00: Recorded command exit 0; command argv SHA-256
  82a21a34e5407a8188b288fc185cd3e2f11b949e40c58b1a31fa58ca04736528.
