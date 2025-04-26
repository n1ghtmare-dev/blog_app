from fastapi import APIRouter, HTTPException, status, Depends
from . import crud
from .schemas import Article, ArticleCreate, ArticleUpdate, ArticleUpdatePartial
from backend.core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import article_by_id


router = APIRouter(tags=["Articles"])


@router.get("/", response_model=list[Article])
async def get_articles(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_articles(session=session)
   

@router.post("/", response_model=Article, status_code=status.HTTP_201_CREATED)
async def create_article(
    article_in: ArticleCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_article(session=session, article_in=article_in)


@router.get("/{article_id}/", response_model=Article)
async def get_article(
    article: Article = Depends(article_by_id),
):
    return article


@router.put("/{article_id}/")
async def update_article(
    article_update: ArticleUpdate,
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_article(
        session=session,
        article=article,
        article_update=article_update,
    )


@router.patch("/{article_id}/")
async def update_article(
    article_update: ArticleUpdatePartial,
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_article(
        session=session,
        article=article,
        article_update=article_update,
        partial=True,
    )

@router.delete("/{article_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article: Article = Depends(article_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_article(article=article, session=session)
