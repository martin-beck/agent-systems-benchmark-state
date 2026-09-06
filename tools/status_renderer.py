"""Deterministic, injection-safe rendering for the public AR status page."""

import html
import re
from collections import Counter
from pathlib import Path
from typing import Any

type Meta = dict[str, Any]
type Task = tuple[Path, Meta, str]

SAFE_ID = re.compile(r"AR-\d{4}")
STATUS_PRESENTATION = {
    "in_progress": ("In progress", "#1565c0", "#ffffff"),
    "open": ("Open", "#2e7d32", "#ffffff"),
    "blocked": ("Blocked", "#c62828", "#ffffff"),
    "planned": ("Planned", "#6a1b9a", "#ffffff"),
    "future": ("Future", "#455a64", "#ffffff"),
    "done": ("Done", "#00695c", "#ffffff"),
    "cancelled": ("Cancelled", "#616161", "#ffffff"),
    "superseded": ("Superseded", "#5d4037", "#ffffff"),
}
SERIES = {
    "00": "Coordination foundation",
    "01": "Contracts and runtime",
    "02": "Analysis",
    "03": "Adapters and workloads",
    "04": "Live measurement",
    "05": "Replay",
    "06": "Metrics",
    "07": "Platforms",
    "08": "Interfaces",
    "09": "Assurance",
    "10": "Reliability and release",
}


class StatusRenderError(ValueError):
    """The task graph cannot be represented safely and unambiguously."""


def _plain(value: object) -> str:
    """Render untrusted front matter as inert, single-line Markdown text."""
    text = " ".join(str(value or "-").splitlines())
    escaped = html.escape(text, quote=True)
    return (
        escaped.replace("|", "&#124;")
        .replace("`", "&#96;")
        .replace("[", "&#91;")
        .replace("]", "&#93;")
        .replace("%", "&#37;")
    )


def _task_dependencies(meta: Meta, known: set[str]) -> tuple[list[str], list[str]]:
    task_id = str(meta.get("id", ""))
    dependencies = meta.get("depends_on", [])
    if not isinstance(dependencies, list) or not all(
        isinstance(item, str) for item in dependencies
    ):
        return [f"{task_id}: dependencies must be a list of AR identifiers"], []
    errors = [
        f"{task_id}: duplicate dependency {item}"
        for item, count in sorted(Counter(dependencies).items())
        if count > 1
    ]
    errors.extend(f"{task_id}: self dependency" for item in dependencies if item == task_id)
    errors.extend(
        f"{task_id}: missing dependency {item}" for item in dependencies if item not in known
    )
    return errors, dependencies


def _dependency_shape(tasks: list[Task]) -> tuple[list[str], dict[str, list[str]]]:
    ids = [str(meta.get("id", "")) for _, meta, _ in tasks]
    counts = Counter(ids)
    errors = [
        f"duplicate graph node {task_id}" for task_id in sorted(counts) if counts[task_id] > 1
    ]
    graph: dict[str, list[str]] = {}
    for _, meta, _ in tasks:
        task_errors, dependencies = _task_dependencies(meta, set(ids))
        errors.extend(task_errors)
        graph[str(meta.get("id", ""))] = dependencies
    return errors, graph


def _cycle_errors(graph: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(task_id: str) -> None:
        if state.get(task_id) == 2:
            return
        if state.get(task_id) == 1:
            start = stack.index(task_id)
            errors.append("dependency cycle: " + " -> ".join([*stack[start:], task_id]))
            return
        state[task_id] = 1
        stack.append(task_id)
        for dependency in sorted(set(graph.get(task_id, []))):
            if dependency in graph:
                visit(dependency)
        stack.pop()
        state[task_id] = 2

    for task_id in sorted(graph):
        visit(task_id)
    return errors


def graph_errors(tasks: list[Task]) -> list[str]:
    """Return deterministic structural errors for the complete dependency graph."""
    errors, graph = _dependency_shape(tasks)
    errors.extend(_cycle_errors(graph))
    return errors


def _task_link(task_id: str, filenames: dict[str, str]) -> str:
    return f"[{task_id}](tasks/{filenames[task_id]})"


def _validated_filenames(
    tasks: list[Task], statuses: tuple[str, ...], priorities: tuple[str, ...]
) -> dict[str, str]:
    errors = graph_errors(tasks)
    if errors:
        raise StatusRenderError("\n".join(errors))
    for path, meta, _ in tasks:
        task_id = str(meta.get("id", ""))
        if not SAFE_ID.fullmatch(task_id) or not re.fullmatch(r"AR-\d{4}[-a-z0-9]*\.md", path.name):
            raise StatusRenderError(f"{task_id}: unsafe task identifier or filename")
        if meta.get("status") not in statuses or meta.get("priority") not in priorities:
            raise StatusRenderError(f"{task_id}: unknown status or priority")
    return {meta["id"]: path.name for path, meta, _ in tasks}


def _overview(tasks: list[Task], statuses: tuple[str, ...]) -> list[str]:
    counts = Counter(meta["status"] for _, meta, _ in tasks)
    active = sum(bool(counts[item]) for item in statuses)
    lines = [
        "# Agent Systems Benchmark status",
        "",
        "> Generated deterministically from task front matter. Do not edit this file directly.",
        "> Status records coordination progress; it is not evidence that product behavior is "
        "accepted.",
        "",
        "## Portfolio overview",
        "",
        f"**{len(tasks)} ARs tracked** across {active} active status categories.",
        "",
        "| Status | Meaning | Count |",
        "| --- | --- | ---: |",
    ]
    meanings = {
        "in_progress": "Claimed work with a live lease",
        "open": "Dependency-ready and available to claim",
        "blocked": "Cannot proceed until its recorded blocker clears",
        "planned": "Defined work awaiting promotion or dependencies",
        "future": "Deferred roadmap work",
        "done": "Accepted, integrated, and durably verified",
        "cancelled": "Stopped with a recorded rationale",
        "superseded": "Replaced by another AR",
    }
    lines.extend(
        f"| **{STATUS_PRESENTATION[status][0]}** | {meanings[status]} | {counts[status]} |"
        for status in statuses
    )
    return lines


def _graph_data(tasks: list[Task]) -> tuple[dict[str, list[str]], list[tuple[str, str]]]:
    reverse: dict[str, list[str]] = {meta["id"]: [] for _, meta, _ in tasks}
    edges: list[tuple[str, str]] = []
    for _, meta, _ in tasks:
        for dependency in meta.get("depends_on", []):
            reverse[dependency].append(meta["id"])
            edges.append((dependency, meta["id"]))
    return reverse, edges


def _graph(tasks: list[Task], statuses: tuple[str, ...], edges: list[tuple[str, str]]) -> list[str]:
    lines = [
        "",
        "## Dependency graph",
        "",
        "Arrows point from each prerequisite to the work that depends on it. Color is redundant",
        "with the status text inside every node; the tables below are the complete text",
        "alternative.",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    observed_series = sorted({task[1]["id"][3:5] for task in tasks})
    for series in observed_series:
        label = SERIES.get(series, "Additional work")
        lines.extend(
            [f'    subgraph series_{series}["{series} - {label}"]', "        direction TB"]
        )
        rows = [task for task in tasks if task[1]["id"][3:5] == series]
        for _, meta, _ in sorted(rows, key=lambda task: task[1]["id"]):
            node = meta["id"].replace("-", "_")
            status_label = STATUS_PRESENTATION[meta["status"]][0]
            lines.append(
                f'        {node}["{meta["id"]} - {status_label}"]:::status_{meta["status"]}'
            )
        lines.append("    end")
    lines.extend(
        f"    {prerequisite.replace('-', '_')} --> {dependent.replace('-', '_')}"
        for prerequisite, dependent in sorted(edges)
    )
    for status in statuses:
        _, fill, color = STATUS_PRESENTATION[status]
        lines.append(
            f"    classDef status_{status} fill:{fill},color:{color},"
            "stroke:#263238,stroke-width:2px"
        )
    lines.extend(["```", ""])
    return lines


def _dependencies(
    tasks: list[Task], filenames: dict[str, str], reverse: dict[str, list[str]]
) -> list[str]:
    lines = [
        "### Accessible dependency index",
        "",
        "| AR | Prerequisites | Dependents |",
        "| --- | --- | --- |",
    ]
    for _, meta, _ in sorted(tasks, key=lambda task: task[1]["id"]):
        task_id = meta["id"]
        prerequisites = (
            ", ".join(_task_link(item, filenames) for item in sorted(meta.get("depends_on", [])))
            or "None"
        )
        dependents = (
            ", ".join(_task_link(item, filenames) for item in sorted(reverse[task_id])) or "None"
        )
        lines.append(f"| {_task_link(task_id, filenames)} | {prerequisites} | {dependents} |")
    return lines


def _inventory(
    tasks: list[Task],
    statuses: tuple[str, ...],
    priorities: tuple[str, ...],
    filenames: dict[str, str],
) -> list[str]:
    ordered = sorted(
        tasks,
        key=lambda task: (
            statuses.index(task[1]["status"]),
            priorities.index(task[1]["priority"]),
            task[1]["id"],
        ),
    )
    lines = ["", "## Complete AR inventory", ""]
    for status in statuses:
        rows = [task for task in ordered if task[1]["status"] == status]
        if not rows:
            continue
        lines.extend(
            [
                f"### {STATUS_PRESENTATION[status][0]} ({len(rows)})",
                "",
                "| Priority | AR | Owner | Summary | Next action |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for _, meta, _ in rows:
            owner = meta.get("owner") or "Unclaimed"
            task = f"{_task_link(meta['id'], filenames)}: {_plain(meta['title'])}"
            lines.append(
                f"| {meta['priority']} | {task} | {_plain(owner)} | "
                f"{_plain(meta['summary'])} | {_plain(meta['next_action'])} |"
            )
        lines.append("")
    return lines


def render_status(tasks: list[Task], statuses: tuple[str, ...], priorities: tuple[str, ...]) -> str:
    """Render the complete inventory and graph, or reject unsafe structure."""
    filenames = _validated_filenames(tasks, statuses, priorities)
    reverse, edges = _graph_data(tasks)
    lines = _overview(tasks, statuses)
    lines.extend(_graph(tasks, statuses, edges))
    lines.extend(_dependencies(tasks, filenames, reverse))
    lines.extend(_inventory(tasks, statuses, priorities, filenames))
    return "\n".join(lines).rstrip() + "\n"
