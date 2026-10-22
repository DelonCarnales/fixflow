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
- [ ] Dashboard with basic counts
- [ ] Repair orders list
- [ ] Search and status filter
- [ ] Create and edit repair order
- [ ] Repair details page
- [ ] Change repair status
- [ ] Customer and device details
- [ ] Simple spare-parts list
- [ ] Public order status lookup
- [ ] Backend API
- [ ] SQLite storage through SQLAlchemy
- [ ] Tests for the main features
- [ ] Manual browser test of the main flow

## Not in MVP
- Online payments
- SMS or email notifications
- AI diagnosis
- Multi-branch shop support
- Complex staff roles and permissions

## Definition of done
A feature is done when it works in the running app, its main behavior has a test where practical, and the related GitHub issue has been checked by QA before closing.
