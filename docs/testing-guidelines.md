# Testing Guidelines

## Frontend service tests
Run from the `frontend` folder with `npm test`. This uses Node's built-in test runner, so there is no install step.

- The service returns the seeded orders.
- Creating an order gives it a new order number and initial history.
- Changing status updates the order and appends a history entry.
- Negative spare-part quantity is rejected.
- Adding a spare part creates a new ID.

## Browser checks for the frontend prototype
The following flows were checked in Chromium against the current frontend source:
- Dashboard summary and recent orders appear.
- Search finds the matching device.
- Status filter only shows matching orders.
- Empty new-order form shows validation errors.
- Valid order can be created and opens its details.
- Changing order status updates the current status and history.
- Spare part can be added.
- Customer lookup displays the correct status.
- Unknown order number shows a clear message.
- The page has no page-level horizontal overflow at a phone-sized viewport.

The browser in the development container blocks direct navigation to local files and local URLs, so these UI flows were tested using an inline test bundle made from the same application source. The normal app itself is served with the command in the README.

## Backend tests (planned)
- Creating an order returns the created order.
- Missing required fields return a validation error.
- Unknown order IDs return 404.
- Invalid statuses are rejected.
- Negative cost and stock values are rejected.
- Updating an order changes its saved values.
- Data remains after restarting the app once SQLite is implemented.

## Bug reporting
For a bug found while using the running app, create a GitHub issue with:
- Label: `user-test-bug`
- Goal
- Description
- Steps to reproduce
- Expected result
- Actual result
- Browser/OS if relevant

Do not write that a test passed unless it was actually run.
