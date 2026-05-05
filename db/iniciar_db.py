from sqlmodel import SQLModel

from db.base import engine
from models.tripulacion import Tripulacion
from models.fruta import Fruta
from models.personajes import Personaje

def iniciar_db():
    SQLModel.metadata.create_all(engine)