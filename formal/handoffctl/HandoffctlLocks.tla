------------------------- MODULE HandoffctlLocks -------------------------
EXTENDS FiniteSets, TLC

(*
Reader/writer refinement model for snapshots and mutations using one lock below
Git's common directory. Three processes are enough to include two simultaneous
readers in separate worktrees and one competing writer.
*)

CONSTANTS Processes, Worktrees, Repository, CommonLock, NoWriter

ASSUME /\ Processes # {}
       /\ Worktrees # {}
       /\ NoWriter \notin Processes

Modes == {"read", "write"}
Phases == {"waiting", "holding", "done"}

LockPath(_worktree) == <<Repository, CommonLock>>
Results == {"pending", "completed", "lock_timeout"}

VARIABLES mode, worktree, phase, writer, readers, result

vars == <<mode, worktree, phase, writer, readers, result>>

Init ==
    /\ mode \in [Processes -> Modes]
    /\ worktree \in [Processes -> Worktrees]
    /\ phase = [p \in Processes |-> "waiting"]
    /\ writer = NoWriter
    /\ readers = {}
    /\ result = [p \in Processes |-> "pending"]

CanAcquire(p) ==
    IF mode[p] = "read"
    THEN writer = NoWriter
    ELSE writer = NoWriter /\ readers = {}

AcquireRead(p) ==
    /\ phase[p] = "waiting"
    /\ mode[p] = "read"
    /\ writer = NoWriter
    /\ readers' = readers \cup {p}
    /\ phase' = [phase EXCEPT ![p] = "holding"]
    /\ UNCHANGED <<mode, worktree, writer, result>>

AcquireWrite(p) ==
    /\ phase[p] = "waiting"
    /\ mode[p] = "write"
    /\ writer = NoWriter
    /\ readers = {}
    /\ writer' = p
    /\ phase' = [phase EXCEPT ![p] = "holding"]
    /\ UNCHANGED <<mode, worktree, readers, result>>

WaitTimeout(p) ==
    /\ phase[p] = "waiting"
    /\ ~CanAcquire(p)
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "lock_timeout"]
    /\ UNCHANGED <<mode, worktree, writer, readers>>

Wait(p) ==
    AcquireRead(p) \/ AcquireWrite(p) \/ WaitTimeout(p)

ReleaseRead(p) ==
    /\ phase[p] = "holding"
    /\ mode[p] = "read"
    /\ p \in readers
    /\ readers' = readers \ {p}
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "completed"]
    /\ UNCHANGED <<mode, worktree, writer>>

ReleaseWrite(p) ==
    /\ phase[p] = "holding"
    /\ mode[p] = "write"
    /\ writer = p
    /\ writer' = NoWriter
    /\ phase' = [phase EXCEPT ![p] = "done"]
    /\ result' = [result EXCEPT ![p] = "completed"]
    /\ UNCHANGED <<mode, worktree, readers>>

Release(p) ==
    ReleaseRead(p) \/ ReleaseWrite(p)

Quiescent ==
    /\ \A p \in Processes: phase[p] = "done"
    /\ UNCHANGED vars

Next ==
    (\E p \in Processes: Wait(p) \/ Release(p))
    \/ Quiescent

Fairness ==
    /\ \A p \in Processes: WF_vars(Wait(p))
    /\ \A p \in Processes: WF_vars(Release(p))

Spec ==
    Init /\ [][Next]_vars /\ Fairness

TypeOK ==
    /\ worktree \in [Processes -> Worktrees]
    /\ mode \in [Processes -> Modes]
    /\ phase \in [Processes -> Phases]
    /\ writer \in Processes \cup {NoWriter}
    /\ readers \subseteq Processes
    /\ result \in [Processes -> Results]

SharedRepositoryLock ==
    \A left \in Worktrees:
        \A right \in Worktrees:
            LockPath(left) = LockPath(right)


ReaderWriterSafety ==
    /\ writer # NoWriter => readers = {}
    /\ \A p \in readers: mode[p] = "read"
    /\ writer # NoWriter => mode[writer] = "write"

HoldingMatchesLock ==
    \A p \in Processes:
        (phase[p] = "holding") <=>
        (p \in readers \/ writer = p)

EventualCompletion ==
    <>(\A p \in Processes: phase[p] = "done")

=============================================================================
