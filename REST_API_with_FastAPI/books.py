from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)


app = FastAPI()

@app.get("/{id}/{name}")
def read_api(id: int, name: str) -> dict:
    
    return {str(id): name}
    