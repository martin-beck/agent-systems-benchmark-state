---
{
  "branch": "feature/ar-1776-supported-tool-acquisition-catalog",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1761", "AR-1762"],
  "id": "AR-1776",
  "next_action": "Define the authoritative supported executable-tool acquisition catalog, official primary sources, binary/source alternatives, verification identities, and build recipes.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1776-supported-tool-acquisition-catalog.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1776.json", "spec_revision": 2, "status": "pending"},
  "spec_ref": "specs/AR-1776.json",
  "spec_revision": 2,
  "status": "planned",
  "summary": "Define pinned official acquisition and build recipes for every ASB-supported executable tool.",
  "task_revision": 2,
  "title": "Supported-tool acquisition catalog",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1776-supported-tool-acquisition-catalog"
}
---

Replace the current local-file-only installer input with an authoritative,
versioned acquisition catalog for every ASB-supported agent, harness, benchmark,
and support tool. Installable workload bundles belong exclusively to the separate
`asb workload` series. Each tool entry names its official
primary distribution/source, supported platform tuple, exact version/revision,
immutable artifact/source identity, digest and signature/provenance verifier when
available, executable entrypoint, license, and one or more bounded
build recipes. It must distinguish a reusable verified system binary, an
official prebuilt artifact, and a source-build fallback.

The catalog is the sole authority behind `asb tool install <supported-id>`;
the default command must not require a user-supplied local source. It may use a
locally present compatible tool only after it validates the same identity and
records that reuse. Unsupported targets, unavailable official artifacts, missing
verification material, incompatible licenses, and unavailable build recipes are
typed actionable outcomes, not a reason to invoke arbitrary package managers or
shell installers. Keep credentials out of records.

The initial catalog inventory must cover the supported executable-agent IDs
`aider`, `codex`, `gemini`, `goose`, `mini-swe`, `opencode`, `opendesk`,
`openhands`, `openjiuwen`, and `qwen-code`; the development-only `cli2key`
bridge/sidecar when enabled; and optional monitoring executables `perf` and
`bpftool`. It must distinguish provider APIs (OpenAI, OpenRouter, Ollama) from
installable executables. Runtime host capabilities such as Linux, cgroup v2,
user systemd delegation, and Bubblewrap are declared by the companion command
dependency/preflight catalog rather than falsely represented as downloadable
tools.
