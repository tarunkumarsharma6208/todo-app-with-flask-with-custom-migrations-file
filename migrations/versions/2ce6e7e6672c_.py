"""empty message

Revision ID: 2ce6e7e6672c
Revises: 
Create Date: 2023-03-11 12:31:09.171198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce6e7e6672c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=1000), nullable=True))
        batch_op.drop_column('completed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('description')

    # ### end Alembic commands ###
