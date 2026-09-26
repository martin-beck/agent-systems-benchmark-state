# AR-1465: Reviewed full-exhaustive seed archival recovery

## Required work

1. Read the complete AR-1464, AR-1307 and AR-1308 tasks and plans plus the
   state development and formal-runner documentation.
2. Locate the previously reviewed full-exhaustive seed through approved,
   durable archives or signed state artifacts only. The required byte digest
   is exactly
   `b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28`.
   Search evidence may include remote state history, retained runner backups,
   and operator-provided archival media, but must not expose private paths or
   credentials in durable evidence.
3. Verify the recovered bytes independently, preserve them under
   `/srv/data/projects`, and bind the path and digest to AR-1308 through the
   state workflow. Reject regenerated, reserialized, unsigned, or merely
   semantically equivalent seeds.
4. If no approved archive contains the exact bytes, record the complete
   search scope and leave this AR blocked. Do not change the seed digest,
   formal model, resource limits, or admission gates.
5. Run the signed AR-1308 preflight only after the exact seed and existing
   capacity inputs are present. Do not boot QEMU/TLC in this AR.

## Acceptance evidence

- exact seed bytes with the required SHA-256 and provenance from an approved
  reviewed archive;
- independent digest verification and privacy-safe durable receipt;
- AR-1308 preflight passes the seed gate without changing any formal contract;
- if unrecoverable, a precise blocked record naming every searched archive and
  the external evidence needed to proceed.

## Boundaries

This AR owns archival recovery only. It does not modify ASB product source,
asb-tui, handoffctl, formal limits, or release policy, and it does not claim
formal qualification or customer-release readiness.
