---
{
  "branch": "feature/tla-source-build-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T05:09:52+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0878",
  "next_action": "Run the proven source-build/repack recipe inside the pinned Temurin 17.0.20+8 amd64 image on an authorized Docker-capable runner, require the same normalized digest twice, then audit the 31 vendored JAR licenses/digests and encode the closed manifest/build/verifier paths. Do not use the host-only digest as qualified output.",
  "observed_branch": "feature/tla-source-build-provenance",
  "observed_dirty": 0,
  "observed_head": "af9fb7dcaabc162b13d6ee1e77d8915b6d82df20",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0878.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify immutable TLA+ tool provenance through an authoritative publication or deterministic source build.",
  "task_revision": 25,
  "title": "Qualify immutable TLA tool provenance",
  "updated_at": "2026-09-09T02:37:48+00:00",
  "worktree_key": "agent-systems-benchmark-tla-source-build-provenance"
}
---
## AR-0878

Resolve AR-0877's mutable and disappearing upstream release-asset blocker without accepting an
unsupported digest override. Qualify either a durable authoritative publication or a deterministic
source-build boundary whose output can safely seed AR-0877's verified online/offline cache.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T02:09:49+00:00: AR-0003, AR-0901, and AR-0902 are durably done. AR-0878 provenance-only
  paths are disjoint from active AR-0806 TUI history and AR-0872 workflow documentation, and AR-0877
  is released open with its four-path prototype preserved. Promote the dependency-free provenance
  repair to resolve the exact mutable-upstream blocker.

- 2026-09-09T02:09:52+00:00: Claimed by replay_20260906.

- 2026-09-09T02:10:21+00:00: Recorded command exit 0; command argv SHA-256
  87591628a4708da948baeca8de57baa3f6a9e497f59362495507839baa5db451.

- 2026-09-09T02:17:02+00:00: Recorded command exit 0; command argv SHA-256
  d08d8411b19e92c040e2cd567daf71d855e13bade075081b5dac56e26d89843a.

- 2026-09-09T02:17:23+00:00: Recorded command exit 0; command argv SHA-256
  4219e4c199150d62da6cf2c66417e42ee4b33de347f0ad2d3729feda716b4992.

- 2026-09-09T02:18:01+00:00: Recorded command exit 0; command argv SHA-256
  55472ab8ad1b582a14fea8d6a164d5db57451bedb3ef23690b5bd97ea4fd768b.

- 2026-09-09T02:18:55+00:00: Recorded command exit 0; command argv SHA-256
  a72c152b345720bf774b58f0a195c9dc83dab2bb1d2a78a8ed69f89822171fc6.

- 2026-09-09T02:20:14+00:00: Recorded command exit 0; command argv SHA-256
  150fe69cdca956b1b20a2ca8c9b9d6e31bea9755873725f9740129b4eaf6f46f.

- 2026-09-09T02:20:52+00:00: Recorded command exit 0; command argv SHA-256
  b79a493ea700e09d46a52b65f082263d1605fae38a3802b431bdc1932d2fcba3.

- 2026-09-09T02:21:29+00:00: Recorded command exit 1; command argv SHA-256
  f937ab5ad620fc6f0614050a586923f21e03553389c78cf7a66b5c303fb7c799.

- 2026-09-09T02:22:32+00:00: Recorded command exit 1; command argv SHA-256
  515806539c16c0ef6421d399b33ad7f0bc5336b0369903a9a111f6e7a9974266.

- 2026-09-09T02:24:03+00:00: Recorded command exit 0; command argv SHA-256
  96889fa9d117224643400da2786044efd66f83596de6e36ae517a105097e47d3.

- 2026-09-09T02:25:16+00:00: Recorded command exit 0; command argv SHA-256
  ba71dce786adebc752b7e3f3aceec7ecd0d2165c3c16ef0cddff88b3a67ae50a.

- 2026-09-09T02:26:07+00:00: Substantive AR-0878 source-build checkpoint; worktree remains clean at
  af9fb7d. The upstream v1.8.0 prerelease is still actively mutable: release 25926686 moved again to
  published_at 2026-09-09T01:53:46Z and asset 551753628 (4490679 bytes, digest a1fc0bfe), so
  immutable-publication branch remains rejected. Exact source archive for b123b226 is 82989507
  bytes/SHA-256 1f96ee7ef950e456794d13b7e4d8123c345a91528257a3a41b7cc1b506d1b58f. Apache Ant 1.10.15
  archive is 6925830 bytes/SHA-256 71334d7e.../published SHA-512 d78427af.... Source includes 31
  vendored JAR inputs. Pinned eclipse-temurin 17.0.20+8 amd64 manifest is sha256:c0d1549d.... Docker
  pull failed before any build with permission denied on /var/run/docker.sock, an
  environment/authorization boundary. A host-only Ubuntu OpenJDK 17.0.20+8 diagnostic built twice
  from independent source trees: raw JARs had equal 4471000-byte size but different hashes; every
  non-directory ZIP entry name and payload was byte-identical. Canonical sorted ZIP repack with
  fixed epoch/mode produced byte-identical 4455492-byte outputs, SHA-256
  0bd598f74102f5c16632fe7dfa2f36b3763479f4757b15fff24a77f6f7268d7e. This proves nondeterminism is
  packaging metadata on this host only, not yet the pinned-container or license-complete acceptance.

- 2026-09-09T02:28:03+00:00: Recorded command exit 0; command argv SHA-256
  2249014c054951d12fa6688e53009f03bed6545243f3ab5b9a7279e8a3d71dd5.

- 2026-09-09T02:28:35+00:00: Recorded command exit 0; command argv SHA-256
  78d53a7aeaa71f22e09d4de3ab6ce37c3c0582db575c286e1210c0db8111edc2.

- 2026-09-09T02:29:12+00:00: Recorded command exit 0; command argv SHA-256
  57b5948513e458d336eda6c0ccc2de5802532235802b60a70c126f3065e98223.

- 2026-09-09T02:29:33+00:00: Recorded command exit 0; command argv SHA-256
  f9c0abf54fcf084921c0f968c000e03b810f9b12f059f7ff554f4a3b1e791803.

- 2026-09-09T02:30:46+00:00: Recorded command exit 1; command argv SHA-256
  529051b2403fc94253b55fa6ba044ff9740e26687b6b302392d554b5b9435c14.

- 2026-09-09T02:32:24+00:00: Recorded command exit 1; command argv SHA-256
  9c33f3b68768d118564eb273c3ec4899a2cb09ba499abc52f271f53b73e2de20.

- 2026-09-09T02:35:59+00:00: Recorded command exit 0; command argv SHA-256
  bd18d9fbab29c5c5b1606d7805df6dcd5a6d1961aea3bf1110243780ccd3be70.

- 2026-09-09T02:36:53+00:00: Recorded command exit 1; command argv SHA-256
  d4ffdadb97617cb3609a61176c46a10e2b46ea320d77ca0fe2ca9d10a240852c.

- 2026-09-09T02:37:48+00:00: Recorded command exit 1; command argv SHA-256
  b1c4baa42c8388a49a5bcab01b0f35f6a32dcabcaed35ec0d4bab5dff5a787c4.
