"""add token session

Revision ID: 33dabf91b731
Revises: d4d13501973d
Create Date: 2024-01-24 14:29:44.834293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33dabf91b731'
down_revision: Union[str, None] = 'd4d13501973d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('token', sa.String(length=255), nullable=False))
    op.create_index(op.f('ix_sessions_token'), 'sessions', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sessions_token'), table_name='sessions')
    op.drop_column('sessions', 'token')
    # ### end Alembic commands ###
