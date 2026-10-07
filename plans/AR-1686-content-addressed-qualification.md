# AR-1686 content-addressed qualification repair

## Scope

Repair the AR-1613/quickstart qualification runner so it uses the repository
owned `asb plan create` flow rather than hand-authored or stale plan documents.
The generated plan must carry the selected configuration, workload, executable
and architecture identity and remain valid through run, cassette recording,
strict offline replay, and comparison.

## Acceptance

- A fresh exact-head install and wizard setup generate a valid plan without an
  API key, with an explicit development-only authentication warning.
- `plan --use-config`, local/mock execution, recording, replay, and comparison
  succeed for at least one selected workload and agent.
- Stale experiment digest and executable/workload mismatch cases fail closed.
- The receipt records exact ASB/TUI heads, plan and experiment digests, run and
  cassette artifacts, comparison output, and a no-secret scan.
- Hosted CI, independent review, and exact-head post-merge verification pass.
