# Cached-observation correspondence

`HandoffctlObservation.tla` is a bounded, best-effort abstraction of
`tools/fast_observation.py` and the resident Git socket route in
`tools/fast_receipt_socket.py`.

| Model transition | Concrete route | Evidence |
| --- | --- | --- |
| `RequestCacheHit` | `ObservationCache.observe` returns `bounded-cache` after matching the input digest and age bound | `tests/test_fast_observation.py` |
| `BeginRefresh` / `JoinRefresh` | condition-protected `_refreshing` single-flight | zero-age and 64-caller tests |
| `CompleteRefresh` | `project_scan`, input recheck, cache generation publication | focused observation tests |
| `RejectChangedInput` | `OBSERVATION_INPUT_CHANGED` failure | changed-input test |
| `Timeout` | bounded condition wait | implementation deadline and negative-path coverage |

The correspondence is best-effort only. TLC proves properties of the finite
model, while tests exercise selected Python paths. Neither establishes that
the Python implementation refines the model or proves Git, sockets, threads,
the filesystem, or operating-system event delivery.
