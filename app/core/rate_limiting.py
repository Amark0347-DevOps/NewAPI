from fastapi import HTTPException, status
from redis.asyncio import Redis
from redis import RedisError
from fastapi_limiter import FastAPILimiter
from .config import settings
from ..loggers.logger import logger

class Myredis:
    def __init__(self) -> None:
        self.client =  Redis.from_url(settings.redis_ratelimiting_url, port=6379)

redisobj = Myredis()
async def connect_Redis_ratelimiter():
    try:
        await FastAPILimiter.init(redisobj.client)
        return await redisobj.client
    except RedisError as error:
        logger.error(f"Failed to connect to redis: {error}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def shutdown_redis_ratelimiter():
    await redisobj.client.close()