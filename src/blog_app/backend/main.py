from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from backend.core.models import Base, db_helper
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

BaseDir = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BaseDir / "frontend/templates"))
app.mount(
    "/static",
    StaticFiles(directory=str(BaseDir / "frontend/static")),
    name="static"
)


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
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles}) 




