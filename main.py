from fastapi import FastAPI

from core.db import db

app = FastAPI(description="url shorter api")
app.state.db = db


@app.on_event("startup")
async def startup():
    database = app.state.db
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    database = app.state.db
    if database.is_connected:
        await database.disconnect()
