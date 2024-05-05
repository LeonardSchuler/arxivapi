import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import CURRENT_API_VERSION, routes
from app.core.config import settings


logger = logging.getLogger(__name__)


tags_metadata = [
    {
        "name": "health",
        "description": "Health check for api",
    }
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FastAPI app starting...")
    logger.info("FastAPI app running...")
    yield
    logger.info("FastAPI app stopping...")


app = FastAPI(
    title="arxivapi",
    description="base project for fastapi backend",
    version=CURRENT_API_VERSION,
    openapi_url=f"/{CURRENT_API_VERSION}/openapi.json",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(routes.api_router)
