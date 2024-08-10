from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from datetime import datetime
from typing import List, Annotated, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]

class URLBase(BaseModel):
    original_url: str
    short_url: Optional[str]
    description: Optional[str]
    alias: Optional[str]
    expires_at: Optional[datetime]
    created_at: Optional[datetime]
    password: Optional[str]

class URLIn(URLBase):
    pass

class URLInDB(URLBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)

class URLCollectionDB(BaseModel):
    urls: List[URLInDB]
