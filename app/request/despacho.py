from pydantic import BaseModel, Field
from fastapi import Query, Path

class DespachoRequest(BaseModel):
    nro_documento: str = Field(..., title="Número de documento", description="Número de documento de la persona que solicita el despacho")
    correo: str = Field(..., title="Correo", description="Correo de la persona que solicita el despacho")