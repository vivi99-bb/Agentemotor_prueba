from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_policy_expired_40_days_not_renewable():

    response = client.get(
        "/api/policies?status=renewable"
    )

    assert response.status_code == 200

    policies = response.json()

    found = any(
        policy["policy_number"] == "POL-006"
        for policy in policies
    )

    assert not found