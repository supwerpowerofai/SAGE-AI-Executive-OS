# SAGE AI Executive OS

**A local-first, human-in-the-loop execution system for turning projects into clear next actions.**

SAGE v0.1 provides a Python command-line interface backed by SQLite. It can create and list projects, create and list tasks, update project/task statuses, and summarize execution counts. It is an early working foundation—not yet a hosted dashboard or autonomous AI agent.

## Current capabilities

- Create projects with a name and optional description.
- Track project status: active, paused, completed.
- Add tasks with priority 1 (highest) through 5 (lowest).
- Track task status: todo, in_progress, done.
- List tasks ordered by status and priority.
- View dashboard counts for active projects and task states.
- Persist data in a local SQLite database.

## Requirements

- Python 3.10 or newer
- pip

The application runtime uses only the Python standard library. Pytest and a Python 3.10 TOML compatibility dependency are used for tests.

## Install locally

Clone the repository, then from its root directory run:

```bash
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install the package and test tools:

```bash
python -m pip install -e .
python -m pip install pytest
```

Run the test suite:

```bash
python -m pytest -q
```

## Quick start

Create a project:

```bash
sage add-project "Launch website" --description "First business milestone"
```

Add a task (use the project ID printed by the previous command):

```bash
sage add-task 1 "Write homepage copy" --priority 1
```

List projects and tasks:

```bash
sage projects
sage tasks
```

Update a task and view the dashboard:

```bash
sage set-task-status 1 in_progress
sage dashboard
```

Use `--db path/to/file.db` before any command to choose a database file. By default, SAGE creates `sage.db` in the current working directory.

You can also launch the CLI with `python -m sage` after installing the package.

## GitHub Actions

The SAGE CI workflow runs the automated test suite on pushes, pull requests, and manual dispatch. It checks Python 3.10, 3.11, and 3.12. A configured workflow is not proof of a passing run; check the repository's Actions tab for the latest result.

## Architecture

- `src/sage/core.py`: SQLite schema and project/task operations.
- `src/sage/cli.py`: command-line interface.
- `src/sage/__main__.py`: `python -m sage` entry point.
- `tests/`: configuration, core behavior and CLI workflow tests.

## Current limitations

- Local single-user database; no cloud sync or hosted accounts.
- No graphical dashboard yet.
- No AI model or external messaging integration.
- No recurring tasks, calendar sync, or multi-user permissions.
- Due dates are stored as supplied; advanced date validation and reminders are not implemented.

## Product principles

1. Evidence before claims.
2. One clear next action over overwhelming task lists.
3. Human approval before consequential external actions.
4. Privacy-conscious local-first storage.
5. Features are marked complete only after implementation and verification.

## Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) and [the 21-project portfolio plan](docs/PORTFOLIO_21_PROJECTS.md).

## License

No open-source license has been selected. Until one is added, no license is granted to reuse, modify, or distribute this code.
