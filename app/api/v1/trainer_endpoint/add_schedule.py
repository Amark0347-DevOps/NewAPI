from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import Trainer_schedule_router
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.trainer_panel_services.create_schedule import TrainerScheduleService
from ....core.security import GetCurrentUser
from ....model.trainer_panel.trainer_schedule import Add_Schedule_Model
from ....core.config import settings
from fastapi import HTTPException, status



################################ Add Schedule in Trainer Panel ##################################################################
@Trainer_schedule_router.post("/v1/trainers/add-schedule", description="Add Schedule Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def trainer_get_courses(data:Add_Schedule_Model, db: AsyncIOMotorClient = Depends(connect_mongodb), Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != "Trainer":
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    course_service = TrainerScheduleService(db)
    # return await course_service.get_all_courses()
    return await course_service.create_course_schedule(data, Token)


################################ Get All Schedule in Teacher Panel ##################################################################
@Trainer_schedule_router.get("/v1/trainers/get-schedules", description="Get All Schedule Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def trainer_get_courses(db: AsyncIOMotorClient = Depends(connect_mongodb), Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != "Trainer":
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    course_service = TrainerScheduleService(db)
    # return await course_service.get_all_courses()
    return await course_service.get_all_created_schedule(Token)


@Trainer_schedule_router.put("/v1/admin/update-schedule/{course_name}", description="Update Trainers Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_get_trainers(course_name:str, data:Add_Schedule_Model,db: AsyncIOMotorClient = Depends(connect_mongodb), Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != "Trainer":
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerScheduleService(db)
    return await trainer_service.update_schedule(course_name, data, Token)


@Trainer_schedule_router.delete("/v1/admin/delete-schedule/{course_name}", description="Delete Trainer Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_delete_course(course_name:str, Token:str = Depends(GetCurrentUser)):
    if Token["UserType"] != "Trainer":
        raise HTTPException(detail=f"This is a {Token["UserType"]} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    trainer_service = TrainerScheduleService()
    return await trainer_service.delete_schedule(course_name,Token)
