"""
Authentication and authorization package for HIPAA-compliant access control.
"""

from .dependencies import (
    get_current_active_user,
    get_current_user,
    require_permission,
    require_role,
)
from .password import PasswordManager
from .rbac import RBACManager
from .session import SessionManager

__all__ = [
    'PasswordManager',
    'RBACManager',
    'SessionManager',
    'get_current_active_user',
    'get_current_user',
    'require_permission',
    'require_role',
]
