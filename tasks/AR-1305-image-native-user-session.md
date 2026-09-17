---
{
  "branch": "feature/ar-1305-image-native-user-session",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T15:40:53+00:00",
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
  "task_revision": 17,
  "title": "Image-native user-session support",
  "updated_at": "2026-09-17T15:12:36+00:00",
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

- 2026-09-17T15:09:06+00:00: Recorded command exit 0; command argv SHA-256
  4e9ac7800433cc02a5ed096741f0ac7325028183abd54dcd1d023c3b8b4eef81.

- 2026-09-17T15:09:33+00:00: Recorded command exit 0; command argv SHA-256
  41a9a5f50271c2865a90821653b1f17b90bb227726fd52d456d98b8bab8a005e.

- 2026-09-17T15:09:45+00:00: Recorded command exit 0; command argv SHA-256
  98abdcf4266ae0e961d5c00015bd88e1919a117724f7fcfad5684b7bf14a846a.

- 2026-09-17T15:10:02+00:00: Successfully staged dbus-user-session 1.14.10-4ubuntu4.1 under project
  storage; SHA256 e585b1694b854c3b75bfb39cc4022cafe7b14e44fd435433b613b8fb9919cb41. Fresh immutable
  image construction remains blocked: only qemu-img is available; guestfish, virt-customize, and
  debootstrap are unavailable, so the stale qcow2 cannot be safely modified. No image-native
  transient qualification produced. Next action: provide an approved offline root-image
  customization tool or prebuilt immutable image pipeline, then install this exact package and rerun
  required transient qualification.

- 2026-09-17T15:10:51+00:00: Install image customization tooling and build fresh root image from
  staged dbus-user-session package

- 2026-09-17T15:10:53+00:00: Claimed by codex-ar1305-image-session-20260917.

- 2026-09-17T15:11:47+00:00: Recorded command exit 2; command argv SHA-256
  5165bde12ea5cf2469cd57dbc3066886bf408a467adcfb7c7311180f73990d4c.

- 2026-09-17T15:11:57+00:00: Recorded command exit 0; command argv SHA-256
  b1108df6f9936ae45f793a7ef21d4c9cdf301bd4df32e97c6f0977b515f5884f.

- 2026-09-17T15:12:36+00:00: Recorded command exit 0; command argv SHA-256
  e383275f0f6b9a6486899ffac6ab3729eae7d19f23074bf2079305334d73aaab.
