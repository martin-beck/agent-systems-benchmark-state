<!-- This page is generated; the root STATUS.md index links the complete view. -->

| P1 | [AR-1353](../tasks/AR-1353-runtime-enrollment-cli-dispatch.md): Runtime enrollment and CLI dispatch | Unclaimed | Add runtime-owned enrollment and opaque live CLI dispatch. | Wire asb-cli run/sweep to acquire through LiveProviderRuntimeService::acquire_from_enrollment, using a runtime-only enrollment implementation that mints the opaque handle; remove the production requirement for caller-injected LiveProviderAttemptFactory. Add positive/negative dispatch and offline/replay tests, then run full gates. |
