"""empty message

Revision ID: c14cd2b8478e
Revises: 7e35660351ef
Create Date: 2021-10-24 00:18:03.214376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c14cd2b8478e'
down_revision = '7e35660351ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('postagem', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'postagem', ['postagem'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'postagem')
    # ### end Alembic commands ###