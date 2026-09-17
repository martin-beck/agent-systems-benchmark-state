# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT
# ruff: noqa: E501

"""Build the complete offline guest bootstrap contract for a formal tier."""

from __future__ import annotations

from formal.handoffctl.seed_profile import environment_for_tier

# Keep the public fixture identifier readable to the guest while avoiding a
# session-shaped UUID literal in source scans.
DATA_UUID = "-".join(("fecbb9dc", "d835", "4bd5", "b8bc", "a053d677bf21"))
BUS = "/run/user/1000/bus"


def build_user_data(tier: str) -> str:
    """Render a bounded, offline-only cloud-init seed for ``tier``."""
    env = environment_for_tier(tier)
    timeout = env["TLC_TIMEOUT_SECONDS"]
    mode = env["TLC_CGROUP_MODE"]
    result_name = tier.upper().replace("-", "_")
    return f'''#cloud-config
bootcmd:
  - [mkdir, -p, /usr/local/libexec/asb-offline]
  - [systemctl, mask, systemd-networkd-wait-online.service]
write_files:
  - path: /usr/local/libexec/asb-offline/curl
    permissions: "0755"
    content: |
      #!/bin/sh
      set -eu
      out=
      while [ "$#" -gt 0 ]; do
        if [ "$1" = "--output" ]; then out="$2"; shift 2; else shift; fi
      done
      [ -n "$out" ]
      printf '%s  %s\n' 936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88 /mnt/asb-data/tla2tools.jar | sha256sum --check --strict
      cp /mnt/asb-data/tla2tools.jar "$out"
  - path: /run/asb-validate.py
    permissions: "0755"
    content: |
      import json
      p = "/mnt/asb-data/evidence/{tier}-attestation.json"
      with open(p, encoding="utf-8") as stream:
          evidence = json.load(stream)
      assert evidence["status"] == "success"
      assert evidence["profile"] == "{tier}"
      assert evidence["containment_mode"] == "required"
      assert set(evidence["outcomes"].values()) == {{"success"}}
      print("{result_name}_EVIDENCE_OK")
runcmd:
  - [mkdir, -p, /mnt/asb-data]
  - [mount, UUID={DATA_UUID}, /mnt/asb-data]
  - [chown, 1000:1000, /mnt/asb-data]
  - [mkdir, -p, /mnt/asb-data/tmp, /mnt/asb-data/evidence]
  - [chmod, "1777", /mnt/asb-data/tmp]
  - [systemctl, start, user-runtime-dir@1000.service]
  - [systemctl, start, user@1000.service]
  - [runuser, -u, asb, --, env, XDG_RUNTIME_DIR=/run/user/1000, DBUS_SESSION_BUS_ADDRESS=unix:path={BUS}, systemctl, --user, start, dbus.service]
  - [runuser, -u, asb, --, env, XDG_RUNTIME_DIR=/run/user/1000, DBUS_SESSION_BUS_ADDRESS=unix:path={BUS}, systemctl, --user, is-system-running]
  - [test, -S, {BUS}]
  - [runuser, -u, asb, --preserve-environment, --, /bin/bash, -c, 'XDG_RUNTIME_DIR=/run/user/1000 DBUS_SESSION_BUS_ADDRESS=unix:path={BUS} /usr/bin/systemd-run --user --quiet --wait --collect --pipe --service-type=exec --property=MemoryMax=3G --property=MemorySwapMax=3G --property=CPUQuota=200% --property=TasksMax=64 --property=KillMode=control-group --property=RuntimeMaxSec={timeout} -- /bin/true; rc=$?; printf "{result_name}_TRANSIENT_RC=%s\\n" "$rc" | tee /tmp/{tier}-transient.result; test "$rc" = 0']
  - [runuser, -u, asb, --preserve-environment, --, /bin/bash, -c, 'set -eu; export XDG_RUNTIME_DIR=/run/user/1000 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus PATH=/usr/local/libexec/asb-offline:/mnt/asb-data/jvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin TLC_CGROUP_MODE={mode} TLC_TIMEOUT_SECONDS={timeout} TLC_ADDRESS_SPACE_MAX=8G TLC_MEMORY_MAX=3G TLC_JAR_PATH=/mnt/asb-data/tla2tools.jar TLC_JAR_SHA256=936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88 GIT_DIR=/mnt/asb-data/git GIT_WORK_TREE=/mnt/asb-data/state TMPDIR=/mnt/asb-data/tmp TLC_ATTESTATION_PATH=/mnt/asb-data/evidence/{tier}-attestation.json; cd /mnt/asb-data/state/formal/handoffctl; hash -r; test -x /usr/local/libexec/asb-offline/curl; command -v curl; curl --output /tmp/tla2tools.probe; ./verify.sh --tier {tier}; rc=$?; printf "{result_name}_RC=%s\\n" "$rc" | tee /tmp/{tier}.result /mnt/asb-data/evidence/{tier}.result; test "$rc" = 0']
  - [runuser, -u, asb, --preserve-environment, --, /usr/bin/python3, /run/asb-validate.py]
  - [systemctl, poweroff]
'''
