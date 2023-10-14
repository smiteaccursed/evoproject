"""UUID

Revision ID: cc49473257ab
Revises: 55dc6b8c6f35
Create Date: 2023-10-10 15:32:15.810515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc49473257ab'
down_revision: Union[str, None] = '55dc6b8c6f35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('library', sa.Column('user_id', sa.UUID(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('library', 'user_id')
    # ### end Alembic commands ###