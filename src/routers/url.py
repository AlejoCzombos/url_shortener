from fastapi import APIRouter, status, HTTPException, Request
from fastapi.responses import RedirectResponse
from datetime import datetime

from ..repository.url import create_url_db, update_url_db, delete_url_db, get_url_by_id_or_alias_db, get_all_urls_db
from ..models.url import URLInDB, URLCollectionDB
from ..schemas.url import URLCreate, URLCollection, URLUpdate, URLResponse, PasswordParam, IdOrAliasParam

from ..mappers.url import url_collection_in_db_to_url_response, url_in_db_to_url_response

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/", 
    name="Get all URLs",
    response_description="List of all URLs",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
    response_model=URLCollection
    )
async def get_all_urls():
    urls_db : URLCollectionDB = await get_all_urls_db()
    
    #Mapping the URLInDB model to the URLResponse model
    urls : URLCollection = url_collection_in_db_to_url_response(urls_db)
    return urls

@router.get(
    "/get/{id_or_alias}",
    name="Get URL by ID or Alias",
    response_description="URL retrieved successfully",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
    response_model=URLResponse,
)
async def get_url_by_id_or_alias(id_or_alias: IdOrAliasParam):
    url_db: URLInDB = await get_url_by_id_or_alias_db(id_or_alias)
    
    if url_db == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    url_response = url_in_db_to_url_response(url_db)
    
    return url_response


@router.get(
    "/{id_or_alias}",
    name="Redirect URL",
    response_description="Redirect to the URL",
    status_code=status.HTTP_302_FOUND,
    response_model_by_alias=False,
    )
async def redirect_to_url(id_or_alias: IdOrAliasParam, password: PasswordParam = None):
    url_db: URLInDB = await get_url_by_id_or_alias_db(id_or_alias)
    
    if url_db == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    if url_db["expiration"] and url_db["expiration"] < datetime.now():
        await delete_url_db(url_db["_id"])
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL expired")
        
    if url_db["password"] and password != url_db["password"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    return RedirectResponse(url_db["url"])
    

@router.post(
    "/",
    name="Create URL",
    response_description="URL created successfully",
    status_code=status.HTTP_201_CREATED,
    response_model=URLResponse,
    response_model_by_alias=False,
    )
async def create_url(url: URLCreate, request: Request):
    url_created : URLInDB = await create_url_db(url)
    
    if url_created is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Alias already exists")
    
    url_response = url_in_db_to_url_response(url_created)
    
    return url_response

@router.put(
    "/{url_id}",
    name="Update URL",
    response_description="URL updated successfully",
    status_code=status.HTTP_200_OK,
    response_model=URLResponse,
    response_model_by_alias=False,
    )
async def update_url(url_id: IdOrAliasParam, url: URLUpdate):
    url_updated : URLInDB = await update_url_db(url, url_id)
    
    if url_updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    url_response = url_in_db_to_url_response(url_updated)
    
    return url_response

@router.delete(
    "/{url_id}",
    name="Delete URL",
    response_description="URL deleted successfully",
    status_code=status.HTTP_200_OK,
    response_model=None,
    response_model_by_alias=False,
    )
async def delete_url(url_id: IdOrAliasParam):
    url_deleted = await delete_url_db(url_id)
    
    if not url_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    return {"message": "URL deleted successfully"}