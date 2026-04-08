"""JWT and authentication configuration settings."""

import os

# Secret key used to sign JWT tokens.
# MUST be set in the environment (.envs/.env) before starting the server.
SECRET_KEY: str = os.getenv('SECRET_KEY', '')
if not SECRET_KEY:
    raise RuntimeError(
        'SECRET_KEY environment variable is not set. '
        'Please add SECRET_KEY to your .envs/.env file.'
    )

ALGORITHM: str = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
    os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '60')
)
