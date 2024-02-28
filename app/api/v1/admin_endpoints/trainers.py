from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import admin_trainer_router
from ....model.adminmodel import Add_Trainer
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.trainer_service import TrainerService
from ....core.security import get_current_user


@admin_trainer_router.post("/v1/admin/add-trainer", description="Add Trainer Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_add_trainer(data: Add_Trainer, db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    trainer_service = TrainerService(db)
    return await trainer_service.add_trainer(data)

@admin_trainer_router.get("/v1/admin/get-trainers", description="Get All Trainers Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_get_trainers(db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    trainer_service = TrainerService(db)
    return await trainer_service.get_all_trainer()
