from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

# Таблица категорий
class Category(Base):
    __tablename__ = "categories"       
    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, unique=True, nullable=False) 
    books = relationship("Book", back_populates="category") 

# Таблица книг
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        # название книги
    description = Column(String)                  # описание
    price = Column(Float)                         # цена
    url = Column(String, default="")             # ссылка на товар
    category_id = Column(Integer, ForeignKey("categories.id")) # связь с категорией
    category = relationship("Category", back_populates="books")