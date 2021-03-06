"""empty message

Revision ID: 66ad55ccee41
Revises: 
Create Date: 2022-03-01 12:52:30.672055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66ad55ccee41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('whiskey',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('alc_percent', sa.String(length=20), nullable=False),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('whiskey')
    op.drop_table('user')
    # ### end Alembic commands ###
