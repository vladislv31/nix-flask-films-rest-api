"""empty message

Revision ID: 38c610a0dd66
Revises: 67b4bc9e1095
Create Date: 2022-06-03 16:48:29.396918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38c610a0dd66'
down_revision = '67b4bc9e1095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film_genres', 'film_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('film_genres', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film_genres', 'genre_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('film_genres', 'film_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
