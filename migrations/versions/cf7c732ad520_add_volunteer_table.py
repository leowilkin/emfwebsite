"""add volunteer table

Revision ID: cf7c732ad520
Revises: 79a1e6e2ebfa
Create Date: 2018-07-29 22:21:07.602218

"""

# revision identifiers, used by Alembic.
revision = 'cf7c732ad520'
down_revision = '79a1e6e2ebfa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('volunteer_role_mapping_version',
    sa.Column('volunteer_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('role_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('volunteer_id', 'role_id', 'transaction_id', name=op.f('pk_volunteer_role_mapping_version'))
    )
    op.create_index(op.f('ix_volunteer_role_mapping_version_operation_type'), 'volunteer_role_mapping_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_volunteer_role_mapping_version_transaction_id'), 'volunteer_role_mapping_version', ['transaction_id'], unique=False)
    op.create_table('volunteer_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('planned_arrival', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('planned_departure', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('nickname', sa.String(), autoincrement=False, nullable=True),
    sa.Column('missing_shifts_opt_in', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('banned', sa.Boolean(), autoincrement=False, nullable=True),
    sa.Column('volunteer_phone', sa.String(), autoincrement=False, nullable=True),
    sa.Column('volunteer_email', sa.String(), autoincrement=False, nullable=True),
    sa.Column('age', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_volunteer_version'))
    )
    op.create_index(op.f('ix_volunteer_version_operation_type'), 'volunteer_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_volunteer_version_transaction_id'), 'volunteer_version', ['transaction_id'], unique=False)
    op.create_table('volunteer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planned_arrival', sa.DateTime(), nullable=True),
    sa.Column('planned_departure', sa.DateTime(), nullable=True),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('missing_shifts_opt_in', sa.Boolean(), nullable=False),
    sa.Column('banned', sa.Boolean(), nullable=False),
    sa.Column('volunteer_phone', sa.String(), nullable=False),
    sa.Column('volunteer_email', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_volunteer_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_volunteer'))
    )
    op.create_table('volunteer_role_mapping',
    sa.Column('volunteer_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['volunteer_role.id'], name=op.f('fk_volunteer_role_mapping_role_id_volunteer_role')),
    sa.ForeignKeyConstraint(['volunteer_id'], ['volunteer.id'], name=op.f('fk_volunteer_role_mapping_volunteer_id_volunteer')),
    sa.PrimaryKeyConstraint('volunteer_id', 'role_id', name=op.f('pk_volunteer_role_mapping'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('volunteer_role_mapping')
    op.drop_table('volunteer')
    op.drop_index(op.f('ix_volunteer_version_transaction_id'), table_name='volunteer_version')
    op.drop_index(op.f('ix_volunteer_version_operation_type'), table_name='volunteer_version')
    op.drop_table('volunteer_version')
    op.drop_index(op.f('ix_volunteer_role_mapping_version_transaction_id'), table_name='volunteer_role_mapping_version')
    op.drop_index(op.f('ix_volunteer_role_mapping_version_operation_type'), table_name='volunteer_role_mapping_version')
    op.drop_table('volunteer_role_mapping_version')
    # ### end Alembic commands ###
