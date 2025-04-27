from pathlib import Path
from pydantic_settings import BaseSettings
from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.core.models import Base, db_helper
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent

class Settings(BaseSettings):
    home_prefix: str = "/home"
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"

settings = Settings()
