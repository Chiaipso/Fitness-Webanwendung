"""empty message

Revision ID: 0a98c5d22bb7
Revises: cccb589b323a
Create Date: 2023-03-23 18:27:28.126453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a98c5d22bb7'
down_revision = 'cccb589b323a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('benutzer', schema=None) as batch_op:
        batch_op.drop_index('ix_benutzer_apitoken')
        batch_op.drop_column('apitoken')
        batch_op.drop_column('ablaufdatum')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('benutzer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ablaufdatum', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('apitoken', mysql.VARCHAR(length=32), nullable=True))
        batch_op.create_index('ix_benutzer_apitoken', ['apitoken'], unique=False)

    # ### end Alembic commands ###
