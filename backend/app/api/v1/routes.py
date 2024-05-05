from fastapi import APIRouter

from app.api.v1 import health
from app.api.v1.arxiv import routes as arxiv


api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(arxiv.router, prefix="/arxiv")
