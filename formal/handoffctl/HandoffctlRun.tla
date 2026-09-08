--------------------------- MODULE HandoffctlRun ---------------------------
EXTENDS FiniteSets, TLC

(*
Refinement contract for wrapped external effects. A command runs only after
preflight succeeds. Once an external effect occurs, a privacy-safe journal
record is durably written before task recording or live reconciliation. Either
post-command stage may fail, but neither can erase the journal evidence.
*)

CONSTANTS Processes

ASSUME Processes # {}

Phases == {"preflight", "effected", "journaled", "recorded", "done"}
Results ==
    {"pending", "preflight_rejected", "completed", "task_record_failed",
     "post_reconcile_failed"}

VARIABLES phase, preflightReady, externalEffect, journal, taskRecord, result

vars == <<phase, preflightReady, externalEffect, journal, taskRecord, result>>

Init ==
    /\ phase = [p \in Processes |-> "preflight"]
    /\ preflightReady \in [Processes -> BOOLEAN]
    /\ externalEffect = [p \in Processes |-> FALSE]
    /\ journal = [p \in Processes |-> FALSE]
    /\ taskRecord = [p \in Processes |-> FALSE]
    /\ result = [p \in Processes |-> "pending"]

RejectPreflight(p) ==
    /\ phase[p] = "preflight"
    /\ ~preflightReady[p]
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "preflight_rejected"]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, taskRecord>>

RunExternal(p) ==
    /\ phase[p] = "preflight"
    /\ preflightReady[p]
    /\ phase' = [phase EXCEPT ![p] = "effected"]
    /\ externalEffect' = [externalEffect EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, journal, taskRecord, result>>

RecordJournal(p) ==
    /\ phase[p] = "effected"
    /\ phase' = [phase EXCEPT ![p] = "journaled"]
    /\ journal' = [journal EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, externalEffect, taskRecord, result>>

RecordTask(p) ==
    /\ phase[p] = "journaled"
    /\ phase' = [phase EXCEPT ![p] = "recorded"]
    /\ taskRecord' = [taskRecord EXCEPT ![p] = TRUE]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, result>>

FailTaskRecord(p) ==
    /\ phase[p] = "journaled"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "task_record_failed"]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, taskRecord>>

FinishReconcile(p) ==
    /\ phase[p] = "recorded"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "completed"]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, taskRecord>>

FailReconcile(p) ==
    /\ phase[p] = "recorded"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "post_reconcile_failed"]
    /\ UNCHANGED <<preflightReady, externalEffect, journal, taskRecord>>

Step(p) ==
    RejectPreflight(p) \/ RunExternal(p) \/ RecordJournal(p) \/
    RecordTask(p) \/ FailTaskRecord(p) \/ FinishReconcile(p) \/ FailReconcile(p)

Quiescent ==
    /\ \A p \in Processes: phase[p] = "done"
    /\ UNCHANGED vars

Next == (\E p \in Processes: Step(p)) \/ Quiescent

Fairness == \A p \in Processes: WF_vars(Step(p))

Spec == Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ phase \in [Processes -> Phases]
    /\ preflightReady \in [Processes -> BOOLEAN]
    /\ externalEffect \in [Processes -> BOOLEAN]
    /\ journal \in [Processes -> BOOLEAN]
    /\ taskRecord \in [Processes -> BOOLEAN]
    /\ result \in [Processes -> Results]

NoEffectWithoutPreflight ==
    \A p \in Processes: externalEffect[p] => preflightReady[p]

JournalPrecedesTaskRecord ==
    \A p \in Processes: taskRecord[p] => journal[p]

CompletedEffectsRemainAuditable ==
    \A p \in Processes:
        (externalEffect[p] /\ phase[p] \in {"journaled", "recorded", "done"})
        => journal[p]

EventualCompletion == <>(\A p \in Processes: phase[p] = "done")

=============================================================================
