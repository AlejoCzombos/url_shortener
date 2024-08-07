from fastapi import FastAPI
from src.routers import url

app = FastAPI()

app.include_router(url.router)