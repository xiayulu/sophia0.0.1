"""User: -phone +email +password_hash

Revision ID: 4594157f7597
Revises: dc2cf08a3dd4
Create Date: 2021-03-08 13:40:55.426203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4594157f7597'
down_revision = 'dc2cf08a3dd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=64)))
    op.add_column('user', sa.Column('password_hash', sa.String()))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_password_hash'), 'user', ['password_hash'], unique=False)
    op.drop_index('ix_user_phone', table_name='user')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.VARCHAR(length=11), autoincrement=False, nullable=False))
    op.create_index('ix_user_phone', 'user', ['phone'], unique=True)
    op.drop_index(op.f('ix_user_password_hash'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
