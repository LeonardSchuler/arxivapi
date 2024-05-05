import os

import httpx
import pytest
from fastapi import FastAPI, Response
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.pool import StaticPool

from app.db.session import get_session
from app.main import app
from app.remotes.arxiv import ArxivApi, get_arxiv

from .helpers import EMPTY_RESPONSE, QUERY_RESPONSE_MAP


# Prevent environment leaking into tests
os.environ["DB_PASSWORD"] = ""  # nosec
os.environ["DB_USER"] = ""
os.environ["DB_HOST"] = ""
os.environ["ENVIRONMENT"] = "local"


@pytest.fixture
def arxiv_server():
    app = FastAPI()

    @app.get("/api/query")
    async def get_api_call(
        search_query: str,
        skip: int = 0,
        max_results: int = 8,
        sortBy: str = "relevance",
        sortOrder: str = "descending",
    ):
        response_text = QUERY_RESPONSE_MAP.get(search_query, EMPTY_RESPONSE)
        # query = "lmm
        # url = f"https://export.arxiv.org/api/query?search_query={query}&skip=0&max_results=8&sortBy=relevance&sortOrder=descending"
        return Response(content=response_text, media_type="application/xml")

    return app


@pytest.fixture
async def arxiv_client(arxiv_server):
    # TestClient cannot be used, see: https://www.starlette.io/testclient/#asynchronous-tests
    # client = TestClient(arxiv_server, backend="asyncio")
    transport = httpx.ASGITransport(app=arxiv_server)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client


@pytest.fixture
async def arxiv(arxiv_client):
    remote = ArxivApi(arxiv_client)
    return remote


@pytest.fixture(name="session")
async def session_fixture():
    # synchronous case
    # engine = create_engine(
    #    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    # )
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     yield session
    # engine = create_engine("sqlite://")
    async_engine = create_async_engine(
        "sqlite+aiosqlite://",
        echo=False,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    async with AsyncSession(async_engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session, arxiv: ArxivApi):
    def get_session_override():
        return session

    def get_arxiv_override():
        return arxiv

    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[get_arxiv] = get_arxiv_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


# sets up asyncio for pytest
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
