from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

author_book_connection = Table(
    "author_book",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.id")),
    Column("book_id", Integer, ForeignKey("books.id"))
)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", secondary=author_book_connection, back_populates="authors")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    authors = relationship("Author", secondary=author_book_connection, back_populates="books")
