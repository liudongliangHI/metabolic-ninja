"""add organism id

Revision ID: a83d6985270b
Revises: edd63b1ec9e3
Create Date: 2018-11-09 16:11:55.802538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83d6985270b'
down_revision = 'edd63b1ec9e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('design_job', sa.Column('organism_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('design_job', 'organism_id')
    # ### end Alembic commands ###
