"""followers

Revision ID: 8231a9cd8df1
Revises: c5ba41b53d95
Create Date: 2024-08-07 18:32:17.071777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8231a9cd8df1'
down_revision = 'c5ba41b53d95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
