from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi_limiter.depends import RateLimiter
from ..routers import user_signup_router
from ....mongo.mongodb import connect_mongodb
from ....model.usermodel import User_SingUp
from ....services.user_services.user import UserService

@user_signup_router.post("/v1/users/signup", description="User Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def create_user(data: User_SingUp, db: AsyncIOMotorClient = Depends(connect_mongodb)):
    user_service = UserService(db)
    return await user_service.Singup_User(data)
