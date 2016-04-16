"""empty message

Revision ID: bc6e4688a6ad
Revises: 67f1700b1be1
Create Date: 2016-04-15 21:01:19.944914

"""

# revision identifiers, used by Alembic.
revision = 'bc6e4688a6ad'
down_revision = '67f1700b1be1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cookies', sa.Column('date', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cookies', 'date')
    ### end Alembic commands ###