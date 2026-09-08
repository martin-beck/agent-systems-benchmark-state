---
{
  "branch": "feature/provider-openai",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T12:57:57+00:00",
  "depends_on": [
    "AR-0301",
    "AR-0302",
    "AR-0303",
    "AR-0304",
    "AR-0305",
    "AR-0306",
    "AR-0307",
    "AR-0308",
    "AR-0309",
    "AR-0310"
  ],
  "id": "AR-0311",
  "next_action": "Extend the three-path OpenAI profile patch with bounded synthetic effective-request observations and negative credential/settings/redaction evidence before candidate gates.",
  "observed_branch": "feature/provider-openai",
  "observed_dirty": 3,
  "observed_head": "e5cdf97dd2954e5d097b1a6c872beafd724aa12f",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0311.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Apply one default OpenAI provider profile consistently to all supported agents.",
  "task_revision": 11,
  "title": "Support a shared OpenAI provider",
  "updated_at": "2026-09-08T10:05:40+00:00",
  "worktree_key": "agent-systems-benchmark-provider-openai"
}
---
## AR-0311

Apply one default OpenAI provider profile consistently to all supported agents.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T09:53:22+00:00: Promote shared OpenAI provider after all adapter dependencies are done
  and AR-0312 Ollama provider is released.

- 2026-09-08T09:53:27+00:00: Claimed by contracts_20260906.

- 2026-09-08T09:55:23+00:00: Recorded command exit 0; command argv SHA-256
  7e88ebced015075b888df28562157975bde6d6e50ea68961a5514a936f9ae278.

- 2026-09-08T09:56:20+00:00: Recorded command exit 0; command argv SHA-256
  4db8c8d9db82832ab21db53ddafd0eddd0af792f22d23605cd9d86a534c33562.

- 2026-09-08T09:57:57+00:00: Heartbeat by contracts_20260906.

- 2026-09-08T10:00:46+00:00: Recorded command exit 2; command argv SHA-256
  842b16cbde21e5f60688efe941941cb128c1eb34b282911637385be2c02c8350.

- 2026-09-08T10:05:02+00:00: Recorded command exit 0; command argv SHA-256
  e4e7b5d30b14991038bf41709ddde33a67e9ff498799346f925ff9c51d600257.

- 2026-09-08T10:05:40+00:00: Material first implementation checkpoint on exact base e5cdf97: dirty
  only crates/asb-agents/src/lib.rs plus new openai.rs and OPENAI.md. Added dated gpt-5.2-2025-12-11
  public-service profile, secret-reference-only credential provenance, eight adapter translations,
  Codex Responses versus Chat Completions routing, Gemini fail-closed rejection, and
  profile/credential/drift negatives. Focused OpenAI tests pass 3/3 after fmt. Two earlier exits 2
  were patch transport misuse only (apply_patch requires one argument, not stdin); neither changed
  product files; corrected external patch artifact applied through wrapper.
