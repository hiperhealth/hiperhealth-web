"""Test cases for the wearable data API endpoints."""

from fastapi.testclient import TestClient


def test_upload_wearable_data_success(
    client: TestClient, test_repo, patients_json
):
    """Test successful upload of a valid wearable data file."""
    # Arrange: Create a patient and consultation
    patient_data = patients_json[0]
    patient_uuid = patient_data['meta']['uuid']
    test_repo.create_patient_and_consultation(patient_data)

    # Create a valid dummy CSV file in memory
    csv_content = b'timestamp,steps,heart_rate\n2024-04-14T10:00:00,500,85\n'
    files = {'files': ('data.csv', csv_content, 'text/csv')}

    # Act
    response = client.post(
        f'/api/consultations/{patient_uuid}/wearable-data/upload', files=files
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['success'] is True
    assert 'uploaded_files' in data
    assert 'data.csv' in [f['filename'] for f in data['uploaded_files']]


def test_upload_wearable_data_unsupported_format(
    client: TestClient, test_repo, patients_json
):
    """Test upload with an unsupported file format."""
    # Arrange
    patient_data = patients_json[0]
    patient_uuid = patient_data['meta']['uuid']
    test_repo.create_patient_and_consultation(patient_data)

    # Create a dummy text file in memory
    txt_content = b'Hello world'
    files = {'files': ('data.txt', txt_content, 'text/plain')}

    # Act
    response = client.post(
        f'/api/consultations/{patient_uuid}/wearable-data/upload', files=files
    )

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert 'Unsupported file format' in data['detail']


def test_upload_wearable_data_no_files(
    client: TestClient, test_repo, patients_json
):
    """Test upload endpoint when no files are provided."""
    # Arrange
    patient_data = patients_json[0]
    patient_uuid = patient_data['meta']['uuid']
    test_repo.create_patient_and_consultation(patient_data)

    # Act: post without files
    response = client.post(
        f'/api/consultations/{patient_uuid}/wearable-data/upload'
    )

    # Assert
    # FastAPI usually returns 422 Unprocessable Entity
    # when required body/form is missing
    assert response.status_code == 422


def test_upload_wearable_data_invalid_patient(client: TestClient):
    """Test upload for a patient that does not exist."""
    csv_content = b'timestamp,steps,heart_rate\n2024-04-14T10:00:00,500,85\n'
    files = {'files': ('data.csv', csv_content, 'text/csv')}

    response = client.post(
        '/api/consultations/invalid-uuid/wearable-data/upload', files=files
    )

    assert response.status_code == 404
    assert response.json()['detail'] == 'Patient not found'
