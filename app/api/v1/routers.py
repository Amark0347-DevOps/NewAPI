from fastapi import APIRouter
############################ Admin Routers ##############################################
admin_signup_router = APIRouter()
admin_login_router = APIRouter()
admin_trainer_router = APIRouter()
adminCourseRouter = APIRouter()
############################ Users Routers ##############################################
user_signup_router = APIRouter()
user_login_router = APIRouter()
############################ Trainer Panle Routers ##############################################
Trainer_login_router = APIRouter()
Trainer_course_router = APIRouter()
Trainer_schedule_router = APIRouter()