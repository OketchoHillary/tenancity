"""empty message

Revision ID: d3bca16ce72c
Revises: 152bb1509596
Create Date: 2023-10-20 12:29:27.774313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3bca16ce72c'
down_revision = '152bb1509596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business_admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'business', ['business_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business_admin', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('business_id')

    # ### end Alembic commands ###