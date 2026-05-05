from fastapi import APIRouter, Depends, HTTPException

from models.personajes import PersonajeCrear, PersonajeLeer, Personaje
from db.base import get_session
from services.crud import (obtener_todos, 
                           obtener_id,
                           crear_personaje
                          )

router = APIRouter(prefix="/personajes", tags=["personajes"])

@router.post("/", response_model=PersonajeLeer)
def crear_personaje(personaje: PersonajeCrear, session = Depends(get_session)):
    nuevo_personaje = crear_personaje(session, personaje)
    return nuevo_personaje

@router.get("/", response_model=list[PersonajeLeer])
def obtener_personakjes(session = Depends(get_session)):
    personajes = obtener_todos(session, model=Personaje)
    return personajes

@router.get("/{personaje_id}", response_model=PersonajeLeer)
def obtener_personaje(personaje_id: int, session = Depends(get_session)):
    personaje = obtener_id(session, model=Personaje, id=personaje_id)
    if personaje is None:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    return personaje