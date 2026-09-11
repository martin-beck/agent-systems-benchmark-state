---
{
  "branch": "fix/tmux-alternate-screen-readiness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T02:43:01+00:00",
  "depends_on": [],
  "id": "AR-1042",
  "next_action": "Reap the exact owned tmux pane process group on every guard cleanup path, prove no process/socket leaks, then amend and rerun all gates.",
  "owner": "codex-ar1042-tmux-readiness-20260911",
  "plan": "../plans/AR-1042.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make tmux TUI readiness validate the displayed alternate screen deterministically.",
  "task_revision": 48,
  "title": "Capture alternate-screen TUI readiness deterministically",
  "updated_at": "2026-09-11T01:09:27+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-alternate-screen-readiness"
}
---

Trusted-main run 34546963576 failed twice in a tmux readiness probe influenced by ambient server
configuration. An exact tmux 3.4 probe established that `capture-pane -p` returns the displayed
live alternate-screen frame while `-a` returns blank alternate-history storage in this state. Use a
clean tmux server, bracket displayed-pane capture with exact `alternate_on=1` observations, and
emit bounded diagnostics; do not change renderer or application semantics.

- 2026-09-11T00:41:41+00:00: Two exact trusted-main failures require a narrow deterministic
  readiness repair; the later exact tmux probe supersedes the initial primary-buffer diagnosis.

- 2026-09-11T00:43:01+00:00: Claimed by codex-ar1042-tmux-readiness-20260911.

- 2026-09-11T00:43:22+00:00: Recorded command exit 0; command argv SHA-256
  83409219a9e7ea09f493ce285302d7c8843b7d29b0bb21d901a7c2464c5d0747.

- 2026-09-11T00:46:29+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-11T00:48:12+00:00: Recorded command exit 0; command argv SHA-256
  db2ee2b39362825df0221f791541c492ad3abaa1c4cc698692fe768476d6f6e8.

- 2026-09-11T00:48:53+00:00: Recorded command exit 0; command argv SHA-256
  41eeb93aed6ccfe2f35024f7139be47ccabccc1164ccf6ff6381031b79230930.

- 2026-09-11T00:49:23+00:00: Recorded command exit 0; command argv SHA-256
  17287eda611d2be781e2f2d18fe9678306860102ea53a39839da73e6a1dd7800.

- 2026-09-11T00:49:37+00:00: Recorded command exit 127; command argv SHA-256
  1173f7418dd4dc8098924107f963619eb63574fb39852fcd6213f5b30498431c.

- 2026-09-11T00:50:00+00:00: Recorded command exit 101; command argv SHA-256
  b2c5d4bc5bc591f6bfe95677b0140cc9adcbec5c168bfbdd236ab51e0ab0c464.

- 2026-09-11T00:50:40+00:00: Recorded command exit 0; command argv SHA-256
  0cc44239b5ab5b9f0ac4556966a5c32470238c9f86a742ba5f28ca57f67b9162.

- 2026-09-11T00:51:23+00:00: Recorded command exit 0; command argv SHA-256
  49c263e45fd152d74642252710b9d260f6f32b9daddaeee262a39452ca85e38c.

- 2026-09-11T00:51:42+00:00: Recorded command exit 0; command argv SHA-256
  b2c5d4bc5bc591f6bfe95677b0140cc9adcbec5c168bfbdd236ab51e0ab0c464.

- 2026-09-11T00:52:01+00:00: Recorded command exit 1; command argv SHA-256
  0bf9b8bff07ba0dee0f3d231eb9601ca051daece295b9bccc93b8f1284b8e453.

- 2026-09-11T00:52:15+00:00: Recorded command exit 0; command argv SHA-256
  cf24195e46a0da051f46eb4cfac9ea2849e183af4478cd17eefaa89277a05ebf.

- 2026-09-11T00:53:07+00:00: Recorded command exit 1; command argv SHA-256
  f5258d2e35428ba55a37283244902b4bb384053f1d68c7b1140a8d7ce0233600.

- 2026-09-11T00:53:44+00:00: Recorded command exit 0; command argv SHA-256
  afcf9a09a29154fd7c71dd4ae195ab04773779b01f86928226deb7daeece5d01.

- 2026-09-11T00:54:16+00:00: Recorded command exit 0; command argv SHA-256
  8cd460aae30f1e39fb6fda77044f38e316d405badb81377ff2e9011dd81426fc.

- 2026-09-11T00:54:40+00:00: Empirical tmux 3.4 probe corrected the capture model: capture-pane -p
  returned the displayed live alternate frame, while -a returned blank alternate-history storage.
  Readiness now requires valid recognized UTF-8 content bracketed by exact alternate_on=1
  observations.

- 2026-09-11T00:55:15+00:00: Recorded command exit 0; command argv SHA-256
  35f99fd9798f9f4cd4ce2999262058b80149389f04814457616e69c4694abeb7.

- 2026-09-11T00:55:46+00:00: Recorded command exit 0; command argv SHA-256
  b2c5d4bc5bc591f6bfe95677b0140cc9adcbec5c168bfbdd236ab51e0ab0c464.

- 2026-09-11T00:56:06+00:00: Recorded command exit 0; command argv SHA-256
  aa269d267d3ef5a90fb15e1db95aece22e0e618f86e74e42e6a3e59d28e07e9e.

- 2026-09-11T00:56:23+00:00: Recorded command exit 1; command argv SHA-256
  1d1fc70393266bff6591e29fc7eee915c807edfb2ce86bed4b0e583a159d82ff.

- 2026-09-11T00:56:39+00:00: Recorded command exit 0; command argv SHA-256
  cf24195e46a0da051f46eb4cfac9ea2849e183af4478cd17eefaa89277a05ebf.

- 2026-09-11T00:57:12+00:00: Recorded command exit 0; command argv SHA-256
  bb5593af06374506f81584540700ccca593fb268f1695eacaedf44ff9cf54920.

- 2026-09-11T00:57:30+00:00: Recorded command exit 0; command argv SHA-256
  a66ceb08337d8bbd43745156c15eccc2e4115111f1b2fd1328a42e788e4d19a5.

- 2026-09-11T00:58:18+00:00: Recorded command exit 0; command argv SHA-256
  cd9e1a1b914ae34b2e1d85c7969b579cc0a4e932dd797d3e47e9befca9c012f8.

- 2026-09-11T00:58:49+00:00: Recorded command exit 0; command argv SHA-256
  721c0c9b639bdb380a010986634c5268dbfb6d26b61becee950a260d94e6f6ef.

- 2026-09-11T00:59:58+00:00: Recorded command exit 0; command argv SHA-256
  3c274358adf44508b6f83b27d4fe7c1affea8a492af3a8e79bdb104bd401b127.

- 2026-09-11T01:00:47+00:00: Recorded command exit 0; command argv SHA-256
  b43926b1d55c10be842099265bdc9ba9ff0ff88cf9b092ded1585c6ddf85ee91.

- 2026-09-11T01:01:03+00:00: Recorded command exit 1; command argv SHA-256
  b2ecd06f0d8b01c23483e72c3038ba783babfa222a250885e0eb8348e374906c.

- 2026-09-11T01:01:33+00:00: Recorded command exit 0; command argv SHA-256
  d672a070849f36a3e50088d9d81b908a9833220ca5c6779111e304393893d8cf.

- 2026-09-11T01:01:47+00:00: Recorded command exit 0; command argv SHA-256
  fbf355966da715b0fa31c58af2353b582a78e08e634938fa6689f8ce553d25e2.

- 2026-09-11T01:02:16+00:00: Recorded command exit 1; command argv SHA-256
  6a5bc909d540c9ede29293da2547bcee5591cf16b0688be87bf9c49684a8f26f.

- 2026-09-11T01:03:25+00:00: Recorded command exit 0; command argv SHA-256
  b1bee2c751498d4bd37f34bedcfa7125c125cc95a3e14e3840032d5d5c89e379.

- 2026-09-11T01:03:46+00:00: Recorded command exit 0; command argv SHA-256
  9105aca52d5f3104729e825e92eb9f3849715d88f82a1412a6ae504b2633dcd1.

- 2026-09-11T01:04:20+00:00: Recorded command exit 0; command argv SHA-256
  545f88059381a271c392abc51e1734196de2e0b30a6a46172eb7c2a3743812b5.

- 2026-09-11T01:04:54+00:00: Leak audit found the failed readiness path could kill only the tmux
  server and orphan a HUP-resistant asb-tui pane group. Three exact historical groups were
  identity-checked, terminated and verified gone. The test guard now owns the validated pane PGID
  and performs bounded TERM/KILL cleanup; runtime hangup behavior remains a separate follow-up
  concern, not a renderer change in AR-1042.

- 2026-09-11T01:05:30+00:00: Recorded command exit 0; command argv SHA-256
  b516144bfbe79c28045b0ec6f4c15a9faea4d19e0d7deaf4790cf337be5848d9.

- 2026-09-11T01:05:53+00:00: Recorded command exit 0; command argv SHA-256
  d672a070849f36a3e50088d9d81b908a9833220ca5c6779111e304393893d8cf.

- 2026-09-11T01:06:13+00:00: Recorded command exit 0; command argv SHA-256
  ef7f6c1489788a54321a2d531528efb93ec0e1c560b69094c57c1cd96635dad8.

- 2026-09-11T01:06:46+00:00: Recorded command exit 0; command argv SHA-256
  d5b7d23c58a0d55365927d1b0b92c6d53120452d822284c546c31ffc19946f29.

- 2026-09-11T01:07:22+00:00: Recorded command exit 0; command argv SHA-256
  c1054a92fb7e7e2a3101b3306c6e27fa325d5c0ab20f15e2c6f242cced3c436e.

- 2026-09-11T01:07:43+00:00: Recorded command exit 0; command argv SHA-256
  01f6eef52960ee1e5fadbc3633fbf456c6705adcc95a797b7cc601d21a6fa60d.

- 2026-09-11T01:08:05+00:00: Recorded command exit 101; command argv SHA-256
  847179a36c6d1d1a46d87bd67b46399367e5ebf50c17bcedbdb744ebbaec95b7.

- 2026-09-11T01:08:36+00:00: Recorded command exit 0; command argv SHA-256
  397b0e5b659858a72881f1c23b25b542c80cd9f344777460b020083b8dfcad55.

- 2026-09-11T01:09:13+00:00: Recorded command exit 0; command argv SHA-256
  ced83376d55af1489e46df0c0d21a3176130ec90d425d13544662b187316c3e0.

- 2026-09-11T01:09:27+00:00: Recorded command exit 0; command argv SHA-256
  d672a070849f36a3e50088d9d81b908a9833220ca5c6779111e304393893d8cf.
