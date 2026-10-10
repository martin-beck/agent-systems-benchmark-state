# AR-1782 plan: verified asb workload installation

1. Add the dedicated public `asb workload` lifecycle parser, including select,
   separate from `asb tool`.
2. Implement catalog-only primary-source retrieval, identity/proof/license/size
   validation, archive safety, bounded preparation, adapter-ready validation,
   atomic project-local publication, and receipts.
3. Implement network-free list/status/remove, explicit repair/update, retained
   prior-good versions, cache/offline behavior, and project-root confinement.
4. Add deterministic official-source fixtures for every AR-1781 suite, including
   SWE-mini, plus hostile archive/proof/license/preparation/rollback tests.
   Production authorization or hosted qualification absence must not make a
   development fixture unavailable.
5. Test human/JSON/quiet output boundaries and independent exact-head review.
