"""description

Revision ID: 3d198cbad967
Revises: 
Create Date: 2025-05-24 09:30:50.212407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d198cbad967'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('discussion', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.Text(),
               nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.drop_column('content')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('discussion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.TEXT(), nullable=False))
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=300),
               nullable=True)

    # ### end Alembic commands ###
