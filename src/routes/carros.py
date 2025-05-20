#dependencias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from esquemas.esquemas_objetos import crearcarro, leercarro, crearmarca, leermarca
from modelos.modelos_carros import Marca, Carro
from utils.deps import get_db
#

#api router
router = APIRouter()

#ruta para enviar un carro
@router.post("/carros/")
def crear_carro(carro: crearcarro, db: Session = Depends(get_db)):
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

#ruta para enviar una marca
@router.post("/marcas/")
def crear_marca(marca:crearmarca, db: Session = Depends(get_db)):
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
    marcas = db.query(Marca),all()
    return marcas
