from db.db import SessionLocal, engine, Base
from db import crud, models


Base.metadata.create_all(bind=engine)
db = SessionLocal()

cat1 = crud.create_category(db, title="Фантастика")
cat2 = crud.create_category(db, title="Детектив")

crud.create_book(db, title = 'Гарри Поттер', description='История о мальчике-волшеюбике', price=100, category_id=cat1.id, url='https://example.com/harry-potter')
crud.create_book(db, title = 'Властелин колец', description='Эпическое фэнтези о борьбе добра и зла', price=200, category_id=cat1.id, url='https://example.com/lord-of-the-rings')
crud.create_book(db, title = 'Шерлок Холмс', description='Приключения знаменитого детектива', price=150, category_id=cat2.id, url='https://example.com/sherlock-holmes')
crud.create_book(db, title = 'Агата Кристи', description='Классические детективные истории', price=120, category_id=cat2.id, url='https://example.com/agatha-christie')
