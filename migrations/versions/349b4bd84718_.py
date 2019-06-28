"""empty message

Revision ID: 349b4bd84718
Revises: 310c005eead8
Create Date: 2019-05-28 21:58:03.389219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349b4bd84718'
down_revision = '310c005eead8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('a', sa.String(), nullable=False))
    op.add_column('questions', sa.Column('b', sa.String(), nullable=False))
    op.add_column('questions', sa.Column('c', sa.String(), nullable=False))
    op.add_column('questions', sa.Column('d', sa.String(), nullable=False))
    op.drop_column('questions', 'options_c')
    op.drop_column('questions', 'options_a')
    op.drop_column('questions', 'options_d')
    op.drop_column('questions', 'options_b')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('options_b', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('questions', sa.Column('options_d', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('questions', sa.Column('options_a', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('questions', sa.Column('options_c', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('questions', 'd')
    op.drop_column('questions', 'c')
    op.drop_column('questions', 'b')
    op.drop_column('questions', 'a')
    # ### end Alembic commands ###