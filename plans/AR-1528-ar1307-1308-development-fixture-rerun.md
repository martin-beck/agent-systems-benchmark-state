# AR-1528 plan: rerun corrected development fixtures

1. Use the exact merged product head and the `unsigned-development` profile.
2. Generate disposable local seeds at runtime; do not read or require a
   reviewed seed digest, signed bundle, or external provider.
3. Exercise positive and negative fixture cases, bounded timeout/OOM cleanup,
   admission fencing, network denial and sanitized evidence.
4. Confirm `qualification_authorized=false` and that formal AR-1307/1308
   qualification remains blocked independently of this diagnostic result.
5. Run focused and full applicable gates, review the complete diff, and record
   exact commands and terminal outcomes through handoffctl.
