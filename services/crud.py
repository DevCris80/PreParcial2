from sqlmodel import SQLModel, Session, select
from typing import Type

from models.personajes import Personaje

def crear(session: Session, objeto: SQLModel) -> SQLModel:
    session.add(objeto)
    session.commit()
    session.refresh(objeto)
    return objeto

def obtener_todos(session: Session, modelo: Type[SQLModel]) -> list[SQLModel]:
    consulta = select(modelo)
    resultado = session.exec(consulta).all()
    return resultado

def obtener_id(session: Session, modelo: Type[SQLModel], id: int) -> SQLModel | None:
    consulta = select(modelo).where(modelo.id == id)
    resultado = session.exec(consulta).first()
    return resultado

def eliminar_personaje(session: Session, personaje_id: int) -> bool:
    personaje = obtener_id(session, modelo=Personaje, id=personaje_id)
    if not personaje:
        return False
    personaje.estado = False
    session.commit()
    return True