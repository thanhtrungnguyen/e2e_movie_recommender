from fastapi import FastAPI
from app.routers import recommend

app = FastAPI()
app.include_router(recommend.router)
