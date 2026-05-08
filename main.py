from fastapi import FastAPI

from db.iniciar_db import iniciar_db
from routes.route import router

app = FastAPI()

app.include_router(router=router) 

@app.on_event("startup")
def on_startup():
    iniciar_db()

@app.get("/")
async def root():
    return {"message": "Pre Parcial"}   