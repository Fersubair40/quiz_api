"""empty message

Revision ID: 77490dc75617
Revises: 32450280245d
Create Date: 2019-05-14 16:55:07.092179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77490dc75617'
down_revision = '32450280245d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answers', 'response_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answers', 'response_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
