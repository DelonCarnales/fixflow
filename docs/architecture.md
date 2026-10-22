# Simple Architecture

## Frontend
The frontend uses ordinary HTML, CSS, and JavaScript modules. Pages call a shared service selector. By default it uses `apiService.js` to send HTTP requests to FastAPI. Opening the app with `?mock=1` uses `mockService.js` and sample data.

## Backend
FastAPI exposes REST endpoints. SQLAlchemy models connect the Python code to SQLite. The database URL is read from `DATABASE_URL`, so a different SQLAlchemy-supported database can be selected later by changing configuration and installing its driver.

## Main data
- Customer: name and phone
- Device: type and model
- RepairOrder: problem, status, dates, estimated cost, customer and device
- StatusHistory: status change and timestamp
- SparePart: name, stock quantity and unit price

## Main flow
Browser UI -> frontend service -> FastAPI -> SQLAlchemy -> SQLite

Mock-only flow:
Browser UI -> service selector -> mockService -> sample data

## Important choice
The frontend does not talk directly to the database. It uses a service layer and API contract so the backend can change without rewriting page components.
