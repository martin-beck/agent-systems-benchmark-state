---------------------------- MODULE HandoffctlRecovery ----------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Naturals

(*
Focused Git-backend recovery admission model. Both tasks start as simultaneously
expired claims held by distinct actors while an unrelated repository finding is
present. Unlike the general transition model, this model excludes injected I/O
rollback and lock timeout so it can prove successful admission rather than mere
command termination. Those failure paths remain covered by Handoffctl.tla and
HandoffctlLocks.tla.
*)

CONSTANTS Processes, Tasks, Actors, NoProcess, NoActor

ASSUME /\ Cardinality(Processes) = 2
       /\ Cardinality(Tasks) = 2
       /\ Cardinality(Actors) = 2
       /\ NoProcess \notin Processes
       /\ NoActor \notin Actors

Phases == {"waiting", "holding", "releasing", "done"}
Results == {"pending", "accepted", "rejected"}

VARIABLES
    status,
    owner,
    revision,
    projectionRevision,
    pc,
    target,
    lockOwner,
    result,
    unrelatedFinding

vars ==
    <<status, owner, revision, projectionRevision, pc, target, lockOwner,
      result, unrelatedFinding>>

OwnerIsUnique(o) ==
    \A a \in Actors:
        Cardinality({t \in Tasks: o[t] = a}) <= 1

Init ==
    /\ status = [t \in Tasks |-> "in_progress"]
    /\ owner \in [Tasks -> Actors]
    /\ OwnerIsUnique(owner)
    /\ revision = [t \in Tasks |-> 0]
    /\ projectionRevision = revision
    /\ pc = [p \in Processes |-> "waiting"]
    /\ target \in [Processes -> Tasks]
    /\ lockOwner = NoProcess
    /\ result = [p \in Processes |-> "pending"]
    /\ unrelatedFinding = TRUE

RecoveryEnabled(p) ==
    LET t == target[p] IN
    /\ status[t] = "in_progress"
    /\ owner[t] # NoActor
    /\ revision[t] = 0

Acquire(p) ==
    /\ pc[p] = "waiting"
    /\ lockOwner = NoProcess
    /\ lockOwner' = p
    /\ pc' = [pc EXCEPT ![p] = "holding"]
    /\ UNCHANGED
        <<status, owner, revision, projectionRevision, target, result,
          unrelatedFinding>>

ExecuteSuccess(p) ==
    LET t == target[p] IN
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ RecoveryEnabled(p)
    /\ status' = [status EXCEPT ![t] = "open"]
    /\ owner' = [owner EXCEPT ![t] = NoActor]
    /\ revision' = [revision EXCEPT ![t] = @ + 1]
    /\ projectionRevision' = [projectionRevision EXCEPT ![t] = @ + 1]
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED <<target, lockOwner, unrelatedFinding>>

ExecuteReject(p) ==
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ ~RecoveryEnabled(p)
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<status, owner, revision, projectionRevision, target, lockOwner,
          unrelatedFinding>>

Release(p) ==
    /\ pc[p] = "releasing"
    /\ lockOwner = p
    /\ lockOwner' = NoProcess
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED
        <<status, owner, revision, projectionRevision, target, result,
          unrelatedFinding>>

Quiescent ==
    /\ \A p \in Processes: pc[p] = "done"
    /\ UNCHANGED vars

Next ==
    (\E p \in Processes:
        Acquire(p) \/ ExecuteSuccess(p) \/ ExecuteReject(p) \/ Release(p))
    \/ Quiescent

Fairness ==
    /\ \A p \in Processes: WF_vars(Acquire(p))
    /\ \A p \in Processes: WF_vars(ExecuteSuccess(p) \/ ExecuteReject(p))
    /\ \A p \in Processes: WF_vars(Release(p))

Spec ==
    Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ status \in [Tasks -> {"in_progress", "open"}]
    /\ owner \in [Tasks -> (Actors \cup {NoActor})]
    /\ revision \in [Tasks -> 0..1]
    /\ projectionRevision \in [Tasks -> 0..1]
    /\ pc \in [Processes -> Phases]
    /\ target \in [Processes -> Tasks]
    /\ lockOwner \in Processes \cup {NoProcess}
    /\ result \in [Processes -> Results]
    /\ unrelatedFinding \in BOOLEAN

OwnershipCoherence ==
    \A t \in Tasks:
        (status[t] = "in_progress") <=> (owner[t] # NoActor)

UniqueActiveOwner ==
    OwnerIsUnique(owner)

RecoveryAtomicity ==
    /\ projectionRevision = revision
    /\ \A t \in Tasks:
        (status[t] = "open") <=> (revision[t] = 1)

LockSafety ==
    /\ Cardinality(
           {p \in Processes: pc[p] = "holding" \/ pc[p] = "releasing"}
       ) <= 1
    /\ (lockOwner = NoProcess) <=>
       (\A p \in Processes:
           pc[p] # "holding" /\ pc[p] # "releasing")

UnrelatedFindingPersists ==
    unrelatedFinding

EligibleRecovery(p) ==
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ RecoveryEnabled(p)

RecoveryAdmissionProgress ==
    \A p \in Processes:
        EligibleRecovery(p) ~> (result[p] = "accepted")

DistinctRecoveryProgress ==
    Cardinality({target[p] : p \in Processes}) = Cardinality(Processes)
        => <>(\A p \in Processes: result[p] = "accepted")

=============================================================================
