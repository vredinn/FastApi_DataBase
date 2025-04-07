from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
import pyd

from typing import List

app = FastAPI()


@app.get("/products", response_model=List[pyd.BaseProduct])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(m.Product).all()
    return products


@app.get("/products/{product_id}", response_model=pyd.BaseProduct)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(m.Product).filter(m.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Не найдено")
    return product


@app.post("/products", response_model=pyd.CreateProduct)
def create_product(product: pyd.CreateProduct, db: Session = Depends(get_db)):
    product_db = db.query(m.Product).filter(m.Product.name == product.name).first()
    if product_db:
        raise HTTPException(status_code=400, detail="Продукт уже существует")
    product_db = m.Product(name=product.name)
    db.add(product_db)
    db.commit()
    return product_db


@app.delete("/products/{product_id}", response_model=pyd.BaseProduct)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(m.Product).filter(m.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Не найдено")
    db.delete(product)
    db.commit()
    return product


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


@app.post("/books", response_model=pyd.CreateBook)
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
