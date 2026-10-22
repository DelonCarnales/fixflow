# Project Plan

## Idea
FixFlow is a simple repair-order management app for a small laptop and computer repair shop.

## Why I picked it
I wanted an idea that is more useful than a basic list app, but still possible to finish for a university project. A repair shop has clear things to manage: customers, devices, repair jobs, statuses, and spare parts.

## Main users
- Shop employee: creates orders and updates their status.
- Technician: checks repair details and adds notes.
- Customer: checks the current status using an order number.

## Development stages
1. **Planning:** agree on MVP, write project docs, prepare GitHub labels and issues.
2. **Frontend with mockService:** build the pages and interactions with local mock data.
3. **OpenAPI contract:** describe the API in `openapi.yaml`.
4. **Backend in memory:** implement the endpoints with temporary data.
5. **SQLite:** add SQLAlchemy models and persistent storage.
6. **Integration:** replace mockService calls with real API calls.
7. **Testing:** run the app and test important flows; fix bugs and document them.

## MVP checklist
- [x] Dashboard with basic counts
- [x] Repair orders list
- [x] Search and status filter
- [x] Create and edit repair order
- [x] Repair details page
- [x] Change repair status
- [x] Customer and device details
- [x] Simple spare-parts list
- [x] Public order status lookup
- [x] Backend API (currently using in-memory data)
- [x] SQLite storage through SQLAlchemy
- [x] Tests for the main features
- [x] Manual/browser checks of the main flow

## Not in MVP
- Online payments
- SMS or email notifications
- AI diagnosis
- Multi-branch shop support
- Complex staff roles and permissions

## Definition of done
A feature is done when it works in the running app, its main behavior has a test where practical, and the related GitHub issue has been checked by QA before closing.
