---
{
  "branch": "feature/ar-1757-human-first-cli-output",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T14:56:56+00:00",
  "depends_on": [
    "AR-1338",
    "AR-1555"
  ],
  "id": "AR-1757",
  "next_action": "Inventory every public ASB command outcome at exact current main, define the command-aware human presentation contract, and replace the generic JSON key/value renderer without changing explicit --json schemas.",
  "owner": "codex-asb-ar1757-human-output-20261009",
  "plan": "../plans/AR-1757-human-first-cli-output.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1757.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make default ASB CLI output concise, command-aware, self-explanatory, and actionable while preserving stable machine-readable output.",
  "task_revision": 3,
  "title": "Human-first ASB command output",
  "updated_at": "2026-10-09T12:56:56+00:00",
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
