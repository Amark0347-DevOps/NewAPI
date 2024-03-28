from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi_limiter.depends import RateLimiter
from ..routers import user_login_router
from ....mongo.mongodb import connect_mongodb
from ....model.user.login_model import User_Login_Model
from ....services.user_services.user import UserService

@user_login_router.post("/v1/users/login", description="User Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def create_user(data: User_Login_Model):
    user_service = UserService()
    return await user_service.Login_User(data)
