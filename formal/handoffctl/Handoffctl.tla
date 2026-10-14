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

CONSTANTS Processes, Tasks, Actors, NoProcess, NoActor, NoTask, MaxRevision

ASSUME /\ Processes # {}
       /\ Tasks # {}
       /\ Actors # {}
       /\ NoProcess \notin Processes
       /\ NoActor \notin Actors
       /\ NoTask \notin Tasks
       /\ MaxRevision >= Cardinality(Processes)

Statuses ==
    {"planned", "open", "in_progress", "blocked", "done", "cancelled", "superseded"}

ReleaseOperations ==
    {"release_planned", "release_open", "release_blocked", "release_done"}

Operations ==
    {"promote", "resume", "unblock", "pause", "claim", "heartbeat", "update", "accept", "bind-spec", "bind-worktree", "bind-envelope", "recover_expired", "recover-execution", "abandon-execution", "change-drift", "assumption"}
        \cup ReleaseOperations

Phases == {"waiting", "holding", "releasing", "done"}
Results == {"pending", "accepted", "rejected", "rolled_back", "lock_timeout"}
PauseProvenances == {"absent", "unique_valid", "unique_incoherent", "duplicate"}
BranchNames == {"branch-1"}
WorktreeKeys == {"worktree-1", "worktree-2"}
NoBranch == "no-branch"
NoWorktreeKey == "no-worktree-key"

ParentMap == [t \in Tasks |-> IF t = "t1" THEN NoTask ELSE "t1"]
ChildrenMap == [t \in Tasks |-> IF t = "t1" THEN {"t2"} ELSE {}]

HierarchyCoherent ==
    /\ \A t \in Tasks: ParentMap[t] = NoTask <=> t \notin UNION {ChildrenMap[p] : p \in Tasks}
    /\ \A t \in Tasks: ParentMap[t] # NoTask => t \in ChildrenMap[ParentMap[t]]
    /\ \A t \in Tasks: IF ParentMap[t] = NoTask THEN TRUE ELSE ParentMap[ParentMap[t]] = NoTask \/ ParentMap[ParentMap[t]] # t

VARIABLES
    status,
    owner,
    revision,
    initialRevision,
    projectionRevision,
    specBound,
    initialSpecBound,
    worktreeBound,
    initialWorktreeBound,
    boundBranch,
    boundWorktreeKey,
    leaseExpired,
    pauseProvenance,
    dependencyReady,
    pc,
    operation,
    target,
    actor,
    expected,
    lockOwner,
    result,
    successCount

ChildrenOpen(t) ==
    \E child \in ChildrenMap[t]:
        status[child] # "done" /\ status[child] # "cancelled" /\ status[child] # "superseded"

vars ==
    <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
      boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, pc, operation, target, actor, expected,
      lockOwner, result, successCount>>

OwnershipIsCoherent(s, o) ==
    \A t \in Tasks:
        (s[t] = "in_progress") <=> (o[t] # NoActor)

OwnerIsUnique(o) ==
    \A a \in Actors:
        Cardinality({t \in Tasks: o[t] = a}) <= 1

ActiveWorktreeIdentitiesAreUnique(s, branches, keys) ==
    \A t \in Tasks:
        s[t] = "in_progress" =>
            /\ branches[t] # NoBranch =>
                Cardinality({u \in Tasks: s[u] = "in_progress" /\ branches[u] = branches[t]}) = 1
            /\ keys[t] # NoWorktreeKey =>
                Cardinality({u \in Tasks: s[u] = "in_progress" /\ keys[u] = keys[t]}) = 1

Init ==
    /\ status \in [Tasks -> Statuses]
    /\ owner \in [Tasks -> (Actors \cup {NoActor})]
    /\ OwnershipIsCoherent(status, owner)
    /\ OwnerIsUnique(owner)
    /\ revision = [t \in Tasks |-> 0]
    /\ initialRevision = revision
    /\ projectionRevision = revision
    /\ specBound \in [Tasks -> BOOLEAN]
    /\ initialSpecBound = specBound
    /\ worktreeBound = [t \in Tasks |-> FALSE]
    /\ initialWorktreeBound = worktreeBound
    /\ boundBranch = [t \in Tasks |-> NoBranch]
    /\ boundWorktreeKey = [t \in Tasks |->
        IF t = "t1" THEN "worktree-1" ELSE NoWorktreeKey]
    /\ \A t \in Tasks: worktreeBound[t] <=>
        (boundBranch[t] # NoBranch /\ boundWorktreeKey[t] # NoWorktreeKey)
    /\ ActiveWorktreeIdentitiesAreUnique(status, boundBranch, boundWorktreeKey)
    /\ leaseExpired \in [Tasks -> BOOLEAN]
    /\ pauseProvenance \in [Tasks -> PauseProvenances]
    /\ \A t \in Tasks: pauseProvenance[t] # "absent" => status[t] = "blocked"
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

RequestedBranch(p) == "branch-1"
\* `dependencyReady` supplies the bounded request-key choice.  It is immutable
\* during a request, so both matching and mismatched partial-key admissions are
\* explored without adding another transition variable.
RequestedWorktreeKey(p) ==
    IF dependencyReady[target[p]] THEN "worktree-1" ELSE "worktree-2"

NoOtherActiveWorktreeIdentity(p) ==
    \A t \in (Tasks \ {target[p]}):
        status[t] # "in_progress" \/
            /\ boundBranch[t] # RequestedBranch(p)
            /\ boundWorktreeKey[t] # RequestedWorktreeKey(p)

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
            /\ pauseProvenance[t] = "unique_valid"
            /\ expected[p] = revision[t]
      [] operation[p] = "unblock" ->
            /\ status[t] = "blocked"
            /\ owner[t] = NoActor
            /\ pauseProvenance[t] = "absent"
            /\ expected[p] = revision[t]
      [] operation[p] = "pause" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ expected[p] = revision[t]
      [] operation[p] = "claim" ->
            /\ status[t] = "open"
            /\ dependencyReady[t]
            /\ NoOtherActiveTask(p)
      [] operation[p] = "heartbeat" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
      [] operation[p] \in {"update", "accept", "change-drift", "assumption"} ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ expected[p] = revision[t]
      [] operation[p] = "bind-spec" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ ~leaseExpired[t]
            /\ ~specBound[t]
            /\ expected[p] = revision[t]
      [] operation[p] = "bind-worktree" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ ~leaseExpired[t]
            /\ NoOtherActiveWorktreeIdentity(p)
            /\ expected[p] = revision[t]
            /\ ((~worktreeBound[t]
                    /\ boundBranch[t] = NoBranch
                    /\ (boundWorktreeKey[t] = NoWorktreeKey
                        \/ boundWorktreeKey[t] = RequestedWorktreeKey(p)))
                \/ (RequestedBranch(p) = boundBranch[t]
                    /\ RequestedWorktreeKey(p) = boundWorktreeKey[t]))
      [] operation[p] = "bind-envelope" ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ ~leaseExpired[t]
            /\ specBound[t]
            /\ expected[p] = revision[t]
      [] operation[p] = "recover_expired" ->
            /\ status[t] = "in_progress"
            /\ owner[t] # NoActor
            /\ leaseExpired[t]
            /\ expected[p] = revision[t]
      [] operation[p] = "recover-execution" ->
            /\ status[t] = "in_progress"
            /\ expected[p] = revision[t]
      [] operation[p] = "abandon-execution" ->
            /\ status[t] = "in_progress"
            /\ expected[p] = revision[t]
      [] operation[p] \in ReleaseOperations ->
            /\ status[t] = "in_progress"
            /\ owner[t] = actor[p]
            /\ operation[p] # "release_done" \/ ~ChildrenOpen(t)

StatusAfter(p) ==
    CASE operation[p] \in {"promote", "resume", "unblock"} -> "open"
      [] operation[p] = "pause" -> "blocked"
      [] operation[p] = "claim" -> "in_progress"
      [] operation[p] \in {"recover_expired", "abandon-execution"} -> "open"
      [] operation[p] \in {"heartbeat", "update", "accept", "bind-spec", "bind-worktree", "bind-envelope", "recover-execution", "abandon-execution", "change-drift", "assumption"} -> status[target[p]]
      [] operation[p] = "release_planned" -> "planned"
      [] operation[p] = "release_open" -> "open"
      [] operation[p] = "release_blocked" -> "blocked"
      [] operation[p] = "release_done" -> "done"

OwnerAfter(p) ==
    IF operation[p] = "claim"
    THEN actor[p]
    ELSE IF operation[p] \in ReleaseOperations \cup {"recover_expired", "abandon-execution", "pause"}
         THEN NoActor
         ELSE owner[target[p]]

ExpiryAfter(p) ==
    IF operation[p] \in ReleaseOperations \cup {"claim", "heartbeat", "recover_expired", "abandon-execution", "pause"}
    THEN FALSE
    ELSE leaseExpired[target[p]]

SpecBoundAfter(p) ==
    IF operation[p] = "bind-spec" THEN TRUE ELSE specBound[target[p]]

WorktreeBoundAfter(p) ==
    IF operation[p] = "bind-worktree" THEN TRUE ELSE worktreeBound[target[p]]

BoundBranchAfter(p) ==
    IF operation[p] = "bind-worktree" THEN RequestedBranch(p) ELSE boundBranch[target[p]]

BoundWorktreeKeyAfter(p) ==
    IF operation[p] = "bind-worktree" THEN RequestedWorktreeKey(p) ELSE boundWorktreeKey[target[p]]

IdempotentWorktreeReplay(p) ==
    /\ operation[p] = "bind-worktree"
    /\ worktreeBound[target[p]]
    /\ RequestedBranch(p) = boundBranch[target[p]]
    /\ RequestedWorktreeKey(p) = boundWorktreeKey[target[p]]

PauseProvenanceAfter(p) ==
    IF operation[p] = "pause" THEN "unique_valid" ELSE "absent"


Acquire(p) ==
    /\ pc[p] = "waiting"
    /\ lockOwner = NoProcess
    /\ lockOwner' = p
    /\ pc' = [pc EXCEPT ![p] = "holding"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
          boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, operation, target, actor, expected, result,
          successCount>>

WaitTimeout(p) ==
    /\ pc[p] = "waiting"
    /\ lockOwner # NoProcess
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "lock_timeout"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
          boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, operation, target, actor, expected, lockOwner,
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
    /\ specBound' = [specBound EXCEPT ![t] = SpecBoundAfter(p)]
    /\ worktreeBound' = [worktreeBound EXCEPT ![t] = WorktreeBoundAfter(p)]
    /\ boundBranch' = [boundBranch EXCEPT ![t] = BoundBranchAfter(p)]
    /\ boundWorktreeKey' = [boundWorktreeKey EXCEPT ![t] = BoundWorktreeKeyAfter(p)]
    /\ leaseExpired' = [leaseExpired EXCEPT ![t] = ExpiryAfter(p)]
    /\ pauseProvenance' = [pauseProvenance EXCEPT ![t] = PauseProvenanceAfter(p)]
    /\ revision' = [revision EXCEPT ![t] = IF IdempotentWorktreeReplay(p) THEN @ ELSE @ + 1]
    /\ projectionRevision' = [projectionRevision EXCEPT ![t] = IF IdempotentWorktreeReplay(p) THEN @ ELSE @ + 1]
    /\ successCount' = [successCount EXCEPT ![t] = IF IdempotentWorktreeReplay(p) THEN @ ELSE @ + 1]
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<initialRevision, initialSpecBound, initialWorktreeBound, dependencyReady, operation, target, actor, expected,
          lockOwner>>

ExecuteReject(p) ==
    /\ pc[p] = "holding"
    /\ lockOwner = p
    /\ ~EnabledOperation(p)
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ pc' = [pc EXCEPT ![p] = "releasing"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
          boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, operation, target, actor, expected, lockOwner,
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
        <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
          boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, operation, target, actor, expected, lockOwner,
          successCount>>

Execute(p) ==
    ExecuteSuccess(p) \/ ExecuteReject(p) \/ ExecuteRollback(p)

Release(p) ==
    /\ pc[p] = "releasing"
    /\ lockOwner = p
    /\ lockOwner' = NoProcess
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED
        <<status, owner, revision, initialRevision, projectionRevision, specBound, initialSpecBound, worktreeBound, initialWorktreeBound,
          boundBranch, boundWorktreeKey, dependencyReady, leaseExpired, pauseProvenance, operation, target, actor, expected, result,
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
    /\ specBound \in [Tasks -> BOOLEAN]
    /\ initialSpecBound \in [Tasks -> BOOLEAN]
    /\ worktreeBound \in [Tasks -> BOOLEAN]
    /\ initialWorktreeBound \in [Tasks -> BOOLEAN]
    /\ boundBranch \in [Tasks -> (BranchNames \cup {NoBranch})]
    /\ boundWorktreeKey \in [Tasks -> (WorktreeKeys \cup {NoWorktreeKey})]
    /\ dependencyReady \in [Tasks -> BOOLEAN]
    /\ leaseExpired \in [Tasks -> BOOLEAN]
    /\ pauseProvenance \in [Tasks -> PauseProvenances]
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

BlockedProvenance ==
    \A t \in Tasks: pauseProvenance[t] # "absent" => status[t] = "blocked"

UniqueActiveOwner ==
    OwnerIsUnique(owner)

UniqueActiveWorktreeIdentity ==
    ActiveWorktreeIdentitiesAreUnique(status, boundBranch, boundWorktreeKey)

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

SpecBindingIsMonotonic ==
    \A t \in Tasks: initialSpecBound[t] => specBound[t]

AcceptedSpecBindIsBound ==
    \A p \in Processes:
        result[p] = "accepted" /\ operation[p] = "bind-spec" => specBound[target[p]]

WorktreeBindingIsMonotonic ==
    \A t \in Tasks: initialWorktreeBound[t] => worktreeBound[t]

AcceptedWorktreeBindIsBound ==
    \A p \in Processes:
        result[p] = "accepted" /\ operation[p] = "bind-worktree" => worktreeBound[target[p]]

PartialWorktreeKeyIsPreserved ==
    boundWorktreeKey["t1"] = "worktree-1"

EventualCompletion ==
    <>(\A p \in Processes: pc[p] = "done")

=============================================================================
