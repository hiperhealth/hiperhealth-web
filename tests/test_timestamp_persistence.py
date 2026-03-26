from __future__ import annotations

from datetime import datetime, timezone

from uuid import uuid4


def test_create_patient_persists_timestamp(test_repo):
    # Create a new patient record via repository and ensure timestamp is stored
    patient_uuid = str(uuid4())
    created_at = datetime.now(timezone.utc).isoformat()
    patient_data = {
        'meta': {'uuid': patient_uuid, 'lang': 'en', 'timestamp': created_at},
        'patient': {},
    }

    test_repo.create_patient_and_consultation(patient_data)

    patient = test_repo.get_patient_by_uuid(patient_uuid)
    assert patient is not None
    assert patient.consultations
    consultation = patient.consultations[-1]
    assert consultation.timestamp is not None

    # Compare parsed timestamps to second precision
    ca = created_at.replace('Z', '+00:00')
    dt_ca = datetime.fromisoformat(ca)
    # The DB now stores and returns timestamps representing UTC.
    # SQLite drops timezone info natively, so we re-attach UTC if missing.
    stored_ts = consultation.timestamp
    if stored_ts.tzinfo is None:
        stored_ts = stored_ts.replace(tzinfo=timezone.utc)
    assert dt_ca.replace(microsecond=0) == stored_ts.replace(
        microsecond=0
    )
