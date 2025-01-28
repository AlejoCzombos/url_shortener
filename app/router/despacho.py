from fastapi import APIRouter, HTTPException, status
from datetime import date

router = APIRouter(
    prefix="/api/test",
    tags=["despachos"],
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    status_code=status.HTTP_200_OK
)
async def web_hook(data: dict):
    print("Data recibida:", data)
    return data

@router.put(
    "/",
    status_code=status.HTTP_200_OK
)
async def web_hook(data: dict):
    print("Data recibida:", data)
    print("Token:", head)
    return data