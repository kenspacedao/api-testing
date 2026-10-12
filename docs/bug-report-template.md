# QA Defect Report Template (Jira Standard)

### [DEFECT-ID] Short, descriptive summary of the issue

- **Severity**: Critical / High / Medium / Low
- **Priority**: P1 (Blocker) / P2 (High) / P3 (Medium) / P4 (Low)
- **Component / Endpoint**: e.g., `POST /posts`
- **Environment**: e.g., Staging / Production (`https://jsonplaceholder.typicode.com`)
- **Reported By**: Kenny
- **Date**: 2026-10-10

---

### Description

Brief summary of what went wrong and why it violates system expectations.

### Steps to Reproduce

1. Send HTTP request to endpoint:
   - Method: `GET` / `POST` / `PUT` / `DELETE`
   - URL: `https://jsonplaceholder.typicode.com/...`
   - Headers: `Content-Type: application/json`
   - Body: `{"..."}`
2. Inspect the HTTP response status code and JSON body.

### Expected Result

What the requirement / specification states should happen.
(e.g., `HTTP 201 Created` with created record ID and matching payload fields).

### Actual Result

What actually happened.
(e.g., `HTTP 500 Internal Server Error` or missing fields in response).

### Evidence / Logs

- **Test Case**: `tests/test_posts.py::test_create_post_returns_201`
- **Failure Output / Stack Trace**:

```text
AssertionError: assert 500 == 201
```
