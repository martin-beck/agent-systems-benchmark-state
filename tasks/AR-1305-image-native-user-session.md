---
{
  "branch": "feature/ar-1305-image-native-user-session",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T15:47:14+00:00",
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
  "task_revision": 35,
  "title": "Image-native user-session support",
  "updated_at": "2026-09-17T15:18:13+00:00",
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

- 2026-09-17T15:12:48+00:00: Recorded command exit 1; command argv SHA-256
  89f4d6beee413945344b533e0ec7ff2385d4694117f259076fc5893eeb39a855.

- 2026-09-17T15:13:03+00:00: Recorded command exit 1; command argv SHA-256
  97d4ce142e20c933433fd5827845597f1b490978a0c7c4b28add66f4d7c4e8e4.

- 2026-09-17T15:13:21+00:00: libguestfs-tools installation completed (1:1.52.0-5ubuntu3), and a
  fresh root copy ar1305-root-fresh.qcow2 was created without mutating stale input. virt-customize
  failed before modification: /usr/bin/supermin exited status 1; no fresh image package injection or
  transient qualification occurred. The retry command also confirmed this tool version lacks the
  attempted inspection option. Next action: repair/qualify libguestfs supermin appliance (capture
  full LIBGUESTFS_DEBUG/TRACE privately), then rerun virt-customize on the fresh copy and record
  resulting image hash/provenance.

- 2026-09-17T15:13:47+00:00: Use qemu-nbd/manual offline image customization or repair supermin;
  qualify fresh root image without mutating backing

- 2026-09-17T15:13:50+00:00: Claimed by codex-ar1305-image-session-20260917.

- 2026-09-17T15:14:04+00:00: Recorded command exit 1; command argv SHA-256
  fd708b4f451ba3a1b3ebfea9e97a1367d0ec95c2bfc0c82b74510405f02b505f.

- 2026-09-17T15:14:36+00:00: Recorded command exit 0; command argv SHA-256
  3562a92a4f4a224cc3f6ad062b3efc0cbab95ac7a351a2bf19d3f739bb624e51.

- 2026-09-17T15:14:54+00:00: Recorded command exit 0; command argv SHA-256
  79ebd228c33b3c9cda0b92f3251b95078286ca487efc153edf57b644fa11d1bd.

- 2026-09-17T15:15:21+00:00: Recorded command exit 1; command argv SHA-256
  a84845cae15e461443214f3e43857da87db588b0e476c0f8f4a42ea166e839fa.

- 2026-09-17T15:15:34+00:00: Recorded command exit 0; command argv SHA-256
  e17a0083ae595e1a9e19b6def41c66928d6f1dc232298af32998b0f5e3144284.

- 2026-09-17T15:16:22+00:00: Recorded command exit 0; command argv SHA-256
  0b0da33192399030b53c5df92c3ce304ba522e5a6cc5a2684898c5f11d7636e2.

- 2026-09-17T15:16:52+00:00: Fresh root image successfully built without mutating stale input:
  ar1305-root-fresh.qcow2 SHA256 1a5db8d846d71588bbebdcaa0fffc708cde5a7aaf6feaca269bafc37aac13cce,
  injected dbus-user-session 1.14.10-4ubuntu4.1 from pinned package SHA e585b169... using sudo
  virt-customize. Fresh QEMU boot still fails required transient with Transport endpoint is not
  connected under the existing seed; package presence alone does not repair image-native
  user-manager transport. No required attestation. Next action: build a seed using the image-native
  dbus-user-session socket/user-manager activation (not standalone custom dbus service), then retry
  AR-1304.

- 2026-09-17T15:17:11+00:00: Fresh root image with dbus-user-session is built; now qualify
  image-native user-session activation path

- 2026-09-17T15:17:14+00:00: Claimed by codex-ar1305-image-session-20260917.

- 2026-09-17T15:17:42+00:00: Recorded command exit 0; command argv SHA-256
  22fa2122a4866c3bdd923877373b9ee30fa29e3f8633dd0004d8ac9c7ac79945.

- 2026-09-17T15:17:54+00:00: Recorded command exit 0; command argv SHA-256
  f321dd784b48b79bd8d2c316921d40566d7ea2361e52c7360f2bf43f1a516113.

- 2026-09-17T15:18:03+00:00: Recorded command exit 0; command argv SHA-256
  01b7773ff6a5df6f2c352a830ebb12c90e42979a04fa08480d075a11eb36676c.

- 2026-09-17T15:18:13+00:00: Recorded command exit 0; command argv SHA-256
  5169da931ba9f4a5d14c53d02d7a05050af65b37c80e14e157ce09ec2aa740be.
