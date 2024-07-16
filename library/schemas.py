from typing import List
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    authors: List['Author'] = []

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List['Book'] = []

    class Config:
        orm_mode = True
