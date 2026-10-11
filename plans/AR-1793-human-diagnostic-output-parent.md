# AR-1793 plan: repair human diagnostic output-parent contract

1. Reproduce the exact failing human diagnostic test on protected-main baseline and the AR-1784 head, recording commit identities and output.
2. Identify the legacy output-parent branch and define stable public wording that names cause, observed state, and actionable recovery without private text.
3. Add positive coverage for the corrected wording and negative coverage preventing the generic no-state-change-only output for this diagnostic.
4. Run focused and unchanged full ASB CLI gates, formatter, clippy, rustdoc, privacy, and exact-diff checks through handoffctl.
5. Obtain independent exact-head review and integrate only through the protected signed-DCO workflow; unblock AR-1784 only after green evidence.

Scope is limited to the legacy human diagnostic contract; no gate weakening or unrelated registry changes.
