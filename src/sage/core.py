"""Core local-first project and task operations for SAGE.

This module deliberately uses only the Python standard library.
It stores data in a SQLite database on the user's machine.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'paused', 'completed')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    priority INTEGER NOT NULL DEFAULT 3
        CHECK (priority BETWEEN 1 AND 5),
    status TEXT NOT NULL DEFAULT 'todo'
        CHECK (status IN ('todo', 'in_progress', 'done')),
    due_date TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);
"""


class SageStore:
    """Small SQLite-backed store for projects and their next actions."""

    def __init__(self, database: str | Path = "sage.db") -> None:
        self.database = str(database)
        with self._connect() as connection:
            connection.executescript(SCHEMA)

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def add_project(self, name: str, description: str = "") -> int:
        name = name.strip()
        if not name:
            raise ValueError("Project name cannot be empty.")
        with self._connect() as connection:
            cursor = connection.execute(
                "INSERT INTO projects (name, description) VALUES (?, ?)",
                (name, description.strip()),
            )
            return int(cursor.lastrowid)

    def list_projects(self, status: str | None = None) -> list[dict[str, Any]]:
        query = "SELECT * FROM projects"
        values: tuple[Any, ...] = ()
        if status is not None:
            if status not in {"active", "paused", "completed"}:
                raise ValueError("Invalid project status.")
            query += " WHERE status = ?"
            values = (status,)
        query += " ORDER BY created_at, id"
        with self._connect() as connection:
            return [dict(row) for row in connection.execute(query, values)]

    def add_task(
        self,
        project_id: int,
        title: str,
        priority: int = 3,
        due_date: str | None = None,
    ) -> int:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if not 1 <= priority <= 5:
            raise ValueError("Priority must be between 1 (highest) and 5 (lowest).")
        with self._connect() as connection:
            project = connection.execute(
                "SELECT id FROM projects WHERE id = ?", (project_id,)
            ).fetchone()
            if project is None:
                raise ValueError(f"Project {project_id} does not exist.")
            cursor = connection.execute(
                """INSERT INTO tasks (project_id, title, priority, due_date)
                   VALUES (?, ?, ?, ?)""",
                (project_id, title, priority, due_date),
            )
            return int(cursor.lastrowid)

    def list_tasks(self, project_id: int | None = None) -> list[dict[str, Any]]:
        query = """
            SELECT tasks.*, projects.name AS project_name
            FROM tasks JOIN projects ON projects.id = tasks.project_id
        """
        values: tuple[Any, ...] = ()
        if project_id is not None:
            query += " WHERE tasks.project_id = ?"
            values = (project_id,)
        query += """
            ORDER BY CASE tasks.status WHEN 'in_progress' THEN 0
                       WHEN 'todo' THEN 1 ELSE 2 END,
                     tasks.priority ASC, tasks.id ASC
        """
        with self._connect() as connection:
            return [dict(row) for row in connection.execute(query, values)]

    def set_task_status(self, task_id: int, status: str) -> None:
        if status not in {"todo", "in_progress", "done"}:
            raise ValueError("Status must be todo, in_progress, or done.")
        with self._connect() as connection:
            cursor = connection.execute(
                "UPDATE tasks SET status = ? WHERE id = ?", (status, task_id)
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Task {task_id} does not exist.")

    def set_project_status(self, project_id: int, status: str) -> None:
        if status not in {"active", "paused", "completed"}:
            raise ValueError("Status must be active, paused, or completed.")
        with self._connect() as connection:
            cursor = connection.execute(
                "UPDATE projects SET status = ? WHERE id = ?",
                (status, project_id),
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Project {project_id} does not exist.")

    def dashboard(self) -> dict[str, int]:
        with self._connect() as connection:
            projects = connection.execute(
                "SELECT COUNT(*) FROM projects WHERE status = 'active'"
            ).fetchone()[0]
            open_tasks = connection.execute(
                "SELECT COUNT(*) FROM tasks WHERE status != 'done'"
            ).fetchone()[0]
            in_progress = connection.execute(
                "SELECT COUNT(*) FROM tasks WHERE status = 'in_progress'"
            ).fetchone()[0]
            completed = connection.execute(
                "SELECT COUNT(*) FROM tasks WHERE status = 'done'"
            ).fetchone()[0]
        return {
            "active_projects": int(projects),
            "open_tasks": int(open_tasks),
            "in_progress_tasks": int(in_progress),
            "completed_tasks": int(completed),
        }
