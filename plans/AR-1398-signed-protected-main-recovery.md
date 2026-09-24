# AR-1398: Signed protected-main recovery after generated merge

## Scope

Recover the signed+DCO publication boundary after protected main accepted
PR #286 as GitHub-generated merge `123ba915d2732ee8a6c99fae301bfd64cf0aac4f`.
Preserve that merge and its seven successful post-merge workflow records as
historical evidence; do not rewrite or bless the unsigned commit. Create the
smallest signed descendant through the established local merge/integration
path, prove that its tree and ancestry preserve the reviewed repair, and run
fresh exact-main gates against that descendant.

## Acceptance

- The repair uses the existing signed local integration path and retains the
  required SSH signature and matching Signed-off-by trailer; no policy gate is
  weakened and no historical ref is replaced.
- Independent review verifies exact parent/tree ancestry, signature, DCO,
  privacy and scope. Hostile tests cover generated unsigned/DCO-less merges and
  reject false completion claims.
- All focused/full gates, exact-head checks, and all seven exact-main
  post-merge workflows for the signed descendant reach terminal success.
- AR-1314, AR-1395 and AR-1397 retain their original evidence and are closed
  only after this fresh recovery is verified.
