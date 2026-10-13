# AR-1843 plan: hosted formal workspace permission repair

1. Reproduce PR #142 run 38379221269's permission failure and inspect the
   self-hosted runner account and approved second-disk root.
2. Add a bounded workflow initialization step and explicit `TLC_WORK_ROOT`
   under `/srv/data/projects/.asb-tlc`, with private per-run permissions and
   no fallback to an interactive user's `/tmp` directory.
3. Add positive and negative regression coverage for the workspace contract,
   then run the complete state quality gates and live doctor.
4. Independently review the complete diff, publish a signed DCO PR, wait for
   exact-head CI, merge only after all required checks are green, and verify
   exact-main formal and coordination workflows.
5. Requalify dependent AR-1841 PR #142 against the repaired main and retain
   the original infrastructure-failure evidence as diagnostic context.

Do not weaken TLC, attestation, privacy, schema, signature, DCO, or exact-head
requirements. The repair changes only runner workspace setup.
