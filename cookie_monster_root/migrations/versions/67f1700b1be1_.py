"""empty message

Revision ID: 67f1700b1be1
Revises: None
Create Date: 2016-04-15 20:57:05.167424

"""

# revision identifiers, used by Alembic.
revision = '67f1700b1be1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cookies',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('host', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('value', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cookies')
    ### end Alembic commands ###