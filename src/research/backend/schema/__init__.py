"""Research schema package.

Expose common Pydantic schemas from the submodules for convenient imports.
"""

from .auth import (
    AuditLogResponse,
    PasswordChange,
    PermissionCheck,
    RoleAssignment,
    UserCreate,
    UserLogin,
    UserResponse,
    UserUpdate,
)
from .ui import (
    Consultation,
    ConsultationBase,
    ConsultationCreate,
    ConsultationDiagnosis,
    ConsultationDiagnosisBase,
    ConsultationDiagnosisCreate,
    ConsultationExam,
    ConsultationExamBase,
    ConsultationExamCreate,
    Diagnosis,
    DiagnosisBase,
    DiagnosisCreate,
    Exam,
    ExamBase,
    ExamCreate,
    Patient,
    PatientBase,
    PatientCreate,
)

__all__ = [  # noqa: RUF022
    'UserLogin',
    'UserCreate',
    'UserUpdate',
    'UserResponse',
    'PasswordChange',
    'RoleAssignment',
    'PermissionCheck',
    'AuditLogResponse',
    'PatientBase',
    'PatientCreate',
    'Patient',
    'ConsultationBase',
    'ConsultationCreate',
    'Consultation',
    'DiagnosisBase',
    'DiagnosisCreate',
    'Diagnosis',
    'ExamBase',
    'ExamCreate',
    'Exam',
    'ConsultationDiagnosisBase',
    'ConsultationDiagnosisCreate',
    'ConsultationDiagnosis',
    'ConsultationExamBase',
    'ConsultationExamCreate',
    'ConsultationExam',
]
