from ..models.url import URLInDB, URLCollectionDB
from ..schemas.url import URLResponse, URLCollection

def url_in_db_to_url_response(url_in_db: URLInDB) -> URLResponse:
    return URLResponse(
        id=url_in_db.id,
        url=url_in_db.url,
        description=url_in_db.description,
        alias=url_in_db.alias,
        expiration=url_in_db.expiration,
        has_password=bool(url_in_db.password),
    )

def url_collection_in_db_to_url_response(url_collection_in_db: URLCollectionDB) -> URLCollection:
    return URLCollection(
        urls=[url_in_db_to_url_response(url) for url in url_collection_in_db.urls]
    )