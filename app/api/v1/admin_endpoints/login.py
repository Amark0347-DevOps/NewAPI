from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import admin_login_router
from ....model.admin.login_model import Admin_Login_Model
from ....mongo.mongodb import connect_mongodb
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.admin import AdminService


@admin_login_router.post("/v1/admin/login", description="Admin Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_login(data: Admin_Login_Model):
    admin_service = AdminService()
    return await admin_service.Login_Admin(data)
