from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, database, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(database.get_db)):
    return crud.create_author(db=db, author=author)


@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    authors = crud.get_author_list(db=db, skip=skip, limit=limit)
    return authors


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    books = crud.get_book_list(db=db, skip=skip, limit=limit)
    return books


@app.post("/books/{book_id}/authors/{author_id}/", response_model=schemas.Book)
def add_author_book(book_id: int, author_id: int, db: Session = Depends(database.get_db)):
    book = crud.get_book(db=db, book_id=book_id)
    author = crud.get_author(db=db, author_id=author_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return crud.add_author_book(db=db, book=book, author=author)
