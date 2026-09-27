# AR-1493: Release-authority enrollment and verification handoff

## Objective

Document and, where safe, validate the repository-side handoff needed for an
authorized operator to sign an ASB runtime bundle. This slice makes the exact
principal, allowed-signers input, SSHSIG namespace, trusted `ssh-keygen`
identity, digest, verifier invocation, and post-signature checks explicit. It
does not create or assume a private key, signature, signer identity, or release
authority.

## Dependencies

AR-1461 and AR-1462 provide the release and pinned bundle contracts. AR-1491
provides the credential-free verifier fixture and AR-1492 provides the
deterministic staging and external-signing handoff. AR-1490 remains blocked on
the real authorized signed customer package and is not replaced by this task.

## Acceptance

- The handoff names the exact SSHSIG namespace `asb-runtime-bundle-v1`, the
  operator-supplied principal, the allowed-signers file contract, the trusted
  `ssh-keygen` path and SHA-256, and the bounded verifier command.
- Repository-side checks/docs reject missing, mismatched, or placeholder
  authority inputs and distinguish staged unsigned material from a signed
  customer release.
- Positive and negative local/mock tests validate handoff shape, signature
  namespace/principal binding, signer-file and tool-digest mismatch, and the
  required post-signature offline verification. No network, credentials, live
  provider, private paths, or raw signature material are retained in evidence.
- The operator procedure explains provisioning and independent validation of
  the detached signature without generating authority in ASB. Actual customer
  release remains blocked until an authorized external signer supplies and
  validates the exact signature.
- Applicable formatting, tests, docs, policy, coverage, release, signed/DCO,
  exact-head CI, and post-merge gates pass if product changes are required.

## Explicit boundary

This is an enrollment/verification handoff, not a release. An absent external
principal, allowed-signers file, trusted tool digest, or detached signature is
an honest unavailable input; it must never be replaced by a generated test key
or unsigned acceptance claim.
