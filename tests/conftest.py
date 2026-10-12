import os
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def session():
    with requests.Session() as s:
        yield s
