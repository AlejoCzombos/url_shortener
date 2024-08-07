from fastapi import FastAPI
from src.routers import url

app = FastAPI()

app.include_router(url.router)

@app.get("/", tags=["root"])
async def read_root():
    return {"Server is running."}