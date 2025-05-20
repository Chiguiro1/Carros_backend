from pydantic import BaseModel

#esquemas carros
class crearcarro(BaseModel):
    id:int
    modelo:str
    precio:int
    kilometraje:int
    marca_id:int

class leercarro(BaseModel):
    id:int
    modelo:str
    precio:int
    kilometraje:int
    marca_id:int

    class config:
        orm_mode = True


#esquemas marcas
class crearmarca(BaseModel):
    nombre: str
    id : int

class leermarca(BaseModel):
    nombre: str
    id :int

    class config:
        orm_mode = True
