"""Changed models

Revision ID: e9fb91def7a6
Revises: 408ab54deff5
Create Date: 2023-12-08 17:23:40.581673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9fb91def7a6'
down_revision = '408ab54deff5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.alter_column('item_name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.alter_column('item_name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
