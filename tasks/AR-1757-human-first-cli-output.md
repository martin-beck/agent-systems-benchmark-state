---
{
  "branch": "feature/ar-1757-human-first-cli-output",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T14:58:15+00:00",
  "depends_on": [
    "AR-1338",
    "AR-1555"
  ],
  "id": "AR-1757",
  "next_action": "Inventory every public ASB command outcome at exact current main, define the command-aware human presentation contract, and replace the generic JSON key/value renderer without changing explicit --json schemas.",
  "observed_branch": "feature/ar-1757-human-first-cli-output",
  "observed_dirty": 1,
  "observed_head": "b3cb9b256cccc15be682dbb1019a239b50edf6cd",
  "owner": "codex-asb-ar1757-human-output-20261009",
  "plan": "../plans/AR-1757-human-first-cli-output.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1757.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make default ASB CLI output concise, command-aware, self-explanatory, and actionable while preserving stable machine-readable output.",
  "task_revision": 9,
  "title": "Human-first ASB command output",
  "updated_at": "2026-10-09T13:01:59+00:00",
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
