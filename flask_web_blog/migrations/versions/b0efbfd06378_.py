"""empty message

Revision ID: b0efbfd06378
Revises: e1c0e0a8b5ce
Create Date: 2018-12-19 12:00:21.151738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b0efbfd06378'
down_revision = 'e1c0e0a8b5ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('uname', table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('uname', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('rold_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('confirmed', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['rold_id'], ['roles.id'], name='users_ibfk_1'),
    sa.PrimaryKeyConstraint('uid'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('uname', 'users', ['uname'], unique=True)
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###
