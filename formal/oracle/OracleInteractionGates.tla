----------------------------- MODULE OracleInteractionGates -----------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Naturals, Sequences

CONSTANTS P1, P2, MaxRevision

Stages == <<"intake", "discussion", "formal_spec_review", "reconciliation">>
StageSet == {"intake", "discussion", "formal_spec_review", "reconciliation"}
Operations == {"open", "resolve", "claim", "run", "release"}
Dispositions == {"accepted", "unresolved"}
Processes == {P1, P2}
VARIABLES revision, completed, openStage, operation, requestedStage,
          expectedRevision, disposition, result
vars == <<revision, completed, openStage, operation, requestedStage,
          expectedRevision, disposition, result>>
Init == revision = 1 /\ completed = <<>> /\ openStage = "none"
    /\ operation = [p \in Processes |-> "open"]
    /\ requestedStage = [p \in Processes |-> "intake"]
    /\ expectedRevision = [p \in Processes |-> 1]
    /\ disposition = [p \in Processes |-> "unresolved"]
    /\ result = [p \in Processes |-> "waiting"]
NextStage == IF Len(completed) < Len(Stages) THEN Stages[Len(completed) + 1] ELSE "none"
Hostile(p) == operation[p] = "open" /\ expectedRevision[p] = revision
    /\ requestedStage[p] # NextStage
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ UNCHANGED <<revision, completed, openStage, operation, requestedStage,
                    expectedRevision, disposition>>
Stale(p) == expectedRevision[p] # revision
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ UNCHANGED <<revision, completed, openStage, operation, requestedStage,
                    expectedRevision, disposition>>
Open(p) == operation[p] = "open" /\ expectedRevision[p] = revision
    /\ requestedStage[p] = NextStage /\ requestedStage[p] # "none"
    /\ openStage = "none"
    /\ openStage' = requestedStage[p] /\ revision' = revision + 1
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ operation' = [operation EXCEPT ![p] = "resolve"]
    /\ expectedRevision' = [expectedRevision EXCEPT ![p] = revision + 1]
    /\ disposition' = [disposition EXCEPT ![p] = "unresolved"]
    /\ UNCHANGED <<completed, requestedStage>>
ResolveAccepted(p) == operation[p] = "resolve" /\ expectedRevision[p] = revision
    /\ openStage # "none" /\ requestedStage[p] = openStage /\ revision' = revision + 1
    /\ completed' = Append(completed, openStage) /\ openStage' = "none"
    /\ operation' = [operation EXCEPT ![p] =
          IF Len(completed) + 1 < Len(Stages) THEN "open" ELSE "claim"]
    /\ requestedStage' = [requestedStage EXCEPT ![p] = NextStage]
    /\ expectedRevision' = [expectedRevision EXCEPT ![p] = revision + 1]
    /\ disposition' = [disposition EXCEPT ![p] = "accepted"]
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ UNCHANGED <<>>
ResolveUnresolved(p) == operation[p] = "resolve" /\ expectedRevision[p] = revision
    /\ openStage # "none" /\ requestedStage[p] = openStage /\ revision' = revision + 1
    /\ UNCHANGED <<completed, openStage, requestedStage, operation>>
    /\ expectedRevision' = [expectedRevision EXCEPT ![p] = revision + 1]
    /\ disposition' = [disposition EXCEPT ![p] = "unresolved"]
    /\ result' = [result EXCEPT ![p] = "accepted"]
Blocked(p) == operation[p] \in {"claim", "run", "release"} /\ openStage # "none"
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ UNCHANGED <<revision, completed, openStage, operation, requestedStage,
                    expectedRevision, disposition>>
Idle(p) == openStage = "none" /\ operation[p] = "claim"
    /\ UNCHANGED vars
Step(p) == Hostile(p) \/ Stale(p) \/ Open(p) \/ ResolveAccepted(p)
    \/ ResolveUnresolved(p) \/ Blocked(p) \/ Idle(p)
Next == (revision < MaxRevision /\ (\E p \in Processes: Step(p)))
    \/ UNCHANGED vars
Spec == Init /\ [][Next]_vars
TypeOK == revision \in 1..MaxRevision /\ completed \in Seq(StageSet)
    /\ openStage \in StageSet \cup {"none"}
    /\ operation \in [Processes -> Operations]
    /\ requestedStage \in [Processes -> StageSet \cup {"none"}]
    /\ expectedRevision \in [Processes -> Nat]
    /\ disposition \in [Processes -> Dispositions]
NoSkippedGate == openStage # "none" => openStage = NextStage
RevisionMonotonic == revision >= 1 /\ revision <= MaxRevision
CompletedPrefix == completed = SubSeq(Stages, 1, Len(completed))
OpenGateBlocksAutonomousWork == openStage # "none" =>
    \A p \in Processes: ~(operation[p] \in {"claim", "run", "release"}
        /\ result[p] = "accepted")
=============================================================================
