from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.models import db_helper, Article
from . import crud


async def article_by_id(
    article_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Article:
    article = await crud.get_article(session=session, article_id=article_id)
    if article:
        return article
    else: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article {article_id} not found!",
        )
