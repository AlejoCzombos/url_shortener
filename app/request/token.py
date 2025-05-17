from pydantic import BaseModel, Field
from fastapi import Query, Path

class TokenRequest(BaseModel):
    issuer : str = Field(..., title="Issuer", description="Issuer del token a generar")
    secret : str = Field(..., title="Secret", description="Secret del token a generar")