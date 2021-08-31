"""create test_ecommerce db and table

Revision ID: bca950936911
Revises: 367ac00537b3
Create Date: 2021-08-31 12:26:32.258140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bca950936911"
down_revision = "367ac00537b3"
branch_labels = None
depends_on = None

"""

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    password = Column(String(200), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
"""


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_name", sa.String(100), nullable=False, unique=True),
        sa.Column("email", sa.String(100), nullable=True, unique=True),
        sa.Column("password", sa.String(200), nullable=False),
        sa.Column("active", sa.Boolean, default=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now()
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table("users")
