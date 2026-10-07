-------------------------- MODULE HandoffctlUpgradeBarrier --------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Naturals, TLC

(***************************************************************************)
(* Bounded v10 barrier/control-store contract.                          *)
(*                                                                         *)
(* This model describes the accepted control-plane boundary only.  It does *)
(* not model SQLite's VFS, WAL fsync, power loss, Python refinement, or the *)
(* coordinator authority itself. It is best-effort design guidance, and no  *)
(* Python refinement proof is required. A writer observes the durable barrier *)
(* at the abstract linearization point; unsafe states reject the write.      *)
(***************************************************************************)

CONSTANTS Processes, NoProcess, NoChild, MaxRevision

Statuses == {"absent", "held", "releasing", "released", "ambiguous"}
UnsafeStatuses == {"held", "releasing", "ambiguous"}
WriterPhases == {"idle", "requested", "accepted", "rejected", "done"}
Targets == {"new", "rollback"}
NoTarget == "none"
TerminalResults == {"none", "new", "rollback"}
LockStages == {"free", "common", "control", "authority"}
CASResults == {"none", "accepted", "rejected"}

VARIABLES
    sessionStatus,
    activeAttempt,
    attemptGeneration,
    fence,
    controlRevision,
    forwardChild,
    rollbackChild,
    forwardFailed,
    terminalTarget,
    terminalVerified,
    freshRuntimeVerified,
    writerPhase,
    writerAcceptedStatus,
    writerMutations,
    writerTarget,
    lockOwner,
    lockStage,
    authorityRevision,
    freshAuthorityRevision,
    authorityRechecked,
    casExpected,
    casObserved,
    casBaselineRevision,
    casResult

vars == <<sessionStatus, activeAttempt, attemptGeneration, fence,
          controlRevision, forwardChild, rollbackChild, forwardFailed,
          terminalTarget, terminalVerified, freshRuntimeVerified,
          writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
          lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
          authorityRechecked, casExpected, casObserved, casBaselineRevision,
          casResult>>

ForwardId(p) ==
    CASE p = "p1" -> "forward-p1"
      [] p = "p2" -> "forward-p2"

RollbackId(p) ==
    CASE p = "p1" -> "rollback-p1"
      [] p = "p2" -> "rollback-p2"

Init ==
    /\ sessionStatus = "absent"
    /\ activeAttempt = NoProcess
    /\ attemptGeneration = 0
    /\ fence = 0
    /\ controlRevision = 0
    /\ forwardChild = NoChild
    /\ rollbackChild = NoChild
    /\ forwardFailed = FALSE
    /\ terminalTarget = NoTarget
    /\ terminalVerified = FALSE
    /\ freshRuntimeVerified = FALSE
    /\ writerPhase = [p \in Processes |-> "idle"]
    /\ writerAcceptedStatus = [p \in Processes |-> "none"]
    /\ writerMutations = 0
    /\ writerTarget = [p \in Processes |-> "authority"]
    /\ lockOwner = NoProcess
    /\ lockStage = "free"
    /\ authorityRevision = 0
    /\ freshAuthorityRevision = 0
    /\ authorityRechecked = FALSE
    /\ casExpected = [p \in Processes |-> 0]
    /\ casObserved = [p \in Processes |-> 0]
    /\ casBaselineRevision = [p \in Processes |-> 0]
    /\ casResult = [p \in Processes |-> "none"]

ControlHeld(p) == lockOwner = p /\ lockStage = "control"
AuthorityHeld(p) == lockOwner = p /\ lockStage = "authority"

AcquireCommon(p) ==
    /\ lockStage = "free" /\ lockOwner = NoProcess
    /\ lockOwner' = p /\ lockStage' = "common"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  authorityRevision, freshAuthorityRevision, authorityRechecked,
                  casExpected, casObserved, casBaselineRevision, casResult>>

AcquireControl(p) ==
    /\ lockOwner = p /\ lockStage = "common"
    /\ lockStage' = "control"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

AcquireAuthority(p) ==
    /\ lockOwner = p /\ lockStage = "control"
    /\ lockStage' = "authority"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

ReleaseAuthority(p) ==
    /\ AuthorityHeld(p)
    /\ lockStage' = "control"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

ReleaseControl(p) ==
    /\ ControlHeld(p)
    /\ lockStage' = "common"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

ReleaseCommon(p) ==
    /\ lockOwner = p /\ lockStage = "common"
    /\ lockOwner' = NoProcess /\ lockStage' = "free"
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  authorityRevision, freshAuthorityRevision, authorityRechecked,
                  casExpected, casObserved, casBaselineRevision, casResult>>

Acquire(p) ==
    /\ sessionStatus \in {"absent", "released"}
    /\ attemptGeneration < MaxRevision
    /\ ControlHeld(p)
    /\ \A q \in Processes: writerPhase[q] # "accepted"
    /\ activeAttempt' = p
    /\ attemptGeneration' = attemptGeneration + 1
    /\ fence' = fence + 1
    /\ controlRevision' = 1
    /\ sessionStatus' = "held"
    /\ forwardChild' = NoChild
    /\ rollbackChild' = NoChild
    /\ forwardFailed' = FALSE
    /\ terminalTarget' = NoTarget
    /\ terminalVerified' = FALSE
    /\ freshRuntimeVerified' = FALSE
    /\ writerPhase' = [q \in Processes |->
          IF writerPhase[q] = "requested" THEN "rejected" ELSE writerPhase[q]]
    /\ authorityRevision' = fence + 1
    /\ freshAuthorityRevision' = 0
    /\ authorityRechecked' = FALSE
    /\ UNCHANGED <<writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, casExpected, casObserved,
                  casBaselineRevision, casResult>>

BindForward(p) ==
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ forwardChild = NoChild
    /\ controlRevision < MaxRevision
    /\ forwardChild' = ForwardId(p)
    /\ controlRevision' = controlRevision + 1
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  rollbackChild, forwardFailed, terminalTarget,
                  terminalVerified, freshRuntimeVerified, writerPhase,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

ForwardFailure(p) ==
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ forwardChild # NoChild
    /\ forwardFailed = FALSE
    /\ forwardFailed' = TRUE
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations,
                  writerTarget, lockOwner, lockStage, authorityRevision,
                  freshAuthorityRevision, authorityRechecked, casExpected,
                  casObserved, casBaselineRevision, casResult>>

BindRollback(p) ==
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ forwardFailed
    /\ forwardChild # NoChild
    /\ rollbackChild = NoChild
    /\ terminalTarget = NoTarget
    /\ ~terminalVerified
    /\ controlRevision < MaxRevision
    /\ rollbackChild' = RollbackId(p)
    /\ controlRevision' = controlRevision + 1
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  forwardChild, forwardFailed, terminalTarget,
                  terminalVerified, freshRuntimeVerified, writerPhase,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

VerifyTerminal(p, target) ==
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ target \in Targets
    /\ IF target = "new"
          THEN /\ forwardChild # NoChild
               /\ ~forwardFailed
          ELSE rollbackChild # NoChild
    /\ ~terminalVerified
    /\ terminalTarget' = target
    /\ terminalVerified' = TRUE
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  freshRuntimeVerified, writerPhase, writerAcceptedStatus,
                  writerMutations, writerTarget, lockOwner, lockStage,
                  authorityRevision, freshAuthorityRevision, authorityRechecked,
                  casExpected, casObserved, casBaselineRevision, casResult>>

BeginReopen(p) ==
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ terminalVerified
    /\ terminalTarget \in Targets
    /\ authorityRechecked
    /\ controlRevision < MaxRevision
    /\ sessionStatus' = "releasing"
    /\ controlRevision' = controlRevision + 1
    /\ UNCHANGED <<activeAttempt, attemptGeneration, fence, forwardChild,
                  rollbackChild, forwardFailed, terminalTarget,
                  terminalVerified, freshRuntimeVerified, writerPhase,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

FreshRuntimeRead(p) ==
    /\ sessionStatus = "releasing"
    /\ activeAttempt = p
    /\ AuthorityHeld(p)
    /\ freshRuntimeVerified' = TRUE
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, writerPhase,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

CompleteReopen(p) ==
    /\ sessionStatus = "releasing"
    /\ activeAttempt = p
    /\ ControlHeld(p)
    /\ terminalVerified
    /\ freshRuntimeVerified
    /\ controlRevision < MaxRevision
    /\ sessionStatus' = "released"
    /\ controlRevision' = controlRevision + 1
    /\ UNCHANGED <<activeAttempt, attemptGeneration, fence, forwardChild,
                  rollbackChild, forwardFailed, terminalTarget,
                  terminalVerified, freshRuntimeVerified, writerPhase,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

MarkAmbiguous(p) ==
    /\ activeAttempt = p
    /\ sessionStatus \in {"held", "releasing"}
    /\ ControlHeld(p)
    /\ \A q \in Processes: writerPhase[q] # "accepted"
    /\ controlRevision < MaxRevision
    /\ sessionStatus' = "ambiguous"
    /\ controlRevision' = controlRevision + 1
    /\ writerPhase' = [q \in Processes |->
          IF writerPhase[q] = "requested" THEN "rejected" ELSE writerPhase[q]]
    /\ UNCHANGED <<activeAttempt, attemptGeneration, fence, forwardChild,
                  rollbackChild, forwardFailed, terminalTarget,
                  terminalVerified, freshRuntimeVerified,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

ObserveAuthority(p, revision) ==
    /\ ControlHeld(p)
    /\ revision \in 0..MaxRevision
    /\ freshAuthorityRevision' = revision
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, authorityRechecked,
                  casExpected, casObserved, casBaselineRevision, casResult>>

RecheckHeld(p) ==
    /\ ControlHeld(p)
    /\ sessionStatus = "held"
    /\ activeAttempt = p
    /\ freshAuthorityRevision = authorityRevision
    /\ authorityRechecked' = TRUE
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  casExpected, casObserved, casBaselineRevision, casResult>>

RejectStaleCAS(p, expected) ==
    /\ ControlHeld(p)
    /\ sessionStatus # "absent"
    /\ expected \in 0..MaxRevision
    /\ expected # controlRevision
    /\ casExpected' = [casExpected EXCEPT ![p] = expected]
    /\ casObserved' = [casObserved EXCEPT ![p] = controlRevision]
    /\ casBaselineRevision' = [casBaselineRevision EXCEPT ![p] = controlRevision]
    /\ casResult' = [casResult EXCEPT ![p] = "rejected"]
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerPhase, writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked>>

RequestWrite(p) ==
    /\ writerPhase[p] = "idle"
    /\ sessionStatus # "ambiguous"
    /\ AuthorityHeld(p)
    /\ writerPhase' = [writerPhase EXCEPT ![p] = "requested"]
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

AcceptWrite(p) ==
    /\ writerPhase[p] = "requested"
    /\ sessionStatus \in {"absent", "released"}
    /\ AuthorityHeld(p)
    /\ writerPhase' = [writerPhase EXCEPT ![p] = "accepted"]
    /\ writerAcceptedStatus' = [writerAcceptedStatus EXCEPT ![p] = sessionStatus]
    /\ writerMutations' = writerMutations + 1
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerTarget, lockOwner, lockStage, authorityRevision,
                  freshAuthorityRevision, authorityRechecked, casExpected,
                  casObserved, casBaselineRevision, casResult>>

RejectWrite(p) ==
    /\ writerPhase[p] = "requested"
    /\ sessionStatus \in UnsafeStatuses
    /\ AuthorityHeld(p)
    /\ writerPhase' = [writerPhase EXCEPT ![p] = "rejected"]
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

FinishWrite(p) ==
    /\ writerPhase[p] \in {"accepted", "rejected"}
    /\ AuthorityHeld(p)
    /\ writerPhase' = [writerPhase EXCEPT ![p] = "done"]
    /\ UNCHANGED <<sessionStatus, activeAttempt, attemptGeneration, fence,
                  controlRevision, forwardChild, rollbackChild, forwardFailed,
                  terminalTarget, terminalVerified, freshRuntimeVerified,
                  writerAcceptedStatus, writerMutations, writerTarget,
                  lockOwner, lockStage, authorityRevision, freshAuthorityRevision,
                  authorityRechecked, casExpected, casObserved,
                  casBaselineRevision, casResult>>

Next ==
    \/ (\E p \in Processes:
          Acquire(p) \/ BindForward(p) \/ ForwardFailure(p) \/ BindRollback(p)
          \/ VerifyTerminal(p, "new") \/ VerifyTerminal(p, "rollback")
          \/ BeginReopen(p) \/ FreshRuntimeRead(p) \/ CompleteReopen(p)
          \/ MarkAmbiguous(p) \/ ObserveAuthority(p, 0)
          \/ ObserveAuthority(p, 1) \/ ObserveAuthority(p, 2)
          \/ ObserveAuthority(p, 3) \/ RecheckHeld(p)
          \/ RejectStaleCAS(p, 0) \/ RejectStaleCAS(p, 1)
          \/ RejectStaleCAS(p, 2) \/ RejectStaleCAS(p, 3)
          \/ RequestWrite(p) \/ AcceptWrite(p)
          \/ RejectWrite(p) \/ FinishWrite(p))
    \/ (\E p \in Processes:
          AcquireCommon(p) \/ AcquireControl(p) \/ AcquireAuthority(p)
          \/ ReleaseAuthority(p) \/ ReleaseControl(p) \/ ReleaseCommon(p))
    \/ UNCHANGED vars

TypeOK ==
    /\ sessionStatus \in Statuses
    /\ activeAttempt \in Processes \cup {NoProcess}
    /\ attemptGeneration \in 0..MaxRevision
    /\ fence \in 0..MaxRevision
    /\ controlRevision \in 0..MaxRevision
    /\ forwardChild \in {NoChild} \cup {ForwardId(p): p \in Processes}
    /\ rollbackChild \in {NoChild} \cup {RollbackId(p): p \in Processes}
    /\ forwardFailed \in BOOLEAN
    /\ terminalTarget \in TerminalResults
    /\ terminalVerified \in BOOLEAN
    /\ freshRuntimeVerified \in BOOLEAN
    /\ writerPhase \in [Processes -> WriterPhases]
    /\ writerAcceptedStatus \in [Processes -> (Statuses \cup {"none"})]
    /\ writerMutations \in 0..MaxRevision
    /\ writerTarget \in [Processes -> {"authority"}]
    /\ lockOwner \in Processes \cup {NoProcess}
    /\ lockStage \in LockStages
    /\ authorityRevision \in 0..MaxRevision
    /\ freshAuthorityRevision \in 0..MaxRevision
    /\ authorityRechecked \in BOOLEAN
    /\ casExpected \in [Processes -> 0..MaxRevision]
    /\ casObserved \in [Processes -> 0..MaxRevision]
    /\ casBaselineRevision \in [Processes -> 0..MaxRevision]
    /\ casResult \in [Processes -> CASResults]

OneActiveSession ==
    Cardinality({p \in Processes:
        sessionStatus \in UnsafeStatuses /\ activeAttempt = p}) <= 1

IdentityStable ==
    sessionStatus # "absent" =>
        /\ activeAttempt # NoProcess
        /\ fence > 0
        /\ attemptGeneration > 0

ChildIdentityStable ==
    /\ forwardChild # NoChild => forwardChild \in {ForwardId(p): p \in Processes}
    /\ rollbackChild # NoChild => rollbackChild \in {RollbackId(p): p \in Processes}
    /\ (forwardChild # NoChild /\ rollbackChild # NoChild) =>
        forwardChild # rollbackChild

NoUnheldRollbackGap ==
    rollbackChild # NoChild => sessionStatus \in {"held", "releasing", "released", "ambiguous"}

ReleaseEvidence ==
    sessionStatus = "released" => terminalVerified /\ freshRuntimeVerified

WriteFence ==
    \A p \in Processes:
        writerPhase[p] = "accepted" => writerAcceptedStatus[p] \in {"absent", "released"}

AmbiguousIsWriteClosed ==
    sessionStatus = "ambiguous" =>
        \A p \in Processes: writerPhase[p] \notin {"requested", "accepted"}

LockOwnership ==
    /\ lockStage = "free" <=> lockOwner = NoProcess
    /\ lockStage # "free" => lockOwner \in Processes

LockOrder ==
    lockStage \in LockStages

RecheckEvidence ==
    sessionStatus = "releasing" => authorityRechecked

StaleCASRejected ==
    \A p \in Processes:
        casResult[p] = "rejected" => casExpected[p] # casObserved[p]

WriterDrainOnAcquire ==
    sessionStatus = "held" =>
        \A p \in Processes: writerPhase[p] # "accepted"

CasBounded ==
    controlRevision <= MaxRevision /\ fence <= MaxRevision

Spec == Init /\ [][Next]_vars

THEOREM Spec => []TypeOK
THEOREM Spec => []OneActiveSession
THEOREM Spec => []IdentityStable
THEOREM Spec => []ChildIdentityStable
THEOREM Spec => []NoUnheldRollbackGap
THEOREM Spec => []ReleaseEvidence
THEOREM Spec => []WriteFence
THEOREM Spec => []AmbiguousIsWriteClosed
THEOREM Spec => []CasBounded
THEOREM Spec => []LockOwnership
THEOREM Spec => []LockOrder
THEOREM Spec => []RecheckEvidence
THEOREM Spec => []StaleCASRejected
THEOREM Spec => []WriterDrainOnAcquire

=============================================================================
