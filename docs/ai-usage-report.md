# AI Usage Report

## How AI was used
AI assistance was used to brainstorm the project idea, organize the specification, draft documentation, and split work into GitHub Issues. The project is intended to stay at a level that a student can understand and explain.

## Decisions made for FixFlow
- Chose a repair shop workflow instead of a generic tracker.
- Kept the MVP to repair orders, order search/filter, status history, spare parts, and customer status lookup.
- Chose HTML, CSS, and JavaScript modules for the first frontend so it stays easy to run and understand.
- Chose FastAPI for the backend.
- Chose OpenAPI as the contract between frontend and backend.
- Chose SQLite with SQLAlchemy for persistent storage.
- Planned to work in stages and run both automated and manual tests.

## How generated work will be checked
AI-generated code and docs are drafts, not proof of correctness. I will run the app locally, check the main user flows, run the tests, and create a `user-test-bug` issue for any bug that I discover by using the running app. An issue should only be closed after QA checks its acceptance criteria.

## Current status
Planning docs and the initial GitHub Issues have been added. The first frontend prototype is implemented and tested locally. The backend, OpenAPI contract, and database are not implemented yet.
