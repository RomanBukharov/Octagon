from db.db import engine, Base, SessionLocal
from db import crud, models

db = SessionLocal()

print("Категории:")
categories = db.query(models.Category).all()
for cat in categories:
    print(f'{cat.id}: {cat.title}')
    for book in cat.books:
        print(f'Книга - {book.title}, описание - {book.description}, цена - {book.price}')

db.close()
