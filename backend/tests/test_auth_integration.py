import uuid

from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.database import SessionLocal
from app.main import app
from app.models import User


def test_register_and_login_against_postgres():
    email = f"integration-{uuid.uuid4()}@example.com"
    client = TestClient(app)
    db = SessionLocal()

    try:
        register_response = client.post(
            "/api/auth/register",
            json={"name": "Integration User", "email": email, "password": "correct horse"},
        )
        assert register_response.status_code == 200
        assert register_response.json()["email"] == email

        login_response = client.post(
            "/api/auth/login",
            json={"email": email, "password": "correct horse"},
        )
        assert login_response.status_code == 200
        assert login_response.json()["email"] == email
        assert login_response.json()["token"]
    except OperationalError as exc:
        raise AssertionError(f"PostgreSQL is required for this integration test: {exc}") from exc
    finally:
        db.query(User).filter(User.email == email).delete()
        db.commit()
        db.close()
