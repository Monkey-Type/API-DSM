"""empty message

Revision ID: 34c57214a046
Revises: 705afb586253
Create Date: 2021-10-19 23:42:23.125172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34c57214a046'
down_revision = '705afb586253'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_area_default'), 'area', ['default'], unique=False)
    op.add_column('user', sa.Column('area_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'area', ['area_id'], ['id'])
    op.drop_column('user', 'cargo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cargo', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'area_id')
    op.drop_index(op.f('ix_area_default'), table_name='area')
    op.drop_table('area')
    # ### end Alembic commands ###