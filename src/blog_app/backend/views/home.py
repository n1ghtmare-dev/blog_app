from fastapi import APIRouter, status, Depends, Request
from sqlalchemy.ext.asyncio.session import AsyncSession
from backend.core.config import settings
from backend.core.models import db_helper
from backend.crud import articles as crud_articles
from backend.utils.templating import templates


router = APIRouter(tags=["Home"])

@router.get("/")
async def home_page(request: Request, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    articles = await crud_articles.get_articles(session=session)
    print(articles)

    return templates.TemplateResponse("index.html", {"request": request, "articles": articles}) 
    


