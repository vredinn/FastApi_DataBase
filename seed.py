from sqlalchemy.orm import Session
from database import engine
import models as m

m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    p = m.Book(
        name="Огни Алапаевска", author="Иванов И.И.", year=2023, genre="Фантастика"
    )
    session.add(p)
    p = m.Book(name="Деревянные леса", author="Петров П.П.", year=2022, genre="Драма")
    session.add(p)

    p = m.Product(name="Молоко")
    session.add(p)
    session.commit()
