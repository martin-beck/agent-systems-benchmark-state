---
{
  "branch": "feature/ar-1326-openrouter-catalog-selection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0313",
    "AR-1325"
  ],
  "id": "AR-1326",
  "next_action": "Add the openrouter profile entry to provider_catalog and provider_catalog_digest, accept it in provider_plan and validate_provider_selection, and bind plans to the pinned OpenRouter model identity.",
  "observed_branch": "feature/ar-1326-openrouter-catalog-selection",
  "observed_dirty": 5,
  "observed_head": "a4934fca0b528ac90d09fb537936584f5af0f75e",
  "owner": "",
  "plan": "../plans/AR-1326.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Advertise the OpenRouter profile in the CLI provider catalog and accept it in provider-plan selection.",
  "task_revision": 3,
  "title": "Select OpenRouter through the CLI provider catalog",
  "updated_at": "2026-09-22T14:44:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1326-openrouter-catalog-selection"
}
---

The closed `asb provider-catalog` output only advertises `openai` as selectable
and `provider-plan` rejects any other profile, so the AR-1325 OpenRouter profile
cannot be selected end to end. This AR extends the CLI catalog identity and the
selection path: `provider_catalog`, `provider_catalog_digest`, `provider_plan`
and `validate_provider_selection` gain the `openrouter` profile with its pinned
model, the selection manifest carries the OpenRouter provider profile, and the
plan/experiment binding accepts the OpenRouter model identity without weakening
the fail-closed content-address checks.
