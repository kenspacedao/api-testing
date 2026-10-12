# API Test Automation & QA Framework

Comprehensive automated test suite and performance testing harness for RESTful APIs built with Python, Pytest, Requests, and Locust.

## Test Architecture

- **Functional Testing (`tests/test_posts.py`)**: Validates REST CRUD behavior, HTTP status codes, payload structures, and response headers.
- **Boundary & Negative Testing (`tests/test_negative.py`)**: Uses parameterized inputs (`@pytest.mark.parametrize`) to test boundary IDs (`0`, `1`, `100`, `101`) and invalid input types.
- **Integration Testing (`tests/test_integration.py`)**: Tests relational data integrity across endpoints (`/users` -> `/posts` -> `/comments`).
- **Performance & SLA Verification (`tests/test_performance.py`)**: Automated latency threshold checks (`< 1.0s`).
- **Load Testing (`performance/locustfile.py`)**: Headless concurrent user load simulation measuring throughput and p95/p99 latency percentiles.
- **Continuous Integration (`.github/workflows/tests.yml`)**: Automated CI pipeline running the regression suite on every push and pull request.

## Setup & Execution

### 1. Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
