"""Add wearable_files table.

Revision ID: a3f7c2d91e84
Revises: 16e578626d45
Create Date: 2026-04-27 17:12:00.000000

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a3f7c2d91e84'
down_revision: Union[str, Sequence[str], None] = '16e578626d45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the wearable_files table for per-file upload tracking."""
    op.create_table(
        'wearable_files',
        sa.Column('id', sa.String(36), nullable=False),
        sa.Column(
            'consultation_id',
            sa.Integer(),
            sa.ForeignKey('consultations.id'),
            nullable=False,
        ),
        sa.Column('filename', sa.String(255), nullable=False),
        sa.Column('file_size', sa.Integer(), nullable=True),
        sa.Column('mime_type', sa.String(100), nullable=True),
        sa.Column('uploaded_at', sa.DateTime(), nullable=True),
        sa.Column('extracted_data', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    """Drop the wearable_files table."""
    op.drop_table('wearable_files')
