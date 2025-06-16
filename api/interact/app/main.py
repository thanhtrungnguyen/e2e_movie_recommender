from fastapi import FastAPI
from app.routers import interact

app = FastAPI()
app.include_router(interact.router)
