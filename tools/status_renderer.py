# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

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


# Keep a margin below the repository-wide 200 KiB privacy/size guard.  The
# margin leaves room for the index and for future renderer metadata without
# making a page unexpectedly cross the hard limit.
STATUS_FILE_LIMIT = 200_000
STATUS_PAGE_TARGET = 180_000


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


def _overview(tasks: list[Task], statuses: tuple[str, ...], project_title: str) -> list[str]:
    counts = Counter(meta["status"] for _, meta, _ in tasks)
    active = sum(bool(counts[item]) for item in statuses)
    lines = [
        f"# {project_title} status",
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


def render_status(
    tasks: list[Task],
    statuses: tuple[str, ...],
    priorities: tuple[str, ...],
    project_title: str,
) -> str:
    """Render the complete inventory and graph, or reject unsafe structure."""
    filenames = _validated_filenames(tasks, statuses, priorities)
    reverse, edges = _graph_data(tasks)
    lines = _overview(tasks, statuses, project_title)
    lines.extend(_graph(tasks, statuses, edges))
    lines.extend(_dependencies(tasks, filenames, reverse))
    lines.extend(_inventory(tasks, statuses, priorities, filenames))
    return "\n".join(lines).rstrip() + "\n"


def _status_index(full: str, page_names: list[str]) -> str:
    """Return a compact root index for a status view split across pages."""
    lines = full.splitlines()
    overview_end = next(
        (index for index, line in enumerate(lines) if line == "## Dependency graph"),
        len(lines),
    )
    overview = lines[:overview_end]
    links = [
        "",
        "## Complete status view",
        "",
        "The generated status view is split into deterministic pages to keep every file below "
        "the 200,000-byte repository limit. The linked pages preserve the complete graph, "
        "dependency index, and AR inventory without omission.",
        "",
    ]
    links.extend(f"- [{name.removesuffix('.md')}]({name})" for name in page_names)
    return "\n".join([*overview, *links]).rstrip() + "\n"


def _split_status(full: str) -> list[str]:
    """Split complete status text at stable line boundaries."""
    prefix = (
        "<!-- This page is generated; the root STATUS.md index links the complete view. -->\n\n"
    )
    chunks: list[str] = []
    current: list[str] = []
    current_bytes = len(prefix.encode())
    budget = STATUS_PAGE_TARGET - len(prefix.encode())
    for line in full.splitlines(keepends=True):
        pieces = [line]
        while len(pieces[0].encode()) > budget:
            encoded = pieces[0].encode()
            cut = encoded[:budget].decode("utf-8", "ignore")
            if not cut:
                raise StatusRenderError("status line cannot be split within the page budget")
            pieces[0] = cut
            pieces.insert(1, encoded[len(cut.encode()) :].decode("utf-8"))
        for piece in pieces:
            line_bytes = len(piece.encode())
            if current and current_bytes + line_bytes > STATUS_PAGE_TARGET:
                chunks.append(prefix + "".join(current).replace("](tasks/", "](../tasks/"))
                current = []
                current_bytes = len(prefix.encode())
            current.append(piece)
            current_bytes += line_bytes
    if current:
        chunks.append(prefix + "".join(current).replace("](tasks/", "](../tasks/"))
    return chunks


def render_status_pages_from_text(full: str) -> dict[str, str]:
    """Paginate an already rendered status document deterministically."""
    if len(full.encode()) <= STATUS_FILE_LIMIT:
        return {"STATUS.md": full}
    chunks = _split_status(full)
    page_names = [f"status/STATUS-{index:04d}.md" for index in range(1, len(chunks) + 1)]
    pages: dict[str, str] = dict(zip(page_names, chunks, strict=True))
    pages["STATUS.md"] = _status_index(full, page_names)
    if any(len(content.encode()) > STATUS_FILE_LIMIT for content in pages.values()):
        raise StatusRenderError("status projection exceeds the per-file size limit")
    return {"STATUS.md": pages.pop("STATUS.md"), **pages}


def render_status_pages(
    tasks: list[Task],
    statuses: tuple[str, ...],
    priorities: tuple[str, ...],
    project_title: str,
) -> dict[str, str]:
    """Render STATUS.md and deterministic shards when the complete view is large.

    The returned keys are repository-relative paths.  Small projects retain the
    historical single-file representation; larger projects receive a compact
    root index and numbered pages under ``status/``.
    """
    return render_status_pages_from_text(render_status(tasks, statuses, priorities, project_title))
