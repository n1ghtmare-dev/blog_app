from fastapi import APIRouter
from .articles.views import router as articles_router

router = APIRouter()
router.include_router(router=articles_router, prefix="/articles")
