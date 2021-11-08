"""empty message

Revision ID: b6e8dea2a4a3
Revises: 92e5392c05ef
Create Date: 2021-10-31 13:22:32.915530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e8dea2a4a3'
down_revision = '92e5392c05ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmado', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmado')
    # ### end Alembic commands ###