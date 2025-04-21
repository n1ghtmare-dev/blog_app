from sqlalchemy.orm import Mapped
from .base import Base


class Article(Base):
    title: Mapped[str]
    date: Mapped[str]
    description: Mapped[str]
