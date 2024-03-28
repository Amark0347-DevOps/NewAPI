from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import Trainer_login_router
from ....model.trainer_panel.login_model import Teacher_Login_Model
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.trainer_panel_services.login_service import TrainerService


@Trainer_login_router.post("/v1/trainer/login", description="trainer Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def trainer_panle_login(data: Teacher_Login_Model):
    admin_service = TrainerService()
    return await admin_service.Trainer_Login_Function(data)
