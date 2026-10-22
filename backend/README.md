# Backend

The first backend version uses a small in-memory store so the API can be tested before adding the database.

## Run locally
From the `backend` folder:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Open http://127.0.0.1:8000/docs for the automatic API page.

## Tests
From the `backend` folder:

```bash
python -m pytest -q
```

## Current limitation
This version resets sample data when the server restarts. The next backend step will replace the lists with SQLite using SQLAlchemy.
