import requests
from fastapi import APIRouter, HTTPException, status, Header

from app.utils.generate_token import generate_token_api
from app.request.token import TokenRequest

router = APIRouter(
    prefix="/api/token",
    tags=["token"],
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    status_code=status.HTTP_200_OK
)
async def generate_token(request : TokenRequest):
    
    if request.issuer == "" or not request.issuer:
        raise HTTPException(status_code=400, detail="issuer es requerido")
    if request.secret == "" or not request.secret:
        raise HTTPException(status_code=400, detail="secret es requerido")
    
    data = request.model_dump()
    
    iss = data["issuer"]
    secret = data["secret"]
    
    try:
        token = generate_token_api(iss, secret)
        return {"token": token}
    except Exception as e:
        print("Error en api token:", e)
        raise HTTPException(status_code=500, detail="Error al generar el token")