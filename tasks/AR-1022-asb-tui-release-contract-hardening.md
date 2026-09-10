---
{
  "branch": "feature/asb-tui-release-contract-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:17:26+00:00",
  "depends_on": [
    "AR-1017",
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1021"
  ],
  "id": "AR-1022",
  "next_action": "Wait for AR-1030 PR 11 to merge, rebase signed+DCO AR-1022 PR 10 onto exact new asb-tui main, reconcile overlaps to source_only_unverified, rerun full gates and exact-head CI, then integrate by protected admin merge only when all requirements are green.",
  "owner": "codex-ar1022-lifecycle-20260910",
  "plan": "../plans/AR-1022.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Turn the tested unverified asb-tui lifecycle boundary into a release-safe delegated contract.",
  "task_revision": 94,
  "title": "Harden the asb-tui release lifecycle contract",
  "updated_at": "2026-09-10T20:27:42+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-release-contract-hardening"
}
---
Repair the pre-release lifecycle boundary without weakening its existing signature, bundle,
transaction, recovery or isolation guarantees. Production requests must not choose their own trust
root or verification time, and a verified public release must not remain labelled as an unverified
extension. Preserve deterministic injection seams only inside tests.

Acceptance requires closed generated schemas, backward/rejection behavior documented explicitly,
embedded signer identity, system-clock verification, honest verified-channel state, hostile request
and filesystem tests, complete local gates, independent review, exact-head CI and post-merge checks.

- 2026-09-10T19:13:59+00:00: Claimed by codex-ar1022-lifecycle-20260910.

- 2026-09-10T19:14:17+00:00: Recorded command exit 0; command argv SHA-256
  8944772fadc13e086aeb779120b568f0f9c23190d34e1aa24ce37ea79900fd7f.

- 2026-09-10T19:24:52+00:00: Baseline wrapper call from the standalone asb-tui worktree was rejected
  by the project binding before cargo ran; subsequent wrapped commands originate in the bound state
  checkout and use explicit asb-tui paths.

- 2026-09-10T19:25:46+00:00: Recorded command exit 101; command argv SHA-256
  2046939d4755a9d214168dbeabd77c7b63f39f4d6101cd267eaf16b3f4abb651.

- 2026-09-10T19:26:09+00:00: Recorded command exit 0; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:29:51+00:00: Recorded command exit 0; command argv SHA-256
  f8b3ce4feca9ace76a7b4534afdb5be1641487571f856a9b93e314c2ff927e83.

- 2026-09-10T19:30:05+00:00: Recorded command exit 0; command argv SHA-256
  9433db6b7bf38cc09dd37ed43e53985ab8fa2a08279972a69d672ae9265d4d55.

- 2026-09-10T19:32:28+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:33:08+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:33:57+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:34:06+00:00: Recorded command exit 101; command argv SHA-256
  02966aaacd1d8c320ad8cbc910eaa8057f02af6621e5ef2540ab601665b224e2.

- 2026-09-10T19:34:36+00:00: Classified focused test exit 101: intended self-test response expanded
  from 9 to 14 closed identity fields; source-only binary correctly exited 3 with ready=false.
  Updated assertions now bind classification, target, empty unpromoted identities, ASB/protocol
  versions and exact field count; rerunning focused and full gates.

- 2026-09-10T19:34:53+00:00: Recorded command exit 101; command argv SHA-256
  7f9593ea33e58ce66d9e808b9aa937d337139e94cebbc422e94711fbbbc7f1fa.

- 2026-09-10T19:36:27+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:36:55+00:00: Recorded command exit 101; command argv SHA-256
  0a3cb09fcc4269379326bd7ad243e1c6d3093c1b7715eee7ab2ada5aa5a26020.

- 2026-09-10T19:37:29+00:00: Recorded command exit 0; command argv SHA-256
  7ee2bf737d03fcce86b526409ffea167f88e25e15048bda3db1eb72c70259649.

- 2026-09-10T19:38:15+00:00: Recorded command exit 0; command argv SHA-256
  ecfb73e71d4b8750c31c66df8486c07b2409ec5d41013849f23fa91ead9b4a41.

- 2026-09-10T19:38:52+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:40:11+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:40:33+00:00: Recorded command exit 0; command argv SHA-256
  0a3cb09fcc4269379326bd7ad243e1c6d3093c1b7715eee7ab2ada5aa5a26020.

- 2026-09-10T19:40:43+00:00: Recorded command exit 0; command argv SHA-256
  0727ab62751f97ac3f8005e4337de58183d93dade158ff996213ea3f424b966a.

- 2026-09-10T19:41:08+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T19:42:21+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:42:43+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:43:23+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:44:55+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:45:15+00:00: Recorded command exit 0; command argv SHA-256
  2534fa89248632489007e34c2ce7f46ad54115b65865b76576241a7304fe1f06.

- 2026-09-10T19:45:25+00:00: Recorded command exit 0; command argv SHA-256
  0727ab62751f97ac3f8005e4337de58183d93dade158ff996213ea3f424b966a.

- 2026-09-10T19:45:35+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T19:46:05+00:00: Recorded command exit 0; command argv SHA-256
  37f93b176210021a8307057c83c9872923de576b22bc81440102a34a8363ed32.

- 2026-09-10T19:46:17+00:00: Recorded command exit 0; command argv SHA-256
  ecfb73e71d4b8750c31c66df8486c07b2409ec5d41013849f23fa91ead9b4a41.

- 2026-09-10T19:46:54+00:00: Recorded command exit 0; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:47:12+00:00: Recorded command exit 0; command argv SHA-256
  815bf65933f4ae1093744ab391250cd061be002c1fa69e3f531aa933e0acb288.

- 2026-09-10T19:47:40+00:00: Recorded command exit 0; command argv SHA-256
  73e13667c404bfe43c7eaa4e1e08fa28b753a78b0b89f969222fc4599998ad6d.

- 2026-09-10T19:47:59+00:00: Recorded command exit 0; command argv SHA-256
  0727ab62751f97ac3f8005e4337de58183d93dade158ff996213ea3f424b966a.

- 2026-09-10T19:49:25+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T19:49:40+00:00: Recorded command exit 0; command argv SHA-256
  37f93b176210021a8307057c83c9872923de576b22bc81440102a34a8363ed32.

- 2026-09-10T19:49:56+00:00: Recorded command exit 0; command argv SHA-256
  75283bd49570efb5daa8c79a6935c9f6178bfeac6154ec1d3d756a57880de21b.

- 2026-09-10T19:50:14+00:00: Recorded command exit 2; command argv SHA-256
  53cbf5beec003e336c791ca430a445389e9b519eb0c526f81645b79552bdbb87.

- 2026-09-10T19:51:00+00:00: Recorded command exit 0; command argv SHA-256
  ede6fd131c695ec317e69b625c4c777f03c345bdd3413d1d2c6ddd9f8cba2e6c.

- 2026-09-10T19:51:22+00:00: Recorded command exit 0; command argv SHA-256
  9b9aa60ff2dd4910312e53b264d502f0b69298f015cdbcd04d3b12102e9377c0.

- 2026-09-10T19:51:42+00:00: Recorded command exit 0; command argv SHA-256
  d8e861e3d92ca5c11b7d769fbc6458d7162a720b4e90ed8dd629abfb19b3ee86.

- 2026-09-10T19:52:11+00:00: Recorded command exit 0; command argv SHA-256
  a1692af7dbc027a3d3f8348c7232b05f08aba1a8231a0286d2daba9f6f974fbe.

- 2026-09-10T19:52:30+00:00: Recorded command exit 0; command argv SHA-256
  709b85180ab603d75e05bdd36f86dcf09a9de14d4caa0bb11e8c916424e91f54.

- 2026-09-10T19:53:20+00:00: Recorded command exit 1; command argv SHA-256
  010dedce34cd99cf7017eecc15e0ec4217e3b10839d3c9a81a07aa8a156185d5.

- 2026-09-10T19:53:46+00:00: Recorded command exit 0; command argv SHA-256
  e4249030b9b5d42c742d4de4800153582a85c8385818f0dc62aa7c5c52191463.

- 2026-09-10T19:55:25+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:55:50+00:00: Recorded command exit 0; command argv SHA-256
  f6900bf196c8996d3291ada14cda996fd07f0e98fe9f8e296fa729b5ab135214.

- 2026-09-10T19:56:01+00:00: Recorded command exit 0; command argv SHA-256
  ecfb73e71d4b8750c31c66df8486c07b2409ec5d41013849f23fa91ead9b4a41.

- 2026-09-10T19:56:21+00:00: Recorded command exit 0; command argv SHA-256
  f1fd40827dc9f4dae73af4aa47dd2e4733a14ddaf0c3f3b55131ca43d5000bce.

- 2026-09-10T19:56:41+00:00: Recorded command exit 0; command argv SHA-256
  927ee57ce58cdf6a04384df16e9a464955803198f340c53ec2e0c3ae28f48e55.

- 2026-09-10T19:57:14+00:00: Recorded command exit 0; command argv SHA-256
  010dedce34cd99cf7017eecc15e0ec4217e3b10839d3c9a81a07aa8a156185d5.

- 2026-09-10T19:57:31+00:00: Recorded command exit 0; command argv SHA-256
  d774991a84bf46cd7ef0540a799019f8cf6cf2c4a1ad34f1104d7bb650317242.

- 2026-09-10T19:57:52+00:00: Recorded command exit 0; command argv SHA-256
  2b1dd69ab62f2fd9ad80e4c9be8a8ed177258e42fbf4803100e97952b2fde2f9.

- 2026-09-10T19:58:06+00:00: Recorded command exit 0; command argv SHA-256
  d6d5d7208d29f663028b5ea6e011ed1379bec3947d7e8e76ecf8fbdbfaf40252.

- 2026-09-10T19:58:26+00:00: Recorded command exit 0; command argv SHA-256
  ed5a4abd587e418ae1457a294a868c2c5cfb59e0242d17adffca9c7c29852d72.

- 2026-09-10T19:59:00+00:00: Recorded command exit 0; command argv SHA-256
  9b9aa60ff2dd4910312e53b264d502f0b69298f015cdbcd04d3b12102e9377c0.

- 2026-09-10T19:59:23+00:00: Recorded command exit 0; command argv SHA-256
  aec7cbf6bc9811a933e23b551213cdc75d8e87331dccf5a8a3731ec8806a754b.

- 2026-09-10T20:00:21+00:00: Recorded command exit 0; command argv SHA-256
  1d55ab3c228d41970f8bee31a8dc1cee0d77fed6536cff35e74a980b8ed0801f.

- 2026-09-10T20:00:54+00:00: Published signed+DCO commit f406af260db8da12356906aaf12d3d75b235e5c3 in
  asb-tui PR 10. Green local evidence: full locked tests, fmt, Clippy -D warnings, rustdoc, release
  build, schemas, release/publication validators, deny/audit, Gitleaks, shell/workflow analyzers,
  ASB-core isolation, and 90.71% line coverage against the 90% gate. Removed generated target/ after
  testing; .gitignore now prevents recurrence.

- 2026-09-10T20:04:27+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T20:04:52+00:00: Recorded command exit 0; command argv SHA-256
  2b8c6c018d03efff505009298f95f6a9e587802c7f6e7085808536ccbd03336f.

- 2026-09-10T20:05:11+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T20:05:34+00:00: Recorded command exit 0; command argv SHA-256
  ecfb73e71d4b8750c31c66df8486c07b2409ec5d41013849f23fa91ead9b4a41.

- 2026-09-10T20:05:53+00:00: Recorded command exit 0; command argv SHA-256
  38d97035eb93675683eda91af05fb797a80f46cf0a81074d5af28b30766fcd45.

- 2026-09-10T20:06:00+00:00: Recorded command exit 0; command argv SHA-256
  927ee57ce58cdf6a04384df16e9a464955803198f340c53ec2e0c3ae28f48e55.

- 2026-09-10T20:06:21+00:00: Recorded command exit 0; command argv SHA-256
  5d0e37991052fdbf0b833eee15324bd7d3ca017b49b22c1b0bd6c6b787e6e015.

- 2026-09-10T20:06:45+00:00: Recorded command exit 0; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T20:07:45+00:00: Recorded command exit 0; command argv SHA-256
  010dedce34cd99cf7017eecc15e0ec4217e3b10839d3c9a81a07aa8a156185d5.

- 2026-09-10T20:09:41+00:00: Recorded command exit 1; command argv SHA-256
  72592e5b77b66c06bce9a2d6f031451ee9037b54a9ec3482d649893d9660d2e8.

- 2026-09-10T20:10:11+00:00: Recorded command exit 1; command argv SHA-256
  66097f8f92e692fae2fa7603544e2c4225659b092d75ab6146a1725c09f7c9ff.

- 2026-09-10T20:10:43+00:00: Recorded command exit 0; command argv SHA-256
  863a45bc4bc6bd7ec46d018f33b46acf53ee9cc77ccbe0aeef45de5020736881.

- 2026-09-10T20:11:04+00:00: Recorded command exit 0; command argv SHA-256
  ad9651af4a929eaae46e90d7cc1cb3e4c4017b32d3ac106a5a2e1109d10c995c.

- 2026-09-10T20:11:20+00:00: Recorded command exit 0; command argv SHA-256
  7bf699f8b9fe8ea423c8b529d2a44639c0a0c799ab821d4d1332f87d54d76094.

- 2026-09-10T20:11:56+00:00: Recorded command exit 0; command argv SHA-256
  010dedce34cd99cf7017eecc15e0ec4217e3b10839d3c9a81a07aa8a156185d5.

- 2026-09-10T20:12:54+00:00: Recorded command exit 0; command argv SHA-256
  1234d870b799bd9c9eb585cbf37d15e3c45436bcd239e393511629a1456f6235.

- 2026-09-10T20:13:31+00:00: Recorded command exit 0; command argv SHA-256
  ec20582851c64317907e2956d169dcb61f9306b0679084eee4036e0de31c2ff4.

- 2026-09-10T20:14:16+00:00: Recorded command exit 0; command argv SHA-256
  161a360ecbed863cd42855fbf95cdbd15ca6a4928531195d83c62bb6be1cd1a1.

- 2026-09-10T20:15:11+00:00: Recorded command exit 0; command argv SHA-256
  9b9aa60ff2dd4910312e53b264d502f0b69298f015cdbcd04d3b12102e9377c0.

- 2026-09-10T20:16:01+00:00: Exact remote PR 10 head 4efdc02aae93dd6fbec561257a37385f70a5d980
  removes self-referential embedded artifact/source hashes: static embedded signer/promotion policy
  bootstraps verification, the signed external manifest binds artifact identities, and mandatory
  ASB_TUI_SOURCE_COMMIT/TREE release-build metadata binds candidate source. Independent re-review
  found no blocking source issue. Exact-head cargo fmt/clippy/test/doc/release build,
  schemas/publication/channel validators, deny/audit, shell/workflow/Gitleaks, ASB isolation (16
  unit + 2 doc), and 90.82% line coverage all pass; GitHub quality CI passes. PR body is current,
  target artifacts removed, tree clean, remote exact. Exit 1 at 20:10:11 UTC was only an apply_patch
  context mismatch; no product mutation or test ran, and the documentation patch was reapplied and
  validated. Integration intentionally waits for overlapping AR-1030 per merge ordering.

- 2026-09-10T20:17:26+00:00: Heartbeat by codex-ar1022-lifecycle-20260910.

- 2026-09-10T20:18:10+00:00: Recorded command exit 1; command argv SHA-256
  73fa30c29214410fadbf5d419d03239fe673a4652a1226eeb2d1db3ba6f04164.

- 2026-09-10T20:18:31+00:00: Recorded command exit 0; command argv SHA-256
  2464597be236edc23793c25f097939ba59362f55b45c36df0ab9f6457d41497e.

- 2026-09-10T20:21:29+00:00: Recorded command exit 0; command argv SHA-256
  fdefef3b68b026c7b0c6d7bb3ff739213359c2f09c145b77614117e6c03806fa.

- 2026-09-10T20:21:57+00:00: Recorded command exit 0; command argv SHA-256
  263270fdf3c9f50abd65c1cebd9be1882947c7724465d197e5a3cafbccd1440f.

- 2026-09-10T20:22:35+00:00: Recorded command exit 0; command argv SHA-256
  010dedce34cd99cf7017eecc15e0ec4217e3b10839d3c9a81a07aa8a156185d5.

- 2026-09-10T20:23:40+00:00: Recorded command exit 0; command argv SHA-256
  1234d870b799bd9c9eb585cbf37d15e3c45436bcd239e393511629a1456f6235.

- 2026-09-10T20:24:08+00:00: Recorded command exit 0; command argv SHA-256
  457dc724bbe3750841289f7117fcdcc23dfaf213243ba5ac415b8fe72f85fe3f.

- 2026-09-10T20:24:36+00:00: Recorded command exit 0; command argv SHA-256
  159517691c3d431433e8a40698daaef7cd5f44b41f03afd55a1ec0581442d2fb.

- 2026-09-10T20:25:09+00:00: Recorded command exit 0; command argv SHA-256
  d54d7589f5ddff82fd65bbddcae754b770d55417b889c34998de31505d9e618d.

- 2026-09-10T20:25:27+00:00: Recorded command exit 0; command argv SHA-256
  9b9aa60ff2dd4910312e53b264d502f0b69298f015cdbcd04d3b12102e9377c0.

- 2026-09-10T20:27:19+00:00: Recorded command exit 0; command argv SHA-256
  8c148503b5a6e18e68b061d7e101d8b65a51968a9512dc0f026ca692fb4fe08c.

- 2026-09-10T20:27:42+00:00: Recorded command exit 0; command argv SHA-256
  c529d776c674b83af2784e49022b7fbe69b44ed9e288ec17203b707c292b4c1f.
