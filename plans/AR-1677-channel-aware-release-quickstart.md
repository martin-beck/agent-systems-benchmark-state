# AR-1677 — Channel-aware release and quickstart gate

Extend the paired quickstart and release qualification so a new user can clone,
select or accept `dev`, configure a provider/model, run selected workloads,
record responses, replay offline, and compare results without retyping channel
state. The receipt must include channel, source/build identity, provider/model
selection, network boundary, and analysis output.

Do not claim interactive TUI success from a non-PTY runner; use a controlling
PTY where required and record any host-runner limitation explicitly.
