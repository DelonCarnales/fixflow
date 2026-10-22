# FixFlow

FixFlow is a small web app idea for a computer and laptop repair shop. It helps the shop keep repair orders, customer details, repair status, and parts in one place.

This is a student project for a Web Frontend course. The goal is to build a working app step by step, not to make a huge commercial system.

## Main features
- View, search, and filter repair orders
- Add repair orders and update their status
- See repair details and status history
- Keep a simple list of spare parts
- Let customers check a repair status by order number

## Planned stack
- Frontend: HTML, CSS, and JavaScript modules
- Backend: Python and FastAPI
- API contract: OpenAPI (`openapi.yaml`)
- Database: SQLite with SQLAlchemy ORM
- Tests: Node's built-in test runner, API tests, and browser checks

The frontend uses ordinary web files to keep the code easy to follow and avoid a large setup for this student project.

## Run the frontend
Open a terminal in the `frontend` folder and run:

```bash
python3 -m http.server 5173
```

Then open http://localhost:5173 in a browser.

## Run frontend service tests
From the `frontend` folder:

```bash
npm test
```

No third-party npm packages are needed for the frontend service tests.

## Development stages
1. Plan the app and write the basic docs.
2. Build the frontend using mock data.
3. Write the OpenAPI contract.
4. Make the backend work with temporary in-memory data.
5. Add SQLite and SQLAlchemy.
6. Connect the frontend to the backend.
7. Run the app and test the main user flows.

## Current status
Stage 1 is complete. The first frontend prototype is implemented locally and its service and browser checks have passed. The backend, OpenAPI contract, and SQLite persistence are still planned work.
