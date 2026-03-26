"""Tests for create patient endpoint behavior."""

from datetime import datetime
from unittest.mock import Mock

from app.main import create_new_patient
from app.schemas import CreatePatientRequest


def test_create_new_patient_persists_consultation_timestamp() -> None:
    """Response created_at should match timestamp persisted in repo payload."""
    repo = Mock()
    req = CreatePatientRequest(lang='en')

    resp = create_new_patient(req=req, repo=repo)

    assert resp.lang == 'en'
    assert resp.patient_id
    datetime.fromisoformat(resp.created_at)

    repo.create_patient_and_consultation.assert_called_once()
    persisted_record = repo.create_patient_and_consultation.call_args.args[0]
    persisted_timestamp = persisted_record['meta']['timestamp']

    assert persisted_record['meta']['lang'] == 'en'
    assert persisted_record['meta']['uuid'] == resp.patient_id
    assert persisted_timestamp == resp.created_at
