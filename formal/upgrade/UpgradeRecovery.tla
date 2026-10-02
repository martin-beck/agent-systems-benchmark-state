---- MODULE UpgradeRecovery ----
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Naturals, FiniteSets, TLC

CONSTANTS Operations, Releases, Backends
Phases == {"discover", "preflight", "quiesce", "backup", "stage", "commit", "validate", "reopen"}
Targets == {"new", "rollback"}
Barriers == {"none", "held", "releasing", "released", "ambiguous"}
Journals == {"planned", "running", "rollback_started", "rollback_verified", "completed", "rolled_back", "safe_mode"}

VARIABLES phase, target, backend, barrier, journal, runtime, backup, fence, available
vars == <<phase, target, backend, barrier, journal, runtime, backup, fence, available>>

Init ==
    /\ phase = [op \in Operations |-> "discover"]
    /\ target = [op \in Operations |-> "new"]
    /\ backend = [op \in Operations |-> IF op = "op1" THEN "git" ELSE "sqlite"]
    /\ barrier = [op \in Operations |-> "none"]
    /\ journal = [op \in Operations |-> "planned"]
    /\ runtime = [op \in Operations |-> "old"]
    /\ backup = [op \in Operations |-> FALSE]
    /\ fence = [op \in Operations |-> 0]
    /\ available = [op \in Operations |-> TRUE]

Advance(op, from, to) ==
    /\ phase[op] = from
    /\ phase' = [phase EXCEPT ![op] = to]
    /\ journal' = [journal EXCEPT ![op] = "running"]
    /\ UNCHANGED <<target, backend, barrier, runtime, backup, fence, available>>

Preflight(op) ==
    /\ phase[op] = "discover"
    /\ phase' = [phase EXCEPT ![op] = "preflight"]
    /\ journal' = [journal EXCEPT ![op] = "running"]
    /\ fence' = [fence EXCEPT ![op] = @ + 1]
    /\ UNCHANGED <<target, backend, barrier, runtime, backup, available>>
Quiesce(op) ==
    /\ phase[op] = "preflight"
    /\ barrier' = [barrier EXCEPT ![op] = "held"]
    /\ phase' = [phase EXCEPT ![op] = "quiesce"]
    /\ journal' = [journal EXCEPT ![op] = "running"]
    /\ UNCHANGED <<target, backend, runtime, backup, fence, available>>
BackupGit(op) ==
    /\ backend[op] = "git"
    /\ phase[op] = "quiesce" /\ barrier[op] = "held"
    /\ backup' = [backup EXCEPT ![op] = TRUE]
    /\ phase' = [phase EXCEPT ![op] = "backup"]
    /\ journal' = [journal EXCEPT ![op] = "running"]
    /\ UNCHANGED <<target, backend, barrier, runtime, fence, available>>
BackupSQLite(op) ==
    /\ backend[op] = "sqlite"
    /\ phase[op] = "quiesce" /\ barrier[op] = "held"
    /\ backup' = [backup EXCEPT ![op] = TRUE]
    /\ phase' = [phase EXCEPT ![op] = "backup"]
    /\ journal' = [journal EXCEPT ![op] = "running"]
    /\ UNCHANGED <<target, backend, barrier, runtime, fence, available>>
Stage(op) ==
    /\ phase[op] = "backup" /\ backup[op]
    /\ phase' = [phase EXCEPT ![op] = "stage"]
    /\ UNCHANGED <<target, backend, barrier, journal, runtime, backup, fence, available>>
Commit(op) ==
    /\ phase[op] = "stage" /\ backup[op] /\ barrier[op] = "held"
    /\ phase' = [phase EXCEPT ![op] = "commit"]
    /\ runtime' = [runtime EXCEPT ![op] = "new"]
    /\ UNCHANGED <<target, backend, barrier, journal, backup, fence, available>>
Validate(op) ==
    /\ phase[op] = "commit" /\ runtime[op] = "new"
    /\ phase' = [phase EXCEPT ![op] = "validate"]
    /\ UNCHANGED <<target, backend, barrier, journal, runtime, backup, fence, available>>
Reopen(op) ==
    /\ phase[op] = "validate" /\ barrier[op] = "held"
    /\ phase' = [phase EXCEPT ![op] = "reopen"]
    /\ barrier' = [barrier EXCEPT ![op] = "released"]
    /\ journal' = [journal EXCEPT ![op] = "completed"]
    /\ UNCHANGED <<target, backend, runtime, backup, fence, available>>
StartRollback(op) ==
    /\ journal[op] \in {"running", "safe_mode"}
    /\ backup[op] /\ barrier[op] = "held"
    /\ target' = [target EXCEPT ![op] = "rollback"]
    /\ journal' = [journal EXCEPT ![op] = "rollback_started"]
    /\ UNCHANGED <<phase, backend, barrier, runtime, backup, fence, available>>
VerifyRollback(op) ==
    /\ journal[op] = "rollback_started" /\ target[op] = "rollback"
    /\ journal' = [journal EXCEPT ![op] = "rollback_verified"]
    /\ UNCHANGED <<phase, target, backend, barrier, runtime, backup, fence, available>>
ReleaseRollback(op) ==
    /\ journal[op] = "rollback_verified" /\ barrier[op] = "held"
    /\ barrier' = [barrier EXCEPT ![op] = "released"]
    /\ journal' = [journal EXCEPT ![op] = "rolled_back"]
    /\ runtime' = [runtime EXCEPT ![op] = "old"]
    /\ UNCHANGED <<phase, target, backend, backup, fence, available>>
Recover(op) ==
    \/ ( /\ journal[op] = "rollback_verified" /\ barrier[op] = "released"
         /\ journal' = [journal EXCEPT ![op] = "rolled_back"]
         /\ runtime' = [runtime EXCEPT ![op] = "old"]
         /\ UNCHANGED <<phase, target, backend, barrier, backup, fence, available>> )
    \/ ( /\ journal[op] = "safe_mode" /\ barrier[op] = "ambiguous" /\ backup[op]
         /\ target' = [target EXCEPT ![op] = "rollback"]
         /\ barrier' = [barrier EXCEPT ![op] = "held"]
         /\ journal' = [journal EXCEPT ![op] = "rollback_started"]
         /\ UNCHANGED <<phase, backend, runtime, backup, fence, available>> )
Crash(op) ==
    /\ barrier[op] = "held"
    /\ journal[op] \in {"running", "rollback_verified"}
    /\ barrier' = [barrier EXCEPT ![op] = "ambiguous"]
    /\ IF journal[op] = "running"
          THEN journal' = [journal EXCEPT ![op] = "safe_mode"]
          ELSE UNCHANGED journal
    /\ UNCHANGED <<phase, target, backend, runtime, backup, fence, available>>

Next == \E op \in Operations:
    Preflight(op) \/ Quiesce(op) \/ BackupGit(op) \/ BackupSQLite(op) \/ Stage(op) \/ Commit(op) \/
    Validate(op) \/ Reopen(op) \/ StartRollback(op) \/ VerifyRollback(op) \/
    ReleaseRollback(op) \/ Recover(op) \/ Crash(op) \/ UNCHANGED vars

FunctionalAvailability == \A op \in Operations: available[op]
NoReplacementBeforeBackup == \A op \in Operations: runtime[op] = "new" => backup[op]
ReleaseOrder == \A op \in Operations: barrier[op] = "released" => journal[op] \in {"completed", "rolled_back"}
RollbackProof == \A op \in Operations: journal[op] = "rolled_back" => target[op] = "rollback" /\ runtime[op] = "old"
RollbackRequiresBackup == \A op \in Operations: journal[op] = "rolled_back" => backup[op]
TypeInvariant ==
    /\ phase \in [Operations -> Phases]
    /\ target \in [Operations -> Targets]
    /\ backend \in [Operations -> Backends]
    /\ barrier \in [Operations -> Barriers]
    /\ journal \in [Operations -> Journals]
    /\ runtime \in [Operations -> Releases]
    /\ backup \in [Operations -> BOOLEAN]
    /\ fence \in [Operations -> Nat]
    /\ available \in [Operations -> BOOLEAN]

Spec == Init /\ [][Next]_vars
THEOREM Spec => []TypeInvariant
THEOREM Spec => []FunctionalAvailability
THEOREM Spec => []NoReplacementBeforeBackup
THEOREM Spec => []ReleaseOrder
THEOREM Spec => []RollbackProof
THEOREM Spec => []RollbackRequiresBackup
====
