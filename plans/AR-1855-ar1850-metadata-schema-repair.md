# AR-1855 plan: AR-1850 coordination metadata schema repair

1. Validate the exact malformed `observed_dirty: false` field against the
   published task schema and preserve the intended zero-dirty observation.
2. Change only AR-1850's coordination metadata from boolean `false` to integer
   `0`; do not claim the task or touch ASB launcher source.
3. Add focused positive and hostile schema tests proving integer dirty counts
   are accepted and booleans are rejected.
4. Run handoffctl validation, independent review, signed-DCO publication, exact
   required CI, merge, and post-merge state validation.
