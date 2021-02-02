"""empty message

Revision ID: 03efb5cc9e31
Revises: c029c87cd5ea
Create Date: 2021-01-30 12:13:31.984596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03efb5cc9e31'
down_revision = 'c029c87cd5ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
