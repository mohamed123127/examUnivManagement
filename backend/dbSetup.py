from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql+psycopg2://"
    "university_exam_planning_db_user:"
    "5ZCjLE4YRz5eY1MrAZzG7ABFiQ4bus8L@"
    "dpg-d5mdjh6mcj7s73c0uvjg-a.oregon-postgres.render.com:5432/"
    "university_exam_planning_db"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
