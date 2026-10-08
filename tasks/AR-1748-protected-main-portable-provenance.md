---
{
  "branch": "repair/ar-1748-portable-main-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T20:27:25+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1748",
  "next_action": "Implement a generally available required CI provenance check and capability-aware ruleset admission, then independently review, merge, verify post-merge CI, and perform one bounded live settings apply with two consecutive audits.",
  "observed_branch": "repair/ar-1748-portable-main-provenance",
  "observed_dirty": 1,
  "observed_head": "0f3e191ad59ca70934f937e6ea6b6e9e999e90c3",
  "owner": "ar1748_portable_main_provenance_20261008",
  "plan": "../plans/AR-1748-protected-main-portable-provenance.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1748.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Replace the unavailable Enterprise-only commit-metadata ruleset with a required portable provenance check while preserving Web Flow rejection and atomic protected-main admission.",
  "task_revision": 55,
  "title": "Portable protected-main provenance and capability admission",
  "updated_at": "2026-10-08T18:06:50+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1748-portable-main-provenance"
}
---

AR-1746 merged bounded settings diagnostics and passed every exact-main
post-merge workflow, but its single live ruleset creation attempt was rejected
atomically with HTTP 422. Two audits prove that no repository setting or
ruleset was partially changed. Read-only diagnosis identifies the requested
`committer_email_pattern` restriction as an Enterprise-organization metadata
feature, while ASB is a public user-owned GitHub Free repository. Core public
rulesets are available and repository administration is working.

This successor must preserve the actual admission predicate. It may not remove
the metadata rule and then claim Web Flow rejection is enforced: GitHub Web
Flow commits can be GitHub-signed and web signoff supplies DCO but does not
prove the reviewed local merge path. Instead, add a mandatory portable CI
provenance check that rejects Web Flow/noreply commits and validates the exact
signed-DCO merge identity, require that check in the generally available core
ruleset, and make the settings tool capability-aware before any mutation.

Development integration requires an independent technical worker but permits
the same GitHub account; it does not require a second account, production
credentials, a verified release, or an Enterprise upgrade. If the portable
contract cannot be expressed and observed on the current repository, fail
closed with an exact typed blocker rather than weakening it.

- 2026-10-08T17:24:52+00:00: Promoted after AR-1746 atomic rejection diagnosis: implement portable
  Web Flow provenance enforcement and capability-aware core ruleset admission without weakening
  development policy.

- 2026-10-08T17:27:25+00:00: Claimed by ar1748_portable_main_provenance_20261008.

- 2026-10-08T17:27:34+00:00: Recorded command exit 0; command argv SHA-256
  b7023a6f6301c30be2548d060b4866d61bffe515b6b2c81f33dc2fb25c858b10.

- 2026-10-08T17:30:20+00:00: Recorded command exit 0; command argv SHA-256
  3a8b5522600b1ac244d11f78d2a060d1a8e60b8ba3477ef6aa7586d54d5a5d8c.

- 2026-10-08T17:31:33+00:00: Recorded command exit 1; command argv SHA-256
  1933e16a4a920a306a9d32682500f1537f49a615d94c6d095dcc6c288fa88e6f.

- 2026-10-08T17:32:11+00:00: Recorded command exit 0; command argv SHA-256
  2c04dad3bf114734e4dadc332f2895b056f1a1c0391d5f3afe4b112cf60dd603.

- 2026-10-08T17:33:15+00:00: Recorded command exit 0; command argv SHA-256
  89271759062811bdecd44b61893fc6c5e9f84d22e32c3680c24a59f1830bca23.

- 2026-10-08T17:34:18+00:00: Recorded command exit 0; command argv SHA-256
  d63e90f8ae54457d339f9b47686f46eba967265df5d7642f02d6501a1414dda7.

- 2026-10-08T17:35:29+00:00: Recorded command exit 0; command argv SHA-256
  3800c82124d3a3bd5076f14ef9f4015d941c14d433b648213f7e7f98b22f7194.

- 2026-10-08T17:36:23+00:00: Recorded command exit 0; command argv SHA-256
  01776cc343dc72841b6be96cc94385211af3f567a39ee755aa05cfdd729a120c.

- 2026-10-08T17:37:22+00:00: Recorded command exit 0; command argv SHA-256
  e715f1e7710a316d80a9064a93f4026cf086ee34e28008219a961375550ec482.

- 2026-10-08T17:38:29+00:00: Recorded command exit 0; command argv SHA-256
  43deabf539411468532103a845b08e52516b30a6e20b99d1145432b4963a4496.

- 2026-10-08T17:39:39+00:00: Recorded command exit 1; command argv SHA-256
  46b0463d9ed539cd84e65e997ecb9d9571e8df343ebc30e4c851d07dfe5625fc.

- 2026-10-08T17:40:23+00:00: Recorded command exit 0; command argv SHA-256
  2bbc8f4f0f4125bfc994cf95057cc8a4fa60bb76c8ebc5127a77d018f2935779.

- 2026-10-08T17:41:03+00:00: Recorded command exit 0; command argv SHA-256
  22cb95ff0d85fc0440379c12418996e08dab806f5bae5a4292a987d567092e52.

- 2026-10-08T17:42:12+00:00: Recorded command exit 0; command argv SHA-256
  fd78dfa56fa41d002935de144ab8a008f414b2bafc8c12d590b0d461585ab114.

- 2026-10-08T17:42:49+00:00: Recorded command exit 0; command argv SHA-256
  b9978a9768478b4fac353b36a0e9e95b094202a9b22ecb6b021234ed3cdd8534.

- 2026-10-08T17:44:04+00:00: Recorded command exit 0; command argv SHA-256
  5eea8a427c9a57ea2f558ec5c86789945653999259c3cf77417272ebb27803df.

- 2026-10-08T17:44:55+00:00: Recorded command exit 0; command argv SHA-256
  cb245c16ea28293d29b342611d152ffebc7d568569be45bfbdfcafed41884c66.

- 2026-10-08T17:45:39+00:00: Recorded command exit 12; command argv SHA-256
  80dc188013551b9d2dcdc7b74af8619dcc30df876d8deb5487ebb87a2fa16d2b.

- 2026-10-08T17:46:17+00:00: Recorded command exit 0; command argv SHA-256
  fdeb4253daa9df8b1c917332717e6494505617cf5d27d8164ce2830c47be57c5.

- 2026-10-08T17:46:55+00:00: Recorded command exit 5; command argv SHA-256
  2aae2265f1e6dec0c9c43f56a332dca8155568efcc4cdf0cbfbaf3ea27498bd5.

- 2026-10-08T17:47:40+00:00: Recorded command exit 1; command argv SHA-256
  d4cad40b7a8688c7636908c9b8113eda17610796d887bd7cfc462226600a38d1.

- 2026-10-08T17:49:50+00:00: Recorded command exit 1; command argv SHA-256
  75da18d879a32eefe687325d3ed4c8ee76b4978d01e06baa175956eb9313c48b.

- 2026-10-08T17:50:43+00:00: Recorded command exit 1; command argv SHA-256
  9c7a68d117c36bf8183561fd3817bece91718e1f7b4f4bdf13cdec31f05e36b7.

- 2026-10-08T17:51:23+00:00: Recorded command exit 0; command argv SHA-256
  b670188e94c8944bf1790db0f6014e9f33a6cd1982f9d8e9cc5bbd16187af03c.

- 2026-10-08T17:52:48+00:00: Recorded command exit 0; command argv SHA-256
  365705a1e124e3860b942a54890fac049776eb1e389b00c11eba9998aa38edce.

- 2026-10-08T17:53:17+00:00: Recorded command exit 1; command argv SHA-256
  796d7d1ed7b79fdc1d888c0a65f65adafd30f881bab11916e0847b99153f7126.

- 2026-10-08T17:53:47+00:00: Recorded command exit 0; command argv SHA-256
  f9535a1710caa4aa90fd3050bfc65744db68f1f58bdce8c6a803aaaebc230b1d.

- 2026-10-08T17:54:31+00:00: Recorded command exit 0; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T17:55:20+00:00: Recorded command exit 0; command argv SHA-256
  97064ed7cb0c9d071cbf447c550d33c000c2c0f2b3ff79146cf5e6a782616a9d.

- 2026-10-08T17:56:45+00:00: Recorded command exit 0; command argv SHA-256
  aa057277b14752f4512606dbae84c1e311b43395938d79aa7e389f4dbd74f430.

- 2026-10-08T17:57:43+00:00: Recorded command exit 1; command argv SHA-256
  d297c0b0a581b166b49116fbc5ae7cb6f5093792793d5ba09c17bbdc36e09749.

- 2026-10-08T17:58:19+00:00: Recorded command exit 0; command argv SHA-256
  e6721fe6c82a8d3baf7c5273cd8d98f231162e20ad6a4a7e1c0ca9126c515760.

- 2026-10-08T17:59:06+00:00: Recorded command exit 1; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T17:59:38+00:00: Recorded command exit 0; command argv SHA-256
  a8485bc578fa832f684c1d15b88c90fd5e02f735c47b373693535bb2ae479dc6.

- 2026-10-08T18:00:15+00:00: Recorded command exit 0; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T18:00:56+00:00: Recorded command exit 0; command argv SHA-256
  91e411b2ca14fdbeab2e918129c0cf8f8b89c85c851eb40e3c06d2984a4254f7.

- 2026-10-08T18:02:03+00:00: Recorded command exit 1; command argv SHA-256
  d28dcd36fe2139b55ed5097dad019d42f53306625fcc04857a9e29071e799287.

- 2026-10-08T18:02:56+00:00: Recorded command exit 0; command argv SHA-256
  6e984ad65f7fb71f5a445d0d884382b3fbf195690b6a0d23b399e6a112f07017.

- 2026-10-08T18:04:27+00:00: Recorded command exit 101; command argv SHA-256
  07754ba7533aa3cd130e27b4aa2b6da57f71c000d2b2f2b3a097ddaf86c26cb4.

- 2026-10-08T18:05:32+00:00: Recorded command exit 101; command argv SHA-256
  ab5a9c92aaf85b753c7682039890e23f35d075b18d538e9be6114dd2986f23f8.

- 2026-10-08T18:06:13+00:00: Recorded command exit 0; command argv SHA-256
  85126b8b38c89ca1823cf2baea6599fad768cf4e2d6c563b6103dc47c8c8264e.

- 2026-10-08T18:06:50+00:00: Recorded command exit 0; command argv SHA-256
  0929435abe4feb91e69776e5a5192d27ba752d1d94e5759c90b9d2888c90e08d.
