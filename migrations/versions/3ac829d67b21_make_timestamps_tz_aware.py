"""Make timestamps tz-aware.

Revision ID: 3ac829d67b21
Revises: 16e578626d45
Create Date: 2026-03-27 02:30:00.000000

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3ac829d67b21'
down_revision: Union[str, Sequence[str], None] = '16e578626d45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('consultations', schema=None) as batch_op:
        batch_op.alter_column(
            'timestamp',
            existing_type=sa.DateTime(),
            type_=sa.DateTime(timezone=True),
            existing_nullable=True,
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('consultations', schema=None) as batch_op:
        batch_op.alter_column(
            'timestamp',
            existing_type=sa.DateTime(timezone=True),
            type_=sa.DateTime(),
            existing_nullable=True,
        )
