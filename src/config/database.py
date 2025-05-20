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
#clases que vamos a usar en la base de datosc:
Base = declarative_base()

#Marcas 
class Marca(Base):
    __tablename__ = "Marcas"
    nombre = Column(String(20),unique=True,nullable=False)
    id= Column(Integer(),primary_key=True)

#Carros
class Carro(Base):
    __tablename__ = "carros"
    
    id = Column(Integer(), primary_key=True)
    modelo = Column(String(30),nullable= False,unique=True)
    precio = Column(Integer()) 
    kilometraje = Column(Integer()) 
    marca_id =  Column(Integer(), ForeignKey("Marcas.id"), nullable=False) 
    
