from fastapi import APIRouter

from routes.tripulacion_route import router as tripulacion_router
from routes.personajes_route import router as personajes_router
from routes.fruta_route import router as fruta_router

router = APIRouter()

router.include_router(tripulacion_router)
router.include_router(personajes_router)
router.include_router(fruta_router)