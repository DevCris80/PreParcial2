from sqlmodel import SQLModel, Session, select
from typing import Type

def crear_personaje(session: Session, personaje: SQLModel) -> SQLModel:
    session.add(personaje)
    session.commit()
    session.refresh(personaje)
    return personaje

def crear_fruta(session: Session, fruta: SQLModel) -> SQLModel:
    session.add(fruta)
    session.commit()
    session.refresh(fruta)
    return fruta

def crear_tripulacion(session: Session, tripulacion: SQLModel) -> SQLModel:
    session.add(tripulacion)
    session.commit()
    session.refresh(tripulacion)
    return tripulacion

def obtener_todos(session: Session, modelo: Type[SQLModel]) -> list[SQLModel]:
    consulta = select(modelo)
    resultado = session.exec(consulta).all()
    return resultado

def obtener_id(session: Session, modelo: Type[SQLModel], id: int) -> SQLModel | None:
    consulta = select(modelo).where(modelo.id == id)
    resultado = session.exec(consulta).first()
    return resultado
