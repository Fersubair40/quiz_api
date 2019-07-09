"""empty message

Revision ID: d276f976d03a
Revises: 0a75c7ab3aa0
Create Date: 2019-07-09 13:12:30.360103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd276f976d03a'
down_revision = '0a75c7ab3aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('responses', sa.Column('answer', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('responses', 'answer')
    # ### end Alembic commands ###
