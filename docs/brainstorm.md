# Brainstorming Before Development

This file keeps a record of the discussion that happened before coding started.

## Assignment and constraints

The assignment asked for a project idea different from Part I, not a basic habit tracker or to-do list. It also asked to follow the two AI Shipping articles, use GitHub Issues, include Markdown documentation, build in iterations, use SQLite with an ORM, and test the app that actually runs.

## First idea

I chose FixFlow, a repair-order management app for a small laptop and computer repair shop. I picked it because it has a real workflow but does not need complicated features to be useful.

## Discussion notes

**My initial request:** I asked to begin by planning the actions for the Web Frontend assignment and said the work should be written in a way that looks like a normal student project.

**Project proposal:** The first idea was FixFlow. Its main features are repair orders, customer/device details, repair statuses, spare parts, and a public status lookup by order number.

**My preferences:** I said not to make it too impressive or too advanced. I asked to use ordinary tools and code that a regular student could understand, except where the assignment specifically requires something.

**Final scope decision:** Keep the first version simple. The interface can use a sidebar, dashboard cards, tables, status labels, and forms. The required technical steps stay: frontend with a mock service, OpenAPI contract, FastAPI with temporary in-memory data, SQLite via SQLAlchemy, frontend/backend integration, and tests.

## What is not part of the MVP

- Online payments
- SMS or email notifications
- AI diagnosis of broken devices
- Complex roles and staff permissions
- Multiple repair-shop branches

## Initial workflow

1. Plan and document the app.
2. Build the frontend with sample data through one service layer.
3. Describe the API in `openapi.yaml`.
4. Implement the API with temporary in-memory data.
5. Replace the temporary store with SQLite and SQLAlchemy.
6. Connect the frontend to the API.
7. Run the app, test the main flow, create bug issues when needed, and fix problems.

## Note

This is a project brainstorming record written before implementation. It summarizes the important decisions from the chat rather than exporting platform metadata or private system messages.
