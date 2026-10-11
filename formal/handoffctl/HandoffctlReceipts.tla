------------------------ MODULE HandoffctlReceipts ------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, TLC

(*
Bounded opt-in Git receipt contract. Queued work is not authority success.
One receipt has at most one verified local commit. A crashed executor can
either recover that verified commit or retain an explicit ambiguous outcome;
it may not blindly execute the intent again. Remote success is recorded only
after an observation containing the local commit.
*)

CONSTANTS Receipts
ASSUME Receipts # {}

Phases == {"new", "queued", "running", "completed_local", "published_remote",
           "rejected", "ambiguous"}
Terminal == {"published_remote", "rejected", "ambiguous"}

VARIABLES phase, committed, remoteObserved, executorUp, publisherUp

vars == <<phase, committed, remoteObserved, executorUp, publisherUp>>

Init ==
    /\ phase = [r \in Receipts |-> "new"]
    /\ committed = [r \in Receipts |-> FALSE]
    /\ remoteObserved = [r \in Receipts |-> FALSE]
    /\ executorUp = TRUE
    /\ publisherUp = TRUE

Enqueue(r) ==
    /\ phase[r] = "new"
    /\ phase' = [phase EXCEPT ![r] = "queued"]
    /\ UNCHANGED <<committed, remoteObserved, executorUp, publisherUp>>

Reject(r) ==
    /\ phase[r] = "queued"
    /\ phase' = [phase EXCEPT ![r] = "rejected"]
    /\ UNCHANGED <<committed, remoteObserved, executorUp, publisherUp>>

Start(r) ==
    /\ executorUp
    /\ phase[r] = "queued"
    /\ phase' = [phase EXCEPT ![r] = "running"]
    /\ UNCHANGED <<committed, remoteObserved, executorUp, publisherUp>>

Commit(r) ==
    /\ executorUp
    /\ phase[r] = "running"
    /\ ~committed[r]
    /\ phase' = [phase EXCEPT ![r] = "completed_local"]
    /\ committed' = [committed EXCEPT ![r] = TRUE]
    /\ UNCHANGED <<remoteObserved, executorUp, publisherUp>>

RecoverCommitted(r) ==
    /\ executorUp
    /\ phase[r] = "running"
    /\ committed[r]
    /\ phase' = [phase EXCEPT ![r] = "completed_local"]
    /\ UNCHANGED <<committed, remoteObserved, executorUp, publisherUp>>

MarkAmbiguous(r) ==
    /\ phase[r] = "running"
    /\ phase' = [phase EXCEPT ![r] = "ambiguous"]
    /\ UNCHANGED <<committed, remoteObserved, executorUp, publisherUp>>

Publish(r) ==
    /\ publisherUp
    /\ phase[r] = "completed_local"
    /\ committed[r]
    /\ phase' = [phase EXCEPT ![r] = "published_remote"]
    /\ remoteObserved' = [remoteObserved EXCEPT ![r] = TRUE]
    /\ UNCHANGED <<committed, executorUp, publisherUp>>

CrashExecutor ==
    /\ executorUp
    /\ executorUp' = FALSE
    /\ UNCHANGED <<phase, committed, remoteObserved, publisherUp>>

RestartExecutor ==
    /\ ~executorUp
    /\ executorUp' = TRUE
    /\ UNCHANGED <<phase, committed, remoteObserved, publisherUp>>

CrashPublisher ==
    /\ publisherUp
    /\ publisherUp' = FALSE
    /\ UNCHANGED <<phase, committed, remoteObserved, executorUp>>

RestartPublisher ==
    /\ ~publisherUp
    /\ publisherUp' = TRUE
    /\ UNCHANGED <<phase, committed, remoteObserved, executorUp>>

Step(r) ==
    Enqueue(r) \/ Reject(r) \/ Start(r) \/ Commit(r) \/
    RecoverCommitted(r) \/ MarkAmbiguous(r) \/ Publish(r)

Next ==
    (\E r \in Receipts: Step(r)) \/ CrashExecutor \/ RestartExecutor \/
    CrashPublisher \/ RestartPublisher

Fairness ==
    /\ \A r \in Receipts: WF_vars(Step(r))
    /\ WF_vars(RestartExecutor)
    /\ WF_vars(RestartPublisher)

Spec == Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ phase \in [Receipts -> Phases]
    /\ committed \in [Receipts -> BOOLEAN]
    /\ remoteObserved \in [Receipts -> BOOLEAN]
    /\ executorUp \in BOOLEAN
    /\ publisherUp \in BOOLEAN

QueuedIsNotSuccess ==
    \A r \in Receipts: phase[r] = "queued" => ~committed[r] /\ ~remoteObserved[r]

LocalReceiptHasCommit ==
    \A r \in Receipts:
        phase[r] \in {"completed_local", "published_remote"} => committed[r]

RemoteReceiptIsObserved ==
    \A r \in Receipts: phase[r] = "published_remote" => remoteObserved[r]

NoRemoteWithoutLocalCommit ==
    \A r \in Receipts: remoteObserved[r] => committed[r]

AmbiguousNeverPublishes ==
    \A r \in Receipts: phase[r] = "ambiguous" => ~remoteObserved[r]

EventualTerminal ==
    <>(\A r \in Receipts: phase[r] \in Terminal)

ServicesEventuallyStable ==
    <>([](executorUp /\ publisherUp))

ProgressAfterServicesStabilize ==
    ServicesEventuallyStable => EventualTerminal

=============================================================================
