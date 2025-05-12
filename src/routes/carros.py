#dependencias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func   
from esquemas.esquemas_objetos import crearcarro, leercarro, crearmarca, leermarca
from modelos.modelos_carros import Marca, Carro
from utils.deps import get_db
#

#api router
router = APIRouter()

#ruta para enviar un carro
@router.post("/carros/")
def crear_carro(carro: crearcarro, db: Session = Depends(get_db)):
    carro_existente= db.query(Carro).filter(
            (func.lower(Carro.modelo)==carro.modelo.lower()) &
            (Carro.precio==carro.precio) &
            (Carro.kilometraje==carro.kilometraje)
        ).first()
    if carro_existente:
        raise HTTPException(status_code=409, detail="El carro ya esta en la base de datos")

    nuevo_carro = Carro(
        modelo=carro.modelo,
        precio=carro.precio,
        kilometraje=carro.kilometraje,
        marca_id=carro.marca_id
    )
    db.add(nuevo_carro)
    db.commit()
    db.refresh(nuevo_carro)
    return nuevo_carro


# ruta para leer un carro
@router.get("/carros/", response_model=list[leercarro])
def leer_carro(db: Session=Depends(get_db)):
    carros= db.query(Carro).all()
    return carros
    
#ruta para leer un carro por id
@router.get("/carros/{id}",response_model=leercarro)
def obtener_carro(id:int,db: Session=Depends(get_db)):
    carro = db.query(Carro).filter(Carro.id==id).first()
    if carro is None:
        raise HTTPException(status_code=404, detail="El carro no esta en la lista intente otro id ")
    return carro

#ruta para actualizar un carro por id
@router.put("/carros/{id}",response_model=leercarro)
def actualizar(id:int,carro:crearcarro, db:Session=Depends(get_db)):
    carro_existente = db.query(Carro).filter(Carro.id==id).first()
    if carro_existente is None:
        raise HTTPException(status_code=404, detail="El carro no esta en la lista intente otro id")

    carro_existente.modelo = carro.modelo
    carro_existente.precio = carro.precio
    carro_existente.kilometraje = carro.kilometraje
    carro_existente.marca_id = carro.marca_id
    
    db.commit()
    db.refresh(carro_existente)
    return carro_existente



#------------------ BUG AUN NO IMPLEMENTAR -----------------------#
#ruta para leer un carro por nombre
#@router.get("/carros/{modelo}",response_model=leercarro)
#def obtener_carro_n(modelo:str,db: Session=Depends(get_db)):
#    carro = db.query(Carro).get(modelo)
#    if carro is None:
#        raise HTTPException(status_code=404, detail="El carro no esta en la lista intente otro modelo")
#    return carro




#ruta para enviar una marca
@router.post("/marcas/")
def crear_marca(marca:crearmarca, db: Session = Depends(get_db)):
    marca_existente = db.query(Marca).filter(
            (func.lower(Marca.nombre)==marca.nombre.lower())
            ).first()
    if marca_existente:
        raise HTTPException(status_code=409,detail="La marca ya existe")
    nueva_marca= Marca(
            nombre=marca.nombre,
            id=marca.id
            )
    db.add(nueva_marca)
    db.commit()
    db.refresh(nueva_marca)
    return nueva_marca

#ruta para leer una marca
@router.get("/marcas/", response_model=list[leermarca])
def leer_marca(db: Session=Depends(get_db)):
    marcas = db.query(Marca).all()
    return marcas

#ruta para leer una marca por el id
@router.get("/marcas/{id}",response_model=leermarca)
def leer_marca_id(id:int,db: Session=Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id==id).first()
    if marca is None:
        raise HTTPException(status_code=404,detail="La marca no esta en la lista, intente otro id")
    return marca


