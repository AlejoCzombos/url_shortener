from pydantic import BaseModel, Field
from fastapi import Query, Path
from typing import List, Annotated
from datetime import datetime

class URLBase(BaseModel):
    url: Annotated[
        str, 
        Query(
            description="URL to be shortened", 
            max_length=200, 
            min_length=1)
        ] = Field(..., example="https://www.google.com")
    description: Annotated[
        str | None, 
        Query(
            description="Description of the URL",
            max_length=100, 
            min_length=1
            )
        ] = Field(None, example="Google's homepage")
    alias: Annotated[
        str | None, 
        Query(
            description="Alias to access the URL more easily", 
            max_length=30, 
            min_length=3
            )
        ] = Field(None, example="google")
    expiration: Annotated[
        datetime | None, 
        Query(
            description="Expiration date of the URL",
            example=datetime.now()
            )
        ] = Field(None, example=datetime.now())

class URLCreate(URLBase):
    password: Annotated[
        str | None,
    # 4 characters or more, at least 1 uppercase, 1 lowercase, 1 number, no spaces
        Query(
            description="Password to access the URL",
            #regex="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?!.* ).{4,}$"
            )
        ] = Field(None, example="Hello123")

class URLWithId(URLBase):
    id: Annotated[
        str, 
        Query(
            description="Unique identifier of the URL", 
            max_length=24, 
            min_length=24
            )
        ] = Field(default="None" , example="60f7b3b3d9f3f3b3d9f3f3b3")

class URLUpdate(URLBase):
    url: Annotated[
        str | None, 
        Query(
            description="URL to be shortened", 
            max_length=200, 
            min_length=1)
        ] = Field(None, example="https://www.google.com")
    description: Annotated[
        str | None, 
        Query(
            description="Description of the URL",
            max_length=100, 
            min_length=1
            )
        ] = Field(None, example="Google's homepage")
    alias: Annotated[
        str | None, 
        Query(
            description="Alias to access the URL more easily", 
            max_length=30, 
            min_length=3
            )
        ] = Field(None, example="google")
    expiration: Annotated[
        datetime | None, 
        Query(
            description="Expiration date of the URL"
            )
        ] = Field(None, example=datetime.now())

class URLResponse(URLWithId):
    pass

class URLCollection(BaseModel):
    urls: List[URLWithId]

IdOrAliasParam = Annotated[
    str,
    Path(
        title="URL ID or Alias",
        description="Unique identifier or alias of the URL",
        example="60f7b3b3d9f3f3b3d9f3f3b3 or google"
        )
    ]

PasswordParam = Annotated[
    str,
    Query(
        alias="password",
        title="Password",
        description="Password to access the URL",
        example="Hello123"
        )
    ]