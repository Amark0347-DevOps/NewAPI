from fastapi import  Depends, UploadFile, File
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import adminCourseRouter
from ....model.admin.course_model import Add_Course_Model, Update_Course_Model
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.course_service import CourseService
from ....core.security import GetCurrentUser
from ....core.config import settings
from fastapi import HTTPException, status



@adminCourseRouter.post("/v1/admin/add-course", description="Add Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def AdminAddCourse(courseModel:Add_Course_Model, Token:str = Depends(GetCurrentUser)):
    if Token.UserType != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token.UserType} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    courseService = CourseService()
    return await courseService.AddCourseFunc(courseModel)

@adminCourseRouter.get("/v1/admin/get-courses", description="Get Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def AdminFindAllCourses( Token:str = Depends(GetCurrentUser)):
    if Token.UserType != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token.UserType} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    courseService = CourseService()
    return await courseService.GetAllCoursesFunc()

@adminCourseRouter.put("/v1/admin/update-course/{courseName}", description="Update Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def AdminUpdateCourse(courseName:str, data:Update_Course_Model, Token:str = Depends(GetCurrentUser)):
    if Token.UserType != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token.UserType} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    courseService = CourseService()
    return await courseService.UpdateCourseFunc(courseName, data)

@adminCourseRouter.delete("/v1/admin/delete-course/{course_name}", description="Update Courses Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def AdminDeleteCourse(courseName:str, Token:str = Depends(GetCurrentUser)):
    if Token.UserType != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token.UserType} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    courseService = CourseService()
    return await courseService.DeleteCourseFunc(courseName)

@adminCourseRouter.post("/v1/admin/upload-course-image/", description="upload course image Endpoint",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def AdminUploadCourseImage(courseName:str, file:UploadFile = File(...), Token:str = Depends(GetCurrentUser)):
    if Token.UserType != settings.UserAdmin:
        raise HTTPException(detail=f"This is a {Token.UserType} Endpoint Token You Need To Enter Admin Endpoint Token ", status_code=status.HTTP_401_UNAUTHORIZED)
    courseService = CourseService()
    return await courseService.UploadCourseImage(file, courseName)
