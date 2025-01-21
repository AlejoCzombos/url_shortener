from fastapi import FastAPI

from app.router import despacho 

app = FastAPI()

app.include_router(despacho.router)

@app.get("/")
async def read_root():
    return {"Server is running."}