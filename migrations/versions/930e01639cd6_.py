"""empty message

Revision ID: 930e01639cd6
Revises: 9aa0810ddc1d
Create Date: 2017-06-14 21:48:40.127650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '930e01639cd6'
down_revision = '9aa0810ddc1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'description')
    # ### end Alembic commands ###