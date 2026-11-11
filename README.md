# SAGE AI Executive OS

**A practical, human-in-the-loop operating system for turning goals, projects, and decisions into accountable execution.**

SAGE is an evolving personal and business operations platform. Its purpose is to bring priorities, projects, tasks, reviews, and decision-making into one clear workflow—without pretending that an AI assistant can act autonomously or safely without permission.

> **Project status:** Initial repository and product definition. Features described as planned are not yet implemented. This README will be updated as working features are built and verified.

## Product vision

SAGE is designed around one operating principle:

**Turn important goals into clear priorities, small executable actions, and measurable progress.**

The system is intended to support:

- **Executive dashboard** — a concise view of current priorities, active projects, and progress.
- **Project operations** — track projects, owners, status, next actions, blockers, and evidence.
- **Daily execution** — convert plans into realistic tasks and make the next action obvious.
- **Review system** — daily, weekly, and monthly reviews that compare plans with actual outcomes.
- **Decision journal** — record decisions, assumptions, risks, and reasons so they can be revisited.
- **AI assistance** — help summarize context, draft plans, and suggest next actions, with human approval before consequential actions.

## Design principles

1. **Evidence before claims** — distinguish verified facts, assumptions, and unknowns.
2. **Human approval** — never imply that an external action was completed without confirmation.
3. **One clear next action** — reduce overload instead of generating endless task lists.
4. **Traceable progress** — connect outcomes to tasks, decisions, and supporting evidence.
5. **Privacy by design** — minimize collected data and document storage and processing choices.
6. **Honest capability boundaries** — label prototypes, planned features, and tested functionality accurately.

## Initial build roadmap

| Phase | Deliverable | Status |
|---|---|---|
| 0 | Product definition and repository foundation | In progress |
| 1 | Local-first project and task dashboard | Planned |
| 2 | Daily execution and review workflows | Planned |
| 3 | Decision journal and evidence tracking | Planned |
| 4 | Optional AI planning assistant | Planned |
| 5 | Integrations, permissions, and automation safeguards | Planned |

## Proposed initial architecture

The first milestone will be a small, understandable application with a local data store and a clear separation between:

- **Interface:** dashboard, project views, task views, and review screens.
- **Application logic:** prioritization, task status transitions, and review calculations.
- **Data layer:** projects, tasks, decisions, and review records.
- **AI adapter (later phase):** optional model integration behind an explicit interface.

The implementation stack will be selected before the first functional milestone and documented here. No cloud service, AI provider, or integration is assumed to be connected.

## Safety and trust

SAGE is an execution-support tool, not a financial, legal, medical, or other professional decision-maker. Recommendations should show their assumptions and uncertainty. External actions—such as sending messages, changing records, or making purchases—must require explicit authorization and a verifiable result.

## Development approach

Each milestone should include:

- Working source code
- Setup and run instructions
- Tests for core behavior
- Screenshots or a short demo when the interface exists
- Known limitations and next steps

A feature is considered implemented only when its code exists and the documented verification has been performed.

## Repository structure

The structure will grow as the application is implemented. The initial planned layout is:

```text
SAGE-AI-Executive-OS/
├── README.md
├── docs/
│   ├── PRODUCT_SPEC.md
│   └── ROADMAP.md
├── src/
│   ├── app/
│   ├── components/
│   └── core/
└── tests/
```

## Contributing

This is currently a personal portfolio project. Issues and constructive feedback are welcome. Before contributing code, please open an issue describing the proposed change.

## License

No license has been selected yet. Until a license is added, the source is not granted an open-source license by this repository.
