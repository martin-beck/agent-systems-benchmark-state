---
{
  "branch": "feature/ar-1305-image-native-user-session",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1304"],
  "id": "AR-1305",
  "next_action": "Promote after review; qualify dbus-user-session and systemd user-manager support in a fresh offline guest image, then hand the immutable image to AR-1304.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1305.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify image-native D-Bus user-session support for required TLC containment.",
  "task_revision": 1,
  "title": "Image-native user-session support",
  "updated_at": "2026-09-17T15:07:00+00:00",
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
