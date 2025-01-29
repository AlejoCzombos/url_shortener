from fastapi import APIRouter, HTTPException, status, Header
from datetime import date

from app.api.despacho import authenticate, obtener_consulta_virtual

router = APIRouter(
    prefix="/api/test",
    tags=["despachos"],
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    status_code=status.HTTP_200_OK
)
async def web_hook(data: dict, authorization: str = Header(None)):
    print("Data recibida:", data)
    print("Authorization recibido:", authorization)
    
    token = authenticate()
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se pudo autenticar")
    
    id_consulta = data.get("id_consulta_virtual")
    data = obtener_consulta_virtual(token, id_consulta)
    # print("Data de la consulta virtual:", data)
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se pudo obtener la consulta virtual")

    dni_paciente = data["data"]["info_paciente"]["valor_identificacion"]
    print("DNI del paciente:", dni_paciente)
    
    conducta_terapeutica = data["data"]["conducta_terapeutica"]
    es_urgencia = "SE INDICA CONSULTA PRESENCIAL DE URGENCIA" in conducta_terapeutica
    print("Es urgencia:", es_urgencia)
    
    #Se duplica el despacho y se cambia el tipo de servicio
    
    return {"Es urgencia:", es_urgencia}