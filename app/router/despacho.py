import requests
from fastapi import APIRouter, HTTPException, status, Header, Request

from app.config import ENDPOINT_DESPACHO_URL
from app.request.despacho import DespachoRequest
from app.utils.generate_token import generate_token, is_token_valid

router = APIRouter(
    prefix="/api/despachos",
    tags=["despacho"],
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    status_code=status.HTTP_200_OK
)
async def enviar_invitacion(data_request: DespachoRequest, request: Request, authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró el token de autorización")
    
    token = authorization.split(" ")[1]
    
    if not is_token_valid(token):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token inválido")
    
    if data_request.correo == "" or not data_request.correo:
        raise HTTPException(status_code=400, detail="Correo es requerido")
    if data_request.nro_documento == "" or not data_request.nro_documento:
        raise HTTPException(status_code=400, detail="Número de documento es requerido")
    
    data = data_request.model_dump()
    print("Data recibida:", data)
    
    try:
        # Enviar la data a la API de emergencias
        token = generate_token()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        
        response = requests.post(ENDPOINT_DESPACHO_URL, json=data, headers=headers)
        response.raise_for_status()
        return {"message": "Data enviada correctamente"}
    except requests.exceptions.RequestException as e:
        print("Error en api despacho:", e)
        raise HTTPException(status_code=500, detail="Error al enviar la data")