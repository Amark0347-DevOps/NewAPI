from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import Trainer_course_router
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.trainer_panel_services.get_courses import TrainerCourseService
from ....core.security import GetCurrentUser



@Trainer_course_router.get("/v1/trainers/get-courses", description="Get Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def trainer_get_courses( Token:str = Depends(GetCurrentUser)):
    course_service = TrainerCourseService()
    # return await course_service.get_all_courses()
    return await course_service.get_all_Assigin_courses(Token)
