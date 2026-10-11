----------------------- MODULE HandoffctlObservation -----------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS FiniteSets, Naturals, TLC

(* Bounded contract for cached-observation-v1.  A completed cache is only
usable for its exact input generation; one refresh serves all waiting callers. *)

CONSTANTS Clients, Inputs, None, MaxAge
ASSUME /\ Clients # {} /\ Inputs # {} /\ None \notin Inputs /\ MaxAge \in Nat /\ MaxAge > 0

CallStates == {"idle", "active", "waiting", "completed", "rejected", "timedout"}
Results == {"none", "cache", "fresh", "input_changed", "timeout"}

VARIABLES currentInput, callState, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation, cacheInput, cacheAge
vars == <<currentInput, callState, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation, cacheInput, cacheAge>>

Init == /\ currentInput \in Inputs
        /\ callState = [c \in Clients |-> "idle"]
        /\ requestedInput = [c \in Clients |-> None]
        /\ requestedMaxAge = [c \in Clients |-> 0]
        /\ deliveredInput = [c \in Clients |-> None]
        /\ result = [c \in Clients |-> "none"]
        /\ scanBusy = FALSE /\ scanInput = None /\ generation = 0 /\ cacheInput = None /\ cacheAge = None

CacheUsable(age) == /\ cacheInput = currentInput
    /\ age \in 1..MaxAge /\ cacheAge \in 0..MaxAge /\ cacheAge <= age

RequestCacheHit(c, age) == /\ callState[c] = "idle" /\ CacheUsable(age)
    /\ callState' = [callState EXCEPT ![c] = "completed"]
    /\ requestedInput' = [requestedInput EXCEPT ![c] = currentInput]
    /\ requestedMaxAge' = [requestedMaxAge EXCEPT ![c] = age]
    /\ deliveredInput' = [deliveredInput EXCEPT ![c] = currentInput]
    /\ result' = [result EXCEPT ![c] = "cache"]
    /\ UNCHANGED <<currentInput, scanBusy, scanInput, generation, cacheInput, cacheAge>>

RequestMiss(c, age) == /\ callState[c] = "idle" /\ age \in 0..MaxAge /\ ~CacheUsable(age)
    /\ callState' = [callState EXCEPT ![c] = "active"]
    /\ requestedInput' = [requestedInput EXCEPT ![c] = currentInput]
    /\ requestedMaxAge' = [requestedMaxAge EXCEPT ![c] = age]
    /\ UNCHANGED <<currentInput, deliveredInput, result, scanBusy, scanInput, generation, cacheInput, cacheAge>>

BeginRefresh(c) == /\ callState[c] = "active" /\ scanBusy = FALSE
    /\ scanBusy' = TRUE /\ scanInput' = requestedInput[c]
    /\ callState' = [callState EXCEPT ![c] = "waiting"]
    /\ UNCHANGED <<currentInput, requestedInput, requestedMaxAge, deliveredInput, result, generation, cacheInput, cacheAge>>

JoinRefresh(c) == /\ callState[c] = "active" /\ scanBusy /\ requestedInput[c] = scanInput
    /\ callState' = [callState EXCEPT ![c] = "waiting"]
    /\ UNCHANGED <<currentInput, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation, cacheInput, cacheAge>>

CompleteRefresh == /\ scanBusy /\ currentInput = scanInput
    /\ cacheInput' = scanInput /\ cacheAge' = 0 /\ generation' = generation + 1 /\ scanBusy' = FALSE /\ scanInput' = None
    /\ callState' = [c \in Clients |-> IF callState[c] = "waiting" THEN "completed" ELSE callState[c]]
    /\ deliveredInput' = [c \in Clients |-> IF callState[c] = "waiting" THEN scanInput ELSE deliveredInput[c]]
    /\ result' = [c \in Clients |-> IF callState[c] = "waiting" THEN "fresh" ELSE result[c]]
    /\ UNCHANGED <<currentInput, requestedInput, requestedMaxAge>>

RejectChangedInput == /\ scanBusy /\ currentInput # scanInput
    /\ scanBusy' = FALSE /\ scanInput' = None
    /\ callState' = [c \in Clients |-> IF callState[c] = "waiting" THEN "rejected" ELSE callState[c]]
    /\ result' = [c \in Clients |-> IF callState[c] = "waiting" THEN "input_changed" ELSE result[c]]
    /\ UNCHANGED <<currentInput, requestedInput, requestedMaxAge, deliveredInput, generation, cacheInput, cacheAge>>

ChangeInput(i) == /\ i \in Inputs /\ i # currentInput
    /\ currentInput' = i
    /\ UNCHANGED <<callState, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation, cacheInput, cacheAge>>

Timeout(c) == /\ callState[c] \in {"active", "waiting"}
    /\ callState' = [callState EXCEPT ![c] = "timedout"]
    /\ result' = [result EXCEPT ![c] = "timeout"]
    /\ UNCHANGED <<currentInput, requestedInput, requestedMaxAge, deliveredInput, scanBusy, scanInput, generation, cacheInput, cacheAge>>

Tick == /\ cacheAge \in 0..(MaxAge - 1)
    /\ cacheAge' = cacheAge + 1
    /\ UNCHANGED <<currentInput, callState, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation, cacheInput>>

Expire == /\ cacheAge = MaxAge
    /\ cacheInput' = None /\ cacheAge' = None
    /\ UNCHANGED <<currentInput, callState, requestedInput, requestedMaxAge, deliveredInput, result, scanBusy, scanInput, generation>>

Next == (\E c \in Clients, age \in 0..MaxAge: RequestCacheHit(c, age) \/ RequestMiss(c, age))
        \/ (\E c \in Clients: BeginRefresh(c) \/ JoinRefresh(c) \/ Timeout(c))
        \/ CompleteRefresh \/ RejectChangedInput \/ (\E i \in Inputs: ChangeInput(i)) \/ Tick \/ Expire
Spec == Init /\ [][Next]_vars

TypeOK == /\ currentInput \in Inputs /\ callState \in [Clients -> CallStates]
          /\ requestedInput \in [Clients -> (Inputs \cup {None})] /\ requestedMaxAge \in [Clients -> 0..MaxAge] /\ deliveredInput \in [Clients -> (Inputs \cup {None})] /\ result \in [Clients -> Results]
          /\ scanBusy \in BOOLEAN /\ scanInput \in (Inputs \cup {None}) /\ generation \in Nat /\ cacheInput \in (Inputs \cup {None}) /\ cacheAge \in ((0..MaxAge) \cup {None})
SingleFlight == scanBusy => scanInput \in Inputs
NoStaleCompletion == \A c \in Clients: result[c] \in {"cache", "fresh"} => requestedInput[c] = deliveredInput[c]
InputChangeFailsClosed == \A c \in Clients: result[c] = "input_changed" => callState[c] = "rejected"
TimeoutIsTerminal == \A c \in Clients: result[c] = "timeout" => callState[c] = "timedout"
CacheHitIsBounded == \A c \in Clients: result[c] = "cache" => requestedMaxAge[c] > 0
=============================================================================
