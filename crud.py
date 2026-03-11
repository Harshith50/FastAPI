from fastapi import FastAPI;
from pydantic import BaseModel;


books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books


class Book(BaseModel):
    id : int
    title : str
    author : str
    publised_date : str


@app.post("/add-book")
def add_book(book:Book):
    new_book = book.model_dump()
    books.append(new_book)    










