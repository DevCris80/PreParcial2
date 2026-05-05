from fastapi import FastAPI

from db.iniciar_db import iniciar_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    iniciar_db()

@app.get("/")
async def root():
    return {"message": "Pre Parcial"}   