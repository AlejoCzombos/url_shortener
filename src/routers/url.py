from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from ..db import urls_collection
from bson import ObjectId

from ..repository.url import create_url, update_url, delete_url, get_url_by_id_or_alias, get_all_urls as get_all_urls_db
from ..models.url import URLInDB, URLCreate, URLCollection as URLCollectionDB
from ..schemas.url import URLCreate, URLCollection, URLUpdate, URLDelete, URLResponse, PasswordParam, IdOrAliasParam

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "/", 
    response_model=URLCollection
    )
async def get_all_urls():
    urls_db : URLCollectionDB = await get_all_urls_db()
    #Mapping the URLInDB model to the URLResponse model
    urls = URLCollection(urls=[URLResponse(**url.model_dump()) for url in urls_db.urls])
    return urls

@router.get(
    "/{id_or_alias}",
    name="Redirect URL",
    description="Redirect to the URL",
    )
async def redirect_to_url(id_or_alias: IdOrAliasParam, password: PasswordParam = None):
    url_db: URLInDB = await get_url_by_id_or_alias(id_or_alias)
    
    if url_db == None:
        #Agregar un return con un mensaje de error con codigo de error
        return {"error": "URL not found"}
    
    if url_db["password"] and password != url_db["password"]:
        return {"error": "Invalid password"}
    
    return RedirectResponse(url_db["url"])
    

@router.post("/")
async def create_url():
    return {"url": "https://www.google.com"}

@router.put("/{url_id}")
async def update_url(url_id: int):
    return {"url_id": url_id}

@router.delete("/{url_id}")
async def delete_url(url_id: int):
    return {"url_id": url_id}