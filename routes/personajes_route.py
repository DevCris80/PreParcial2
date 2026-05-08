from fastapi import APIRouter, Depends, HTTPException

from models.personajes import PersonajeCrear, PersonajeLeer, PersonajeActualizar, Personaje
from db.base import get_session
from services.crud import (actualizar, obtener_todos, 
                           obtener_id,
                           crear,
                           eliminar
                          )

router = APIRouter(prefix="/personajes", tags=["personajes"])

@router.post("/", response_model=PersonajeLeer)
def crear_personaje(personaje: PersonajeCrear, session = Depends(get_session)):
    nuevo_personaje = Personaje.model_validate(personaje)
    return crear(session, nuevo_personaje)

@router.get("/", response_model=list[PersonajeLeer])
def obtener_personajes(session = Depends(get_session)):
    personajes = obtener_todos(session, modelo=Personaje)
    return personajes

@router.get("/{personaje_id}", response_model=PersonajeLeer)
def obtener_personaje(personaje_id: int, session = Depends(get_session)):
    personaje = obtener_id(session, modelo=Personaje, id=personaje_id)
    if personaje is None:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    return personaje

@router.delete("/{personaje_id}")
def eliminar_personaje(personaje_id: int, session = Depends(get_session)):
    exito = eliminar(session, personaje_id, Personaje)
    if not exito:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    return {"detail": "Personaje eliminado exitosamente"}

@router.patch("/{personaje_id}", response_model=PersonajeLeer)
def actualizar_personaje(personaje_id: int, personaje_data: PersonajeActualizar, session = Depends(get_session)):
    personaje_db = obtener_id(session, Personaje, personaje_id)

    if not personaje_db:
        raise HTTPException(404, "Personaje no encontrado")

    return actualizar(session, personaje_db, personaje_data)