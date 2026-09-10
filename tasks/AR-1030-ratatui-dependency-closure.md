---
{
  "branch": "build/ratatui-dependency-closure",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:52:14+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1030",
  "next_action": "Resolve the exact Ratatui release dependency closure through a reviewed upstream feature or narrowly justified fail-closed policy decision.",
  "owner": "codex-ar1030-ratatui-policy-20260910",
  "plan": "../plans/AR-1030.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the maintained Ratatui release consumable by standalone asb-tui without hiding supply-chain exceptions.",
  "task_revision": 20,
  "title": "Resolve the Ratatui dependency closure",
  "updated_at": "2026-09-10T20:03:32+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ratatui-dependency-closure"
}
---
The exact Ratatui 0.30.2 graph is advisory-clean but fails the repository's zero-exception
supply-chain policy because it necessarily contains Zlib-licensed foldhash, hashbrown 0.16/0.17,
and syn 2/3. Resolve this visibly before AR-1010 adds a renderer.

- 2026-09-10T19:50:04+00:00: Claimed by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:50:21+00:00: Recorded command exit 0; command argv SHA-256
  7e0d0efe0ae08a4c308f06db576693eff2b55df1b1195c580afd000b6237ceef.

- 2026-09-10T19:52:14+00:00: Heartbeat by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:52:20+00:00: Recorded command exit 0; command argv SHA-256
  70c299ac34f80fb148951f6d687b81c0133841c6f66036e826bbc90974c0544e.

- 2026-09-10T19:52:41+00:00: Recorded command exit 0; command argv SHA-256
  cb54c6475fcaf9c988b46643c213a1b77cd1b8ed1bfe7d6a8102356c7f0369e7.

- 2026-09-10T19:53:11+00:00: Recorded command exit 101; command argv SHA-256
  e409e268e66f59053c6cd20940690d0e09eac3f60de24e38e2629e7a4361a927.

- 2026-09-10T19:53:29+00:00: Recorded command exit 0; command argv SHA-256
  076056546ce14cbf7b9647a94cf99017d780620e3677ae653b2cb5bc5cc14e7d.

- 2026-09-10T19:54:05+00:00: Recorded command exit 0; command argv SHA-256
  9943ddd4923917bb053c83f7782fec1994419775043b4cf9fb78576bcedc006e.

- 2026-09-10T19:54:56+00:00: Recorded command exit 0; command argv SHA-256
  8f2e42d256187d9d0fd1bae895503b9b4a321b008688badb7b0eccf873b1cb77.

- 2026-09-10T19:55:11+00:00: Recorded command exit 0; command argv SHA-256
  9943ddd4923917bb053c83f7782fec1994419775043b4cf9fb78576bcedc006e.

- 2026-09-10T19:56:12+00:00: Recorded command exit 0; command argv SHA-256
  913e1e1a99f1a1f0601e06b33726299a3fb54fd4c3be66f8cb5b36d654161349.

- 2026-09-10T19:56:50+00:00: Recorded command exit 1; command argv SHA-256
  5d8fa64d1b08568dbf52607648ff129ed525244547b1fcb1c5fdbd5497ee211a.

- 2026-09-10T19:57:03+00:00: Recorded command exit 0; command argv SHA-256
  640948d3f18fb76c7fe74848a9e4afa459231e5623ddc6c817129b5f2c1eb132.

- 2026-09-10T19:57:42+00:00: Recorded command exit 0; command argv SHA-256
  2aa6b014e73a1bb170294bbe0e5ef4716cc88fded01fb11ee6badeda1c1fb60c.

- 2026-09-10T19:59:34+00:00: Recorded command exit 0; command argv SHA-256
  21dc06e7209084658fa85892384918c10e444fe737770961bc46c7b7e0d1d2c3.

- 2026-09-10T19:59:55+00:00: Recorded command exit 0; command argv SHA-256
  c00112b64e784a7f4c698089805699206b77ba008b8f8024af0860840648e28f.

- 2026-09-10T20:01:29+00:00: Recorded command exit 0; command argv SHA-256
  7fa82e8765053a59560320decb8682195ac34e596f504a383b823a524af265d1.

- 2026-09-10T20:02:45+00:00: Recorded command exit 0; command argv SHA-256
  e12d2eed605135b4e139f5ba5486133e68b97142a812d8111c8b8a27fbf799b4.

- 2026-09-10T20:03:32+00:00: Recorded command exit 0; command argv SHA-256
  d5782c4543cb8abf62435db0be5de407bfd9ec83ab23673101317c8f991b18ea.
