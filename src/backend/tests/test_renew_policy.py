from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_renew_policy():

    payload = {
        "new_expiration_date": "2027-12-31"
    }

    response = client.post(
        "/api/policies/4/renew",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Policy renewed successfully"