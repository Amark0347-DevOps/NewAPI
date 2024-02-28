from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import admin_course_router
from ....model.adminmodel import Add_Course_Model
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.course_service import CourseService
from ....core.security import get_current_user


@admin_course_router.post("/v1/admin/add-course", description="Add Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_add_course(data: Add_Course_Model, db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    course_service = CourseService(db)
    return await course_service.add_course(data)

@admin_course_router.get("/v1/admin/get-courses", description="Get Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_get_courses(db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    course_service = CourseService(db)
    return await course_service.get_all_courses()

@admin_course_router.put("/v1/admin/update-course/{item_id}", description="Update Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_update_course(item_id:str, data:Add_Course_Model, db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    course_service = CourseService(db)
    return await course_service.update_course(item_id, data)

@admin_course_router.delete("/v1/admin/delete-course/{item_id}", description="Update Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_delete_course(item_id:str, db: AsyncIOMotorClient = Depends(connect_mongodb), token:str = Depends(get_current_user)):
    course_service = CourseService(db)
    return await course_service.delete_course(item_id)
