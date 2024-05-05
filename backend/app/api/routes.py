from fastapi import APIRouter

from app.api.v1 import routes as v1


api_router = APIRouter(prefix="/v1")
api_router.include_router(v1.api_router)
