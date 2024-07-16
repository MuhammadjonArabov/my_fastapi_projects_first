from sqlalchemy.orm import Session
from . import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_author_list(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(name=book.name)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def add_author_book(db: Session, book: models.Book, author: models.Author):
    book.authors.append(author)
    db.commit()
    db.refresh(book)
    return book
