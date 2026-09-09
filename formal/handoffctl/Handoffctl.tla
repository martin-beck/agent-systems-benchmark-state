---------------------------- MODULE Handoffctl ----------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Integers, Naturals, Sequences, TLC

(*
Finite-state refinement model for handoffctl's state-changing commands.

Each process arrives with one request. Requests race for the same advisory
repository lock, validate against state observed while holding that lock, and
either linearize one transition or leave all durable state unchanged. TLC
enumerates every initial task state, request, stale/current expected revision,
dependency condition, failure choice, and process interleaving in the scope
declared by Handoffctl.cfg.
*)

CONSTANTS Processes, Tasks, Actors, NoProcess, NoActor, MaxRevision

ASSUME /\ Processes # {}
       /\ Tasks # {}
       /\ Actors # {}
       /\ NoProcess \notin Processes
       /\ NoActor \notin Actors
       /\ MaxRevision >= Cardinality(Processes)

Statuses ==
    {"planned", "open", "in_progress", "blocked", "done"}

ReleaseOperations ==
    {"release_planned", "release_open", "release_blocked", "release_done"}

Operations ==
    {"promote", "resume", "claim", "heartbeat", "update", "recover_expired"}
        \cup ReleaseOperations

Phases == {"waiting", "holding", "releasing", "done"}
Results == {"pending", "accepted", "rejected", "rolled_back", "lock_timeout"}

VARIABLES
    status,
    owner,
    revision,
    initialRevision,
    projectionRevision,
    leaseExpired,
    dependencyReady,
    pc,
    operation,
    target,
    actor,
    expected,
    lockOwner,
    result,
    successCount

vars ==
    <<status, owner, revision, initialRevision, projectionRevision,
      dependencyReady, leaseExpired, pc, operation, target, actor, expected,
      lockOwner, result, successCount>>

OwnershipIsCoherent(s, o) ==
    \A t \in Tasks:
        (s[t] = "in_progress") <=> (o[t] # NoActor)

OwnerIsUnique(o) ==
    \A a \in Actors:
        Cardinality({t \in Tasks: o[t] = a}) <= 1

Init ==
    /\ status \in [Tasks -> Statuses]
    /\ owner \in [Tasks -> (Actors \cup {NoActor})]
    /\ OwnershipIsCoherent(status, owner)
    /\ OwnerIsUnique(owner)
    /\ revision = [t \in Tasks |-> 0]
    /\ initialRevision = revision
    /\ projectionRevision = revision
    /\ leaseExpired \in [Tasks -> BOOLEAN]
    /\ dependencyReady \in [Tasks -> BOOLEAN]
    /\ pc = [p \in Processes |-> "waiting"]
    /\ operation \in [Processes -> Operations]
    /\ target \in [Processes -> Tasks]
    /\ actor \in [Processes -> Actors]
    /\ expected \in [Processes -> (0..MaxRevision)]
    /\ lockOwner = NoProcess
    /\ result = [p \in Processes |-> "pending"]
    /\ successCount = [t \in Tasks |-> 0]

NoOtherActiveTask(p) ==
    \A t \in (Tasks \ {target[p]}):
        owner[t] # actor[p]

EnabledOperation(p) ==
    LET t == target[p] IN
    CASE operation[p] = "promote" ->
            /\ status[t] = "planned"
            /\ owner[t] = NoActor
            /\ dependencyReady[t]
            /\ expected[p] = revision[t]
      [] operation[p] = "resume" ->
            /\ status[t] = "blocked"
            /\ owner[t] = NoActor
            /\ expected[p] = revision[t]
      [] operation[p] = "claim" ->
            /\ status[t] = "open"
            /\ dependencyReady[t]
            /\ NoOtherActiveTask(p)
      [] operation[p] = "heartbeat" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
      [] operation[p] = "update" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ expected[p] = revision[t]
      [] operation[p] = "recover_expired" ->
            /\ status[t] = "in_progress"
            /\ owner[t] # NoActor
            /\ leaseExpired[t]
            /\ expected[p] = revision[t]
      [] operation[p] \in ReleaseOperations ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]

StatusAfter(p) ==
    CASE operation[p] \in {"promote", "resume"} -> "open"
      [] operation[p] = "claim" -> "in_progress"
      [] operation[p] = "recover_expired" -> "open"
      [] operation[p] \in {"heartbeat", "update"} -> status[target[p]]
      [] operation[p] = "release_planned" -> "planned"
      [] operation[p] = "release_open" -> "open"
      [] operation[p] = "release_blocked" -> "blocked"
      [] operation[p] = "release_done" -> "done"

OwnerAfter(p) ==
    IF operation[p] = "claim"
    THEN actor[p]
    ELSE IF operation[p] \in ReleaseOperations \cup {"recover_expired"}
         THEN NoActor
         ELSE owner[target[p]]

ExpiryAfter(p) ==
    IF operation[p] \in ReleaseOperations \cup {"claim", "heartbeat", "recover_expired"}
    THEN FALSE
    ELSE leaseExpired[target[p]]


Acquire(p) ==
    /\ pc[p] = "waiting"
    /\ lockOwner = NoProcess
    /\ lockOwner' = p
    /\ pc' = [pc EXCEPT ![p] = "holding"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision,
          dependencyReady, leaseExpired, operation, target, actor, expected, result,
          successCount>>

WaitTimeout(p) ==
    /\ pc[p] = "waiting"
    /\ lockOwner # NoProcess
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "lock_timeout"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision,
          dependencyReady, leaseExpired, operation, target, actor, expected, lockOwner,
          successCount>>

Wait(p) ==
    Acquire(p) \/ WaitTimeout(p)

ExecuteSuccess(p) ==
    LET t == target[p] IN
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ EnabledOperation(p)
    /\ status' = [status EXCEPT ![t] = StatusAfter(p)]
    /\ owner' = [owner EXCEPT ![t] = OwnerAfter(p)]
    /\ leaseExpired' = [leaseExpired EXCEPT ![t] = ExpiryAfter(p)]
    /\ revision' = [revision EXCEPT ![t] = @ + 1]
    /\ projectionRevision' = [projectionRevision EXCEPT ![t] = @ + 1]
    /\ successCount' = [successCount EXCEPT ![t] = @ + 1]
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<initialRevision, dependencyReady, operation, target, actor, expected,
          lockOwner>>

ExecuteReject(p) ==
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ ~EnabledOperation(p)
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision,
          dependencyReady, leaseExpired, operation, target, actor, expected, lockOwner,
          successCount>>

(*
Models any detected exception before a local Git commit. The implementation
must restore the task and every generated projection before releasing the lock.
*)
ExecuteRollback(p) ==
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ result' = [result EXCEPT ![p] = "rolled_back"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision,
          dependencyReady, leaseExpired, operation, target, actor, expected, lockOwner,
          successCount>>

Execute(p) ==
    ExecuteSuccess(p) \/ ExecuteReject(p) \/ ExecuteRollback(p)

Release(p) ==
    /\ pc[p] = "releasing"
    /\ lockOwner = p
    /\ lockOwner' = NoProcess
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision,
          dependencyReady, leaseExpired, operation, target, actor, expected, result,
          successCount>>

Quiescent ==
    /\ \A p \in Processes: pc[p] = "done"
    /\ UNCHANGED vars

Next ==
    (\E p \in Processes:
        Wait(p) \/ Execute(p) \/ Release(p))
    \/ Quiescent

Fairness ==
    /\ \A p \in Processes: WF_vars(Wait(p))
    /\ \A p \in Processes: WF_vars(Execute(p))
    /\ \A p \in Processes: WF_vars(Release(p))

Spec ==
    Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ status \in [Tasks -> Statuses]
    /\ owner \in [Tasks -> (Actors \cup {NoActor})]
    /\ revision \in [Tasks -> Nat]
    /\ initialRevision \in [Tasks -> Nat]
    /\ projectionRevision \in [Tasks -> Nat]
    /\ dependencyReady \in [Tasks -> BOOLEAN]
    /\ leaseExpired \in [Tasks -> BOOLEAN]
    /\ pc \in [Processes -> Phases]
    /\ operation \in [Processes -> Operations]
    /\ target \in [Processes -> Tasks]
    /\ actor \in [Processes -> Actors]
    /\ expected \in [Processes -> (0..MaxRevision)]
    /\ lockOwner \in Processes \cup {NoProcess}
    /\ result \in [Processes -> Results]
    /\ successCount \in [Tasks -> Nat]

OwnershipCoherence ==
    OwnershipIsCoherent(status, owner)

UniqueActiveOwner ==
    OwnerIsUnique(owner)

LockSafety ==
    /\ Cardinality(
           {p \in Processes: pc[p] = "holding" \/ pc[p] = "releasing"}
       ) <= 1
    /\ (lockOwner = NoProcess) <=>
       (\A p \in Processes:
           pc[p] # "holding" /\ pc[p] # "releasing")
    /\ lockOwner # NoProcess =>
       pc[lockOwner] \in {"holding", "releasing"}

RevisionAccounting ==
    \A t \in Tasks:
        revision[t] = initialRevision[t] + successCount[t]

ProjectionAtomicity ==
    projectionRevision = revision

EventualCompletion ==
    <>(\A p \in Processes: pc[p] = "done")

=============================================================================
