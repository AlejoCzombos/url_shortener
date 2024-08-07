from ..db import urls_collection
from ..models.url import URLInDB, URLIn, URLCollectionDB
from bson import ObjectId

async def create_url_db(url_in: URLIn):
    url = URLIn(**url_in.model_dump())
    
    alias_exists = await urls_collection.find({"alias": url.alias}).to_list(1)
    if alias_exists:
        return None
    
    url_data = url.model_dump(by_alias=True)
    new_url = await urls_collection.insert_one(url_data)
    url_created = await urls_collection.find_one({"_id": new_url.inserted_id})
    
    return URLInDB(**url_created)

async def update_url_db(url_in: URLIn, url_id: str):
    # convert URLIn to URLInDB and remove None values
    url = URLIn(**url_in.model_dump())
    url_data = {attribute: value for attribute, value in url.model_dump(by_alias=True).items() if value is not None}
    
    if url_data.get("alias"):
        alias_exists = await urls_collection.find({"alias": url.alias}).to_list(1)
        if alias_exists:
            return None
    
    exists = await urls_collection.find_one({"_id": ObjectId(url_id)})
    if not exists:
        return None
    
    url_updated = await urls_collection.find_one_and_update({"_id": ObjectId(url_id)}, {"$set": url_data}, return_document=True)
    
    return URLInDB(**url_updated)

async def delete_url_db(url_id: str) -> bool:
    url_deleted = await urls_collection.delete_one({"_id": ObjectId(url_id)})
    
    return url_deleted.deleted_count > 0

async def get_all_urls_db():
    urls_db = await urls_collection.find().to_list(1000)
    
    for url in urls_db:
        if 'description' not in url:
            url['description'] = None
        if 'alias' not in url:
            url['alias'] = None
        if 'expiration' not in url:
            url['expiration'] = None
        if 'password' not in url:
            url['password'] = None
    
    return URLCollectionDB(urls=urls_db)

async def get_url_by_id_or_alias_db(id_or_alias: str):
    alias_is_valid = ObjectId.is_valid(id_or_alias)
    
    if alias_is_valid:
        url_db: URLInDB = await urls_collection.find_one({"_id": ObjectId(id_or_alias)})
        return url_db
    
    url_db: URLInDB = await urls_collection.find_one({"alias": id_or_alias})
    return url_db

async def get_url_by_id_db(url_id: str):
    url_data = await urls_collection.find_one({"_id": ObjectId(url_id)})
    return URLInDB(**url_data) if url_data else None

async def get_url_by_alias_db(alias: str):
    url_data = await urls_collection.find_one({"alias": alias})
    return URLInDB(**url_data) if url_data else None
