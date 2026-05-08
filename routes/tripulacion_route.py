from fastapi import APIRouter, Depends, HTTPException

from models.tripulacion import TripulacionCrear, TripulacionLeer, Tripulacion
from db.base import get_session
from services.crud import (actualizar, obtener_todos, 
                           obtener_id,
                           crear,
                           eliminar
                          )

router = APIRouter(prefix="/tripulacion", tags=["tripulacion"])

@router.post("/", response_model=TripulacionLeer)
def crear_tripulacion(tripulacion: TripulacionCrear, session = Depends(get_session)):
    nueva_tripulacion = Tripulacion.model_validate(tripulacion)
    return crear(session, nueva_tripulacion)

@router.get("/", response_model=list[TripulacionLeer])
def obtener_tripulaciones(session = Depends(get_session)):
    tripulaciones = obtener_todos(session, model=Tripulacion)
    return tripulaciones

@router.get("/{tripulacion_id}", response_model=TripulacionLeer)
def obtener_tripulacion(tripulacion_id: int, session = Depends(get_session)):
    tripulacion = obtener_id(session, model=Tripulacion, id=tripulacion_id)
    if tripulacion is None:
        raise HTTPException(status_code=404, detail="Tripulación no encontrada")
    return tripulacion

@router.delete("/{tripulacion_id}")
def eliminar_tripulacion(tripulacion_id: int, session = Depends(get_session)):
    exito = eliminar(session, tripulacion_id, Tripulacion)
    if not exito:
        raise HTTPException(status_code=404, detail="Tripulación no encontrada")
    return {"detail": "Tripulación eliminada exitosamente"}

@router.patch("/{tripulacion_id}", response_model=TripulacionLeer)
def actualizar_tripulacion(tripulacion_id: int, tripulacion_data: TripulacionActualizar, session: Session = Depends(get_session)):
    tripulacion_db = obtener_id(session, Tripulacion, tripulacion_id)

    if not tripulacion_db:
        raise HTTPException(404, "Tripulación no encontrada")

    return actualizar(session, tripulacion_db, tripulacion_data)