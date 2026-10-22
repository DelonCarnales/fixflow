# Simple Architecture

## Frontend
The frontend uses ordinary HTML, CSS, and JavaScript modules. The pages call one service file. During the first stage, the service returns sample data. Later, the same service will send HTTP requests to FastAPI.

## Backend
FastAPI exposes REST endpoints. SQLAlchemy models connect the Python code to SQLite.

## Main data
- Customer: name and phone
- Device: type and model
- RepairOrder: problem, status, dates, estimated cost, customer and device
- StatusHistory: status change and timestamp
- SparePart: name, stock quantity and unit price

## Main flow
Browser UI -> frontend service -> FastAPI -> SQLAlchemy -> SQLite

During the frontend-only stage:
Browser UI -> mockService -> sample data

## Important choice
The frontend should not talk directly to the database. It will use the API contract so the backend can change without rewriting the page behavior.
