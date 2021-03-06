"""Correcting downvote column name

Revision ID: e0a79d0a79c4
Revises: 945ea394e797
Create Date: 2022-05-18 23:29:59.267138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a79d0a79c4'
down_revision = '945ea394e797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('downvotes', sa.Column('blog_id', sa.Integer(), nullable=True))
    op.drop_constraint('downvotes_blogs_id_fkey', 'downvotes', type_='foreignkey')
    op.create_foreign_key(None, 'downvotes', 'blogs', ['blog_id'], ['id'])
    op.drop_column('downvotes', 'blogs_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('downvotes', sa.Column('blogs_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.create_foreign_key('downvotes_blogs_id_fkey', 'downvotes', 'blogs', ['blogs_id'], ['id'])
    op.drop_column('downvotes', 'blog_id')
    # ### end Alembic commands ###
