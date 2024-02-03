"""update session

Revision ID: f5bfb31307a2
Revises: 33dabf91b731
Create Date: 2024-01-24 14:30:53.383855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5bfb31307a2'
down_revision: Union[str, None] = '33dabf91b731'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'data',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_column('sessions', 'state')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('state', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.alter_column('sessions', 'data',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###