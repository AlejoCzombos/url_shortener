from fastapi import APIRouter

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_urls():
    return {"urls": ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]}

@router.get("/{url_id}")
async def get_url_by_id(url_id: int):
    return {"url_id": url_id}

@router.post("/")
async def create_url():
    return {"url": "https://www.google.com"}

@router.put("/{url_id}")
async def update_url(url_id: int):
    return {"url_id": url_id}

@router.delete("/{url_id}")
async def delete_url(url_id: int):
    return {"url_id": url_id}