from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum
from enum import StrEnum


class Rol(StrEnum):
    CAPITAN = "Capitan"
    NAVEGANTE = "Navegante"
    COCINERO = "Cocinero"
    DOCTOR = "Doctor"
    CARPINTERO = "Carpintero"
    MUSICO = "Musico"
    RECLUTA = "Recluta"
    ESPADACHIN = "Espadachin"


class PersonajeBase(SQLModel):
    nombre: str
    rol: Rol = Field(sa_type=Enum(Rol))
    recompensa: float
    tripulacion_id: int | None = Field(default=None, foreign_key="tripulacion.id")
    fruta_id: int | None = Field(default=None, foreign_key="fruta.id")


class Personaje(PersonajeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    estado: bool = Field(default=True)

    fruta: "Fruta" = Relationship(back_populates="personajes")
    tripulacion: "Tripulacion" = Relationship(back_populates="personajes")


class PersonajeLeer(PersonajeBase):
    id: int
    estado: bool


class PersonajeCrear(PersonajeBase):
    pass

class PersonajeActualizar(SQLModel):
    nombre: str | None = None
    rol: Rol | None = None
    recompensa: float | None = None
    tripulacion_id: int | None = None
    fruta_id: int | None = None