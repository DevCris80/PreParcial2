from fastapi import APIRouter, Depends, HTTPException

from models.fruta import FrutaCrear, FrutaLeer, Fruta
from db.base import get_session
from services.crud import (obtener_todos, 
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
def obtener_frutaes(session = Depends(get_session)):
    frutaes = obtener_todos(session, model=Fruta)
    return frutaes

@router.get("/{fruta_id}", response_model=FrutaLeer)
def obtener_fruta(fruta_id: int, session = Depends(get_session)):
    fruta = obtener_id(session, model=Fruta, id=fruta_id)
    if fruta is None:
        raise HTTPException(status_code=404, detail="Fruta no encontrada")
    return fruta

@router.delete("/{fruta_id}")
def eliminar_fruta(fruta_id: int, session = Depends(get_session)):
    exito = eliminar(session, fruta_id, Fruta)
    if not exito:
        raise HTTPException(status_code=404, detail="Fruta no encontrada")
    return {"detail": "Fruta eliminada exitosamente"}