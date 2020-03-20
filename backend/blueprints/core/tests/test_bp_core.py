
def test_bp_health_status_code_ok(client):
    url = '/health'
    response = client.get(url)
    assert response.status_code == 200
