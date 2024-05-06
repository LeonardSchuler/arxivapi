from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.arxiv import ArxivDatabase
from app.db.session import get_session
from app.models import ArticleTitleAuthorJournal


router = APIRouter()


@router.get("/", response_model=list[ArticleTitleAuthorJournal])
async def get_query_articles(
    session: Annotated[AsyncSession, Depends(get_session)],
    query_id: int = Query(..., description="The query id you want to find the articles for."),
    page: int = Query(..., description="Page number"),
    items_per_page: int = Query(
        ..., description="Describes the desired number of articles to get."
    ),
) -> list[ArticleTitleAuthorJournal]:
    articles = await ArxivDatabase(session).get_paginated_articles_of(
        query_id, page, items_per_page
    )
    output = [
        ArticleTitleAuthorJournal(title=a.title, author=a.author_name, journal=a.journal)
        for a in articles
    ]
    return output
