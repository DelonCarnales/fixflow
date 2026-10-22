# Frontend

This first version uses plain HTML, CSS, and JavaScript modules. It has no third-party frontend dependencies.

## Run it
From this folder:

```bash
python3 -m http.server 5173
```

Open http://localhost:5173.

## Tests
Run the mock service tests with:

```bash
npm test
```

All demo data is currently stored in memory in `src/services/mockService.js`. Refreshing the page resets changes. This is expected at this stage; persistent storage will be added later through the backend and SQLite.
