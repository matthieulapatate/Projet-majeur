"""Vehicules table

Revision ID: 8f157bd2622a
Revises: 
Create Date: 2020-05-29 15:09:13.041682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f157bd2622a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caserne',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position_x', sa.Float(), nullable=True),
    sa.Column('position_y', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_caserne_position_x'), 'caserne', ['position_x'], unique=False)
    op.create_index(op.f('ix_caserne_position_y'), 'caserne', ['position_y'], unique=False)
    op.create_table('personnel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categorie_personnel', sa.String(length=10), nullable=True),
    sa.Column('vehicule', sa.Integer(), nullable=True),
    sa.Column('experience', sa.Float(), nullable=True),
    sa.Column('caserne', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_personnel_caserne'), 'personnel', ['caserne'], unique=False)
    op.create_index(op.f('ix_personnel_categorie_personnel'), 'personnel', ['categorie_personnel'], unique=False)
    op.create_index(op.f('ix_personnel_experience'), 'personnel', ['experience'], unique=False)
    op.create_index(op.f('ix_personnel_vehicule'), 'personnel', ['vehicule'], unique=False)
    op.create_table('sonde',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position_x', sa.Float(), nullable=True),
    sa.Column('position_y', sa.Float(), nullable=True),
    sa.Column('etat', sa.Float(), nullable=True),
    sa.Column('alarme', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sonde_alarme'), 'sonde', ['alarme'], unique=False)
    op.create_index(op.f('ix_sonde_etat'), 'sonde', ['etat'], unique=False)
    op.create_index(op.f('ix_sonde_position_x'), 'sonde', ['position_x'], unique=False)
    op.create_index(op.f('ix_sonde_position_y'), 'sonde', ['position_y'], unique=False)
    op.create_table('vehicules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position_x', sa.Float(), nullable=True),
    sa.Column('position_y', sa.Float(), nullable=True),
    sa.Column('type_vehicule', sa.String(length=20), nullable=True),
    sa.Column('type_produit', sa.String(length=20), nullable=True),
    sa.Column('produit', sa.Float(), nullable=True),
    sa.Column('carburant', sa.Float(), nullable=True),
    sa.Column('caserne', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicules_carburant'), 'vehicules', ['carburant'], unique=False)
    op.create_index(op.f('ix_vehicules_caserne'), 'vehicules', ['caserne'], unique=False)
    op.create_index(op.f('ix_vehicules_position_x'), 'vehicules', ['position_x'], unique=False)
    op.create_index(op.f('ix_vehicules_position_y'), 'vehicules', ['position_y'], unique=False)
    op.create_index(op.f('ix_vehicules_produit'), 'vehicules', ['produit'], unique=False)
    op.create_index(op.f('ix_vehicules_type_produit'), 'vehicules', ['type_produit'], unique=False)
    op.create_index(op.f('ix_vehicules_type_vehicule'), 'vehicules', ['type_vehicule'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vehicules_type_vehicule'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_type_produit'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_produit'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_position_y'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_position_x'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_caserne'), table_name='vehicules')
    op.drop_index(op.f('ix_vehicules_carburant'), table_name='vehicules')
    op.drop_table('vehicules')
    op.drop_index(op.f('ix_sonde_position_y'), table_name='sonde')
    op.drop_index(op.f('ix_sonde_position_x'), table_name='sonde')
    op.drop_index(op.f('ix_sonde_etat'), table_name='sonde')
    op.drop_index(op.f('ix_sonde_alarme'), table_name='sonde')
    op.drop_table('sonde')
    op.drop_index(op.f('ix_personnel_vehicule'), table_name='personnel')
    op.drop_index(op.f('ix_personnel_experience'), table_name='personnel')
    op.drop_index(op.f('ix_personnel_categorie_personnel'), table_name='personnel')
    op.drop_index(op.f('ix_personnel_caserne'), table_name='personnel')
    op.drop_table('personnel')
    op.drop_index(op.f('ix_caserne_position_y'), table_name='caserne')
    op.drop_index(op.f('ix_caserne_position_x'), table_name='caserne')
    op.drop_table('caserne')
    # ### end Alembic commands ###
