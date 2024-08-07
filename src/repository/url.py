from ..db import urls_collection
from ..models.url import URLInDB, URLCreate, URLCollection
from bson import ObjectId

async def create_url(url: URLCreate):
    url_data = url
    url_created = await urls_collection.insert_one(url_data)
    print(url_created)
    return url_created

async def update_url(url_id: str, url: URLCreate):
    url_data = url
    url_updated = await urls_collection.update_one({"_id": ObjectId(url_id)}, {"$set": url_data})
    print(url_updated)
    return url_updated

async def delete_url(url_id: str):
    url_deleted = await urls_collection.delete_one({"_id": ObjectId(url_id)})
    print(url_deleted)
    return url_deleted

async def get_all_urls():
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
    
    return URLCollection(urls=urls_db)

async def get_url_by_id_or_alias(id_or_alias: str):
    url_db: URLInDB = await urls_collection.find_one({
            "$or": [
                {"_id": ObjectId(id_or_alias)},
                {"alias": id_or_alias}
            ]
    })
    return url_db

async def get_url_by_id(url_id: str):
    url_data = await urls_collection.find_one({"_id": ObjectId(url_id)})
    return URLInDB(**url_data) if url_data else None

async def get_url_by_alias(alias: str):
    url_data = await urls_collection.find_one({"alias": alias})
    return URLInDB(**url_data) if url_data else None
