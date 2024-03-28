from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import admin_trainer_router
from ....model.admin.trainer_model import Add_Trainer_Model
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.trainer_service import TrainerService
from ....core.security import GetCurrentUser
from ....core.config import settings
from fastapi import HTTPException, status


@admin_trainer_router.post("/v1/admin/add-trainer", description="Add Trainer Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_add_trainer(data: Add_Trainer_Model, Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerService()
    return await trainer_service.add_trainer(data)


@admin_trainer_router.get("/v1/admin/get-trainers", description="Get All Trainers Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_get_trainers(Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerService()
    return await trainer_service.get_all_trainer()

@admin_trainer_router.put("/v1/admin/update-trainer/{trainer_phone}", description="Update Trainers Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_get_trainers(trainer_phone:str, data:Add_Trainer_Model, Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerService()
    return await trainer_service.update_trainer(trainer_phone, data)


@admin_trainer_router.delete("/v1/admin/delete-trainer/{trainer_phone}", description="Delete Trainer Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_delete_course(trainer_phone:str, Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerService()
    return await trainer_service.delete_trainer(trainer_phone)