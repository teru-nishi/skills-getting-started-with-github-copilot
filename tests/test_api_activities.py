def test_get_activities_returns_activity_map(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "Debate Club" in data
    assert "participants" in data["Debate Club"]
