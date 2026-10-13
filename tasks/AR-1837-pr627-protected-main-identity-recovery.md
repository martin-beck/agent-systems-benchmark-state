---
{
  "branch": "repair/ar-1837-pr627-protected-main-identity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1837",
  "next_action": "Await completion of exact-main rerun attempt 2 for Credential-free benchmark path plus remaining Rust, Repository quality, and Emulated AArch64 workflows; release only after all terminal-success and reconcile AR-1835 evidence.",
  "observed_branch": "repair/ar-1837-pr627-protected-main-identity",
  "observed_dirty": 0,
  "observed_head": "6ea3648e483f25179c3112b54ed7c348e141cad4",
  "owner": "",
  "plan": "../plans/AR-1837-pr627-protected-main-identity-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:1d74a4ae886d24a0cb23a7d6bbd50fffe7c206c5d2e19036a36af5342781b08d",
    "evidence_ref": "quality/AR-1837-postmerge-receipt.json",
    "spec_ref": "specs/AR-1837.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1837.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Recover current protected-main provenance after PR #627 was web-merged with a noreply committer, without rewriting history or weakening gates.",
  "task_revision": 34,
  "title": "PR #627 protected-main identity recovery",
  "updated_at": "2026-10-13T06:07:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1837-pr627-protected-main-identity"
}
---

PR #627 was correctly reviewed and all exact-head checks passed, but its GitHub
merge commit `6ea3648e483f25179c3112b54ed7c348e141cad4` was created by
`GitHub <noreply@github.com>`. The protected-main provenance gate therefore
failed, as designed. Preserve that immutable historical merge and its failure
receipt. This AR owns only a forward recovery from the current main tip.

- Do not rewrite or force-update main, reuse the old-base PR, weaken the
  provenance policy, accept arbitrary signers, or alter unrelated ARs.
- Create the smallest signed-DCO recovery topic preserving the current product
  tree, review it independently, run all focused/full gates and exact-head CI,
  and publish a local signed two-parent merge only through
  `tools/integration/merge_pr.py`.
- Verify the repaired exact-main merge, every required post-merge workflow, and
  durable state before acceptance.

- 2026-10-13T05:30:19+00:00: Promoted as an independent forward recovery; it preserves PR #627
  history and requires local signed integration.

- 2026-10-13T05:30:22+00:00: Claimed by ar1837-protected-main-repair-luna.

- 2026-10-13T05:31:20+00:00: Recorded command exit 0; command argv SHA-256
  819507c80908e7d0f961bda582bed4551953e58ffbff136a489cbb200f46f81e.

- 2026-10-13T05:31:41+00:00: Recorded command exit 0; command argv SHA-256
  11b2dffef7908e9c3962538d06308618fb66a17e2faa9796b7050fbf6f5854a6.

- 2026-10-13T05:31:53+00:00: Recorded command exit 0; command argv SHA-256
  0abe2a88b3c0de762bc6784f9db549737556dd139bc87ce4a9f12e8c1efd2d58.

- 2026-10-13T05:32:08+00:00: Recorded command exit 0; command argv SHA-256
  12a7a6f9c64082cafd9bf0cc38aa8025e343cce8caa73825e85976580fdb3a98.

- 2026-10-13T05:33:58+00:00: Independent review at exact head
  5e78a03bcd0988da32b681ad7c0bff9f2d17c68f: metadata-only tree
  bf0cab4849363586724b29e649992319c642a6a7 equals current main parent tree; parent is immutable web
  merge 6ea3648e483f25179c3112b54ed7c348e141cad4; HEAD SSH signature and matching Martin Beck DCO
  verified; repository policy, current-topic-base, portable provenance, and 57 focused
  integration/policy tests passed. Hosted PR #628: provenance and 7 other checks passed; 6 required
  checks still pending at review time. No merge authorized until all exact-head required checks
  terminal-success.

- 2026-10-13T05:36:48+00:00: Created exact-tree signed-DCO recovery topic 5e78a03b from immutable
  main 6ea3648e; PR #628 exact-head provenance and most checks pass, with Rust, repository quality,
  and emulated-aarch64 still pending. Local repository policy and signature tests pass.

- 2026-10-13T05:39:46+00:00: Recorded command exit 0; command argv SHA-256
  88ca7864cb9316c6bd317236ea560f8f4d162e9c033542ebb6339f45412060de.

- 2026-10-13T05:40:22+00:00: Recorded command exit 0; command argv SHA-256
  acb9e76f0ab803d47bc3bb755b59054859f060c84e60cbce9137696dd1019947.

- 2026-10-13T05:40:30+00:00: Recorded command exit 1; command argv SHA-256
  e275ff2c2ee1c6c3c8f5c971b03b46fcf8d2f60f2961c35f7b0428f88534012d.

- 2026-10-13T05:46:53+00:00: Heartbeat by ar1837-protected-main-repair-luna.

- 2026-10-13T05:51:20+00:00: Recorded command exit 0; command argv SHA-256
  0bac8af44b521ce07e90307bdb641df182dc2efbf38166cc9e52da33de0c83a1.

- 2026-10-13T05:51:53+00:00: Heartbeat by ar1837-protected-main-repair-luna.

- 2026-10-13T05:52:02+00:00: Recorded command exit 1; command argv SHA-256
  eb674d367ec4e53fc98d674a5cf9bcaa0b4ff8ffe3a0006a1975ea9fefcb6f63.

- 2026-10-13T05:52:14+00:00: Recorded command exit 0; command argv SHA-256
  ce2d425f5b38455d8897da01b729c8816e35b419878e14b93898fd0bf6e00c22.

- 2026-10-13T05:52:47+00:00: Recorded command exit 0; command argv SHA-256
  83e556d140af1aefd73c66241fd7648e7513e2e721688e8ab2d1b8d36aab640b.

- 2026-10-13T05:53:51+00:00: Heartbeat by ar1837-protected-main-repair-luna.

- 2026-10-13T05:55:33+00:00: Recorded command exit 0; command argv SHA-256
  1ab504a5fb11209e5585ebd093ff13461f2e2cb94f7f2b3fb39a9ae1b2747676.

- 2026-10-13T05:56:02+00:00: Recorded command exit 0; command argv SHA-256
  819507c80908e7d0f961bda582bed4551953e58ffbff136a489cbb200f46f81e.

- 2026-10-13T05:57:31+00:00: Published signed local merge 4a486e97abbb450eb5927faf599119a5aa8be6fb
  with exact parents 6ea3648e and 5e78a03b, exact tree bf0cab48, and verified SSH signature/DCO.
  Exact-main provenance passed. Credential-free attempt 1 failed on transient source_checkout
  fixture Unavailable at source_checkout.rs:913; rerun attempt 2 requested. Other workflows
  terminal-success or still running.

- 2026-10-13T06:00:57+00:00: Recorded command exit 0; command argv SHA-256
  1301824539827075d1cd3dc80f453ea2ca75469a53a5ddaad14dbedb28011799.

- 2026-10-13T06:01:05+00:00: Recorded command exit 0; command argv SHA-256
  654fd22e907f66e0690dd26e03fd80e6d29e167b87cff24eb9c014c59979416f.

- 2026-10-13T06:01:13+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-10-13T06:05:33+00:00: Heartbeat by ar1837-protected-main-repair-luna.

- 2026-10-13T06:06:19+00:00: Recorded command exit 0; command argv SHA-256
  1c7075d6b5acabcc6dd55cfbe9618c040f8f5ec4a533b5c61dfa06db3aaeb04c.

- 2026-10-13T06:06:46+00:00: Recorded command exit 0; command argv SHA-256
  819507c80908e7d0f961bda582bed4551953e58ffbff136a489cbb200f46f81e.

- 2026-10-13T06:07:00+00:00: Exact signed merge 4a486e97 and all ten exact-main workflows
  terminal-success; Credential-free succeeded on rerun attempt 2. Immutable web merge 6ea3648e and
  its failure remain preserved.

- 2026-10-13T06:07:08+00:00: Completed forward-only protected-main identity recovery. Preserved
  immutable web merge 6ea3648e483f25179c3112b54ed7c348e141cad4 and failure evidence. PR #628 exact
  head 5e78a03b passed all checks. Published signed+DCO local two-parent merge
  4a486e97abbb450eb5927faf599119a5aa8be6fb with parents 6ea3648e and 5e78a03b, exact tree bf0cab48,
  verified SSH signature/DCO. All ten exact-main workflows terminal-success; Credential-free passed
  on rerun attempt 2. Receipt quality/AR-1837-postmerge-receipt.json.
