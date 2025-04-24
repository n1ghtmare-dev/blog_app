from fastapi import APIRouter, HTTPException, status, Depends
from . import crud
from .schemas import Article, ArticleCreate
from backend.core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["Articles"])


@router.get("/", response_model=list[Article])
async def get_articles(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_articles(session=session)
   

@router.post("/", response_model=Article)
async def create_article(
    article_in: ArticleCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_article(session=session, article_in=article_in)


@router.get("/{article_id}/", response_model=Article)
async def get_article(
    article_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    article = await crud.get_article(session=session, article_id=article_id)
    if article:
        return article
    else: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article {article_id} not found!",
        )
