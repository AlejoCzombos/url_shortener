import requests
from fastapi import APIRouter, HTTPException, status, Header, Request

from app.config import ENDPOINT_EMERGENCIA_URL
from app.utils.generate_token import generate_token

router = APIRouter(
    prefix="/api/urgencias",
    tags=["emergencia"],
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    status_code=status.HTTP_200_OK
)
async def web_hook(data: dict, request: Request, authorization: str = Header(None)):
    print("Data recibida:", data)
    
    try:
        # Enviar la data a la API de despachos
        token = generate_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        
        response = requests.post(ENDPOINT_EMERGENCIA_URL, json=data, headers=headers)
        response.raise_for_status()
        return {"message": "Data enviada correctamente"}
    except requests.exceptions.RequestException as e:
        print("Error en api despacho:", e)
        raise HTTPException(status_code=500, detail="Error al enviar la data a la api de despachos")