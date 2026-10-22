# QA Notes

Before closing an issue:
1. Read the issue and acceptance criteria.
2. Run the relevant automated tests.
3. Test the feature in the running app when possible.
4. Check a normal case and at least one invalid or edge case where relevant.
5. Record any failure and create a `user-test-bug` issue.
6. If a bug was fixed, retest the exact reproduction steps.
7. Close the issue only after the criteria pass.

For each bug, add test cases to `docs/testing-guidelines.md` if they are useful for future checks.
