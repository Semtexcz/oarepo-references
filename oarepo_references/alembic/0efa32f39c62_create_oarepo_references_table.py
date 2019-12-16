#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Create oarepo_references table."""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = '0efa32f39c62'
down_revision = '4a3d88773122'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('oarepo_records_references',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('record_uuid', sqlalchemy_utils.types.uuid.UUIDType(), nullable=False),
    sa.Column('reference', sa.String(length=255), nullable=False),
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_oarepo_records_references')),
    sa.UniqueConstraint('record_uuid', 'reference', name='_record_reference_uc')
    )
    op.create_index(op.f('ix_oarepo_records_references_record_uuid'), 'oarepo_records_references', ['record_uuid'], unique=False)
    op.create_index(op.f('ix_oarepo_records_references_reference'), 'oarepo_records_references', ['reference'], unique=False)
    op.create_table('oarepo_records_references_version',
    sa.Column('created', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('updated', sa.DateTime(), autoincrement=False, nullable=True),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=False),
    sa.Column('record_uuid', sqlalchemy_utils.types.uuid.UUIDType(), autoincrement=False, nullable=True),
    sa.Column('reference', sa.String(length=255), autoincrement=False, nullable=True),
    sa.Column('version_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name=op.f('pk_oarepo_records_references_version'))
    )
    op.create_index(op.f('ix_oarepo_records_references_version_end_transaction_id'), 'oarepo_records_references_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_oarepo_records_references_version_operation_type'), 'oarepo_records_references_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_oarepo_records_references_version_record_uuid'), 'oarepo_records_references_version', ['record_uuid'], unique=False)
    op.create_index(op.f('ix_oarepo_records_references_version_reference'), 'oarepo_records_references_version', ['reference'], unique=False)
    op.create_index(op.f('ix_oarepo_records_references_version_transaction_id'), 'oarepo_records_references_version', ['transaction_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_oarepo_records_references_version_transaction_id'), table_name='oarepo_records_references_version')
    op.drop_index(op.f('ix_oarepo_records_references_version_reference'), table_name='oarepo_records_references_version')
    op.drop_index(op.f('ix_oarepo_records_references_version_record_uuid'), table_name='oarepo_records_references_version')
    op.drop_index(op.f('ix_oarepo_records_references_version_operation_type'), table_name='oarepo_records_references_version')
    op.drop_index(op.f('ix_oarepo_records_references_version_end_transaction_id'), table_name='oarepo_records_references_version')
    op.drop_table('oarepo_records_references_version')
    op.drop_index(op.f('ix_oarepo_records_references_reference'), table_name='oarepo_records_references')
    op.drop_index(op.f('ix_oarepo_records_references_record_uuid'), table_name='oarepo_records_references')
    op.drop_table('oarepo_records_references')
    # ### end Alembic commands ###
