----------------------- MODULE HandoffctlAutonomyLimits -----------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Naturals, TLC

CONSTANTS MaxCommands, MaxElapsed

VARIABLES revision, commands, elapsed, effects, held, heldRevision,
          lastAction, bypassPreEffects, bypassEffects

vars == <<revision, commands, elapsed, effects, held, heldRevision,
          lastAction, bypassPreEffects, bypassEffects>>

Init == /\ revision = 1 /\ commands = 0 /\ elapsed = 0 /\ effects = 0
        /\ held = FALSE /\ heldRevision = 0 /\ lastAction = "init"
        /\ bypassPreEffects = 0 /\ bypassEffects = 0

Run == /\ ~held /\ commands < MaxCommands /\ elapsed < MaxElapsed
       /\ revision' = revision + 1 /\ commands' = commands + 1 /\ effects' = effects + 1
       /\ elapsed' = elapsed
       /\ held' = (commands + 1 = MaxCommands)
       /\ heldRevision' = IF commands + 1 = MaxCommands THEN revision + 1 ELSE 0
       /\ lastAction' = "run"
       /\ UNCHANGED <<bypassPreEffects, bypassEffects>>

Expire == /\ ~held /\ elapsed < MaxElapsed
          /\ revision' = revision + 1 /\ elapsed' = elapsed + 1
          /\ commands' = commands /\ effects' = effects
          /\ held' = (elapsed + 1 = MaxElapsed)
          /\ heldRevision' = IF elapsed + 1 = MaxElapsed THEN revision + 1 ELSE 0
          /\ lastAction' = "expire"
          /\ UNCHANGED <<bypassPreEffects, bypassEffects>>

Dispose == /\ held /\ heldRevision = revision
           /\ revision' = revision + 1 /\ held' = FALSE /\ heldRevision' = 0
           /\ lastAction' = "dispose"
           /\ UNCHANGED <<commands, elapsed, effects, bypassPreEffects, bypassEffects>>

\* An attempted effect while held is retained as an observable transition.  Its
\* result snapshots the count before and after the rejected attempt, rather than
\* disappearing as an unconstrained stutter step.
BypassAttempt == /\ held
                 /\ bypassPreEffects' = effects
                 /\ effects' = effects
                 /\ bypassEffects' = effects'
                 /\ lastAction' = "bypass"
                 /\ UNCHANGED <<revision, commands, elapsed, held, heldRevision>>

Next == Run \/ Expire \/ Dispose \/ BypassAttempt
Spec == Init /\ [][Next]_vars

TypeOK == /\ revision \in Nat /\ commands \in Nat /\ elapsed \in Nat /\ effects \in Nat
          /\ held \in BOOLEAN /\ heldRevision \in Nat
          /\ lastAction \in {"init", "run", "expire", "dispose", "bypass"}
          /\ bypassPreEffects \in Nat /\ bypassEffects \in Nat
FencedHold == held => heldRevision = revision
\* The immediate post-attempt snapshot proves that an attempted held effect was
\* rejected: the durable effect count equals its value before that attempt.
NoEffectBypass == lastAction = "bypass" => bypassEffects = bypassPreEffects
=============================================================================
