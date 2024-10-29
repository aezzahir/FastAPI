from pydantic import BaseModel, Field
from uuid import UUID


class Book(BaseModel):
    title: str = Field(min_lenght=1)
    author: str = Field(min_lenght=1, max_lenght=100)
    description: str = Field(min_lenght=1, max_lenght=100)
    rating: int = Field(gt=-1, lt=101)