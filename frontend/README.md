# Frontend

This first version uses plain HTML, CSS, and JavaScript modules. It has no third-party frontend dependencies.

## Run it with the backend
Start the FastAPI backend first (see `../backend/README.md`). Then from this folder run:

```bash
python3 -m http.server 5173
```

Open http://localhost:5173. The frontend will call the backend at http://127.0.0.1:8000.

## Run with mock data
Open http://localhost:5173/?mock=1. This loads `src/services/mockService.js` without calling the backend. The data is kept in memory and resets when the page reloads.

## Tests
Run the mock service tests with:

```bash
npm test
```

The Playwright browser tests exercise the main pages against the local SQLite-backed API. See `tests/browser_smoke.py`.
