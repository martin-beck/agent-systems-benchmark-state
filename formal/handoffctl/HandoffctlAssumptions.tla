---------------------- MODULE HandoffctlAssumptions ----------------------
\* Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
\* SPDX-License-Identifier: MIT
EXTENDS Naturals, TLC

(*******************************************************************************
Bounded contract for opt-in freshness-sensitive task assumptions. A base head,
dependency revision, and local observation may move independently. Material
stale bindings require explicit revalidation or disposition before accept or
done; a non-material binding remains explainable without blocking progress.
*******************************************************************************)

CONSTANTS Processes, Actors, NoActor

Heads == {"head-a", "head-b"}
DependencyRevisions == {1, 2}
Observations == {"observation-a", "observation-b"}
Actions == {"declare-base", "declare-dependency", "declare-observation",
            "revalidate-base", "revalidate-dependency", "revalidate-observation",
            "dispose-base", "dispose-dependency", "dispose-observation", "accept",
            "release-done"}
Phases == {"ready", "done"}
Results == {"pending", "accepted", "rejected"}

VARIABLES status, owner, revision, currentBase, currentDependency, currentObservation,
          baseDeclared, dependencyDeclared, observationDeclared,
          baseMaterial, dependencyMaterial, observationMaterial,
          boundBase, boundDependency, boundObservation,
          baseDisposed, dependencyDisposed, observationDisposed,
          acceptanceRecorded, acceptanceFresh,
          pc, action, requestedActor, expectedRevision, result

vars == <<status, owner, revision, currentBase, currentDependency, currentObservation,
          baseDeclared, dependencyDeclared, observationDeclared,
          baseMaterial, dependencyMaterial, observationMaterial,
          boundBase, boundDependency, boundObservation,
          baseDisposed, dependencyDisposed, observationDisposed,
          acceptanceRecorded, acceptanceFresh,
          pc, action, requestedActor, expectedRevision, result>>

BaseFresh == ~baseDeclared \/ ~baseMaterial \/ baseDisposed \/ boundBase = currentBase
DependencyFresh == ~dependencyDeclared \/ ~dependencyMaterial \/ dependencyDisposed \/ boundDependency = currentDependency
ObservationFresh == ~observationDeclared \/ ~observationMaterial \/ observationDisposed \/ boundObservation = currentObservation
Fresh == BaseFresh /\ DependencyFresh /\ ObservationFresh

Init ==
    /\ status = "in_progress" /\ owner = "owner-a" /\ revision = 0
    /\ currentBase = "head-a" /\ currentDependency = 1 /\ currentObservation = "observation-a"
    /\ baseDeclared = FALSE /\ dependencyDeclared = FALSE /\ observationDeclared = FALSE
    /\ baseMaterial \in BOOLEAN /\ dependencyMaterial \in BOOLEAN /\ observationMaterial \in BOOLEAN
    /\ boundBase = "head-a" /\ boundDependency = 1 /\ boundObservation = "observation-a"
    /\ baseDisposed = FALSE /\ dependencyDisposed = FALSE /\ observationDisposed = FALSE
    /\ acceptanceRecorded = FALSE /\ acceptanceFresh = FALSE
    /\ pc = [p \in Processes |-> "ready"] /\ action \in [Processes -> Actions]
    /\ requestedActor \in [Processes -> Actors] /\ expectedRevision \in [Processes -> 0..2]
    /\ result = [p \in Processes |-> "pending"]

Ready(p, name) == /\ pc[p] = "ready" /\ action[p] = name /\ requestedActor[p] = owner /\ expectedRevision[p] = revision
Finish(p) == /\ result' = [result EXCEPT ![p] = "accepted"] /\ pc' = [pc EXCEPT ![p] = "done"]
DeclareBaseEnabled(p) == Ready(p, "declare-base") /\ ~baseDeclared
DeclareBase(p) == /\ DeclareBaseEnabled(p) /\ baseDeclared' = TRUE /\ boundBase' = currentBase /\ revision' = revision + 1 /\ Finish(p)
                  /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
DeclareDependencyEnabled(p) == Ready(p, "declare-dependency") /\ ~dependencyDeclared
DeclareDependency(p) == /\ DeclareDependencyEnabled(p) /\ dependencyDeclared' = TRUE /\ boundDependency' = currentDependency /\ revision' = revision + 1 /\ Finish(p)
                        /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
DeclareObservationEnabled(p) == Ready(p, "declare-observation") /\ ~observationDeclared
DeclareObservation(p) == /\ DeclareObservationEnabled(p) /\ observationDeclared' = TRUE /\ boundObservation' = currentObservation /\ revision' = revision + 1 /\ Finish(p)
                         /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>

RevalidateBaseEnabled(p) == Ready(p, "revalidate-base") /\ baseDeclared /\ ~baseDisposed /\ boundBase # currentBase
RevalidateBase(p) == /\ RevalidateBaseEnabled(p) /\ boundBase' = currentBase /\ revision' = revision + 1 /\ Finish(p)
                    /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
RevalidateDependencyEnabled(p) == Ready(p, "revalidate-dependency") /\ dependencyDeclared /\ ~dependencyDisposed /\ boundDependency # currentDependency
RevalidateDependency(p) == /\ RevalidateDependencyEnabled(p) /\ boundDependency' = currentDependency /\ revision' = revision + 1 /\ Finish(p)
                          /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
RevalidateObservationEnabled(p) == Ready(p, "revalidate-observation") /\ observationDeclared /\ ~observationDisposed /\ boundObservation # currentObservation
RevalidateObservation(p) == /\ RevalidateObservationEnabled(p) /\ boundObservation' = currentObservation /\ revision' = revision + 1 /\ Finish(p)
                           /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>

DisposeBaseEnabled(p) == Ready(p, "dispose-base") /\ baseDeclared /\ ~baseDisposed
DisposeBase(p) == /\ DisposeBaseEnabled(p) /\ baseDisposed' = TRUE /\ revision' = revision + 1 /\ Finish(p)
                 /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
DisposeDependencyEnabled(p) == Ready(p, "dispose-dependency") /\ dependencyDeclared /\ ~dependencyDisposed
DisposeDependency(p) == /\ DisposeDependencyEnabled(p) /\ dependencyDisposed' = TRUE /\ revision' = revision + 1 /\ Finish(p)
                       /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>
DisposeObservationEnabled(p) == Ready(p, "dispose-observation") /\ observationDeclared /\ ~observationDisposed
DisposeObservation(p) == /\ DisposeObservationEnabled(p) /\ observationDisposed' = TRUE /\ revision' = revision + 1 /\ Finish(p)
                        /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, dependencyDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>

AcceptEnabled(p) == Ready(p, "accept") /\ Fresh
Accept(p) == /\ AcceptEnabled(p) /\ revision' = revision + 1 /\ acceptanceRecorded' = TRUE /\ acceptanceFresh' = Fresh /\ Finish(p)
             /\ UNCHANGED <<status, owner, currentBase, currentDependency, currentObservation,
                           baseDeclared, dependencyDeclared, observationDeclared,
                           baseMaterial, dependencyMaterial, observationMaterial,
                           boundBase, boundDependency, boundObservation,
                           baseDisposed, dependencyDisposed, observationDisposed,
                           action, requestedActor, expectedRevision>>
ReleaseDoneEnabled(p) == /\ pc[p] = "ready" /\ action[p] = "release-done" /\ requestedActor[p] = owner /\ Fresh
ReleaseDone(p) == /\ ReleaseDoneEnabled(p) /\ status' = "done" /\ owner' = NoActor /\ revision' = revision + 1 /\ Finish(p)
                  /\ UNCHANGED <<currentBase, currentDependency, currentObservation,
                                baseDeclared, dependencyDeclared, observationDeclared,
                                baseMaterial, dependencyMaterial, observationMaterial,
                                boundBase, boundDependency, boundObservation,
                                baseDisposed, dependencyDisposed, observationDisposed,
                                acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>

Reject(p) ==
    /\ pc[p] = "ready"
    /\ ~DeclareBaseEnabled(p) /\ ~DeclareDependencyEnabled(p) /\ ~DeclareObservationEnabled(p)
    /\ ~RevalidateBaseEnabled(p) /\ ~RevalidateDependencyEnabled(p) /\ ~RevalidateObservationEnabled(p)
    /\ ~DisposeBaseEnabled(p) /\ ~DisposeDependencyEnabled(p) /\ ~DisposeObservationEnabled(p)
    /\ ~AcceptEnabled(p) /\ ~ReleaseDoneEnabled(p)
    /\ result' = [result EXCEPT ![p] = "rejected"] /\ pc' = [pc EXCEPT ![p] = "done"]
    /\ UNCHANGED <<status, owner, revision, currentBase, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, action, requestedActor, expectedRevision>>

MoveBase == /\ status = "in_progress" /\ currentBase' \in Heads /\ currentBase' # currentBase
            /\ UNCHANGED <<status, owner, revision, currentDependency, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, pc, action, requestedActor, expectedRevision, result>>
MoveDependency == /\ status = "in_progress" /\ currentDependency' \in DependencyRevisions /\ currentDependency' # currentDependency
                  /\ UNCHANGED <<status, owner, revision, currentBase, currentObservation, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, pc, action, requestedActor, expectedRevision, result>>
MoveObservation == /\ status = "in_progress" /\ currentObservation' \in Observations /\ currentObservation' # currentObservation
                  /\ UNCHANGED <<status, owner, revision, currentBase, currentDependency, baseDeclared, dependencyDeclared, observationDeclared, baseMaterial, dependencyMaterial, observationMaterial, boundBase, boundDependency, boundObservation, baseDisposed, dependencyDisposed, observationDisposed, acceptanceRecorded, acceptanceFresh, pc, action, requestedActor, expectedRevision, result>>
Quiescent == /\ \A p \in Processes: pc[p] = "done" /\ UNCHANGED vars

Next == (\E p \in Processes: DeclareBase(p) \/ DeclareDependency(p) \/ DeclareObservation(p) \/ RevalidateBase(p) \/ RevalidateDependency(p) \/ RevalidateObservation(p) \/ DisposeBase(p) \/ DisposeDependency(p) \/ DisposeObservation(p) \/ Accept(p) \/ ReleaseDone(p) \/ Reject(p)) \/ MoveBase \/ MoveDependency \/ MoveObservation \/ Quiescent
Spec == Init /\ [][Next]_vars

TypeOK == /\ status \in {"in_progress", "done"} /\ owner \in Actors \cup {NoActor} /\ revision \in Nat
          /\ currentBase \in Heads /\ currentDependency \in DependencyRevisions /\ currentObservation \in Observations
          /\ baseDeclared \in BOOLEAN /\ dependencyDeclared \in BOOLEAN /\ observationDeclared \in BOOLEAN
          /\ baseMaterial \in BOOLEAN /\ dependencyMaterial \in BOOLEAN /\ observationMaterial \in BOOLEAN
          /\ boundBase \in Heads /\ boundDependency \in DependencyRevisions /\ boundObservation \in Observations
          /\ baseDisposed \in BOOLEAN /\ dependencyDisposed \in BOOLEAN /\ observationDisposed \in BOOLEAN
          /\ acceptanceRecorded \in BOOLEAN /\ acceptanceFresh \in BOOLEAN
          /\ pc \in [Processes -> Phases] /\ result \in [Processes -> Results]
          /\ action \in [Processes -> Actions] /\ requestedActor \in [Processes -> Actors] /\ expectedRevision \in [Processes -> Nat]
DoneRequiresFreshMaterialAssumptions == status = "done" => Fresh
AcceptanceRequiresFreshMaterialAssumptions == acceptanceRecorded => acceptanceFresh
DisposedAssumptionsAreExplicit == /\ (baseDisposed => baseDeclared) /\ (dependencyDisposed => dependencyDeclared) /\ (observationDisposed => observationDeclared)
NonmaterialDoesNotUniversallyBlock == /\ (~baseMaterial => BaseFresh) /\ (~dependencyMaterial => DependencyFresh) /\ (~observationMaterial => ObservationFresh)
=============================================================================
