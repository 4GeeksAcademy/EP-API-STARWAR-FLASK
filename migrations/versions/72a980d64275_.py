"""empty message

Revision ID: 72a980d64275
Revises: b4c30293747e
Create Date: 2024-11-12 02:53:16.176022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a980d64275'
down_revision = 'b4c30293747e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_favorites_id_people'), ['id_people'], unique=False)
        batch_op.create_index(batch_op.f('ix_favorites_id_planet'), ['id_planet'], unique=False)
        batch_op.create_index(batch_op.f('ix_favorites_id_user'), ['id_user'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_favorites_id_user'))
        batch_op.drop_index(batch_op.f('ix_favorites_id_planet'))
        batch_op.drop_index(batch_op.f('ix_favorites_id_people'))

    # ### end Alembic commands ###