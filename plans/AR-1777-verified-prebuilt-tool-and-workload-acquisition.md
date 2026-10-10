# AR-1777 plan: verified prebuilt tool acquisition

1. Implement catalog-driven platform selection and verified compatible-system
   binary reuse without trusting ambient PATH identity alone.
2. Implement bounded official retrieval with time/size limits, immutable digest,
   declared signature/provenance verification, archive safety, and offline
   classification.
3. Publish verified tools atomically into project-local storage
   and persist the complete acquisition receipt in project configuration.
4. Preserve previous good installations through failed updates and provide
   precise diagnostics/remediation for every acquisition failure class.
5. Add local deterministic source-server fixtures and hostile archive/artifact
   tests; test no root, no arbitrary script, no secret persistence, and all
   supported platform selection outcomes.
