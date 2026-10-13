------------------------- MODULE HandoffctlRetryCircuit -------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Naturals, FiniteSets, TLC

(*
Bounded unbound retry admission with the task owner and durable revision fence.
A reservation records its creating owner and pre-mutation revision. Its result
can resolve only while that owner still owns the task at the immediately
following revision. An intervening mutation therefore leaves the slot durable
but makes the result stale. Expired slots may be cleaned; expired-claim recovery
cannot clear ownership while any live unbound slot remains. Explicit circuit
recovery starts a fresh bounded series while preserving a bounded audit count.
*)

CONSTANTS MaxAttempts, Launchers, Owners, NoOwner, MaxRevision, MaxRecoveries

ASSUME /\ MaxAttempts >= 3
       /\ Cardinality(Launchers) >= MaxAttempts
       /\ NoOwner \notin Owners
       /\ MaxRevision >= (2 * MaxAttempts) + 2
       /\ MaxRecoveries >= 1

SlotValues == {"idle", "reserved"}

VARIABLES owner, claimExpired, revision, attempts, held, recoveries,
          slots, reservationOwner, reservationRevision, cleaned

vars == <<owner, claimExpired, revision, attempts, held, recoveries,
          slots, reservationOwner, reservationRevision, cleaned>>

ReservedCount == Cardinality({launcher \in Launchers: slots[launcher] = "reserved"})
LiveReservation == ReservedCount > 0

Init ==
    /\ owner \in Owners
    /\ claimExpired = FALSE
    /\ revision = 0
    /\ attempts = 0
    /\ held = FALSE
    /\ recoveries = 0
    /\ slots = [launcher \in Launchers |-> "idle"]
    /\ reservationOwner = [launcher \in Launchers |-> NoOwner]
    /\ reservationRevision = [launcher \in Launchers |-> 0]
    /\ cleaned = FALSE

Reserve(launcher) ==
    /\ launcher \in Launchers
    /\ owner \in Owners
    /\ slots[launcher] = "idle"
    /\ ~held
    /\ attempts + ReservedCount < MaxAttempts
    /\ revision < MaxRevision
    /\ slots' = [slots EXCEPT ![launcher] = "reserved"]
    /\ reservationOwner' = [reservationOwner EXCEPT ![launcher] = owner]
    /\ reservationRevision' = [reservationRevision EXCEPT ![launcher] = revision]
    /\ revision' = revision + 1
    /\ UNCHANGED <<owner, claimExpired, attempts, held, recoveries, cleaned>>

ResolveFailure(launcher) ==
    /\ launcher \in Launchers
    /\ slots[launcher] = "reserved"
    /\ owner = reservationOwner[launcher]
    /\ revision = reservationRevision[launcher] + 1
    /\ revision < MaxRevision
    /\ slots' = [slots EXCEPT ![launcher] = "idle"]
    /\ attempts' = attempts + 1
    /\ held' = (attempts + 1 = MaxAttempts)
    /\ revision' = revision + 1
    /\ UNCHANGED <<owner, claimExpired, recoveries, reservationOwner,
                reservationRevision, cleaned>>

ResolveSuccess(launcher) ==
    /\ launcher \in Launchers
    /\ slots[launcher] = "reserved"
    /\ owner = reservationOwner[launcher]
    /\ revision = reservationRevision[launcher] + 1
    /\ revision < MaxRevision
    /\ slots' = [slots EXCEPT ![launcher] = "idle"]
    /\ revision' = revision + 1
    /\ UNCHANGED <<owner, claimExpired, attempts, held, recoveries,
                reservationOwner, reservationRevision, cleaned>>

InterveningMutation ==
    /\ owner \in Owners
    /\ revision < MaxRevision
    /\ revision' = revision + 1
    /\ UNCHANGED <<owner, claimExpired, attempts, held, recoveries, slots,
                reservationOwner, reservationRevision, cleaned>>

Expire(launcher) ==
    /\ launcher \in Launchers
    /\ slots[launcher] = "reserved"
    /\ slots' = [slots EXCEPT ![launcher] = "idle"]
    /\ reservationOwner' = [reservationOwner EXCEPT ![launcher] = NoOwner]
    /\ cleaned' = TRUE
    /\ UNCHANGED <<owner, claimExpired, revision, attempts, held, recoveries,
                reservationRevision>>

MarkClaimExpired ==
    /\ owner \in Owners
    /\ claimExpired' = TRUE
    /\ UNCHANGED <<owner, revision, attempts, held, recoveries, slots,
                reservationOwner, reservationRevision, cleaned>>

RecoverExpired ==
    /\ owner \in Owners
    /\ claimExpired
    /\ ~LiveReservation
    /\ revision < MaxRevision
    /\ owner' = NoOwner
    /\ revision' = revision + 1
    /\ UNCHANGED <<claimExpired, attempts, held, recoveries, slots,
                reservationOwner, reservationRevision, cleaned>>

RecoverCircuit ==
    /\ owner \in Owners
    /\ held
    /\ ~LiveReservation
    /\ recoveries < MaxRecoveries
    /\ revision < MaxRevision
    /\ attempts' = 0
    /\ held' = FALSE
    /\ recoveries' = recoveries + 1
    /\ revision' = revision + 1
    /\ UNCHANGED <<owner, claimExpired, slots, reservationOwner,
                reservationRevision, cleaned>>

Next ==
    \/ \E launcher \in Launchers: Reserve(launcher)
    \/ \E launcher \in Launchers: ResolveFailure(launcher)
    \/ \E launcher \in Launchers: ResolveSuccess(launcher)
    \/ \E launcher \in Launchers: Expire(launcher)
    \/ InterveningMutation
    \/ MarkClaimExpired
    \/ RecoverExpired
    \/ RecoverCircuit
    \/ UNCHANGED vars

Spec == /\ Init /\ [][Next]_vars

TypeOK ==
    /\ owner \in Owners \cup {NoOwner}
    /\ claimExpired \in BOOLEAN
    /\ revision \in 0..MaxRevision
    /\ attempts \in 0..MaxAttempts
    /\ held \in BOOLEAN
    /\ recoveries \in 0..MaxRecoveries
    /\ slots \in [Launchers -> SlotValues]
    /\ reservationOwner \in [Launchers -> (Owners \cup {NoOwner})]
    /\ reservationRevision \in [Launchers -> 0..MaxRevision]
    /\ cleaned \in BOOLEAN

CapacityBound == attempts + ReservedCount <= MaxAttempts
HeldAtExactBound == held <=> attempts = MaxAttempts
HeldHasNoLiveSlot == held => ~LiveReservation
ReservationOwnerBound == \A launcher \in Launchers:
    slots[launcher] = "reserved" => reservationOwner[launcher] \in Owners
ExpiredClaimRecoveryFenced == owner = NoOwner => ~LiveReservation
FreshRecoverySeries == recoveries > 0 /\ ~held => attempts < MaxAttempts
=============================================================================
