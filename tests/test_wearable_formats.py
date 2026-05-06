"""Tests for wearable data format pre-processing helpers."""

from pathlib import Path

from app.wearable_formats import process_pdf, process_xlsx, process_zip

DATA_DIR = Path(__file__).parent / 'data' / 'wearable'


def test_process_xlsx() -> None:
    """Verify XLSX files are parsed into row dictionaries."""
    file_path = DATA_DIR / 'sample_data.xlsx'
    with open(file_path, 'rb') as f:
        content = f.read()

    data = process_xlsx(content)
    assert len(data) == 2
    assert data[0]['timestamp'] == '2024-04-14T10:00:00'
    assert data[0]['steps'] == 500
    assert data[1]['heart_rate'] == 85


def test_process_pdf() -> None:
    """Verify PDF tables are extracted into row dictionaries."""
    file_path = DATA_DIR / 'sample_report.pdf'
    with open(file_path, 'rb') as f:
        content = f.read()

    data = process_pdf(content)
    assert len(data) >= 1
    # Check if the first row contains our expected data
    found = False
    for row in data:
        if 'timestamp' in row and '2024-04-14T10:00' in str(row['timestamp']):
            assert str(row['steps']) == '1500'
            found = True
            break
    assert found, 'Expected data not found in PDF output'


def test_process_zip() -> None:
    """Verify ZIP archives are unpacked and inner files parsed."""
    file_path = DATA_DIR / 'sample_export.zip'
    with open(file_path, 'rb') as f:
        content = f.read()

    data = process_zip(content)
    # CSV has 2 rows, JSON has 1 object => 3 items
    assert len(data) == 3
    # Check for CSV data
    assert any(item.get('timestamp') == '2024-04-14T08:00:00' for item in data)
    assert any(item.get('steps') == '300' for item in data)
    # Check for JSON metadata
    assert any(item.get('source') == 'Apple Health' for item in data)
