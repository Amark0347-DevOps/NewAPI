from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException, status
from pymongo.errors import ServerSelectionTimeoutError
from ..core.config import settings
from ..loggers.logger import logger


class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.mongo_url, maxPoolSize=10, minPoolSize=5)
        # self.db = self.client.get_database("safeshooters")
        # self.adminCollection = self.db.get_collection("Admin")
        # self.adminCollection.fin
mongodb = MongoDB()

async def connect_mongodb():
    try:
        yield mongodb.client
    except ServerSelectionTimeoutError as error:
        logger.error(f"Failed to connect to MongoDB: {error}")
        raise HTTPException(detail="unable to connect server with database", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
async def shutdown_mongodb():
    return await mongodb.client