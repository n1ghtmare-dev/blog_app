from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    title: str
    date: str
    description: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleCreate):
    pass

class ArticleUpdatePartial(ArticleCreate):
    title: str | None = None
    date: str | None = None
    description: str | None = None

class Article(ArticleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
