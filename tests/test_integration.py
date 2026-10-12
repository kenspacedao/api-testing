import requests

def test_user_posts_belong_to_user(base_url, session):
    user = session.get(f"{base_url}/users/1").json()
    posts = session.get(f"{base_url}/users/{user['id']}/posts").json()
    assert len(posts) > 0
    for post in posts:
        assert post["userId"] == user["id"]

def test_post_comments_belong_to_post(base_url, session):
    post = session.get(f"{base_url}/posts/1").json()
    comments = session.get(f"{base_url}/posts/{post['id']}/comments").json()
    assert len(comments) > 0
    for comment in comments:
        assert comment["postId"] == post["id"]
