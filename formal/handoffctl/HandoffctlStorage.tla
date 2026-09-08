------------------------- MODULE HandoffctlStorage -------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Naturals, TLC

(*
SQLite/Git backend refinement boundary.  A task mutation has one transactional
linearization point.  Migration prepares a complete SQLite database before one
durable selector switch.  Projections and optional publication occur only
after authority commits and cannot roll it back.
*)

CONSTANTS Processes
ASSUME Processes # {}

Backends == {"git", "sqlite"}
Phases == {"ready", "transaction", "committed", "projected", "done"}
NoOwner == "none"

VARIABLES backend, selector, databaseReady, migration, transactionOwner,
          revision, applied, phase, projectionRevision, publishedRevision

vars == <<backend, selector, databaseReady, migration, transactionOwner,
          revision, applied, phase, projectionRevision, publishedRevision>>

Init ==
    /\ backend \in Backends
    /\ selector = backend
    /\ databaseReady = (backend = "sqlite")
    /\ migration = "idle"
    /\ transactionOwner = NoOwner
    /\ revision = 0
    /\ applied = [p \in Processes |-> FALSE]
    /\ phase = [p \in Processes |-> "ready"]
    /\ projectionRevision = 0
    /\ publishedRevision = 0

Begin(p) ==
    /\ phase[p] = "ready"
    /\ transactionOwner = NoOwner
    /\ migration \notin {"to_sqlite", "to_git"}
    /\ transactionOwner' = p
    /\ phase' = [phase EXCEPT ![p] = "transaction"]
    /\ UNCHANGED <<backend, selector, databaseReady, migration, revision,
                    applied, projectionRevision, publishedRevision>>

Commit(p) ==
    /\ phase[p] = "transaction"
    /\ transactionOwner = p
    /\ transactionOwner' = NoOwner
    /\ revision' = revision + 1
    /\ applied' = [applied EXCEPT ![p] = TRUE]
    /\ phase' = [phase EXCEPT ![p] = "committed"]
    /\ UNCHANGED <<backend, selector, databaseReady, migration,
                    projectionRevision, publishedRevision>>

Project(p) ==
    /\ phase[p] = "committed"
    /\ projectionRevision' = revision
    /\ phase' = [phase EXCEPT ![p] = "projected"]
    /\ UNCHANGED <<backend, selector, databaseReady, migration,
                    transactionOwner, revision, applied, publishedRevision>>

Publish(p) ==
    /\ phase[p] = "projected"
    /\ publishedRevision' = projectionRevision
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ UNCHANGED <<backend, selector, databaseReady, migration,
                    transactionOwner, revision, applied, projectionRevision>>

SkipPublication(p) ==
    /\ phase[p] = "projected"
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ UNCHANGED <<backend, selector, databaseReady, migration,
                    transactionOwner, revision, applied,
                    projectionRevision, publishedRevision>>

PrepareToSQLite ==
    /\ backend = "git"
    /\ migration = "idle"
    /\ transactionOwner = NoOwner
    /\ databaseReady' = TRUE
    /\ migration' = "to_sqlite"
    /\ UNCHANGED <<backend, selector, transactionOwner, revision, applied,
                    phase, projectionRevision, publishedRevision>>

SwitchToSQLite ==
    /\ migration = "to_sqlite"
    /\ databaseReady
    /\ transactionOwner = NoOwner
    /\ backend' = "sqlite"
    /\ selector' = "sqlite"
    /\ migration' = "switched"
    /\ UNCHANGED <<databaseReady, transactionOwner, revision, applied,
                    phase, projectionRevision, publishedRevision>>

PrepareToGit ==
    /\ backend = "sqlite"
    /\ migration = "idle"
    /\ transactionOwner = NoOwner
    /\ migration' = "to_git"
    /\ UNCHANGED <<backend, selector, databaseReady, transactionOwner,
                    revision, applied, phase, projectionRevision, publishedRevision>>

SwitchToGit ==
    /\ migration = "to_git"
    /\ transactionOwner = NoOwner
    /\ backend' = "git"
    /\ selector' = "git"
    /\ migration' = "switched"
    /\ UNCHANGED <<databaseReady, transactionOwner, revision, applied,
                    phase, projectionRevision, publishedRevision>>

Step(p) == Begin(p) \/ Commit(p) \/ Project(p) \/ Publish(p) \/ SkipPublication(p)
Quiescent == /\ \A p \in Processes: phase[p] = "done"
             /\ UNCHANGED vars
Next == (\E p \in Processes: Step(p)) \/ PrepareToSQLite \/ SwitchToSQLite \/
        PrepareToGit \/ SwitchToGit \/ Quiescent

Fairness == /\ \A p \in Processes: WF_vars(Step(p))
            /\ WF_vars(SwitchToSQLite)
            /\ WF_vars(SwitchToGit)
Spec == Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ backend \in Backends
    /\ selector \in Backends
    /\ databaseReady \in BOOLEAN
    /\ migration \in {"idle", "to_sqlite", "to_git", "switched"}
    /\ transactionOwner \in Processes \cup {NoOwner}
    /\ revision \in Nat
    /\ applied \in [Processes -> BOOLEAN]
    /\ phase \in [Processes -> Phases]
    /\ projectionRevision \in 0..revision
    /\ publishedRevision \in 0..projectionRevision

SelectorMatchesAuthority == selector = backend
SQLiteAuthorityIsPrepared == backend = "sqlite" => databaseReady
MigrationFencesWriters == migration \in {"to_sqlite", "to_git"} => transactionOwner = NoOwner
SingleLinearization == revision = Cardinality({p \in Processes: applied[p]})
CommittedCannotBeUndone == \A p \in Processes: applied[p] => phase[p] # "ready"
EventualCommandsComplete == <>(\A p \in Processes: phase[p] = "done")
PreparedMigrationEventuallySwitches == [](
    migration \in {"to_sqlite", "to_git"} ~> migration = "switched")

=============================================================================
