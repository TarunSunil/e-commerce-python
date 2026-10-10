"""Create the initial ecommerce schema.

Revision ID: 0001_baseline
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_baseline"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.Column("roles", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column("preferences", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String()),
        sa.Column("categories", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column("price", sa.Numeric(12, 2), nullable=False),
        sa.Column("images", postgresql.ARRAY(sa.String()), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False),
        sa.Column("attributes", postgresql.JSONB(), nullable=False),
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("total", sa.Numeric(12, 2), nullable=False),
        sa.Column("shipping_address", postgresql.JSONB(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "order_items",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("order_id", sa.String(), sa.ForeignKey("orders.id", ondelete="CASCADE"), nullable=False),
        sa.Column("product_id", sa.String(), sa.ForeignKey("products.id", ondelete="SET NULL")),
        sa.Column("qty", sa.Integer(), nullable=False),
        sa.Column("price", sa.Numeric(12, 2), nullable=False),
        sa.Column("product_name", sa.String(), nullable=False),
        sa.Column("unit_price", sa.Numeric(12, 2), nullable=False),
    )
    op.create_table(
        "carts",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("product_id", sa.String(), sa.ForeignKey("products.id", ondelete="CASCADE"), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("price", sa.Numeric(12, 2), nullable=False),
        sa.Index("ix_cart_user_product", "user_id", "product_id", unique=True),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_index("ix_products_name", "products", ["name"])
    op.create_index("ix_products_categories", "products", ["categories"])
    op.create_index("ix_orders_user_id", "orders", ["user_id"])
    op.create_index("ix_order_items_order_id", "order_items", ["order_id"])
    op.create_index("ix_carts_user_id", "carts", ["user_id"])
    op.create_index("ix_carts_product_id", "carts", ["product_id"])


def downgrade() -> None:
    op.drop_index("ix_carts_product_id", table_name="carts")
    op.drop_index("ix_carts_user_id", table_name="carts")
    op.drop_index("ix_order_items_order_id", table_name="order_items")
    op.drop_index("ix_orders_user_id", table_name="orders")
    op.drop_index("ix_products_categories", table_name="products")
    op.drop_index("ix_products_name", table_name="products")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("carts")
    op.drop_table("order_items")
    op.drop_table("orders")
    op.drop_table("products")
    op.drop_table("users")
