---
{
  "id": "AR-1591",
  "title": "Post-release fresh-clone ASB consumption qualification",
  "priority": "P0",
  "depends_on": ["AR-1589", "AR-1590"],
  "summary": "Verify a fresh user can consume the released ASB dev channel and complete the paired TUI setup and benchmark journey.",
  "status": "planned"
}
---

After the exact inherited-fd bridge and provenance/fault work are released,
validate from fresh temporary clones that ASB dev-channel install, bootstrap,
provider/model/default projection, broker launch, recording, replay, and
comparison work with the pinned TUI. Record exact release identities and
artifacts, including unavailable/development provenance. No live provider or
production secret is required; stable routes must remain fail-closed.
