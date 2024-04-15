"""Added Auth Table

Revision ID: 6ea2e9c4a3ed
Revises: b82d2e3367b2
Create Date: 2024-04-14 14:50:31.003067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ea2e9c4a3ed'
down_revision: Union[str, None] = 'b82d2e3367b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'authentications_', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'authentications_', type_='unique')
    # ### end Alembic commands ###