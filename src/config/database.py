from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker


URL="postgresql://tester:testerpass@localhost:5432/carros"
engine = create_engine(URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)
def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
