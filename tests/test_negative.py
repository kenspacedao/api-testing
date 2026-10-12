import pytest
import requests

@pytest.mark.parametrize("post_id, expected_status", [
    (1, 200),      # first valid ID
    (100, 200),    # last valid ID
    (0, 404),      # just below the range
    (101, 404),    # just above the range
    (9999, 404),   # far out of range
    ("abc", 404),  # wrong type
])
def test_post_id_boundaries(post_id, expected_status, base_url, session):
    r = session.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == expected_status
