import datetime
import math

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.models import Article, ArticleCreate, Author, AuthorCreate, Query, QueryCreate


class ArxivDatabase:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, query: QueryCreate) -> Query:
        db_articles = []
        for article in query.articles:
            db_articles.append(await self.get_or_create_article(article))

        # query.articles = db_articles
        db_query = Query(
            query=query.query,
            num_results=query.num_results,
            status=query.status,
            articles=db_articles,
        )
        # db_query = Query.model_validate(query)
        self._session.add(db_query)
        await self._session.commit()
        await self._session.refresh(db_query)
        return db_query

    async def get_or_create_article(self, article: ArticleCreate) -> Article:
        db_article = await self.get_article(article.title)
        if db_article:
            return db_article
        db_article = await self.create_article(article)
        return db_article

    async def get_or_create_author(self, author: AuthorCreate) -> Author:
        db_author = await self.get_author(author.name)
        if db_author:
            return db_author
        db_author = await self.create_author(author)
        return db_author

    async def get_article(self, title: str) -> None | Article:
        statement = select(Article).where(Article.title == title)
        results = await self._session.exec(statement)
        article = results.first()
        return article

    async def get_author(self, name: str) -> None | Author:
        statement = select(Author).where(Author.name == name)
        results = await self._session.exec(statement)
        author = results.first()
        return author

    async def create_author(self, author: AuthorCreate) -> Author:
        db_author = Author.model_validate(author)
        self._session.add(db_author)
        return db_author

    async def create_article(self, article: ArticleCreate) -> Article:
        author = AuthorCreate(name=article.author_name)
        db_author = await self.get_or_create_author(author)
        db_coauthors = []
        for coauthor in article.coauthors:
            db_coauthor = await self.get_or_create_author(coauthor)
            db_coauthors.append(db_coauthor)

        # article.author = db_author
        # article.coauthors = db_coauthors
        # db_article = Article.model_validate(article)
        db_article = Article(
            title=article.title,
            journal=article.journal,
            summary=article.summary,
            author_name=article.author_name,
            author=db_author,
            coauthors=db_coauthors,
        )

        self._session.add(db_article)
        return db_article

    async def get_queries_between(
        self, start: datetime.datetime, end: None | datetime.datetime = None
    ) -> list[Query]:
        statement = select(Query).where(Query.timestamp >= start)
        if end:
            statement = statement.where(Query.timestamp <= end)
        results = await self._session.exec(statement)
        queries = results.all()
        return queries

    async def get_paginated_articles_of(
        self, query_id: int, page: int, items_per_page: int
    ) -> list[Article]:
        query_statement = select(Query).where(Query.id == query_id)
        results = await self._session.exec(query_statement)
        query = results.first()
        if query is None:
            return []
        num_pages = math.ceil(query.num_results / items_per_page)
        if page > num_pages:
            return []
        start_index = (page - 1) * items_per_page
        end_index = page * items_per_page
        paginated_articles = query.articles[start_index:end_index]
        # paginated_articles = [await query.articles[0]]
        return paginated_articles
