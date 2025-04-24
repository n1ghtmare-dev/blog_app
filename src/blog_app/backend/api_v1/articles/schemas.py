from pydantic import BaseModel, ConfigDict


class ArticleBase(BaseModel):
    title: str
    date: str
    description: str

class ArticleCreate(BaseModel):
    pass

class Article(ArticleBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
