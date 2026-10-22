# GitHub Issues Index

GitHub Issues are the canonical backlog. This document is only a quick index; GitHub issue state, labels, and comments take precedence if anything differs.

## MVP issues
- #1 Set up the frontend project — closed
- #2 Finalize MVP scope and acceptance criteria — closed
- #3 Set up basic app layout and sidebar — closed
- #4 Add dashboard with mock data — closed
- #5 Add repair orders table — closed
- #6 Add order search and status filter — closed
- #7 Add create repair order form — closed
- #8 Add repair order form validation — closed
- #9 Add repair order details page — closed
- #10 Add status updates and repair history — closed
- #11 Add edit repair order form — closed
- #12 Add spare parts page — closed
- #13 Add customer order status lookup page — closed
- #14 Create OpenAPI contract — closed
- #15 Set up FastAPI backend — closed
- #16 Implement in-memory repair order endpoints — closed
- #17 Implement in-memory spare parts endpoints — closed
- #18 Add SQLAlchemy models — closed
- #19 Replace in-memory store with SQLite — closed
- #20 Connect frontend service to the real API — open until full browser integration passes
- #21 Add frontend tests — closed
- #22 Add backend API tests — closed
- #23 Run full repair workflow in a browser — open until full browser integration passes
- #24 Update README with setup and testing commands — closed
- #28 Create one mockService for frontend data — closed

## Post-MVP issues
- #25 Improve mobile layout
- #26 Add sorting to repair orders table
- #27 Add CSV export for repair orders

## Bugs found while testing
- #29 Fix spare-part ID generation syntax — closed
- #30 Treat the expected unknown-order 404 as handled — awaiting final CI verification

## Workflow
Every issue should have Goal, Description, Acceptance criteria, Out of scope, and Constraints. PM grooms its scope. The engineer implements without closing it. QA checks the acceptance criteria, runs tests, posts a PASS/FAIL comment, and closes only after PASS.
