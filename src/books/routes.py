from fastapi.exceptions import HTTPException
from fastapi import  status
from typing import List
from .schemes import Book, BookUpdate
from .book_data import books
from fastapi import APIRouter

book_router = APIRouter()

@book_router.get("/", response_model= List[Book])
async def get_all_books():
    return books

@book_router.post('/create_book', status_code= status.HTTP_201_CREATED)
async def create_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book
    


@book_router.get('/{book_id}')
async def get_bookBy_id(book_id: int,) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail="Boook not found"
                        )    


@book_router.patch('/update_book/{book_id}')
async def update_boook(book_id: int, update_book: BookUpdate) -> dict :
    for book in books:
        if book['id'] == book_id:
            book['title'] = update_book.title
            book['author'] =update_book.author
            book['genre'] = update_book.genre
            book['price'] = update_book.price
            book['in_stock'] = update_book.in_stock


            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not")    


@book_router.delete('/delete_book/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

        return {}   

    raise HTTPException(status_code= status.HTTP_204_NO_CONTENT,detail="book not found") 
