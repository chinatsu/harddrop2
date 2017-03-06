"""modify password column

Revision ID: 8aa3ac86df05
Revises: 
Create Date: 2017-03-06 19:29:55.486251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import VARCHAR


# revision identifiers, used by Alembic.
revision = '8aa3ac86df05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('phpfox_user', 'password', type_=VARCHAR(90))


def downgrade():
    op.alter_column('phpfox_user', 'password', type_=VARCHAR(35))
