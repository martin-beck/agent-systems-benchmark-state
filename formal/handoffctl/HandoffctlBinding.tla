-------------------------- MODULE HandoffctlBinding --------------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Integers, TLC

CONSTANT Projects, BoundProject

VARIABLES caller, revision, previousRevision, lastAccepted

vars == <<caller, revision, previousRevision, lastAccepted>>

OtherProject == CHOOSE project \in Projects : project # BoundProject

Init ==
    /\ BoundProject \in Projects
    /\ \E project \in Projects : project # BoundProject
    /\ caller = OtherProject
    /\ revision = FALSE
    /\ previousRevision = FALSE
    /\ lastAccepted = FALSE

Call(project) ==
    /\ project \in Projects
    /\ caller' = project
    /\ previousRevision' = revision
    /\ lastAccepted' = (project = BoundProject)
    /\ revision' = IF project = BoundProject THEN ~revision ELSE revision

Next == \E project \in Projects : Call(project)

CorrectCall == Call(BoundProject)

Spec == Init /\ [][Next]_vars /\ WF_vars(CorrectCall)

TypeOK ==
    /\ caller \in Projects
    /\ revision \in BOOLEAN
    /\ previousRevision \in BOOLEAN
    /\ lastAccepted \in BOOLEAN

AcceptedIffBound == lastAccepted <=> caller = BoundProject
RejectedPreserves == ~lastAccepted => revision = previousRevision
AcceptedMutates == lastAccepted => revision # previousRevision
EventuallyBoundCallSucceeds == []<>(lastAccepted)

=============================================================================
