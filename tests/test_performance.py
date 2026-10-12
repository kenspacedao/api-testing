def test_get_posts_latency_under_one_second(base_url, session):
    response = session.get(f"{base_url}/posts")
    assert response.status_code == 200
    
    # response.elapsed measures the round-trip time in seconds
    elapsed_seconds = response.elapsed.total_seconds()
    print(f"\nResponse time: {elapsed_seconds:.3f}s")
    
    # SLA threshold: must be under 1.0 second
    assert elapsed_seconds < 1.0
