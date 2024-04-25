from fastapi import FastAPI
from config.db import init_db
from routes.user import user
from routes.board import board

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(user)
app.include_router(board)