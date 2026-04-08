"""Password hashing utilities using bcrypt via passlib."""

from passlib.context import CryptContext

_pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(plain_password: str) -> str:
    """Hash a plain-text password using bcrypt."""
    return _pwd_context.hash(plain_password)  # type: ignore[no-any-return]


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a bcrypt hash."""
    return _pwd_context.verify(  # type: ignore[no-any-return]
        plain_password, hashed_password
    )
