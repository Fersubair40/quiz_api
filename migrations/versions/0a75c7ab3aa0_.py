"""empty message

Revision ID: 0a75c7ab3aa0
Revises: 349b4bd84718
Create Date: 2019-07-09 12:21:39.090712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a75c7ab3aa0'
down_revision = '349b4bd84718'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('responses', 'answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('responses', sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
