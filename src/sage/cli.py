"""Command-line interface for the SAGE local execution tracker."""
from __future__ import annotations

import argparse
from pathlib import Path

from .core import SageStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sage",
        description="A local-first project and next-action tracker.",
    )
    parser.add_argument(
        "--db", default="sage.db", help="SQLite database path (default: sage.db)"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    project_add = commands.add_parser("add-project", help="Create a project")
    project_add.add_argument("name")
    project_add.add_argument("--description", default="")

    commands.add_parser("projects", help="List projects")

    task_add = commands.add_parser("add-task", help="Add a task to a project")
    task_add.add_argument("project_id", type=int)
    task_add.add_argument("title")
    task_add.add_argument("--priority", type=int, default=3)
    task_add.add_argument("--due-date")

    task_list = commands.add_parser("tasks", help="List tasks")
    task_list.add_argument("--project-id", type=int)

    task_status = commands.add_parser("set-task-status", help="Update a task")
    task_status.add_argument("task_id", type=int)
    task_status.add_argument("status", choices=["todo", "in_progress", "done"])

    project_status = commands.add_parser(
        "set-project-status", help="Update a project"
    )
    project_status.add_argument(
        "project_id", type=int, help="Project ID"
    )
    project_status.add_argument(
        "status", choices=["active", "paused", "completed"]
    )

    commands.add_parser("dashboard", help="Show a summary")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = SageStore(Path(args.db))

    try:
        if args.command == "add-project":
            project_id = store.add_project(args.name, args.description)
            print(f"Created project #{project_id}: {args.name}")
        elif args.command == "projects":
            for project in store.list_projects():
                print(
                    f"#{project['id']} [{project['status']}] "
                    f"{project['name']} — {project['description']}"
                )
        elif args.command == "add-task":
            task_id = store.add_task(
                args.project_id, args.title, args.priority, args.due_date
            )
            print(f"Created task #{task_id}: {args.title}")
        elif args.command == "tasks":
            for task in store.list_tasks(args.project_id):
                print(
                    f"#{task['id']} [{task['status']}] "
                    f"P{task['priority']} {task['title']} "
                    f"(project: {task['project_name']})"
                )
        elif args.command == "set-task-status":
            store.set_task_status(args.task_id, args.status)
            print(f"Updated task #{args.task_id} to {args.status}")
        elif args.command == "set-project-status":
            store.set_project_status(args.project_id, args.status)
            print(f"Updated project #{args.project_id} to {args.status}")
        elif args.command == "dashboard":
            for label, value in store.dashboard().items():
                print(f"{label.replace('_', ' ').title()}: {value}")
    except (ValueError, OSError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
