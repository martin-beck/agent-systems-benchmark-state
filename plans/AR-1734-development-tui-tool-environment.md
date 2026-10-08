# AR-1734 plan: bounded development TUI tool environment

1. Reproduce the installed `asb tui` launch failure from the exact paired
   AR-1713 receipt while keeping caller environment inheritance disabled.
2. Inventory the frontend's launch-time tool requirements and reuse the
   descriptor-bound Cargo/Rustc selection from AR-1726 plus the existing
   validated Git, setsid, compiler, and signature-tool policy.
3. Construct a minimal development-only tool environment. Do not forward the
   caller PATH wholesale, reopen mutable rustup paths, or weaken stable launch.
4. Add hostile PATH, pathname replacement, missing-tool, descriptor-lifetime,
   and human/JSON diagnostic tests.
5. Qualify install, status, bare launch, dynamic catalog, and provider-free
   selected/all capture through the installed boundary; keep live-provider and
   public-release qualification separate.

