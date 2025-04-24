from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.models import Article
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import ArticleCreate


async def get_articles(session: AsyncSession) -> list[Article]:
    stmt = select(Article).order_by(Article.id)
    result: Result = await session.execute(stmt)
    articles = result.scalars().all()
    return list(articles)

async def get_article(session: AsyncSession, article_id: int) -> Article | None:
    return await session.get(Article, article_id)

async def create_article(session: AsyncSession, article_in: ArticleCreate) -> Article:
    article = Article(**article_in.model_dump())
    session.add(article)
    await session.commit()
    # await session.refresh(article)
    return article

