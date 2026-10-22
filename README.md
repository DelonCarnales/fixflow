# FixFlow

FixFlow is a small web app for a computer and laptop repair shop. It keeps repair orders, customer details, repair status, and spare parts in one place.

This is a student project for a Web Frontend course. The goal is to build a working app step by step and keep the code easy to understand.

## Main features
- View, search, and filter repair orders
- Add and edit repair orders
- Change repair status and view its history
- Add and edit spare parts
- Let customers check a repair status by order number

## Stack
- Frontend: HTML, CSS, and JavaScript modules
- Backend: Python and FastAPI
- API contract: OpenAPI in `openapi.yaml`
- Database: SQLite with SQLAlchemy ORM (next backend stage)
- Tests: Node's built-in test runner, Pytest, and Playwright browser checks

## Run the frontend
In one terminal:

```bash
cd frontend
python3 -m http.server 5173
```

Open http://localhost:5173.

## Run the backend
In a second terminal:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

The API docs are at http://127.0.0.1:8000/docs.

## Run tests
Frontend mock service tests:

```bash
cd frontend
npm test
```

Backend and OpenAPI contract tests:

```bash
cd backend
python -m pytest -q
```

Browser smoke tests need Playwright. Start the frontend server first, then run:

```bash
python -m pip install -r frontend/requirements-test.txt
python -m playwright install chromium
python frontend/tests/browser_smoke.py
```

GitHub Actions runs the syntax checks, unit tests, browser smoke tests, and backend tests when relevant frontend/backend files change.

## Development stages
1. Plan and write the docs.
2. Build the frontend using mock data.
3. Define the API in OpenAPI.
4. Build the backend with temporary in-memory data.
5. Replace the temporary store with SQLite using SQLAlchemy.
6. Connect the frontend to the backend.
7. Run the complete app and test the main flows.

## Current status
The planning docs, frontend with mockService, OpenAPI contract, and in-memory FastAPI endpoints are in place. The frontend browser smoke tests and backend API tests pass in GitHub Actions. The next step is replacing the in-memory backend store with SQLite; the frontend is still using sample data and is not connected to the backend yet.
