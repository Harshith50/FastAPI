from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title : str
    author : str
    genre : str
    published_year : int
    price : float
    in_stock : bool


class BookUpdate(BaseModel):
    title : str
    author : str
    genre : str
    price : float
    in_stock : bool