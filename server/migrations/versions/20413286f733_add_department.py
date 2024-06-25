"""add department

Revision ID: 20413286f733
Revises: 89ecfa68b7b6
Create Date: 2024-06-25 14:26:31.790289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20413286f733'
down_revision = '89ecfa68b7b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
