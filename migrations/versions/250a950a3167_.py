"""empty message

Revision ID: 250a950a3167
Revises: 
Create Date: 2021-04-07 12:19:51.136215

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '250a950a3167'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('doors', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('inventario')
    op.drop_table('ventas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ventas',
    sa.Column('idproducto', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('descripcion', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('precio', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('cantidad', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('fechaventa', postgresql.TIME(precision=0), autoincrement=False, nullable=True)
    )
    op.create_table('inventario',
    sa.Column('idproducto', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('precio', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('cantidad', sa.SMALLINT(), autoincrement=False, nullable=True)
    )
    op.drop_table('cars')
    # ### end Alembic commands ###
