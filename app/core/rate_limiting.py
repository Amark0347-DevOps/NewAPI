from fastapi import HTTPException, status
from redis.asyncio import Redis
from redis import RedisError
from fastapi_limiter import FastAPILimiter
from .config import settings
from ..loggers.logger import logger

# class Myredis:
#     def __init__(self) -> None:
#         self.client =  Redis.from_url(f"{redis_url}:{redis_port}")

# redisobj = Myredis()
# async def connect_Redis_ratelimiter():
#     try:
#         await FastAPILimiter.init(redisobj.client)
#         return await redisobj.client
#     except RedisError as error:
#         logger.error(f"Failed to connect to redis: {error}")
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# async def shutdown_redis_ratelimiter():
#     await redisobj.client.close()


class Myredis:
    def __init__(self):
        redis_url = "redis://localhost"
        redis_port = 6379
        self.client =  FastAPILimiter.init(f"{redis_url}:{redis_port}")
        # self.client = FastAPILimiter.redis

    async def connect_Redis_ratelimiter(self):
        try:
            return self.client
        except RedisError as error:
            logger.error(f"Failed to connect to redis: {error}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    async def shutdown_redis_ratelimiter(self):
        self.client.close()

redisobj = Myredis()