"""First commit

Revision ID: 491fc72a3816
Revises: 
Create Date: 2024-04-25 09:58:48.637301

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '491fc72a3816'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('directors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('studios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('studio_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['director_id'], ['directors.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['studio_id'], ['studios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_actor',
    sa.Column('movies_id', sa.Integer(), nullable=True),
    sa.Column('actors_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actors_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['movies_id'], ['movies.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_actor')
    op.drop_table('movies')
    op.drop_table('studios')
    op.drop_table('genres')
    op.drop_table('directors')
    op.drop_table('actors')
    # ### end Alembic commands ###
