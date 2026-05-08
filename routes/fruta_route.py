from fastapi import APIRouter, Depends, HTTPException

from models.fruta import FrutaCrear, FrutaLeer, FrutaActualizar, Fruta
from db.base import get_session
from services.crud import (actualizar, obtener_todos, 
                           obtener_id,
                           crear,
                           eliminar
                          )

router = APIRouter(prefix="/fruta", tags=["fruta"])

@router.post("/", response_model=FrutaLeer)
def crear_fruta(fruta: FrutaCrear, session = Depends(get_session)):
    nueva_fruta = Fruta.model_validate(fruta)
    return crear(session, nueva_fruta)

@router.get("/", response_model=list[FrutaLeer])
def obtener_frutas(session = Depends(get_session)):
    frutas = obtener_todos(session, modelo=Fruta)
    return frutas

@router.get("/{fruta_id}", response_model=FrutaLeer)
def obtener_fruta(fruta_id: int, session = Depends(get_session)):
    fruta = obtener_id(session, modelo=Fruta, id=fruta_id)
    if fruta is None:
        raise HTTPException(status_code=404, detail="Fruta no encontrada")
    return fruta

@router.delete("/{fruta_id}")
def eliminar_fruta(fruta_id: int, session = Depends(get_session)):
    exito = eliminar(session, fruta_id, Fruta)
    if not exito:
        raise HTTPException(status_code=404, detail="Fruta no encontrada")
    return {"detail": "Fruta eliminada exitosamente"}

@router.patch("/{fruta_id}", response_model=FrutaLeer)
def actualizar_fruta(fruta_id: int, fruta_data: FrutaActualizar, session = Depends(get_session)):
    fruta_db = obtener_id(session, Fruta, fruta_id)

    if not fruta_db:
        raise HTTPException(404, "Fruta no encontrada")

    return actualizar(session, fruta_db, fruta_data)