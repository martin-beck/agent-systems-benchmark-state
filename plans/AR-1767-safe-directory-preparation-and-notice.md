# AR-1767 plan: safe directory preparation and notice

1. Classify every path as input-only, caller-owned existing root, or ASB-owned
   output destination. Cover setup, config/auth, project init, easy lifecycle,
   tool install/registry, catalogs, plan output, execution/results, reports,
   record/replay artifacts, and routed TUI lifecycle state.
2. Define one safe directory-preparation primitive with resource role, required
   mode, ancestor policy, symlink/replacement checks, created/reused result, and
   fine-grained typed failures. Do not blindly recurse across trust boundaries.
3. Before the first directory mutation in human mode, emit one bounded message
   such as `ASB will create directory <PATH> for <PURPOSE>.` on stderr. Quote and
   sanitize the local path without exposing secrets; keep JSON stdout unchanged.
4. Make eligible commands create safe missing parents themselves. Keep inputs
   fail-closed and preserve atomic installation, cleanup, fsync, permissions,
   and concurrent-writer behavior.
5. Test dry-run, first/repeat run, nested parents, non-directory, permission,
   read-only, symlink, replacement race, partial creation, and cleanup, including
   exact path-specific messages and unchanged machine contracts.
6. Update setup/project/tool and workflow documentation so users are never told
   to create an ASB-owned directory manually.

