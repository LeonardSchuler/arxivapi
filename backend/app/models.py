import datetime

from sqlmodel import Column, DateTime, Field, Relationship, SQLModel


class AuthorBase(SQLModel):
    name: str = Field(index=True, unique=True)


class AuthorCreate(AuthorBase):
    pass


class ArticleBase(SQLModel):
    title: str = Field(index=True)
    journal: None | str = None
    summary: str = ""
    author_name: str = Field(foreign_key="author.name")


class ArticleCreate(ArticleBase):
    author: AuthorCreate
    coauthors: list[AuthorCreate]


class QueryBase(SQLModel):
    query: str
    num_results: int
    status: int


class QueryCreate(QueryBase):
    articles: list[ArticleCreate]


class QueryArticleLink(SQLModel, table=True):
    query_id: int | None = Field(default=None, foreign_key="query.id", primary_key=True)
    article_id: int | None = Field(default=None, foreign_key="article.id", primary_key=True)


class CoauthorArticleLink(SQLModel, table=True):
    author_id: int | None = Field(default=None, foreign_key="author.id", primary_key=True)
    article_id: int | None = Field(default=None, foreign_key="article.id", primary_key=True)


class Query(QueryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    timestamp: datetime.datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            default=lambda: datetime.datetime.now(datetime.UTC),
            nullable=False,
        )
    )
    articles: list["Article"] = Relationship(
        back_populates="queries",
        link_model=QueryArticleLink,
        sa_relationship_kwargs={"lazy": "selectin"},  # required for async to work
    )


class Article(ArticleBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: "Author" = Relationship(back_populates="articles")
    coauthors: list["Author"] = Relationship(
        back_populates="coauthor_articles", link_model=CoauthorArticleLink
    )
    queries: list[Query] = Relationship(back_populates="articles", link_model=QueryArticleLink)


class Author(AuthorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    articles: list[Article] = Relationship(back_populates="author")  # type: ignore
    coauthor_articles: list[Article] = Relationship(
        back_populates="coauthors", link_model=CoauthorArticleLink
    )


class QueryWithSearchResultAndTimestamp(QueryBase):
    timestamp: datetime.datetime


class ArticleTitleAuthorJournal(SQLModel):
    title: str
    author: str
    journal: str
