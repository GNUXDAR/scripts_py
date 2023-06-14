from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    page: int
    editor: Optional[str]

@app.get('/')
def index():
    return 'Hello world, FastAPI'

@app.get("/1")
def read_root():
    return {"Hello": "World"}

# parametros variables
@app.get('/book/{id}')
def show_book(id: int):
    return {"data": id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post('/book')
def insert_book(book: Book):
    return {"message": f"Book {book.title} inserted"}