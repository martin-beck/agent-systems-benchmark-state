# AR-1520 plan: qualify the reduced development profile in a disposable VM

1. Build a self-contained disposable x86_64 guest fixture from the exact
   AR-1519 state commit, with a locally generated unsigned-development seed,
   preloaded pinned TLA+ JAR, no network interface, and the explicit
   `development-reduced` resource contract.
2. Run the guest through the state handoff tool with a finite outer timeout
   shorter than the profile bound plus boot allowance. Capture only sanitized
   markers: transient admission, model outcome, cleanup, and the explicit
   `qualification_authorized=false` non-claim.
3. Verify that missing, altered, or full-tier attestation files fail closed;
   a reduced result must never be accepted as AR-1307/AR-1308 formal evidence.
4. Independently inspect the exact state head, focused/full tests, VM command
   boundary, and sanitized evidence. Leave this AR blocked if the reduced
   profile cannot terminate within its explicit bound.

No external provider, signing authority, reviewed seed digest, or native ARM
host is required for this development qualification. This AR cannot change
the full-tier resource limits or release gates.
