"""Final Design

Revision ID: 2fdb1ce376f5
Revises: cfe302323b63
Create Date: 2024-07-06 23:32:44.321872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2fdb1ce376f5'
down_revision: Union[str, None] = 'cfe302323b63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    op.alter_column('user_address', 'postal_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user_address', 'country',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user_address', 'state')
    op.add_column('user_profile', sa.Column('national_id', sa.String(), nullable=True))
    op.add_column('user_profile', sa.Column('role', sa.String(), nullable=False))
    op.add_column('user_profile', sa.Column('verified_at', sa.DateTime(timezone=True), nullable=True))
    op.drop_constraint('user_profile_email_key', 'user_profile', type_='unique')
    op.drop_column('user_profile', 'email')
    op.drop_column('user_profile', 'is_verified')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('user_profile', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_profile_email_key', 'user_profile', ['email'])
    op.drop_column('user_profile', 'verified_at')
    op.drop_column('user_profile', 'role')
    op.drop_column('user_profile', 'national_id')
    op.add_column('user_address', sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('user_address', 'country',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user_address', 'postal_code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_table('role',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_profile.id'], name='role_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='role_pkey')
    )
    # ### end Alembic commands ###
