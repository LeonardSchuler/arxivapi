from fastapi import APIRouter

from app.api.v1 import health
from app.api.v1.arxiv import routes as arxiv
from app.api.v1.queries import routes as queries
from app.api.v1.results import routes as results


api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(arxiv.router, prefix="/arxiv")
api_router.include_router(queries.router, prefix="/queries")
api_router.include_router(results.router, prefix="/results")
