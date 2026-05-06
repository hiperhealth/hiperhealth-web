"""Wearable data format helpers for XLSX, PDF, and ZIP pre-processing.

These utilities convert non-CSV/JSON wearable files into the
``list[dict]`` structure expected by the rest of the pipeline,
allowing the upload endpoint to accept XLSX, PDF and ZIP exports
from wearable devices and health apps.
"""

from __future__ import annotations

import csv
import io
import json
import logging
import zipfile

from typing import Any, Dict, List

import openpyxl
import pdfplumber

logger = logging.getLogger(__name__)

# --- XLSX Processing ---


def process_xlsx(file_bytes: bytes) -> List[Dict[str, Any]]:
    """Convert an XLSX file to a list of row dictionaries.

    Parameters
    ----------
    file_bytes : bytes
        Raw bytes of the XLSX file.

    Returns
    -------
    List[Dict[str, Any]]
        Each dict maps column headers to cell values.

    Raises
    ------
    ValueError
        If the workbook contains no data rows.
    """
    wb = openpyxl.load_workbook(
        io.BytesIO(file_bytes), read_only=True, data_only=True
    )
    ws = wb.active
    if ws is None:
        raise ValueError('XLSX workbook has no active sheet.')

    rows = list(ws.iter_rows(values_only=True))
    wb.close()

    if len(rows) < 2:
        raise ValueError(
            'XLSX file must contain a header row and at least one data row.'
        )

    headers = [
        str(h).strip() if h is not None else f'col_{i}'
        for i, h in enumerate(rows[0])
    ]
    result: List[Dict[str, Any]] = []
    for row in rows[1:]:
        row_dict: Dict[str, Any] = {}
        for header, value in zip(headers, row):
            row_dict[header] = value
        result.append(row_dict)
    return result


# --- PDF Processing ---


def process_pdf(file_bytes: bytes) -> List[Dict[str, Any]]:
    """Extract tabular data from a PDF file.

    Parameters
    ----------
    file_bytes : bytes
        Raw bytes of the PDF file.

    Returns
    -------
    List[Dict[str, Any]]
        Extracted rows from the first table found across pages.

    Raises
    ------
    ValueError
        If no tables are found in the PDF.
    """
    all_rows: List[Dict[str, Any]] = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if not table or len(table) < 2:
                    continue
                headers = [
                    str(h).strip() if h else f'col_{i}'
                    for i, h in enumerate(table[0])
                ]
                for row in table[1:]:
                    row_dict: Dict[str, Any] = {}
                    for header, value in zip(headers, row):
                        row_dict[header] = (
                            value.strip() if isinstance(value, str) else value
                        )
                    all_rows.append(row_dict)

    if not all_rows:
        raise ValueError(
            'No tabular data found in the PDF. '
            'Please upload a PDF containing health data tables.'
        )
    return all_rows


# --- ZIP Processing ---

# Extensions we look for inside ZIP archives.
_SUPPORTED_INNER = {'.csv', '.json', '.xlsx'}


def process_zip(file_bytes: bytes) -> List[Dict[str, Any]]:
    """Extract and process wearable data files from a ZIP archive.

    Parameters
    ----------
    file_bytes : bytes
        Raw bytes of the ZIP file.

    Returns
    -------
    List[Dict[str, Any]]
        Combined rows from all supported files found in the archive.

    Raises
    ------
    ValueError
        If the archive contains no supported files.
    """
    combined: List[Dict[str, Any]] = []

    with zipfile.ZipFile(io.BytesIO(file_bytes)) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            suffix = _get_suffix(info.filename)
            if suffix not in _SUPPORTED_INNER:
                continue

            inner_bytes = zf.read(info.filename)
            try:
                if suffix == '.csv':
                    combined.extend(_csv_bytes_to_dicts(inner_bytes))
                elif suffix == '.json':
                    combined.extend(_json_bytes_to_dicts(inner_bytes))
                elif suffix == '.xlsx':
                    combined.extend(process_xlsx(inner_bytes))
            except Exception:
                logger.warning(
                    'Skipping unreadable file in ZIP: %s', info.filename
                )

    if not combined:
        raise ValueError(
            'ZIP archive contains no supported wearable data files '
            '(CSV, JSON, XLSX).'
        )
    return combined


# --- Internal helpers ---


def _get_suffix(filename: str) -> str:
    """Return the lowercase file extension (e.g. '.csv')."""
    dot = filename.rfind('.')
    return filename[dot:].lower() if dot != -1 else ''


def _csv_bytes_to_dicts(data: bytes) -> List[Dict[str, Any]]:
    """Parse CSV bytes into a list of dictionaries."""
    text = data.decode('utf-8')
    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def _json_bytes_to_dicts(data: bytes) -> List[Dict[str, Any]]:
    """Parse JSON bytes into a list of dictionaries."""
    parsed = json.loads(data.decode('utf-8'))
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        return [parsed]
    return [{'value': parsed}]
