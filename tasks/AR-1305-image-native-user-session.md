---
{
  "branch": "feature/ar-1305-image-native-user-session",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T15:38:51+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1305",
  "next_action": "Promote after review; qualify dbus-user-session and systemd user-manager support in a fresh offline guest image, then hand the immutable image to AR-1304.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1305-image-session-20260917",
  "plan": "../plans/AR-1305.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify image-native D-Bus user-session support for required TLC containment.",
  "task_revision": 8,
  "title": "Image-native user-session support",
  "updated_at": "2026-09-17T15:08:51+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1305-image-native-user-session"
}
---

## AR-1305

AR-1304 has a green isolated QEMU and bus socket, but the image-native user
manager returns `Transport endpoint is not connected` for transient units. This
AR owns only the supported guest image/session dependency; required resource
limits and fail-closed behavior remain unchanged.

- 2026-09-17T15:07:00+00:00: Created from repeated AR-1304 required-tier
  transport failures; no portable fallback is authorized.

- 2026-09-17T15:06:59+00:00: AR-1302 done; image repair unblocks AR-1304

- 2026-09-17T15:07:01+00:00: Claimed by codex-ar1305-image-session-20260917.

- 2026-09-17T15:07:43+00:00: Heartbeat by codex-ar1305-image-session-20260917.

- 2026-09-17T15:07:48+00:00: Recorded command exit 0; command argv SHA-256
  ad1ed7ff263a54de81425f1be1569bf15d2356c5b428c57abc1f01328929e8b7.

- 2026-09-17T15:08:13+00:00: Host has dbus-user-session installed (1.14.10-4ubuntu4.1), but no
  offline dbus-user-session package artifact or image customization tool is available under
  /srv/data/projects to build a fresh immutable guest. Existing prepared qcow2 is stale and cannot
  be mutated/reused as provenance. No image-native transient qualification was produced. Next
  action: stage a reviewed dbus-user-session package/base-image artifact under project storage,
  build a fresh image, then prove user@1000/systemd-run transient success with all AR-1304 limits.

- 2026-09-17T15:08:48+00:00: Stage immutable dbus-user-session package/base artifact and build a
  fresh offline image; do not mutate stale qcow2

- 2026-09-17T15:08:51+00:00: Claimed by codex-ar1305-image-session-20260917.
