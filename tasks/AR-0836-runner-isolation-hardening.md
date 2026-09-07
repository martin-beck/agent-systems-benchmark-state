---
{
  "branch": "fix/runner-isolation-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T10:52:38+00:00",
  "depends_on": [
    "AR-0830",
    "AR-0831"
  ],
  "id": "AR-0836",
  "next_action": "Independently review immutable signed candidate 9b4e7084e02cdb3a1ff56dc55bbdce413ed6b1d3; keep trusted workflows blocked and AR-0836 in progress until required AR-0837 proves the digest-pinned no-host-mount job-container boundary.",
  "observed_branch": "fix/runner-isolation-hardening",
  "observed_dirty": 0,
  "observed_head": "9b4e7084e02cdb3a1ff56dc55bbdce413ed6b1d3",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0836.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden development-host runner isolation against same-UID job tampering and diagnostic leakage.",
  "task_revision": 106,
  "title": "Harden runner isolation and credential boundaries",
  "updated_at": "2026-09-07T09:23:10+00:00",
  "worktree_key": "agent-systems-benchmark-runner-isolation-hardening"
}
---
## AR-0836

Independent audit found that the runner job identity can traverse or modify installation,
credentials, control files, manifests, and diagnostics, and that diagnostics can expose private
paths and session metadata. Harden before any trusted workflow is dispatched.

Acceptance criteria:

- Use separate operator/service and job identities or an equivalent namespace/broker boundary.
- Make complete installation and control state immutable or operator-owned; verify all relevant files.
- Ensure jobs cannot read registration credentials or poison future registrations.
- Bound and redact diagnostics before storage/upload; add leakage and tamper negative tests.
- Qualify interrupted jobs, reset/recovery, and repeated runs with independent security review.

- 2026-09-07T07:49:35+00:00: Dependencies AR-0830 and AR-0831 are durably done; prioritize P0
  remediation of runner identity separation, credential isolation, immutable control state, bounded
  redacted diagnostics, tamper negatives, and interrupted-run recovery before any further trusted
  dispatch.

- 2026-09-07T07:49:37+00:00: Claimed by quality-20260906.

- 2026-09-07T07:50:01+00:00: Recorded command exit 0; command argv SHA-256
  9a1739e9c710ce7f387f2db688102a1fcc80c6ad43de52642f5a203c2ba519e6.

- 2026-09-07T07:55:50+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T07:57:01+00:00: Recorded command exit 0; command argv SHA-256
  27ac70419368a1d3ddbe62275667441e246bdde59c0eca0883a54627472b9f68.

- 2026-09-07T07:57:52+00:00: Recorded command exit 0; command argv SHA-256
  cc2b0cdf61f91b222db05b6e9f34eb233e5d4faa656f0cde31c361e5d1d9b853.

- 2026-09-07T07:58:30+00:00: Recorded command exit 0; command argv SHA-256
  ccefacb149fdae1a5c214d1ff6e95a8f77c55df373d93bfbdd50163917246584.

- 2026-09-07T08:00:12+00:00: Recorded command exit 0; command argv SHA-256
  cca8fe48e2d3d9221f212048745a9c098a98fee19b5c29afa6a7809bd6ff68a1.

- 2026-09-07T08:00:59+00:00: Recorded command exit 1; command argv SHA-256
  90a5da478cc50ecbbe19f6766816c1d4803b001999e4158892959e0e80654801.

- 2026-09-07T08:01:31+00:00: Recorded command exit 0; command argv SHA-256
  c45a1cb3b8c1fa36ab0ee3a556760bc66e045c4c18dbfa5cd5b3590e81474ea0.

- 2026-09-07T08:02:57+00:00: Recorded command exit 0; command argv SHA-256
  c6603d204547733c7d0dbb0a37c3b0933fbbb68a2e8f17f65cf54b452bb0966b.

- 2026-09-07T08:03:09+00:00: Recorded command exit 0; command argv SHA-256
  eb119a8a48344ba43e77c3b9f2d801d856fe2c7e4a5f67c2462f5f221b9986d7.

- 2026-09-07T08:04:52+00:00: Recorded command exit 1; command argv SHA-256
  24f66769c368b570600c9c24f9660140ffce8bcb300af03447c4a13f47e0bd82.

- 2026-09-07T08:05:30+00:00: Recorded command exit 0; command argv SHA-256
  1f1a7fab33fd09fed4a7339d0c1f640689b0b1820178fcf21e241a9c63b170dd.

- 2026-09-07T08:05:48+00:00: Recorded command exit 0; command argv SHA-256
  6bd8e4f072ef10523763ee459a49038a2d121e1e7d36a08ea22fcb5a222868fd.

- 2026-09-07T08:06:30+00:00: Recorded command exit 0; command argv SHA-256
  bbe49068a531f818998b8a1da454fefe414b43696bc3b05f7633e7ae5becf4bc.

- 2026-09-07T08:06:48+00:00: Recorded command exit 0; command argv SHA-256
  a41298a442999533466d42788cba5dd270e9e05e7f9e2f3e9008184621c37fe3.

- 2026-09-07T08:07:30+00:00: Recorded command exit 1; command argv SHA-256
  b5a5c3cbc903817f67deaabd211c4dd3416dbaab74be7491210cb8d375a3a4ad.

- 2026-09-07T08:07:55+00:00: Recorded command exit 0; command argv SHA-256
  e33236c7cad5e0522445c668b4df39b461d36bd420f3b392ee84357f1876a2d7.

- 2026-09-07T08:13:22+00:00: Recorded command exit 0; command argv SHA-256
  b5a5c3cbc903817f67deaabd211c4dd3416dbaab74be7491210cb8d375a3a4ad.

- 2026-09-07T08:14:31+00:00: Recorded command exit 0; command argv SHA-256
  a7d21dc10772753961015f53d9165f4279d2d850bf4120ee6de133108e6c2285.

- 2026-09-07T08:14:47+00:00: Recorded command exit 0; command argv SHA-256
  bb2063a4a6a7725c9314e61353dab967375a449286f548d33e177c9d74a9e666.

- 2026-09-07T08:15:42+00:00: Recorded command exit 1; command argv SHA-256
  0cc7b1104ae450f1e182e67b28c8eaa8e6157a4c2829a9afc5dcd1b039f8d1c4.

- 2026-09-07T08:16:07+00:00: Recorded command exit 1; command argv SHA-256
  4fbe3a81cab7f41d67025f8c763b9f85c929a70f4355c66d0685484efbb31e09.

- 2026-09-07T08:16:29+00:00: Recorded command exit 0; command argv SHA-256
  8adecd334fcd474e1336ecbd403b24a50161ec9feccd4512a63f57463ff2f94e.

- 2026-09-07T08:17:15+00:00: Recorded command exit 1; command argv SHA-256
  7f01881641d1ee924503f4e1fceacf0f8cecb7536316e0a046b3078f05221d0a.

- 2026-09-07T08:17:52+00:00: Recorded command exit 0; command argv SHA-256
  f49e59811f5d35c5804509e93e07cba6f503895469f539994bba686ff0818b8f.

- 2026-09-07T08:20:23+00:00: Recorded command exit 0; command argv SHA-256
  1c6d2f0a72aa4251ca5b109e4316056c01c1d91a221395146eb24bed04bf03ac.

- 2026-09-07T08:23:36+00:00: Heartbeat by quality-20260906.

- 2026-09-07T08:24:43+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:26:02+00:00: Recorded command exit 0; command argv SHA-256
  f60b2cc9e9ba4a52e7020a16f6b9d31c68f8500a8fd3bb70fde740c910ebf94f.

- 2026-09-07T08:27:47+00:00: Recorded command exit 0; command argv SHA-256
  236bf925b3bd6acb59dc2153b45727aabffdbd2c69c334329c15790693a278ca.

- 2026-09-07T08:29:07+00:00: Recorded command exit 0; command argv SHA-256
  9e78099a86acb99c0693f576e333d2269173569154d7324c3d3a6ace25ba248e.

- 2026-09-07T08:29:47+00:00: Recorded command exit 0; command argv SHA-256
  5e4c90e8eff8cfc09507dd2b9c4d7fc3750e30664dc9758e698945df823cad9e.

- 2026-09-07T08:32:22+00:00: Recorded command exit 0; command argv SHA-256
  bb2cfea474a970108989559fadd3f2ae2fdf46c889f315f658fea94f55dd54ce.

- 2026-09-07T08:34:40+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-07T08:35:59+00:00: Recorded command exit 1; command argv SHA-256
  20987eb4a9d1e9581e3b375e9593e790d1207e67674978cf2835f2d78cf15374.

- 2026-09-07T08:37:14+00:00: Recorded command exit 0; command argv SHA-256
  710422624481f3bdc039f34214632c270d73e4d4d4ccfbb6d46bfa99424c7a6e.

- 2026-09-07T08:37:33+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:37:57+00:00: Recorded command exit 0; command argv SHA-256
  6abf29342514d07de4a31300c9f147d1dbea87566817f837061163d4160c4570.

- 2026-09-07T08:38:14+00:00: Recorded command exit 1; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:38:40+00:00: Recorded command exit 0; command argv SHA-256
  90a2742cb9934f9cd6955d31ecd3b5eecd88cfca8803055ad331d52346fa61a1.

- 2026-09-07T08:38:50+00:00: Recorded command exit 1; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:39:11+00:00: Recorded command exit 0; command argv SHA-256
  96e78807ee140bb09ae932f5ec77b9d4b008fa4e19722248482df14e248aa422.

- 2026-09-07T08:39:24+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:41:24+00:00: Recorded command exit 1; command argv SHA-256
  88e52a19b5fd302cf77562feebb152d763dd6689c93a354f42c0a708735b727a.

- 2026-09-07T08:42:29+00:00: Recorded command exit 0; command argv SHA-256
  770b02c164fa349fb2d7ccbf4b13f8a4a19c8428772d63715faef09de737e336.

- 2026-09-07T08:42:49+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:43:18+00:00: Recorded command exit 0; command argv SHA-256
  f3d87d6cdd17d39058c9e62a2370c65ab9d728d0143c2556b2c01df66931c635.

- 2026-09-07T08:43:45+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:45:49+00:00: Recorded command exit 0; command argv SHA-256
  fd7a1611e54f62b2e70adc44dce8c37e362d308222a6affd42c34018da2d6bc7.

- 2026-09-07T08:46:02+00:00: Recorded command exit 1; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:46:25+00:00: Recorded command exit 0; command argv SHA-256
  242e303dc04031e09b768da70a7cb9126382f0fae17f95f5a4c4b1dd2bc66fbb.

- 2026-09-07T08:46:44+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:46:59+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:47:50+00:00: Recorded command exit 0; command argv SHA-256
  5b6b303cb0dd4e2e74a71b9297c6029a4887d87c93a39eaa1918bd9136161b29.

- 2026-09-07T08:53:41+00:00: Recorded command exit 1; command argv SHA-256
  20104d499873291abce80df40a8b875589db628c22dcb0e8970cd209b8e6a0cd.

- 2026-09-07T08:55:54+00:00: Recorded command exit 0; command argv SHA-256
  42b4a54cb4bd3d539319e721977cba1ef4b4fef1080e7799851e544b9a11d9a7.

- 2026-09-07T08:56:13+00:00: Recorded command exit 2; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:56:55+00:00: Recorded command exit 0; command argv SHA-256
  aa3eb6bb85ebce32c1b65da397055a4fc75b4be9a99f4fff865d1fc846c237f3.

- 2026-09-07T08:57:10+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T08:57:28+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T08:57:48+00:00: Recorded command exit 1; command argv SHA-256
  108aaca05160cbfa7975662adbdb34421b6f3ffbe5c0778e2866f0c26d8747d2.

- 2026-09-07T08:58:11+00:00: Recorded command exit 0; command argv SHA-256
  2896979a3bfb398f31f2cc5fc36d4a9dab6b63d6b5c3a516fb16f1240f91d52e.

- 2026-09-07T08:58:36+00:00: Recorded command exit 1; command argv SHA-256
  108aaca05160cbfa7975662adbdb34421b6f3ffbe5c0778e2866f0c26d8747d2.

- 2026-09-07T08:59:49+00:00: Recorded command exit 0; command argv SHA-256
  0640b2a1db1fe9f119feb52e5a2b76e9c8d2a3025ba2e511360652d3f6be8dea.

- 2026-09-07T09:00:07+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T09:00:22+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T09:00:41+00:00: Recorded command exit 0; command argv SHA-256
  108aaca05160cbfa7975662adbdb34421b6f3ffbe5c0778e2866f0c26d8747d2.

- 2026-09-07T09:02:13+00:00: Recorded command exit 0; command argv SHA-256
  7b5547bc52417e698d38d7dc1f4dcaeb8a58efdbede7edc7e830f3f081f3a155.

- 2026-09-07T09:02:25+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T09:02:57+00:00: Recorded command exit 2; command argv SHA-256
  2deab4116e303e3c36b1bdbb19efe75e0119aa8f70c540e41a417ccb3f668ce5.

- 2026-09-07T09:03:18+00:00: Recorded command exit 0; command argv SHA-256
  dae60d52df93c95d36029d78557a94b3202de1d87bc8a17a64dca9c43a4a59fa.

- 2026-09-07T09:04:00+00:00: Recorded command exit 0; command argv SHA-256
  4187fef0ecc6b0cbc361a7f1e5ba4c984f699ecef289e1f283c17e31e771e9d0.

- 2026-09-07T09:04:34+00:00: Recorded command exit 0; command argv SHA-256
  9e7948294b716bc9ced70bca60c24f4564618bb69266e9f0d64c77695f019eab.

- 2026-09-07T09:08:24+00:00: Recorded command exit 0; command argv SHA-256
  3fda5eddb0a4a91ec576d2a489cf2ed4a65c127d2c1c91110bd60d211733cdee.

- 2026-09-07T09:08:45+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T09:09:03+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T09:10:17+00:00: Recorded command exit 0; command argv SHA-256
  19a9e451bc01171c38ea687175245b301d01f8cbae8052c705259bec175d4a14.

- 2026-09-07T09:10:36+00:00: Recorded command exit 0; command argv SHA-256
  c3ffd96328f1b348eeb5d3a7ebfa822e11b9272f787c67c1c779d89f71614104.

- 2026-09-07T09:10:53+00:00: Recorded command exit 0; command argv SHA-256
  5006e498fa2dfe33da9a4e6aeb1b3ddabc295b6ce95c9a362fea3d7d60eb4381.

- 2026-09-07T09:11:25+00:00: Recorded command exit 0; command argv SHA-256
  41300a2dff52272e29a9a2cf5352f3ddc0de11eaf18370b7c89b34da1c344de9.

- 2026-09-07T09:11:41+00:00: Recorded command exit 0; command argv SHA-256
  0007e77f9437825846e37dc5b797ea6d1d977e05d1573d51db10d36a6c7e1284.

- 2026-09-07T09:12:04+00:00: Recorded command exit 0; command argv SHA-256
  108aaca05160cbfa7975662adbdb34421b6f3ffbe5c0778e2866f0c26d8747d2.

- 2026-09-07T09:13:00+00:00: Recorded command exit 0; command argv SHA-256
  3d47354594ebaa2fc2b50cbfcad46b8328bbeee7079f0f5c918056c872a8f2e3.

- 2026-09-07T09:13:27+00:00: Recorded command exit 0; command argv SHA-256
  1ef009c4e34c2be5aeb311adb495e1a43ed7a6b7bf6cd7553e72846b87f75677.

- 2026-09-07T09:14:01+00:00: Recorded command exit 0; command argv SHA-256
  555bf630bf8894cd3564f317e17046d8842a068156a48e30922cceccb8baf4db.

- 2026-09-07T09:17:02+00:00: Recorded command exit 0; command argv SHA-256
  519fbec9af2ac49172bebce27289e75f35b0c60c638343833adf59df2f3b09c4.

- 2026-09-07T09:18:22+00:00: Recorded command exit 0; command argv SHA-256
  8cdf0329a8f9c6360d5f467c697e6715e1037b45c7a5e263af8265419af4eadc.

- 2026-09-07T09:18:39+00:00: Recorded command exit 0; command argv SHA-256
  e967f5de9ead82ef94f2900787ddf398596dd6cfebf28a99741cf562148f771c.

- 2026-09-07T09:19:00+00:00: Recorded command exit 0; command argv SHA-256
  c73d3d068381f713c83976489e671d5fd5a9dff9c8ad3d26c5d3b46b5d77ede5.

- 2026-09-07T09:20:12+00:00: Recorded command exit 0; command argv SHA-256
  10c4154b2b8a9a87fcbf43d9999fb57358027935ee756605aef286bd995f1632.

- 2026-09-07T09:21:22+00:00: Recorded command exit 0; command argv SHA-256
  6282dd50ec0c96aa4253d483abc3983fa4e6300b59909475c3969adf07b1bf69.

- 2026-09-07T09:22:02+00:00: Recorded command exit 0; command argv SHA-256
  db4cc6484533e1a01df3c274e9fce6fb702de4444d23184af3ce4a05113e7708.

- 2026-09-07T09:22:38+00:00: Heartbeat by quality-20260906.

- 2026-09-07T09:23:10+00:00: Exact immutable candidate 9b4e7084e02cdb3a1ff56dc55bbdce413ed6b1d3 tree
  a92927d96a0a261108be8f368ca1edcc88b06d5e on base dc224fcfddea8f5dbfae2da5c795535486f2c45b is clean
  and SSH-signed+DCO. Exact-head fmt/clippy/workspace tests/docs/release build, runner security
  fixture, native systemd interruption/reset fixture, real pinned 2.337.0 archive
  setup/idempotence/listener boundary, Ruff, repository policy, actionlint, zizmor, introduced-range
  Gitleaks, cargo-deny/audit, platform validation, configured coverage, deliberate failure fixtures,
  Kani 5/5 plus rejected false assertion, Loom/production/state model tests all pass. External
  fixture SHA-256: native fc153618185174b43231dea34e4e03ea886eef76caad9464951bbc11f41bb8cc; real
  archive test f65039a124d81efce48fdc725caf04247f6d943e87476afdb6badcae3ebf3765. Completion remains
  blocked on AR-0837 containerized job-principal boundary.
