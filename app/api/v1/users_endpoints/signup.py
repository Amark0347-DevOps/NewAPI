from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi_limiter.depends import RateLimiter
from ..routers import user_signup_router
from ....mongo.mongodb import connect_mongodb
from ....model.user.signup_model import User_SingUp_Model
from ....services.user_services.user import UserService

@user_signup_router.post("/v1/users/signup", description="User Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def create_user(data: User_SingUp_Model):
    user_service = UserService()
    return await user_service.Singup_User(data)
