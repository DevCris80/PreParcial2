from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum
from enum import StrEnum


class TipoFruta(StrEnum):
    PARAMECIA = "Paramecia"
    ZOAN = "Zoan"
    LOGIA = "Logia"


class FrutaBase(SQLModel):
    nombre: str
    tipo: TipoFruta = Field(sa_type=Enum(TipoFruta))
    descripcion: str


class Fruta(FrutaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    estado: bool = Field(default=True)

    personajes: list["Personaje"] = Relationship(back_populates="fruta")


class FrutaLeer(FrutaBase):
    id: int
    estado: bool


class FrutaCrear(FrutaBase):
    pass

class FrutaActualizar(SQLModel):
    nombre: str | None = None
    tipo: TipoFruta | None = None
    descripcion: str | None = None