from fastapi import FastAPI, HTTPException, Depends
from model.books import Book
from model import models
from model.books import Book
from model.database import engine, sessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.post("/")
def read_api(book: Book, db: Session = Depends(get_db)):

    book_model = models.Books()
    book_model.author = book.author
    book_model.title = book.title
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()
    return book