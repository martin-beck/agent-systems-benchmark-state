# AR-1780 plan: installed tool and workload execution qualification

1. Create deterministic fresh-project fixtures representing verified system,
   official prebuilt, source-built dependency closure, and workload bundle paths.
2. Install/select every AR-1781 development workload through the public
   supported-ID command and prove the run/sweep path consumes exact project-local
   identities, not ambient tools; use controlled development backends where needed.
3. Exercise report/compare/recording identity propagation and offline-after-
   install behavior.
4. Exercise update/repair/remove, stale/revoked/mismatch rejection, interrupted
   installation, failed build, and benchmark-vs-installer error distinctions.
5. Run applicable exact-head and exact-main gates with privacy-safe receipts and
   independent review.
