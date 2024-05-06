from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.arxiv import ArxivDatabase
from app.db.session import get_session
from app.models import QueryWithSearchResult


router = APIRouter()


@router.get("/", response_model=list[QueryWithSearchResult])
async def search(
    session: Annotated[AsyncSession, Depends(get_session)],
    query_timestamp_start: datetime = Query(
        ..., description="Start timestamp (format: yyyy-MM-ddTHH:mm:ss)", format="%Y-%m-%dT%H:%M:%S"
    ),
    query_timestamp_end: datetime = Query(
        None, description="End timestamp (format: yyyy-MM-ddTHH:mm:ss)", format="%Y-%m-%dT%H:%M:%S"
    ),
) -> list[QueryWithSearchResult]:
    queries = await ArxivDatabase(session).get_queries_between(
        query_timestamp_start, query_timestamp_end
    )
    output = [QueryWithSearchResult.model_validate(q) for q in queries]
    return output
