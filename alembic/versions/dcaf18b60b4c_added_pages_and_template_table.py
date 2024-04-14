"""Added Pages and Template Table

Revision ID: dcaf18b60b4c
Revises: 7452e7b79a64
Create Date: 2024-04-14 19:09:15.324297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'dcaf18b60b4c'
down_revision: Union[str, None] = '7452e7b79a64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('site_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('meta', sa.JSON(), nullable=True),
    sa.Column('page_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('page_handle', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('store_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tag', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('templates',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('meta', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('templates')
    op.drop_table('pages')
    # ### end Alembic commands ###
