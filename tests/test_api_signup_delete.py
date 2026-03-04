from src.app import activities


def test_unregister_participant_success(client):
    activity_name = "Robotics Club"
    email = activities[activity_name]["participants"][0]

    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_missing_activity_returns_404(client):
    response = client.delete(
        "/activities/Not%20A%20Real%20Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_participant_returns_404(client):
    response = client.delete(
        "/activities/Debate%20Club/signup",
        params={"email": "not-registered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_missing_email_returns_422(client):
    response = client.delete("/activities/Debate%20Club/signup")

    assert response.status_code == 422
