"""SQLAlchemy model for user authentication."""

from hiperhealth.models.sqla.fhirx import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    """User model for physician authentication."""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
