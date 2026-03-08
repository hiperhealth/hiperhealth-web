"""Unit tests for the request body size middleware."""

import pytest

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

_LIMIT = 100


def _create_app(max_bytes: int = _LIMIT) -> FastAPI:
    """Build a minimal app with the body size middleware."""
    mini = FastAPI()

    @mini.middleware('http')
    async def limit_body(request: Request, call_next):
        """Reject bodies exceeding the configured limit."""
        cl = request.headers.get('content-length')
        if cl is not None:
            try:
                if int(cl) > max_bytes:
                    return JSONResponse(
                        status_code=413,
                        content={'detail': 'Request body too large'},
                    )
            except ValueError:
                pass

        body = await request.body()
        if len(body) > max_bytes:
            return JSONResponse(
                status_code=413,
                content={'detail': 'Request body too large'},
            )

        return await call_next(request)

    @mini.post('/echo')
    async def echo():
        """Return ok for any request."""
        return {'ok': True}

    return mini


@pytest.fixture()
def poc_client():
    """Provide a TestClient with the body size middleware."""
    return TestClient(_create_app(), raise_server_exceptions=True)


def test_oversized_content_length_rejected(poc_client):
    """Content-Length above the limit must return 413."""
    resp = poc_client.post(
        '/echo',
        headers={'content-length': str(_LIMIT + 1)},
    )
    assert resp.status_code == 413
    assert resp.json()['detail'] == 'Request body too large'


def test_oversized_body_rejected(poc_client):
    """Actual body exceeding limit must return 413."""
    resp = poc_client.post('/echo', content=b'x' * (_LIMIT + 1))
    assert resp.status_code == 413


def test_exact_limit_allowed(poc_client):
    """Content-Length exactly at the limit must pass."""
    resp = poc_client.post(
        '/echo',
        headers={'content-length': str(_LIMIT)},
    )
    assert resp.status_code == 200


def test_under_limit_allowed(poc_client):
    """Content-Length below the limit must pass."""
    resp = poc_client.post(
        '/echo',
        headers={'content-length': '1'},
    )
    assert resp.status_code == 200


def test_no_content_length_small_body_allowed(poc_client):
    """Small body without Content-Length must pass."""
    resp = poc_client.post('/echo', content=b'hi')
    assert resp.status_code == 200


def test_invalid_content_length_allowed(poc_client):
    """Non-integer Content-Length must not crash."""
    resp = poc_client.post(
        '/echo',
        headers={'content-length': 'not-a-number'},
    )
    assert resp.status_code == 200
