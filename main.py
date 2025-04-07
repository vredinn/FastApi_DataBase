from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
import pyd

from typing import List

app = FastAPI()


@app.get("/books", response_model=List[pyd.BaseBook])
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(m.Book).all()
    return books


@app.get("/books/{book_id}", response_model=pyd.BaseBook)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(m.Book).filter(m.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Не найдено")
    return book


@app.post("/books", response_model=pyd.BaseBook)
def create_book(book: pyd.CreateBook, db: Session = Depends(get_db)):
    book_db = db.query(m.Book).filter(m.Book.name == book.name).first()
    if book_db:
        raise HTTPException(status_code=400, detail="Книга уже существует")
    book_db = m.Book(
        name=book.name, author=book.author, year=book.year, genre=book.genre
    )
    db.add(book_db)
    db.commit()
    return book_db


@app.delete("/books/{book_id}", response_model=pyd.BaseBook)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(m.Book).filter(m.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Не найдено")
    db.delete(book)
    db.commit()
    return book
