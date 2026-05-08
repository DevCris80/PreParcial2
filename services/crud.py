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

def eliminar(session: Session, id: int, modelo: Type[SQLModel]) -> bool:
    objeto = obtener_id(session, modelo=modelo, id=id)
    if not objeto:
        return False
    objeto.estado = False
    session.commit()
    return True