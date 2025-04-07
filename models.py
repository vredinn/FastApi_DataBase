from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    author = Column(String(255))
    year = Column(Integer)
    genre = Column(String(255))
