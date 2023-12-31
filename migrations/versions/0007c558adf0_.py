"""empty message

Revision ID: 0007c558adf0
Revises: c3728fea0d8b
Create Date: 2023-10-21 10:46:42.907743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0007c558adf0'
down_revision = 'c3728fea0d8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=125), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
