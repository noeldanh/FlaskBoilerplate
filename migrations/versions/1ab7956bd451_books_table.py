"""books table

Revision ID: 1ab7956bd451
Revises: 9fbaa59dfcb6
Create Date: 2018-02-15 19:43:51.401571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ab7956bd451'
down_revision = '9fbaa59dfcb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('review', sa.String(length=140), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_timestamp'), 'book', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_timestamp'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
