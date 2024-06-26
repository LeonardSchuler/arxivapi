"""init

Revision ID: ead3fa8b26cb
Revises:
Create Date: 2024-05-06 17:26:04.336244

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op


# revision identifiers, used by Alembic.
revision = "ead3fa8b26cb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_author_name"), "author", ["name"], unique=True)
    op.create_table(
        "query",
        sa.Column("query", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("num_results", sa.Integer(), nullable=False),
        sa.Column("status", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "article",
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("journal", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("summary", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("author_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_name"],
            ["author.name"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_article_title"), "article", ["title"], unique=False)
    op.create_table(
        "coauthorarticlelink",
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["article.id"],
        ),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
        ),
        sa.PrimaryKeyConstraint("author_id", "article_id"),
    )
    op.create_table(
        "queryarticlelink",
        sa.Column("query_id", sa.Integer(), nullable=False),
        sa.Column("article_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["article_id"],
            ["article.id"],
        ),
        sa.ForeignKeyConstraint(
            ["query_id"],
            ["query.id"],
        ),
        sa.PrimaryKeyConstraint("query_id", "article_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("queryarticlelink")
    op.drop_table("coauthorarticlelink")
    op.drop_index(op.f("ix_article_title"), table_name="article")
    op.drop_table("article")
    op.drop_table("query")
    op.drop_index(op.f("ix_author_name"), table_name="author")
    op.drop_table("author")
    # ### end Alembic commands ###
