from .config import MONGODB_URL

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.get_database("urlshortener")

urls_collection = database.get_collection("urls")