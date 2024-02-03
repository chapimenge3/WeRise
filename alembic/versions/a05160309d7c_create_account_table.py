"""create account table

Revision ID: a05160309d7c
Revises: 
Create Date: 2024-01-24 12:17:42.282399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a05160309d7c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telegram_verifications',
    sa.Column('telegram_id', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('passport_data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('personal_details', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('driver_license', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('identity_card', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('utility_bill', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('bank_statement', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('address', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('address_documents', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('identity_front_side', sa.String(length=255), nullable=True),
    sa.Column('identity_reverse_side', sa.String(length=255), nullable=True),
    sa.Column('selfie', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('pending', 'approved', 'rejected', name='statusenum'), nullable=False),
    sa.Column('rejected_reason', sa.Text(), nullable=True),
    sa.Column('approved_at', sa.DateTime(), nullable=True),
    sa.Column('rejected_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_telegram_verifications_id'), 'telegram_verifications', ['id'], unique=False)
    op.create_index(op.f('ix_telegram_verifications_telegram_id'), 'telegram_verifications', ['telegram_id'], unique=True)
    op.create_table('users',
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('telegram_id', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_telegram_id'), 'users', ['telegram_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_telegram_id'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_telegram_verifications_telegram_id'), table_name='telegram_verifications')
    op.drop_index(op.f('ix_telegram_verifications_id'), table_name='telegram_verifications')
    op.drop_table('telegram_verifications')
    # ### end Alembic commands ###
