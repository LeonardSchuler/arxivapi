import http
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.arxiv import ArxivDatabase
from app.db.session import get_session
from app.models import QueryCreate
from app.remotes.arxiv import ArxivApi, get_arxiv


router = APIRouter()


@router.get("/search", response_model=QueryCreate)
async def get_articles_from_arxiv(
    arxiv: Annotated[ArxivApi, Depends(get_arxiv)],
    session: Annotated[AsyncSession, Depends(get_session)],
    author: str = "",
    title: str = "",
    journal: str = "",
    max_query_results: int = 8,
) -> QueryCreate:
    # Handles all empty string case
    if not author and not title and not journal:
        query = QueryCreate(
            query="", num_results=0, status=http.HTTPStatus.BAD_REQUEST.value, articles=[]
        )
        return query
    query = await arxiv.query(author, title, journal, max_query_results)
    # TODO: Backgroundtask
    await ArxivDatabase(session).save(query)
    return query
