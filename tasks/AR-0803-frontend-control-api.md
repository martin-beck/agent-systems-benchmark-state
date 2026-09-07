---
{
  "branch": "feature/frontend-control-api",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T04:26:28+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204",
    "AR-0801"
  ],
  "id": "AR-0803",
  "next_action": "Define a bounded versioned control/status API between the runner and independent frontends.",
  "observed_branch": "feature/frontend-control-api",
  "observed_dirty": 0,
  "observed_head": "cfa2cf9184f2b12f1bf870cde436d776a57254be",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0803.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.",
  "task_revision": 57,
  "title": "Define the frontend control API",
  "updated_at": "2026-09-07T03:39:03+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-control-api"
}
---
## AR-0803

Expose runner planning, launch, status, cancellation, history, and analysis through a stable frontend boundary.

The benchmark runner remains independently operable when no frontend is present or when a frontend crashes.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T02:56:13+00:00: Dependencies AR-0101, AR-0104, AR-0204 and AR-0801 are durably done;
  AR-0801 exact-main b2833ab CI and post-merge verification are green. Promote the highest-priority
  compatible frontend control boundary after releasing its Cargo/scheduler fences.

- 2026-09-07T02:56:28+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T03:12:45+00:00: Recorded command exit 0; command argv SHA-256
  2112362c51cef85781237610d9b9e060605ef818fbc3842b7637243011b6072d.

- 2026-09-07T03:14:02+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-07T03:14:55+00:00: Recorded command exit 1; command argv SHA-256
  119a2544b57bc260d3736a8c380cb862336dcb3828b84394350db9659ad2e775.

- 2026-09-07T03:15:19+00:00: Recorded command exit 2; command argv SHA-256
  8bc998ab7b97ddd3689435d527789bef02f835b0eaf4edea3eb44d40eda18b6d.

- 2026-09-07T03:16:20+00:00: Recorded command exit 0; command argv SHA-256
  0abe16459841183b1c87533de5496a6b32348f12b93116537775513a95c9fca7.

- 2026-09-07T03:17:52+00:00: Recorded command exit 0; command argv SHA-256
  fca74cf20e25dfa6f5c081431044ca67513dad3c8d08f41a256e74b0f8c1d7ea.

- 2026-09-07T03:18:35+00:00: Recorded command exit 0; command argv SHA-256
  0d969cea7c6abd88e73a08fa66d0dc0d021ea41dd86666a0bd912be5ae398cf8.

- 2026-09-07T03:20:40+00:00: Recorded command exit 0; command argv SHA-256
  29edb89936fae8949ecff5ce1d8f65f1d5b22895939819c00fd22579efc6be41.

- 2026-09-07T03:21:46+00:00: Recorded command exit 0; command argv SHA-256
  f8c05adc56c7dd166f048c9549d034ce2230c511e4fea79a05c704f84f8bf78d.

- 2026-09-07T03:22:04+00:00: Recorded command exit 127; command argv SHA-256
  6ed4c4670327e5fee3971d31b475508b1557c7b1af50c61f10b93c29ca90ed67.

- 2026-09-07T03:22:22+00:00: Recorded command exit 101; command argv SHA-256
  6d046ec0ea3fcb81dfa5c60c9c2deb6822991c7dd90c1f0a868d691a1bf5f724.

- 2026-09-07T03:22:32+00:00: Recorded command exit 101; command argv SHA-256
  eb4580fb0cfa8ee65783040f56ad5eea0facc89e0a4e083b985002929fe9abc9.

- 2026-09-07T03:22:52+00:00: Recorded command exit 101; command argv SHA-256
  e6dfbd88d5865227dc296f9b320027567ad103fe984418f6601488eccf39b6b1.

- 2026-09-07T03:23:06+00:00: Recorded command exit 0; command argv SHA-256
  f2846dece264eb519b00d71e54c44cc9a4f0841844d4f852f5d36c5e54d56dc0.

- 2026-09-07T03:23:19+00:00: Recorded command exit 101; command argv SHA-256
  eb4580fb0cfa8ee65783040f56ad5eea0facc89e0a4e083b985002929fe9abc9.

- 2026-09-07T03:23:39+00:00: Recorded command exit 0; command argv SHA-256
  48c873b9b5b878c0ec63bedf3bfb35491a6c7c2edbc3a7775b10b57ecc7be9b1.

- 2026-09-07T03:24:08+00:00: Recorded command exit 101; command argv SHA-256
  eb4580fb0cfa8ee65783040f56ad5eea0facc89e0a4e083b985002929fe9abc9.

- 2026-09-07T03:24:36+00:00: Recorded command exit 0; command argv SHA-256
  2e6dfab732f35b46234b742feec5518510ffc86f94b906320fd5c9fc89615cd1.

- 2026-09-07T03:26:19+00:00: Recorded command exit 0; command argv SHA-256
  15e56d1742b7c1e7eee38be4775fa32b045b47a090a5118651205bb9b5958a38.

- 2026-09-07T03:27:17+00:00: Recorded command exit 0; command argv SHA-256
  a7f63de807c47e88bf6e6bfc44b4460abb47a0a9b50d9c3b7d03e31565ec73b7.

- 2026-09-07T03:27:39+00:00: Recorded command exit 0; command argv SHA-256
  fbb0d9a3c7747cf8969a359e0fe1469dd7bc7d7d2627d361425f8647a2bb3306.

- 2026-09-07T03:28:14+00:00: Recorded command exit 0; command argv SHA-256
  37fc1cd75c7da616a0ec951f7f78f57be294f150658b9a07216e607134f8cce9.

- 2026-09-07T03:28:26+00:00: Recorded command exit 1; command argv SHA-256
  1c77fafd61757db82aba2ae79c38c832b55f8b010f58dd25b519df6cb3ff9999.

- 2026-09-07T03:28:39+00:00: Recorded command exit 0; command argv SHA-256
  f09ec4fb474166f926818d73b9829b45b2e73311346a74f15eba151a6bfe6b22.

- 2026-09-07T03:28:51+00:00: Recorded command exit 0; command argv SHA-256
  a7f63de807c47e88bf6e6bfc44b4460abb47a0a9b50d9c3b7d03e31565ec73b7.

- 2026-09-07T03:29:36+00:00: Recorded command exit 0; command argv SHA-256
  75e8ad17f512e86c3412880ec797619058eba7896b096fe06cd671ff4555fc7c.

- 2026-09-07T03:29:53+00:00: Recorded command exit 0; command argv SHA-256
  ed14c6a3ec60c0d199d388f3735d98803782965e51004f13ff43d708c5d4ccef.

- 2026-09-07T03:30:34+00:00: Recorded command exit 0; command argv SHA-256
  dc7b0f89318f3fadd0561ebdaa6d49989edf2e07c403e2115fb3655877eb2aea.

- 2026-09-07T03:30:49+00:00: Recorded command exit 0; command argv SHA-256
  3811ed75e3a46797ba9e6aba4b7ed6ab6d69c1ecf34f12d6616a5fec529f0e09.

- 2026-09-07T03:31:06+00:00: Recorded command exit 0; command argv SHA-256
  62671a09093bd0984028506ea5687ce1fcf498517169dc87105f63b3d0366b39.

- 2026-09-07T03:31:43+00:00: Recorded command exit 0; command argv SHA-256
  6ba64fb8b27e4cf26f538570ae8aa49002b3ad7792ca4c81d9bc28aa9fbded81.

- 2026-09-07T03:32:04+00:00: Recorded command exit 101; command argv SHA-256
  883690dc58e2d49f4091026443d24dd40e1a77e12394793e3636c521c7efbaa5.

- 2026-09-07T03:32:18+00:00: Recorded command exit 0; command argv SHA-256
  01ac58474d1a2e52a576392e3a4c66dd2544baea1eee529c4b141bab64423e0e.

- 2026-09-07T03:32:30+00:00: Recorded command exit 101; command argv SHA-256
  883690dc58e2d49f4091026443d24dd40e1a77e12394793e3636c521c7efbaa5.

- 2026-09-07T03:32:43+00:00: Recorded command exit 0; command argv SHA-256
  6271d182cc47efdadc7c8de5a60f1c3b555bf6339182f64f0986809e90031057.

- 2026-09-07T03:33:11+00:00: Recorded command exit 0; command argv SHA-256
  883690dc58e2d49f4091026443d24dd40e1a77e12394793e3636c521c7efbaa5.

- 2026-09-07T03:33:37+00:00: Recorded command exit 0; command argv SHA-256
  af1dbf68cf3bef7063a2ba1be236d2546d08e14f870b5635f8115501d770d4e7.

- 2026-09-07T03:33:55+00:00: Recorded command exit 0; command argv SHA-256
  56b14118e4cb447e53b66649a01062ea680c7f9665d0971b287a404669e9b081.

- 2026-09-07T03:34:43+00:00: Recorded command exit 1; command argv SHA-256
  6bee86a72820dede6e745e95e16b3cbf89547b463692cf1eacfb12134c446a0d.

- 2026-09-07T03:35:09+00:00: Recorded command exit 0; command argv SHA-256
  113701b81deabde6989b437a31c252fa75e8052baa996ceb3babfbf08cbc87fe.

- 2026-09-07T03:35:22+00:00: Recorded command exit 0; command argv SHA-256
  8a1a350fb508eb11563688e696a9686b1e38a641dfbd5ce42d486a6f1f23e2bd.

- 2026-09-07T03:35:56+00:00: Recorded command exit 0; command argv SHA-256
  c1e01290718f10e5694ca4d69d00768e46e26a729df66a63db3bf381153d2a74.

- 2026-09-07T03:36:41+00:00: Recorded command exit 0; command argv SHA-256
  b4cab6df1a702e841b57e3c63e696e0943479a1ee757603bbfa39c7aad8042f6.

- 2026-09-07T03:37:30+00:00: Recorded command exit 0; command argv SHA-256
  4a602b498883c347402f64acd84e69f50897ffce4a3e2910533dd3d3d13458f5.

- 2026-09-07T03:37:53+00:00: Recorded command exit 0; command argv SHA-256
  9d8f4fd3a1339d6dc7561fe6ef575e7f944ad205a79c013a245322f520deb0ea.

- 2026-09-07T03:38:08+00:00: Recorded command exit 0; command argv SHA-256
  c7fafc8d3724d4efcf548588645ef6ddad62c1a77c1b9f57bd7413a5a03fb706.

- 2026-09-07T03:38:26+00:00: Recorded command exit 0; command argv SHA-256
  d259c25a3f26b3cd21809239ad7a603fb07bfab6efd3ae8fbe533f04a71f3e92.
