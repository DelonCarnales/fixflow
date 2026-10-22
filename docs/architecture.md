# Simple Architecture

## Frontend
The frontend uses ordinary HTML, CSS, and JavaScript modules. Pages call a service file. Right now the service returns sample data; the next integration step will replace it with HTTP requests to FastAPI.

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

Current frontend-only flow:
Browser UI -> mockService -> sample data

## Important choice
The frontend does not talk directly to the database. It uses a service layer and API contract so the backend can change without rewriting page components.
