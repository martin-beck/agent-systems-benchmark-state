---
{"branch":"feature/containerized-runner-boundary","checkpoint_commit":"","claim_expires":"","depends_on":["AR-0835","AR-0836"],"id":"AR-0837","next_action":"Define and qualify a digest-pinned workflow container boundary separating operator, listener, and job principals without host mounts.","owner":"","plan":"../plans/AR-0837.md","priority":"P0","schema_version":1,"status":"planned","summary":"Provide the containerized workflow boundary required for safe trusted runner claims.","task_revision":1,"title":"Qualify containerized runner boundary","updated_at":"2026-09-07T00:00:00+00:00","worktree_key":"agent-systems-benchmark-containerized-runner-boundary"}
---
## AR-0837

Separate operator root, runner listener service, and workflow job principals using a reviewed,
digest-pinned container runtime. Reject host mounts/options that expose credentials, control files,
installation, or diagnostics. Prove identity separation, network/filesystem limits, tamper resistance,
interruption cleanup, and reproducible image provenance before trusted workflow dispatch.
