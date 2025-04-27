from fastapi import Request, FastAPI
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from .api_v1 import router as router_v1
from .core.config import settings
from backend.views.home import router as router_home 
from contextlib import asynccontextmanager
from backend.core.models import Base, db_helper
from backend.utils.templating import templates


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "src/blog_app/frontend/static")),
    name="static"
)

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(router=router_home, prefix=settings.home_prefix)

@app.get("/")
def main_path():
    return RedirectResponse("/home/", status_code=301)

@app.get("/home/")
def get_articles(request: Request):
    articles = [
        {
            'id': 1,
            'title': 'first article',
            'date': 'August 7, 2024'
        },
        {
            'id': 2,
            'title': 'second article',
            'date': 'August 7, 2024'
        },
        {
            'id': 3,
            'title': 'third article',
            'date': 'August 7, 2024'
        },
    ]

    articles = ...
    print(articles)

    return templates.TemplateResponse("index.html", {"request": request, "articles": articles}) 




