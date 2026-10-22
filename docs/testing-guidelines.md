# Testing Guidelines

## Frontend
- The order list displays sample orders.
- Search returns matching orders.
- Status filter shows only orders with the selected status.
- Required fields show validation errors.
- A valid order can be added and appears in the list.
- A user can open an order details page.
- Status labels show the correct text.

## Backend
- Creating an order returns the created order.
- Missing required fields return a validation error.
- Unknown order IDs return 404.
- Invalid statuses are rejected.
- Negative cost and stock values are rejected.
- Updating an order changes its saved values.
- Data remains after restarting the app once SQLite is implemented.

## Manual browser testing
Follow this main flow:
1. Open the app.
2. Open Repair Orders.
3. Search for an existing order.
4. Create a new order with valid data.
5. Open the new order.
6. Change its status to Diagnosing.
7. Refresh and confirm the data is still present after database integration.
8. Use the customer lookup page with the order number.
9. Try submitting a form with required fields missing.
10. Check the browser console for errors.

## Bug reporting
For a bug found during manual testing, create a GitHub issue with:
- Label: `user-test-bug`
- Goal
- Description
- Steps to reproduce
- Expected result
- Actual result
- Browser/OS if relevant

Do not write that a test passed unless it was actually run.
