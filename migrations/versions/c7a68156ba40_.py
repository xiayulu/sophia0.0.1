"""empty message

Revision ID: c7a68156ba40
Revises: a5b96f01ad6f
Create Date: 2021-03-06 16:20:11.791408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7a68156ba40'
down_revision = 'a5b96f01ad6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('latest_version_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chapter', 'version', ['latest_version_id'], ['id'])
    op.add_column('user', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'status')
    op.drop_constraint(None, 'chapter', type_='foreignkey')
    op.drop_column('chapter', 'latest_version_id')
    # ### end Alembic commands ###
