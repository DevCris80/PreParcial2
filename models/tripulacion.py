from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum
from enum import StrEnum


class Origen(StrEnum):
    EAST_BLUE = "East Blue"
    WEST_BLUE = "West Blue"
    NORTH_BLUE = "North Blue"
    SOUTH_BLUE = "South Blue"
    GRAND_LINE = "Grand Line"
    NEW_WORLD = "New World"


class TripulacionBase(SQLModel):
    nombre: str
    capitan: str
    origen: Origen = Field(sa_type=Enum(Origen))


class Tripulacion(TripulacionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    estado: bool = Field(default=True)

    personajes: list["Personaje"] = Relationship(back_populates="tripulacion")


class TripulacionLeer(TripulacionBase):
    id: int
    estado: bool


class TripulacionCrear(TripulacionBase):
    pass