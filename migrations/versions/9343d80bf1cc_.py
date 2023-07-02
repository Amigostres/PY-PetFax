"""empty message

Revision ID: 9343d80bf1cc
Revises: 
Create Date: 2023-07-02 11:16:00.496033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9343d80bf1cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('fact_id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('fact_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###