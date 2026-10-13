--------------------------- MODULE HandoffctlRun ---------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, TLC

(*
Best-effort model guidance for wrapped external effects. A bound command runs
only after preflight and one durable execution fence. Once an external effect
occurs, a privacy-safe journal record is durably written before task recording
or live reconciliation. Either post-command stage may fail, but neither can
erase the journal evidence; a failed fence completion retains its fence.
*)

CONSTANTS Processes

ASSUME Processes # {}
NoReservation == "no_reservation"
EvidenceBackends == {"git", "sqlite"}
ExecutionIdentity(p) ==
    [task_id |-> p, owner |-> p, argv_sha256 |-> p, execution_id |-> p]
ExecutionIdentities == {ExecutionIdentity(p) : p \in Processes}

Phases == {"preflight", "reserved", "effected", "journaled", "recorded",
           "released", "done"}
Results ==
    {"pending", "preflight_rejected", "completed", "task_record_failed",
     "journal_failed", "reservation_completion_failed", "post_reconcile_failed"}

VARIABLES phase, preflightReady, reservation, admitted, externalEffect,
          journal, evidence, taskRecord, result

vars == <<phase, preflightReady, reservation, admitted, externalEffect,
          journal, evidence, taskRecord, result>>

Init ==
    /\ phase = [p \in Processes |-> "preflight"]
    /\ preflightReady \in [Processes -> BOOLEAN]
    /\ reservation = NoReservation
    /\ admitted = [p \in Processes |-> FALSE]
    /\ externalEffect = [p \in Processes |-> FALSE]
    /\ journal = [p \in Processes |-> FALSE]
    /\ evidence = [b \in EvidenceBackends |-> {}]
    /\ taskRecord = [p \in Processes |-> FALSE]
    /\ result = [p \in Processes |-> "pending"]

RejectPreflight(p) ==
    /\ phase[p] = "preflight"
    /\ ~preflightReady[p]
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "preflight_rejected"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

ReserveExecution(p) ==
    /\ phase[p] = "preflight"
    /\ preflightReady[p]
    /\ reservation = NoReservation
    /\ phase' = [phase EXCEPT ![p] = "reserved"]
    /\ reservation' = p
    /\ admitted' = [admitted EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, evidence, taskRecord, result>>

RunExternal(p) ==
    /\ phase[p] = "reserved"
    /\ reservation = p
    /\ admitted[p]
    /\ phase' = [phase EXCEPT ![p] = "effected"]
    /\ externalEffect' = [externalEffect EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, reservation, admitted, journal, evidence, taskRecord, result>>

RecordJournal(p) ==
    /\ phase[p] = "effected"
    /\ phase' = [phase EXCEPT ![p] = "journaled"]
    /\ \E b \in EvidenceBackends:
        /\ journal' = [journal EXCEPT ![p] = TRUE]
        /\ evidence' = [evidence EXCEPT ![b] = @ \cup {ExecutionIdentity(p)}]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   taskRecord, result>>

FailJournal(p) ==
    /\ phase[p] = "effected"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "journal_failed"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

RecordTask(p) ==
    /\ phase[p] = "journaled"
    /\ phase' = [phase EXCEPT ![p] = "recorded"]
    /\ taskRecord' = [taskRecord EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, result>>

FailTaskRecord(p) ==
    /\ phase[p] = "journaled"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "task_record_failed"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

ReleaseReservation(p) ==
    /\ phase[p] = "recorded"
    /\ reservation = p
    /\ phase' = [phase EXCEPT ![p] = "released"]
    /\ reservation' = NoReservation
    /\ UNCHANGED <<preflightReady, admitted, externalEffect, journal, evidence, taskRecord, result>>

FailReservationCompletion(p) ==
    /\ phase[p] = "recorded"
    /\ reservation = p
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "reservation_completion_failed"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

FinishReconcile(p) ==
    /\ phase[p] = "released"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "completed"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

FailReconcile(p) ==
    /\ phase[p] = "released"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "post_reconcile_failed"]
    /\ UNCHANGED <<preflightReady, reservation, admitted, externalEffect,
                   journal, evidence, taskRecord>>

RecoverRecordedFence(p) ==
    /\ phase[p] = "done"
    /\ result[p] \in {"task_record_failed", "reservation_completion_failed"}
    /\ reservation = p
    /\ \E b \in EvidenceBackends: ExecutionIdentity(p) \in evidence[b]
    /\ reservation' = NoReservation
    /\ UNCHANGED <<phase, preflightReady, admitted, externalEffect, journal, evidence, taskRecord, result>>

RetainUnknownFence(p) ==
    /\ phase[p] = "done"
    /\ result[p] = "journal_failed"
    /\ reservation = p
    /\ UNCHANGED vars

Step(p) ==
    RejectPreflight(p) \/ ReserveExecution(p) \/ RunExternal(p) \/
    RecordJournal(p) \/ FailJournal(p) \/ RecordTask(p) \/ FailTaskRecord(p) \/
    ReleaseReservation(p) \/ FailReservationCompletion(p) \/
    FinishReconcile(p) \/ FailReconcile(p) \/ RecoverRecordedFence(p) \/
    RetainUnknownFence(p)

Quiescent ==
    /\ \A p \in Processes: phase[p] = "done"
    /\ UNCHANGED vars

Next == (\E p \in Processes: Step(p)) \/ Quiescent

Fairness == \A p \in Processes: WF_vars(Step(p))

Spec == Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ phase \in [Processes -> Phases]
    /\ preflightReady \in [Processes -> BOOLEAN]
    /\ reservation \in Processes \cup {NoReservation}
    /\ admitted \in [Processes -> BOOLEAN]
    /\ externalEffect \in [Processes -> BOOLEAN]
    /\ journal \in [Processes -> BOOLEAN]
    /\ evidence \in [EvidenceBackends -> SUBSET ExecutionIdentities]
    /\ taskRecord \in [Processes -> BOOLEAN]
    /\ result \in [Processes -> Results]

NoEffectWithoutPreflight ==
    \A p \in Processes: externalEffect[p] => preflightReady[p]

NoEffectWithoutReservation ==
    \A p \in Processes: externalEffect[p] => admitted[p]

LiveReservationMatchesReservedPhase ==
    reservation # NoReservation =>
        \/ phase[reservation] \in {"reserved", "effected", "journaled", "recorded"}
        \/ /\ phase[reservation] = "done"
           /\ result[reservation] \in {"journal_failed", "task_record_failed", "reservation_completion_failed"}

JournalPrecedesTaskRecord ==
    \A p \in Processes: taskRecord[p] => journal[p]

EvidenceMatchesRecordedExecution ==
    \A b \in EvidenceBackends:
        \A p \in Processes: ExecutionIdentity(p) \in evidence[b] => journal[p]

CompletedEffectsRemainAuditable ==
    \A p \in Processes:
        (externalEffect[p] /\ phase[p] \in {"journaled", "recorded", "released", "done"})
        => journal[p] \/ reservation = p

EventualCompletion == <>(
    (\A p \in Processes: phase[p] = "done") \/
    (\E p \in Processes:
        result[p] = "journal_failed" /\ reservation = p)
)

=============================================================================
