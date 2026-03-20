"""Pytest configuration for the hiperhealth package tests."""

# ruff: noqa: E402
from __future__ import annotations

import json
import os
import sys
import warnings

from pathlib import Path

import pytest

BACKEND_DIR = Path(__file__).parents[1] / 'src' / 'research' / 'backend'
sys.path.insert(0, str(BACKEND_DIR))

# Set SECRET_KEY before importing the app so auth.config does not raise.
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-pytest')

from app.auth.dependencies import _get_db as auth_get_db
from app.main import app
from app.models.auth import User  # noqa: F401 — registers users table
from app.models.repositories import ResearchRepository
from app.models.ui import (  # noqa: F401 — registers all tables
    Consultation,
    Patient,
)
from dotenv import dotenv_values, load_dotenv
from fastapi.testclient import TestClient
from hiperhealth.agents.extraction.medical_reports import (
    MedicalReportFileExtractor,
)
from hiperhealth.agents.extraction.wearable import WearableDataFileExtractor
from hiperhealth.models.sqla.fhirx import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


@pytest.fixture
def env() -> dict[str, str | None]:
    """Return a fixture for the environment variables from .env file."""
    # This assumes a .envs/.env file at the project root
    dotenv_path = Path(__file__).parents[1] / '.envs' / '.env'
    if not dotenv_path.exists():
        warnings.warn(
            f"'.env' file not found at {dotenv_path}. Some "
            'tests requiring environment variables might fail or be skipped.'
        )
        return {}
    load_dotenv(dotenv_path=dotenv_path)
    return dotenv_values(dotenv_path)


@pytest.fixture
def api_key_openai(env: dict[str, str | None]) -> str | None:
    """Fixture providing the OpenAI API key. Skips test if not found."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        pytest.skip('OpenAI API key not available')
    return api_key


@pytest.fixture
def test_data_dir() -> Path:
    """Fixture providing the path to the test data directory."""
    return Path(__file__).parent / 'data'


@pytest.fixture
def reports_pdf_dir(test_data_dir: Path) -> Path:
    """Fixture for the directory containing PDF report files."""
    return test_data_dir / 'reports' / 'pdf_reports'


@pytest.fixture
def reports_image_dir(test_data_dir: Path) -> Path:
    """Fixture for the directory containing image report files."""
    return test_data_dir / 'reports' / 'image_reports'


@pytest.fixture(scope='session')
def patients_json() -> list[dict]:
    """Load the test patients JSON data."""
    path = Path(__file__).parent / 'data' / 'patients' / 'patients.json'
    return json.loads(path.read_text())


@pytest.fixture
def wearable_extractor():
    """Provide a WearableDataFileExtractor instance for tests."""
    return WearableDataFileExtractor()


@pytest.fixture
def medical_extractor():
    """Provide a MedicalReportFileExtractor instance for tests."""
    return MedicalReportFileExtractor()


# Use StaticPool so all sessions share the same in-memory SQLite connection.
# Without this, each new connection gets its own isolated :memory: database.
TEST_DB_URL = 'sqlite:///:memory:'
engine = create_engine(
    TEST_DB_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


@pytest.fixture(scope='function')
def db_session():
    """Create a new database session for each test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope='function')
def test_repo(db_session):
    """Provide a ResearchRepository instance with a test database session."""
    return ResearchRepository(db_session)


def _override_get_db():
    """Yield an in-memory DB session for test client dependency overrides."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    """FastAPI test client fixture with in-memory DB overrides."""
    from app.main import get_db as main_get_db

    app.dependency_overrides[auth_get_db] = _override_get_db
    app.dependency_overrides[main_get_db] = _override_get_db
    Base.metadata.create_all(bind=engine)
    tc = TestClient(app)
    yield tc
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def auth_headers(client: TestClient) -> dict[str, str]:
    """Register and log in a test physician; return authorization headers."""
    client.post(
        '/api/auth/register',
        json={
            'username': 'testphysician',
            'email': 'physician@test.com',
            'password': 'testpassword123',
        },
    )
    resp = client.post(
        '/api/auth/login',
        data={
            'username': 'physician@test.com',
            'password': 'testpassword123',
        },
    )
    token = resp.json()['access_token']
    return {'Authorization': f'Bearer {token}'}
