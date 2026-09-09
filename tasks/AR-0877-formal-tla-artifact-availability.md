---
{
  "branch": "fix/formal-tla-artifact-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T16:25:26+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0877",
  "next_action": "Keep the four-path prototype unchanged. Obtain an authoritative immutable TLA+ 1.8.0 artifact or authorization for a reproducible source-build boundary; then refresh metadata once, finish deterministic faults, and run TLC/Alloy. Do not chase replaceable pre-release assets.",
  "observed_branch": "fix/formal-tla-artifact-availability",
  "observed_dirty": 8,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0877.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the formal workflow's unavailable TLA+ artifact pin without weakening provenance or offline verification.",
  "task_revision": 45,
  "title": "Repair formal TLA artifact availability",
  "updated_at": "2026-09-09T13:44:01+00:00",
  "worktree_key": "agent-systems-benchmark-formal-tla-artifact-availability"
}
---
## AR-0877

Replace the TLA+ release-asset URL that returns HTTP 404 with an authoritative, durable,
content-verified acquisition and offline-cache boundary. Preserve all positive and deliberate
mutation formal checks.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T01:01:21+00:00: Dependencies AR-0003, AR-0901, and AR-0902 are done; owned formal
  acquisition paths are disjoint from active AR-0806 TUI, AR-0855 state vendor, and AR-0876
  provider-launch scopes. Promote for the blocking TLA+ artifact availability repair.

- 2026-09-09T01:01:25+00:00: Claimed by replay_20260906.

- 2026-09-09T01:01:44+00:00: Recorded command exit 0; command argv SHA-256
  dd885d3beb1c7712be2c40fc7a268651d94964934cea87ee439edf2d698d0f77.

- 2026-09-09T01:02:47+00:00: Claimed clean isolated worktree
  /srv/data/projects/agent-systems-benchmark-formal-tla-artifact-availability at exact product main
  dca243ab7b8cbb0b2b49a568dec99c517e0719c2 after reading required docs and full plan. Initial audit
  found existing signed commit 7add29f already changed four owned paths to GitHub API asset
  551007111, SHA-256 4c7bb1f6..., and 4487756 bytes, but the current shell fetch still follows
  redirects generically and lacks the plan's metadata/approved-final-host, create-new atomic
  concurrency, hardlink/owner-mode, bounded retry, and comprehensive offline/cache fault boundary.
  Preserve this partial repin as provenance and implement the remaining fail-closed acquisition
  contract without changing authoritative TLA/Alloy models.

- 2026-09-09T01:15:21+00:00: Recorded command exit 0; command argv SHA-256
  70f1fead417b3551ce217b80588f20f9dbde4f1dcadb78008ccc4be6ff343440.

- 2026-09-09T01:16:06+00:00: Recorded command exit 0; command argv SHA-256
  5e5ecd106803e960373de65301f4e5653ca8202f0b4a5150d59a5b3ccdeeeded.

- 2026-09-09T01:18:10+00:00: Recorded command exit 0; command argv SHA-256
  ba8ee64e9597bd068dffbae0ae9f9eee17f60682a6c59868f2dcae8a4b48f195.

- 2026-09-09T01:19:30+00:00: Recorded command exit 1; command argv SHA-256
  32b5fe4cf3e4b6847c396e7fc5fd5e904e79d55d6de51d689484ea716904e270.

- 2026-09-09T01:20:05+00:00: Recorded command exit 2; command argv SHA-256
  5f2552aa6dd90afe912fa78e648362c3ca4d79143c30fa8a390c6f20faa59895.

- 2026-09-09T01:21:40+00:00: Recorded command exit 127; command argv SHA-256
  4b17e7752a0c32c0141c6e60bcda040b8eb37f78ac08d824c892eabbe339a747.

- 2026-09-09T01:22:11+00:00: Recorded command exit 125; command argv SHA-256
  511e90a6efd8c1956407c06f49626a12dd557162cdd22cb36acda7c42a27bfb0.

- 2026-09-09T01:22:47+00:00: Recorded command exit 0; command argv SHA-256
  7fee32c1d48c1dd50db6f6ef51a231d7b74f22e25d6c4d7d55d05e96152780ea.

- 2026-09-09T01:23:15+00:00: Recorded command exit 0; command argv SHA-256
  58ce5aefe9171d539aa56c74501defa195cf02ff0703e7eb4486682dcb6a5efa.

- 2026-09-09T01:24:53+00:00: Recorded command exit 0; command argv SHA-256
  6db81dfd389a4e735655ca6c6769d7240798c9a7fe78bbdc832fcaa9fe2785d0.

- 2026-09-09T01:25:24+00:00: Recorded command exit 0; command argv SHA-256
  67a1ac3216b08a8447f308a1f703911a2d34cfca400ab44b12f349632349210f.

- 2026-09-09T01:26:09+00:00: Substantive acquisition implementation checkpoint on exact base
  dca243ab with four owned dirty paths: formal/run_temporal_models.sh, formal/toolchains.toml,
  formal/tests/toolchain_pins.rs, formal/README.md. Live authoritative release evidence changed
  after the earlier partial repin: tag v1.8.0 still resolves to source b123b226, but current release
  25926686 publishes tla2tools.jar asset 551679598 created 2026-09-09T00:59:49Z, 44892330?
  Superseded typo: exact size is 4489230 bytes and SHA-256
  13885c0971b5faf31c89b89b90784c2bf3e2939632aa1ab10499504627e47209. Implementation binds
  release/tag/asset metadata, exact source ref, stable browser route, approved HTTPS final host set,
  bounded retries/bytes/time, exclusive cache lock, create-new partials, atomic no-clobber
  promotion, owner/mode/single-link checks, strict offline reuse, and cleanup. Real online acquire
  and offline zero-network cache reuse pass; cache mode 400/link count 1/digest exact. Offline
  missing, corrupt, symlink, and hardlink cases fail before a curl sentinel. bash -n, diff-check,
  and formal toolchain-pin test pass. One earlier wrapper exit was operator-only PATH loss and
  corrected with pinned cargo; no product failure. ShellCheck is unavailable locally and remains a
  required hosted/final gate.

- 2026-09-09T01:49:17+00:00: Recorded command exit 2; command argv SHA-256
  aa40dbb37fa84371f5b5b2b8fef237998d4b73113063ecdcd7bd4e49080835f6.

- 2026-09-09T01:50:30+00:00: Recorded command exit 0; command argv SHA-256
  a14346543cf4e68d0c93d7e0e9f2c45417c4ddc196c53fae34ae1ac567675bdb.

- 2026-09-09T01:51:08+00:00: Recorded command exit 0; command argv SHA-256
  1048003a12beab80a5c070bfa62dc6bbf9cc0c57bcd6b3b4969de2d26c52513e.

- 2026-09-09T01:51:49+00:00: Exact upstream blocker discovered during full acquisition verification.
  GitHub release 25926686 is a mutable v1.8.0 pre-release rebuilt from the same b123b226 tag: asset
  551007111 is now HTTP 404; asset 551679598 observed at 00:59:49Z with 4489230 bytes/digest
  13885c09 was deleted during this AR and is now HTTP 404; replacement 551717837 created 01:24:53Z
  has 4489229 bytes/digest f3a6ba40 and is HTTP 200. Published_at also changed from 01:01:29Z to
  01:26:05Z. The pre-body redirect hardening and owner/single-link/offline cache prototype remains
  dirty, bash syntax/diff-check and focused pin test pass, but its exact metadata intentionally
  rejects the replacement and full TLC cannot run. Re-pinning each transient rebuild would violate
  AR-0877 durable-asset acceptance; no signed candidate was created.

- 2026-09-09T02:08:16+00:00: Released without discarding the four-path dirty prototype. Exact
  blocker remains: upstream TLA+ v1.8.0 prerelease asset IDs 551007111 and 551679598 were deleted,
  replacement 551717837 changed bytes/digest/publication time, so AR-0877 cannot select a durable
  artifact. Continue only after AR-0878 qualifies an immutable publication or deterministic
  source-build contract.

- 2026-09-09T03:45:56+00:00: Claimed by codex-longrun-tla-20260909.

- 2026-09-09T03:45:59+00:00: Heartbeat by codex-longrun-tla-20260909.

- 2026-09-09T03:46:22+00:00: Reconciled existing prototype: authoritative v1.8.0 prerelease asset
  was deleted/rebuilt with changed bytes; no durable artifact exists. Preserve dirty four-path
  prototype and wait for AR-0878 immutable publication or approved source-build boundary.

- 2026-09-09T06:09:00+00:00: Coordinator metadata maintenance shortened only the stale
  front-matter projection to satisfy the existing schema. Prior value preserved verbatim:
  `Hold the four-path acquisition prototype unchanged and obtain an authoritative immutable TLA+ 1.8.0 artifact publication (or coordinator authorization for a separately specified reproducible source-build boundary); then refresh exact metadata once, finish deterministic faults, and run TLC/Alloy. Do not chase the continuously replaced v1.8.0 pre-release asset.`

- 2026-09-09T13:25:24+00:00: AR-0878 is durably done and supplies the independently qualified
  deterministic source-build manifest and output digest; resume AR-0877 to integrate that immutable
  artifact boundary instead of repinning the mutable v1.8.0 prerelease asset.

- 2026-09-09T13:25:26+00:00: Claimed by quality_20260906.

- 2026-09-09T13:26:19+00:00: Recorded command exit 0; command argv SHA-256
  c78581320d3e12633fef33a74574afb816fe7ba23d209b6b6b0e0143e9ecb31a.

- 2026-09-09T13:26:37+00:00: Recorded command exit 0; command argv SHA-256
  6013953a513ecfd22921b2c034badd44c2c2f70cdda6189ff3d5811efba751c4.

- 2026-09-09T13:35:20+00:00: Recorded command exit 0; command argv SHA-256
  cafd01ec6c28e186f06b27562a07d847df1892ef19eb2056eb33e646e7b6baca.

- 2026-09-09T13:35:39+00:00: Recorded command exit 101; command argv SHA-256
  ea1da65c43465b78823f9b39067dfee3e72ea05fe75e2ff086c9b16946893b92.

- 2026-09-09T13:36:24+00:00: Recorded command exit 101; command argv SHA-256
  133ea1df118454ba013b64456e63149ab94db6abba97e4f7f9204f68d8d74f37.

- 2026-09-09T13:36:58+00:00: Recorded command exit 101; command argv SHA-256
  ea1da65c43465b78823f9b39067dfee3e72ea05fe75e2ff086c9b16946893b92.

- 2026-09-09T13:37:39+00:00: Recorded command exit 0; command argv SHA-256
  1369d5c809bd46b3578e5d66ef11b3341668df701fe2d64b03bf667ba35b66dd.

- 2026-09-09T13:39:47+00:00: Recorded command exit 0; command argv SHA-256
  af697b674346d72fd2d1062eb60e19c8a3da7e839ae2e6a18631dfc6a50270fe.

- 2026-09-09T13:40:21+00:00: Recorded command exit 0; command argv SHA-256
  2b46248d1133fe995051da3408e766a1c0f4c87b210b9c462153c0e835be24cf.

- 2026-09-09T13:40:50+00:00: Recorded command exit 0; command argv SHA-256
  90c97aca0c958127f4373918c6d5fc85fa0ba79ef91e25acc28e233d8550508b.

- 2026-09-09T13:44:01+00:00: Recorded command exit 0; command argv SHA-256
  5eeb5b21ac80d3ad10cdaa66e608eb739c1f6d90cb233de423c4c2bca27556f9.
