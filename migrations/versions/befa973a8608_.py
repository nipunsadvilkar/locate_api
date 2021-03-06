"""empty message

Revision ID: befa973a8608
Revises: None
Create Date: 2017-12-07 21:33:46.453040

"""

# revision identifiers, used by Alembic.
revision = 'befa973a8608'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locate',
    sa.Column('locate_id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=500), nullable=True),
    sa.Column('type_col', sa.String(length=15), nullable=True),
    sa.Column('response_dump', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('locate_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('locate')
    # ### end Alembic commands ###
