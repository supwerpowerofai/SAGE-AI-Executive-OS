# SAGE MVP Product Specification

## Problem

People managing multiple goals and projects often lack a reliable view of active work, the next action, and actual progress. SAGE aims to reduce that operational noise.

## MVP user

A solo founder or operator who needs a lightweight way to track projects and their next actions locally.

## MVP scope

- Create and list projects.
- Set a project to active, paused, or completed.
- Add tasks to a project.
- Set task priority from 1 (highest) to 5 (lowest).
- Track tasks as todo, in progress, or done.
- View a compact execution dashboard.
- Store data in a local SQLite database.

## Out of scope for this milestone

- Hosted multi-user accounts or synchronization.
- Autonomous agents or background actions.
- Sending email, SMS, WhatsApp, or social messages.
- Financial recommendations or brokerage integrations.
- External AI model calls.

## Acceptance criteria

1. A user can create a project from the CLI.
2. A user can add a task to an existing project.
3. Tasks can be listed in a useful priority/status order.
4. Project and task statuses can be updated.
5. Dashboard counts reflect persisted database records.
6. Invalid project names, priorities, IDs, and statuses are rejected.
7. Core behavior is covered by automated tests.

## Data and privacy

The first version stores information in a SQLite file at the path selected by the user. The database is local to the machine unless the user chooses to move or share it. Users should not store passwords, API keys, or sensitive personal data in project descriptions or task titles.

## AI integration policy

AI features are a later milestone. Any future model integration must identify what context is sent to a provider, allow users to review it, and keep consequential actions behind explicit human approval.
