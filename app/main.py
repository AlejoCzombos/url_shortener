from fastapi import FastAPI, Request, HTTPException
from time import time

from app.router import urgencia, despacho, token

# from slowapi.errors import RateLimitExceeded
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address

# limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(urgencia.router)
app.include_router(despacho.router)
app.include_router(token.router)

@app.get("/")
async def read_root():
    return {"Server is running."}