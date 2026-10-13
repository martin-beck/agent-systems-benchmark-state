--------------------- MODULE HandoffctlPredicateLedger ---------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Naturals, Sequences, TLC

(*******************************************************************************
Bounded contract for predicate-aware `handoffctl accept`.

`candidateRef` and `candidateDigest` are deliberately independent state
variables. The finite candidate domain is their complete Cartesian product:
the same reference may name a changed artifact digest, and different
references may name identical artifact content. A process supplies one fixed
request; TLC explores both owners, current/stale revisions, all candidate
identities, both predicates, valid/invalid evidence, and the presence or
absence of explicit --reopen.
*******************************************************************************)

CONSTANTS Processes, Actors, Predicates, NoActor, NoRef, NoDigest

VARIABLES
    status,
    owner,
    revision,
    candidateRef,
    candidateDigest,
    ledger,
    retiredEvidence,
    candidateChanges,
    lastCandidateChangeWasReopen,
    lastCandidateChangeKind,
    pc,
    action,
    requestedActor,
    expectedRevision,
    requestedPredicate,
    requestedRef,
    requestedDigest,
    requestedReopen,
    evidenceValid,
    result

Refs == {"ref-a", "ref-b"}
Digests == {"digest-a", "digest-b"}
StepStatuses == {"pass", "stale"}
Actions == {"accept", "release_done"}
Phases == {"ready", "done"}
Results == {"pending", "accepted", "rejected"}

NoCandidate(ref, digest) ==
    /\ ref = NoRef
    /\ digest = NoDigest

CandidateIdentity(ref, digest) ==
    /\ ref \in Refs
    /\ digest \in Digests

CandidateMatches(ref, digest) ==
    /\ ref = candidateRef
    /\ digest = candidateDigest

EvidenceId(row) ==
    [predicate |-> row.predicate, ref |-> row.ref, digest |-> row.digest]

Row ==
    [predicate : Predicates, status : StepStatuses, ref : Refs, digest : Digests]

InitialPassingRow(ref, digest) ==
    [predicate |-> "predicate-a", status |-> "pass", ref |-> ref, digest |-> digest]

RowsFor(predicate) ==
    {ledger[i] : i \in {j \in 1..Len(ledger) : ledger[j].predicate = predicate}}

LiveRowsFor(predicate) ==
    {row \in RowsFor(predicate) : row.status = "pass"}

LedgerCoherent ==
    /\ \A i \in 1..Len(ledger): ledger[i] \in Row
    /\ \A i \in 1..Len(ledger): CandidateIdentity(ledger[i].ref, ledger[i].digest)
    /\ \A i \in 1..Len(ledger):
          ledger[i].status = "pass" => CandidateMatches(ledger[i].ref, ledger[i].digest)
    /\ \A i \in 1..Len(ledger):
          ledger[i].status = "stale" => ~CandidateMatches(ledger[i].ref, ledger[i].digest)
    /\ \A predicate \in Predicates: Cardinality(LiveRowsFor(predicate)) <= 1
    /\ candidateRef = NoRef <=> Len(ledger) = 0

PredicateComplete ==
    /\ candidateRef # NoRef
    /\ \A predicate \in Predicates: Cardinality(LiveRowsFor(predicate)) = 1

RECURSIVE RemovePredicate(_, _)
RemovePredicate(history, predicate) ==
    IF Len(history) = 0 THEN <<>>
    ELSE LET tail == RemovePredicate(SubSeq(history, 2, Len(history)), predicate) IN
         IF history[1].predicate = predicate THEN tail ELSE <<history[1]>> \o tail

MarkPassesStale(history) ==
    [i \in 1..Len(history) |->
        IF history[i].status = "pass"
        THEN [history[i] EXCEPT !.status = "stale"]
        ELSE history[i]]

RequestedRow(p) ==
    [predicate |-> requestedPredicate[p], status |-> "pass",
     ref |-> requestedRef[p], digest |-> requestedDigest[p]]

SameCandidate(p) ==
    /\ candidateRef # NoRef
    /\ CandidateMatches(requestedRef[p], requestedDigest[p])

CandidateChanged(p) ==
    /\ candidateRef # NoRef
    /\ ~CandidateMatches(requestedRef[p], requestedDigest[p])

CandidateChangeKind(p) ==
    IF requestedRef[p] # candidateRef /\ requestedDigest[p] = candidateDigest
    THEN "ref_only"
    ELSE IF requestedRef[p] = candidateRef /\ requestedDigest[p] # candidateDigest
         THEN "digest_only"
         ELSE "ref_and_digest"

RequestedCandidateHasNoStaleHistory(p) ==
    \A i \in 1..Len(ledger):
        ledger[i].status # "stale" \/
            ledger[i].ref # requestedRef[p] \/ ledger[i].digest # requestedDigest[p]

AcceptEnabled(p) ==
    /\ action[p] = "accept"
    /\ owner = requestedActor[p]
    /\ expectedRevision[p] = revision
    /\ evidenceValid[p]
    /\ (candidateRef = NoRef /\ ~requestedReopen[p])
       \/ (SameCandidate(p) /\ ~requestedReopen[p])
       \/ (CandidateChanged(p) /\ requestedReopen[p] /\ RequestedCandidateHasNoStaleHistory(p))

ReleaseDoneEnabled(p) ==
    /\ action[p] = "release_done"
    /\ owner = requestedActor[p]
    /\ PredicateComplete

NextLedger(p) ==
    IF candidateRef = NoRef THEN Append(ledger, RequestedRow(p))
    ELSE IF SameCandidate(p)
         THEN Append(RemovePredicate(ledger, requestedPredicate[p]), RequestedRow(p))
         ELSE Append(MarkPassesStale(ledger), RequestedRow(p))

vars ==
    <<status, owner, revision, candidateRef, candidateDigest, ledger, retiredEvidence,
      candidateChanges, lastCandidateChangeWasReopen, lastCandidateChangeKind, pc, action, requestedActor,
      expectedRevision, requestedPredicate, requestedRef, requestedDigest,
      requestedReopen, evidenceValid, result>>

Init ==
    /\ status = "in_progress"
    /\ owner = "owner-a"
    /\ revision = 0
    /\ \/ /\ candidateRef = NoRef
          /\ candidateDigest = NoDigest
          /\ ledger = <<>>
       \/ /\ CandidateIdentity(candidateRef, candidateDigest)
          /\ ledger = <<InitialPassingRow(candidateRef, candidateDigest)>>
    /\ LedgerCoherent
    /\ retiredEvidence = {EvidenceId(ledger[i]) :
          i \in {j \in 1..Len(ledger) : ledger[j].status = "stale"}}
    /\ candidateChanges = 0
    /\ lastCandidateChangeWasReopen = TRUE
    /\ lastCandidateChangeKind = "none"
    /\ pc = [p \in Processes |-> "ready"]
    /\ action \in [Processes -> Actions]
    /\ requestedActor \in [Processes -> Actors]
    /\ expectedRevision \in [Processes -> 0..2]
    /\ requestedPredicate \in [Processes -> Predicates]
    /\ requestedRef \in [Processes -> Refs]
    /\ requestedDigest \in [Processes -> Digests]
    /\ \A p \in Processes: CandidateIdentity(requestedRef[p], requestedDigest[p])
    /\ requestedReopen \in [Processes -> BOOLEAN]
    /\ evidenceValid \in [Processes -> BOOLEAN]
    /\ result = [p \in Processes |-> "pending"]

Accept(p) ==
    /\ pc[p] = "ready"
    /\ AcceptEnabled(p)
    /\ status' = status
    /\ owner' = owner
    /\ revision' = revision + 1
    /\ candidateRef' = requestedRef[p]
    /\ candidateDigest' = requestedDigest[p]
    /\ ledger' = NextLedger(p)
    /\ retiredEvidence' =
         IF CandidateChanged(p) THEN retiredEvidence \cup {EvidenceId(ledger[i]) :
             i \in 1..Len(ledger)} ELSE retiredEvidence
    /\ candidateChanges' = IF CandidateChanged(p) THEN candidateChanges + 1 ELSE candidateChanges
    /\ lastCandidateChangeWasReopen' =
         IF CandidateChanged(p) THEN requestedReopen[p] ELSE lastCandidateChangeWasReopen
    /\ lastCandidateChangeKind' =
         IF CandidateChanged(p) THEN CandidateChangeKind(p) ELSE lastCandidateChangeKind
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED <<action, requestedActor, expectedRevision, requestedPredicate,
                   requestedRef, requestedDigest, requestedReopen, evidenceValid>>

ReleaseDone(p) ==
    /\ pc[p] = "ready"
    /\ ReleaseDoneEnabled(p)
    /\ status' = "done"
    /\ owner' = NoActor
    /\ revision' = revision + 1
    /\ result' = [result EXCEPT ![p] = "accepted"]
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED <<candidateRef, candidateDigest, ledger, retiredEvidence, candidateChanges,
                   lastCandidateChangeWasReopen, lastCandidateChangeKind, action, requestedActor, expectedRevision,
                   requestedPredicate, requestedRef, requestedDigest, requestedReopen,
                   evidenceValid>>

Reject(p) ==
    /\ pc[p] = "ready"
    /\ ~AcceptEnabled(p)
    /\ ~ReleaseDoneEnabled(p)
    /\ result' = [result EXCEPT ![p] = "rejected"]
    /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED <<status, owner, revision, candidateRef, candidateDigest, ledger,
                   retiredEvidence, candidateChanges, lastCandidateChangeWasReopen, lastCandidateChangeKind, action,
                   requestedActor, expectedRevision, requestedPredicate, requestedRef,
                   requestedDigest, requestedReopen, evidenceValid>>

Quiescent ==
    /\ \A p \in Processes: pc[p] = "done"
    /\ UNCHANGED vars

Next == (\E p \in Processes: Accept(p) \/ ReleaseDone(p) \/ Reject(p)) \/ Quiescent

Spec == Init /\ [][Next]_vars

TypeOK ==
    /\ status \in {"in_progress", "done"}
    /\ owner \in Actors \cup {NoActor}
    /\ revision \in Nat
    /\ candidateRef \in Refs \cup {NoRef}
    /\ candidateDigest \in Digests \cup {NoDigest}
    /\ ledger \in Seq(Row)
    /\ retiredEvidence \subseteq [predicate : Predicates, ref : Refs, digest : Digests]
    /\ candidateChanges \in Nat
    /\ lastCandidateChangeWasReopen \in BOOLEAN
    /\ lastCandidateChangeKind \in {"none", "ref_only", "digest_only", "ref_and_digest"}
    /\ pc \in [Processes -> Phases]
    /\ action \in [Processes -> Actions]
    /\ requestedActor \in [Processes -> Actors]
    /\ expectedRevision \in [Processes -> Nat]
    /\ requestedPredicate \in [Processes -> Predicates]
    /\ requestedRef \in [Processes -> Refs]
    /\ requestedDigest \in [Processes -> Digests]
    /\ requestedReopen \in [Processes -> BOOLEAN]
    /\ evidenceValid \in [Processes -> BOOLEAN]
    /\ result \in [Processes -> Results]

CandidateBinding ==
    /\ NoCandidate(candidateRef, candidateDigest) \/ CandidateIdentity(candidateRef, candidateDigest)
    /\ LedgerCoherent

ExplicitReopenOnCandidateChange ==
    candidateChanges > 0 => lastCandidateChangeWasReopen

RefOnlyCandidateChangeRequiresReopen ==
    lastCandidateChangeKind = "ref_only" => lastCandidateChangeWasReopen

DigestOnlyCandidateChangeRequiresReopen ==
    lastCandidateChangeKind = "digest_only" => lastCandidateChangeWasReopen

RefAndDigestCandidateChangeRequiresReopen ==
    lastCandidateChangeKind = "ref_and_digest" => lastCandidateChangeWasReopen

StaleEvidenceIsHistorical ==
    \A i \in 1..Len(ledger): ledger[i].status = "stale" =>
        /\ EvidenceId(ledger[i]) \in retiredEvidence
        /\ ~CandidateMatches(ledger[i].ref, ledger[i].digest)

StaleEvidenceCannotComplete ==
    PredicateComplete => \A predicate \in Predicates:
        \E row \in LiveRowsFor(predicate): CandidateMatches(row.ref, row.digest)

DoneRequiresCompletePredicates ==
    status = "done" => PredicateComplete

AcceptPreservesLifecycleStatus ==
    \A p \in Processes:
        result[p] = "accepted" /\ action[p] = "accept" => status \in {"in_progress", "done"}

=============================================================================
