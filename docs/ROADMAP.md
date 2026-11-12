# SAGE Development Roadmap

This roadmap distinguishes implemented code from behavior that has actually been verified.

## v0.1 — Local execution core

- [x] SQLite-backed project and task model
- [x] CLI commands for projects and tasks
- [x] Priority and status handling
- [x] Dashboard counts
- [x] Core unit tests
- [x] CLI workflow tests
- [x] `python -m sage` entry point
- [x] GitHub Actions matrix for Python 3.10, 3.11 and 3.12
- [ ] Confirm a successful clean CI run across the matrix

## v0.2 — Usability

- [ ] Interactive dashboard
- [ ] Due-date filtering and overdue view
- [ ] Edit and archive workflows
- [ ] Export and backup

## v0.3 — Executive review

- [ ] Daily review record
- [ ] Weekly review summary
- [ ] Blocker and dependency tracking
- [ ] Decision journal

## v0.4 — Optional AI assistance

- [ ] Provider-neutral model adapter
- [ ] Context preview before external transmission
- [ ] AI-generated plans clearly labeled as suggestions
- [ ] Human approval for consequential actions

## Release discipline

A checkbox is marked complete only after code exists and the documented behavior has been verified. The presence of a workflow or test file alone is not proof of a passing test run. Planned integrations must not be described as active capabilities.
