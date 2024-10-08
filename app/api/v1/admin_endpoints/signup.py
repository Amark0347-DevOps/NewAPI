from fastapi import  Depends
from motor.motor_asyncio import AsyncIOMotorClient
from ..routers import admin_signup_router
from ....model.admin.singup_model import Admin_SingUp_Model
from fastapi_limiter.depends import RateLimiter
from ....services.admin_services.admin import AdminService

@admin_signup_router.post("/v1/admin/signup", description="Admin Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def admin_signup(data: Admin_SingUp_Model):
    admin_service = AdminService()
    return await admin_service.Singup_Admin(data)
