"""Tests for the authentication layer (register, login, JWT)."""

# ruff: noqa: E402
import sys

from pathlib import Path

BACKEND_DIR = Path(__file__).parents[1] / 'src' / 'research' / 'backend'
sys.path.insert(0, str(BACKEND_DIR))


from fastapi.testclient import TestClient

# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------


def test_register_success(client: TestClient) -> None:
    """POST /api/auth/register should create a user and return 201."""
    resp = client.post(
        '/api/auth/register',
        json={
            'username': 'drsmith',
            'email': 'drsmith@example.com',
            'password': 'securepassword',
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data['username'] == 'drsmith'
    assert data['email'] == 'drsmith@example.com'
    assert data['is_active'] is True
    assert 'id' in data


def test_register_duplicate_email(client: TestClient) -> None:
    """POST /api/auth/register with an existing email should return 400."""
    payload = {
        'username': 'drjones',
        'email': 'duplicate@example.com',
        'password': 'password123',
    }
    client.post('/api/auth/register', json=payload)
    resp = client.post(
        '/api/auth/register',
        json={
            'username': 'drjones2',
            'email': 'duplicate@example.com',
            'password': 'anotherpassword',
        },
    )
    assert resp.status_code == 400


def test_register_duplicate_username(client: TestClient) -> None:
    """POST /api/auth/register with an existing username should return 400."""
    client.post(
        '/api/auth/register',
        json={
            'username': 'sameuser',
            'email': 'user1@example.com',
            'password': 'pass',
        },
    )
    resp = client.post(
        '/api/auth/register',
        json={
            'username': 'sameuser',
            'email': 'user2@example.com',
            'password': 'pass',
        },
    )
    assert resp.status_code == 400


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------


def test_login_success(client: TestClient) -> None:
    """POST /api/auth/login returns an access token on success."""
    client.post(
        '/api/auth/register',
        json={
            'username': 'drlogin',
            'email': 'drlogin@example.com',
            'password': 'correctpassword',
        },
    )
    resp = client.post(
        '/api/auth/login',
        data={
            'username': 'drlogin@example.com',
            'password': 'correctpassword',
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert 'access_token' in data
    assert data['token_type'] == 'bearer'


def test_login_wrong_password(client: TestClient) -> None:
    """POST /api/auth/login with wrong password returns 401."""
    client.post(
        '/api/auth/register',
        json={
            'username': 'drwrong',
            'email': 'drwrong@example.com',
            'password': 'rightpassword',
        },
    )
    resp = client.post(
        '/api/auth/login',
        data={
            'username': 'drwrong@example.com',
            'password': 'wrongpassword',
        },
    )
    assert resp.status_code == 401


def test_login_nonexistent_user(client: TestClient) -> None:
    """POST /api/auth/login for unknown user returns 401."""
    resp = client.post(
        '/api/auth/login',
        data={
            'username': 'nobody@example.com',
            'password': 'irrelevant',
        },
    )
    assert resp.status_code == 401


def test_login_with_username(client: TestClient) -> None:
    """POST /api/auth/login accepts username (not just email)."""
    client.post(
        '/api/auth/register',
        json={
            'username': 'byusername',
            'email': 'byusername@example.com',
            'password': 'mypass',
        },
    )
    resp = client.post(
        '/api/auth/login',
        data={'username': 'byusername', 'password': 'mypass'},
    )
    assert resp.status_code == 200
    assert 'access_token' in resp.json()


# ---------------------------------------------------------------------------
# /me endpoint
# ---------------------------------------------------------------------------


def test_me_authenticated(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """GET /api/auth/me returns the current user when token is valid."""
    resp = client.get('/api/auth/me', headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data['email'] == 'physician@test.com'
    assert data['username'] == 'testphysician'


def test_me_unauthenticated(client: TestClient) -> None:
    """GET /api/auth/me returns 401 when no token is provided."""
    resp = client.get('/api/auth/me')
    assert resp.status_code == 401


def test_me_invalid_token(client: TestClient) -> None:
    """GET /api/auth/me returns 401 for a tampered token."""
    resp = client.get(
        '/api/auth/me', headers={'Authorization': 'Bearer invalidtoken'}
    )
    assert resp.status_code == 401


# ---------------------------------------------------------------------------
# Protected patient endpoints
# ---------------------------------------------------------------------------


def test_protected_patients_without_token(client: TestClient) -> None:
    """GET /api/patients returns 401 when no authorization header is sent."""
    resp = client.get('/api/patients')
    assert resp.status_code == 401


def test_protected_patients_with_token(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    """GET /api/patients returns 200 when a valid token is included."""
    resp = client.get('/api/patients', headers=auth_headers)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_protected_post_patients_without_token(client: TestClient) -> None:
    """POST /api/patients returns 401 without authorization."""
    resp = client.post('/api/patients', json={'lang': 'en'})
    assert resp.status_code == 401


def test_health_check_is_public(client: TestClient) -> None:
    """GET /api/health should be accessible without authentication."""
    resp = client.get('/api/health')
    assert resp.status_code == 200
    assert resp.json()['status'] == 'ok'
