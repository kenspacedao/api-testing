import requests

def test_get_post_returns_200_and_fields(base_url, session):
    r = session.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    body = r.json()
    assert body["id"] == 1
    assert "title" in body

def test_get_all_posts_returns_100(base_url, session):
    r = session.get(f"{base_url}/posts")
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) == 100

def test_create_post_returns_201(base_url, session):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = session.post(f"{base_url}/posts", json = payload)
    assert r.status_code == 201
    assert r.json()["title"] == "foo"

def test_update_post_returns_200(base_url, session):
    payload = {"id": 1, "title": "updated", "body": "new body", "userId": 1}
    r = session.put(f"{base_url}/posts/1", json=payload)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"

def test_delete_post_returns_200(base_url, session):
    r = session.delete(f"{base_url}/posts/1")
    assert r.status_code == 200
