---
{
  "branch": "feature/ar-1757-human-first-cli-output",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T15:29:25+00:00",
  "depends_on": [
    "AR-1338",
    "AR-1555"
  ],
  "id": "AR-1757",
  "next_action": "Inventory every public ASB command outcome at exact current main, define the command-aware human presentation contract, and replace the generic JSON key/value renderer without changing explicit --json schemas.",
  "observed_branch": "feature/ar-1757-human-first-cli-output",
  "observed_dirty": 7,
  "observed_head": "b3cb9b256cccc15be682dbb1019a239b50edf6cd",
  "owner": "codex-asb-ar1757-human-output-20261009",
  "plan": "../plans/AR-1757-human-first-cli-output.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1757.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make default ASB CLI output concise, command-aware, self-explanatory, and actionable while preserving stable machine-readable output.",
  "task_revision": 91,
  "title": "Human-first ASB command output",
  "updated_at": "2026-10-09T13:40:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1757-human-first-cli-output"
}
---

ASB currently calls its default output human-readable, but the shared renderer
mostly walks the structured JSON response and prints every field as `key: value`.
That exposes implementation vocabulary such as schema versions, classifications,
booleans, transport state, development flags, digests, and network state even
when those fields do not help a person complete the command. Failures can name a
code without plainly explaining what failed, what remains unchanged, or the one
safe command the user should run next.

Replace this generic projection with a human-first presentation layer for every
public `asb` command family. Default output must say, in clear sentences:

1. what the requested command did;
2. whether it succeeded, partially completed, or failed;
3. the small set of result facts relevant to that command; and
4. the next useful step and exact safe command, when another step is required.

Successful terminal commands must not invent a next step. Failures must lead
with the user-facing cause rather than a status code, preserve the nonzero exit
status, distinguish user correction from host limitation and product failure,
and state whether files/configuration/runs were created or left unchanged when
that matters. Suggested commands must be valid, copyable, context-appropriate,
shell-safe, and must never contain credentials or secret values.

The default view must suppress irrelevant internal metadata. Stable identifiers,
digests, paths, counts, warnings, and technical classifications are shown only
when a person needs them to find an artifact, understand risk, choose an option,
or recover. An opt-in verbose/details view may expose bounded diagnostic context.
Explicit `--json` and the supported JSON compatibility spelling remain the
authoritative complete machine interface and must retain their schemas and field
semantics.

Scope is the ASB CLI presentation and its tests/documentation in
`martin-beck/agent-systems-benchmark`. Do not move business logic into rendering,
change exit-code meanings, weaken typed errors, duplicate provider/catalog
authority, alter asb-tui's actual application UI, or treat development
authentication/signing warnings as blockers.

- 2026-10-09T12:53:02+00:00: Dependencies AR-1338 and AR-1555 are done; exact current-main generic
  JSON projection defect and owned CLI presentation paths were reviewed. Human-output repair is
  ready to claim.

- 2026-10-09T12:56:56+00:00: Claimed by codex-asb-ar1757-human-output-20261009.

- 2026-10-09T12:58:15+00:00: Heartbeat by codex-asb-ar1757-human-output-20261009.

- 2026-10-09T12:58:36+00:00: Recorded command exit 0; command argv SHA-256
  61ff72e4713e9b84080b3dcee0735c8f6253425b7c636cc511028094c6a9d421.

- 2026-10-09T13:00:24+00:00: Recorded command exit 128; command argv SHA-256
  da0ddf71bd6e7f5b02bf52a6164055f1dec49c7e2e5a9974be033ef8c0ee3560.

- 2026-10-09T13:00:48+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-09T13:01:07+00:00: Recorded command exit 0; command argv SHA-256
  b800083cc962c5a0fcece76b23ad5d13fe20c0a98ece59aaee6c9c2cc9c572bb.

- 2026-10-09T13:03:48+00:00: Recorded command exit 0; command argv SHA-256
  930410fddf044e00080633c6531e6825c055f152b850edbc5094c59420bba263.

- 2026-10-09T13:04:09+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T13:04:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:05:25+00:00: Recorded command exit 101; command argv SHA-256
  cf5ec1200877768a6cf31e69f1c1aac5778c789a47058834ee16ec173cfed6eb.

- 2026-10-09T13:06:10+00:00: Recorded command exit 0; command argv SHA-256
  e4c7d60df5300a25e00f9e570a2db5d97a407927ade7c5d51a52362bc673aac4.

- 2026-10-09T13:08:19+00:00: Recorded command exit 0; command argv SHA-256
  5b1c8678134b0676b937c14cc78c24a000b74e8ec17e999e3395c417371cdbb8.

- 2026-10-09T13:09:21+00:00: Recorded command exit 0; command argv SHA-256
  b3863b25a92f2bebf3d550b9ac1555f2c63a86614f2a92e7c86e5eb5292c96aa.

- 2026-10-09T13:10:11+00:00: Recorded command exit 0; command argv SHA-256
  27346b68a39736ddf484a29e657c4e7c8c348dcf784c048d25cf35372016d104.

- 2026-10-09T13:11:08+00:00: Recorded command exit 0; command argv SHA-256
  55d0092cc24ae098802055f24fb0be9987dc7446e54729f39ff3bab1efab6f72.

- 2026-10-09T13:11:42+00:00: Recorded command exit 0; command argv SHA-256
  62d10a96af1db2b4b98c086757f42967bde21829c795b206feb185763a5495fc.

- 2026-10-09T13:12:09+00:00: Recorded command exit 101; command argv SHA-256
  cf5ec1200877768a6cf31e69f1c1aac5778c789a47058834ee16ec173cfed6eb.

- 2026-10-09T13:13:22+00:00: Recorded command exit 1; command argv SHA-256
  579c2de4db7a6f4e444903517340d40a6052513f5133d801d2c5f78fcab62caf.

- 2026-10-09T13:13:41+00:00: Recorded command exit 1; command argv SHA-256
  3bf1134d8cda722a5669a39daa49386dc338290b7e26eb67ab3b07c19044618e.

- 2026-10-09T13:14:01+00:00: Recorded command exit 0; command argv SHA-256
  fb901d21311455dab18169deb9a8a9ee2d7e9212af1d20284b9ff174e99950f3.

- 2026-10-09T13:14:45+00:00: Recorded command exit 1; command argv SHA-256
  3cfc5611d47dff41ca698aed78111af2d167e0358832e7e08b424eff83d4b70c.

- 2026-10-09T13:16:04+00:00: Recorded command exit 0; command argv SHA-256
  bc5d9cf2862a723d9204316ecf0f820b8c86608624b70a47400d72300d348893.

- 2026-10-09T13:16:27+00:00: Recorded command exit 0; command argv SHA-256
  d792c9e818d247f1c2a168fafe96f1da457907b7eb91572278acbdb68c5ab6ba.

- 2026-10-09T13:16:48+00:00: Recorded command exit 0; command argv SHA-256
  8b8a8bd01ea79e6bef0e7e62e234de518801dae842354a5834728e0584eb6a98.

- 2026-10-09T13:18:06+00:00: Recorded command exit 1; command argv SHA-256
  56dddcd56f8ec4e475d520c973118c18a66cf323b7a611c6ffa306de1e5cf731.

- 2026-10-09T13:18:42+00:00: Recorded command exit 0; command argv SHA-256
  3bb9d9572df0ab5851d9b523411e7ff72498950b8581de3cc7f505d3a5d00891.

- 2026-10-09T13:18:49+00:00: Recorded command exit 1; command argv SHA-256
  7854e63063b570dd7bfab6ca73e04d07793673892e819ce82647117849a07fb9.

- 2026-10-09T13:19:05+00:00: Recorded command exit 0; command argv SHA-256
  391021aece35eea0eff6b36e8af454adbe182e8993ec5cb202b3e99e1dbfc0a0.

- 2026-10-09T13:19:22+00:00: Recorded command exit 0; command argv SHA-256
  c58c7503e46feb5bdf09933ad2b0a54a8a6d8c11dc34b8c9b7b6108cf93e3dc9.

- 2026-10-09T13:19:36+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:19:54+00:00: Recorded command exit 1; command argv SHA-256
  44bd7fce2b60e0a469101e9fb10e441468d247d3ce2fc3dfe6523465fc4cf201.

- 2026-10-09T13:20:10+00:00: Recorded command exit 0; command argv SHA-256
  5d70f309e2cee70fc7cd9210bc447bb8ffe53ffeb20f98eaa786c3a9379b5ed0.

- 2026-10-09T13:20:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:20:37+00:00: Recorded command exit 101; command argv SHA-256
  cf5ec1200877768a6cf31e69f1c1aac5778c789a47058834ee16ec173cfed6eb.

- 2026-10-09T13:21:04+00:00: Recorded command exit 0; command argv SHA-256
  bf795ed1388a88bce1d28ac0333e70130d522424b096d05eb10c5f3a93fd0c1a.

- 2026-10-09T13:21:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:21:25+00:00: Recorded command exit 101; command argv SHA-256
  cf5ec1200877768a6cf31e69f1c1aac5778c789a47058834ee16ec173cfed6eb.

- 2026-10-09T13:21:56+00:00: Recorded command exit 0; command argv SHA-256
  0120a345ca841435ede3d7ce28c8f49cf22e9be8ab056ab2db8818c99212403b.

- 2026-10-09T13:22:05+00:00: Recorded command exit 0; command argv SHA-256
  4ea782a161ca40d5dc121194f87d3139a1a1141a8f1222e84c50c70fdc3a61f5.

- 2026-10-09T13:22:16+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:22:34+00:00: Recorded command exit 0; command argv SHA-256
  cf5ec1200877768a6cf31e69f1c1aac5778c789a47058834ee16ec173cfed6eb.

- 2026-10-09T13:23:07+00:00: Recorded command exit 101; command argv SHA-256
  9e6b34e88869751a7ddf52f62e40ec661d4d1a112149bca1b9ad82b271641989.

- 2026-10-09T13:23:45+00:00: Recorded command exit 0; command argv SHA-256
  2c8d391f1d476bfd93a8c0826a903da07960860049bfbf9f181ba0d85efdf5f3.

- 2026-10-09T13:23:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:24:04+00:00: Recorded command exit 0; command argv SHA-256
  9e6b34e88869751a7ddf52f62e40ec661d4d1a112149bca1b9ad82b271641989.

- 2026-10-09T13:25:04+00:00: Recorded command exit 0; command argv SHA-256
  820732dde62befa7782495911bf221ab4cba613a81451d534ef24f9e463f3fa2.

- 2026-10-09T13:25:15+00:00: Recorded command exit 0; command argv SHA-256
  cf815f9f0b1fd35b7882df02366d7b92a672edc90a0ff6b3a4ca4b4ed7153cb5.

- 2026-10-09T13:25:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:25:37+00:00: Recorded command exit 1; command argv SHA-256
  e09bd1399a81f1780cc9231703191ac6f2a0b3318b701a0f4dee169ce5807a0b.

- 2026-10-09T13:25:55+00:00: Recorded command exit 101; command argv SHA-256
  2c8f96692329425e83dfa6c40a09c267af44e3fb12d6a5673fb42f6328f86b65.

- 2026-10-09T13:26:20+00:00: Recorded command exit 1; command argv SHA-256
  1c1d90a37bf8e1f0430dc9902933670606663f2063b0cd9daaa6cb2aa652f111.

- 2026-10-09T13:26:49+00:00: Recorded command exit 0; command argv SHA-256
  b16aa48e4bcf651aa8d1ef309d6b0d413ec7001700afe24e4e7e238543461c99.

- 2026-10-09T13:26:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:27:11+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-09T13:27:59+00:00: Recorded command exit 0; command argv SHA-256
  26b350deaff2b166c75f23493da951aa71c3f25a6e3108738dc696d2c6cf4a09.

- 2026-10-09T13:29:25+00:00: Heartbeat by codex-asb-ar1757-human-output-20261009.

- 2026-10-09T13:30:10+00:00: Recorded command exit 2; command argv SHA-256
  b2d289d06f0543f78d99b29dab5b2465600dd21a137a61dc44d5777a12b66c3c.

- 2026-10-09T13:30:23+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-09T13:31:05+00:00: Recorded command exit 0; command argv SHA-256
  546dc3160c6e3287ea80486f86ec2ce2e7e03484ee967ef59aea04d4327ac2e4.

- 2026-10-09T13:31:55+00:00: Recorded command exit 0; command argv SHA-256
  1ed809699e02c7dc87763d2b34ddb2192f0f99303d73276be7e3b0136364c1cd.

- 2026-10-09T13:32:15+00:00: Recorded command exit 101; command argv SHA-256
  d2161f2d87cf6fa3a2edfc2a0cdca1677b0d9847f493507633d64ddb7c6ea7a7.

- 2026-10-09T13:32:34+00:00: Recorded command exit 1; command argv SHA-256
  9bc7f4ddb997c9da748ac77d37570fcb6c537b591330bd7367904fe929ad93e1.

- 2026-10-09T13:32:49+00:00: Recorded command exit 0; command argv SHA-256
  c0cc7347235655499ef881d3dd2463da135361e4631bc5ab5079718e1f187eae.

- 2026-10-09T13:33:05+00:00: Recorded command exit 0; command argv SHA-256
  55f3e362430917e35b8271b70e62f0a4ed012c174f6c5f33187428193103ee13.

- 2026-10-09T13:33:25+00:00: Recorded command exit 101; command argv SHA-256
  d2161f2d87cf6fa3a2edfc2a0cdca1677b0d9847f493507633d64ddb7c6ea7a7.

- 2026-10-09T13:33:43+00:00: Recorded command exit 0; command argv SHA-256
  af6a3ec3f5dba93a3e730d2a70f53542800b4351fbceb4cd0cb6a850b7451ef2.

- 2026-10-09T13:33:57+00:00: Recorded command exit 1; command argv SHA-256
  b84342c47b812bc9883385d78572469dcd2415e51d0e425e6f268c1e853f4082.

- 2026-10-09T13:34:11+00:00: Recorded command exit 0; command argv SHA-256
  d2161f2d87cf6fa3a2edfc2a0cdca1677b0d9847f493507633d64ddb7c6ea7a7.

- 2026-10-09T13:34:37+00:00: Recorded command exit 0; command argv SHA-256
  53ee521d5fbaab344e8125b364cc4869fc613bf0fd7fe8179a68e0a102abf4b7.

- 2026-10-09T13:34:48+00:00: Recorded command exit 0; command argv SHA-256
  0490d097667d783acde5f948d70b8bbfe9c4e554d849a1f6eff38ec32d5fb5b1.

- 2026-10-09T13:35:35+00:00: Recorded command exit 1; command argv SHA-256
  bb4dd129238bea807db754ee758ebb60a8c4a4e88896c58a8c9f6b67a43056c3.

- 2026-10-09T13:35:57+00:00: Recorded command exit 0; command argv SHA-256
  c63fb0ef78ad57b1b9c60cc1b5c0088c2d6749e426ba99a05fa6479389eb96e1.

- 2026-10-09T13:36:52+00:00: Recorded command exit 0; command argv SHA-256
  f047bff30f01b4d93e7dab77a1354bd7b06ff6d1a5515019b939ac55834db30a.

- 2026-10-09T13:37:06+00:00: Recorded command exit 0; command argv SHA-256
  7c9cb2c441c638dc9aece9e324f1900364ad3ca6216aee3d2244325d9367c593.

- 2026-10-09T13:37:40+00:00: Recorded command exit 0; command argv SHA-256
  950f006cba6cd7201c7916204ecc0b8db0a631142172dfeb901bae4a27da1258.

- 2026-10-09T13:37:52+00:00: Recorded command exit 101; command argv SHA-256
  e0a9f630b9b405cd29a33ce19a51b90a82037a60e591a46f5f7987bb327b634a.

- 2026-10-09T13:38:13+00:00: Recorded command exit 0; command argv SHA-256
  63a962060092eb94962e41cc034f81637dc813af2b0966e18510fc6d941f5b9f.

- 2026-10-09T13:38:25+00:00: Recorded command exit 101; command argv SHA-256
  e0a9f630b9b405cd29a33ce19a51b90a82037a60e591a46f5f7987bb327b634a.

- 2026-10-09T13:38:43+00:00: Recorded command exit 0; command argv SHA-256
  ec1e259d9dd7abc6b8089449a04bc8820bb6b1efa3830590a8341d072a8183e2.

- 2026-10-09T13:38:56+00:00: Recorded command exit 101; command argv SHA-256
  e14e2d0f33a75f36ea900fb35321e92ebdb6d28020b714591f5b5bc384b11d2e.

- 2026-10-09T13:39:13+00:00: Recorded command exit 0; command argv SHA-256
  0bccd38d4aeafd17c45fdc7762c712257b7ae282c545c44ffd22410bfe00ab51.

- 2026-10-09T13:39:27+00:00: Recorded command exit 0; command argv SHA-256
  cccc24308f4ca5a67f4755c94253943888aef9752ebe1b9d7c7570d7d0670f4e.

- 2026-10-09T13:39:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T13:39:51+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T13:40:20+00:00: Recorded command exit 0; command argv SHA-256
  fbd2c2f0780163a26c8f6e3adfd58f9af59bc92b02f544b5e8548b369a636016.
