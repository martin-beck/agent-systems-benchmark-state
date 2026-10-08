# AR-1745 plan: user-local ASB installation prefix

1. Audit the current ASB `make install` target and every equivalent ASB
   binary-install path, including any `asb install` wrapper, against the exact
   protected main head. Identify whether a shared prefix contract is needed.
2. Change the development/default install destination to the invoking user's
   `$HOME/.local`, with the executable at `$HOME/.local/bin/asb`. Preserve an
   explicit, validated `PREFIX` override for packaging and CI; never require
   root privileges or write to `/usr/local` by default.
3. Keep staging, build, test, update, release, uninstall, and TUI materializer
   paths bounded and explicit. Do not make the TUI or runtime depend on Make.
   Ensure `$HOME` is resolved for the invoking user, not a hard-coded host
   account, and reject empty, relative, or unsafe prefixes.
4. Add deterministic tests using a disposable HOME/prefix that prove the
   default binary location, idempotent reinstall, explicit-prefix behavior,
   no writes outside the prefix, and actionable PATH guidance. Cover the
   corresponding `asb` path if it shares the install implementation.
5. Independently review the complete diff, run focused and full applicable
   gates, publish a signed+DCO PR, merge only through the documented signed
   integration path, and record exact-main post-merge evidence before release.

Development mode must remain warning-only for missing authentication,
signatures, and key management; this AR concerns filesystem installation
location only and must not introduce a security or release-channel bypass.
