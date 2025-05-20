from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


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

