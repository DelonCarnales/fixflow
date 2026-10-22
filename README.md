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
- Database: SQLite with SQLAlchemy ORM
- Tests: Node's built-in test runner, Pytest, and Playwright browser checks

## Run the app

Start the backend in one terminal:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Start the frontend in another terminal:

```bash
cd frontend
python3 -m http.server 5173
```

Open http://localhost:5173. The normal mode uses the FastAPI backend. To work with sample data only, open http://localhost:5173/?mock=1.

The API docs are at http://127.0.0.1:8000/docs.

## Run it in GitHub without installing anything on your Mac

This repository is configured for GitHub Codespaces. Codespaces runs the app in a cloud development environment, so you only need a browser. In Codespaces, FastAPI also serves the frontend on port 8000 so browser requests to the API stay on the same origin and avoid forwarded-port CORS/authentication issues.

1. Open the repository on GitHub.
2. Click the green **Code** button and select **Codespaces**.
3. Click **Create codespace on main**.
4. Wait for the setup to finish. The configured environment installs the Python test/API packages and Node.js, then starts the app.
5. Open the forwarded **FixFlow App** port (8000). If it did not open automatically, find port 8000 in the **Ports** tab and choose **Open in Browser**. Use port 8000 for Codespaces; port 5173 is only for local development and CI tests.

If you pull updates to this repository and the old server is still running, open the Codespaces terminal and run:

```bash
bash .devcontainer/start.sh
```

Codespaces has monthly usage limits; use is subject to the quota for your GitHub account. The forwarded ports are private by default. Do not switch them to public when using real customer data. The app only contains fictional demo records.

## Run tests

Frontend mock service tests:

```bash
cd frontend
npm test
```

Backend API and OpenAPI tests:

```bash
cd backend
python -m pip install -r requirements.txt
python -m pytest -q
```

Browser smoke tests need Playwright. Start the backend and frontend first, then run:

```bash
python -m pip install -r frontend/requirements-test.txt
python -m playwright install chromium
python frontend/tests/browser_smoke.py
```

GitHub Actions runs JavaScript syntax checks, mock service tests, browser smoke tests against the SQLite-backed API, and backend tests when relevant files change.

## Development stages
1. Plan and write the docs.
2. Build the frontend using mock data.
3. Define the API in OpenAPI.
4. Build the backend with temporary in-memory data.
5. Replace the temporary store with SQLite using SQLAlchemy.
6. Connect the frontend to the backend.
7. Run the complete app and test the main flows.

## Current status
Planning docs, the frontend, mock service, OpenAPI contract, and FastAPI backend with SQLite/SQLAlchemy are in the repository. The frontend now defaults to the real API and can still run in mock mode with `?mock=1`. Check the latest GitHub Actions run for the current full-flow test result.
