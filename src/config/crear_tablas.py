from sqlalchemy import create_engine
from config.database import Base,engine,Marca, Carro

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    

