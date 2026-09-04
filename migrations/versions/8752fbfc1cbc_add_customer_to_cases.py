"""add customer to cases

Revision ID: 8752fbfc1cbc
Revises: 79eae3ae26b5
Create Date: 2026-08-10 01:04:11.608913

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision: str = "8752fbfc1cbc"

down_revision: Union[str, Sequence[str], None] = "79eae3ae26b5"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # --------------------------------------------------
    # Add customer_id to fact_case
    # --------------------------------------------------

    op.add_column(
        "fact_case",
        sa.Column(
            "customer_id",
            sa.String(length=30),
            nullable=True,
        ),
    )

    # --------------------------------------------------
    # Create foreign key
    # fact_case.customer_id
    # -> dim_customer.customer_id
    # --------------------------------------------------

    op.create_foreign_key(
        "fk_fact_case_customer_id",
        "fact_case",
        "dim_customer",
        ["customer_id"],
        ["customer_id"],
    )

    # --------------------------------------------------
    # Make alert_key nullable
    # --------------------------------------------------

    op.alter_column(
        "fact_case",
        "alert_key",
        existing_type=sa.Integer(),
        nullable=True,
    )

    # --------------------------------------------------
    # Create index for customer_id
    # --------------------------------------------------

    op.create_index(
        "ix_fact_case_customer_id",
        "fact_case",
        ["customer_id"],
    )


def downgrade() -> None:

    # --------------------------------------------------
    # Remove customer_id index
    # --------------------------------------------------

    op.drop_index(
        "ix_fact_case_customer_id",
        table_name="fact_case",
    )

    # --------------------------------------------------
    # Remove customer foreign key
    # --------------------------------------------------

    op.drop_constraint(
        "fk_fact_case_customer_id",
        "fact_case",
        type_="foreignkey",
    )

    # --------------------------------------------------
    # Restore alert_key as NOT NULL
    # --------------------------------------------------

    op.alter_column(
        "fact_case",
        "alert_key",
        existing_type=sa.Integer(),
        nullable=False,
    )

    # --------------------------------------------------
    # Remove customer_id
    # --------------------------------------------------

    op.drop_column(
        "fact_case",
        "customer_id",
    )