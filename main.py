from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from app.mongo.mongodb import connect_mongodb, shutdown_mongodb
from app.core.rate_limiting import connect_Redis_ratelimiter, shutdown_redis_ratelimiter
from app.core.rate_limiting import redisobj
from app.api.v1.admin_endpoints.signup import admin_signup_router
from app.api.v1.admin_endpoints.login import admin_login_router
from app.api.v1.admin_endpoints.trainers import admin_trainer_router
from app.api.v1.admin_endpoints.courses import adminCourseRouter
from app.api.v1.users_endpoints.signup import user_signup_router
from app.api.v1.users_endpoints.login import user_login_router
from app.api.v1.trainer_endpoint.login import Trainer_login_router
from app.api.v1.trainer_endpoint.courses import Trainer_course_router
from app.api.v1.trainer_endpoint.add_schedule import Trainer_schedule_router
from app.services.aws_service.s3_bucket import s3_manager
app = FastAPI()
#################################### Cors Middleware #########################################
origins = [
    "http://localhost",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["GET", "POST", "PUT", "DELETE",],
    allow_methods=["*"],
    allow_headers=["*"],
)
#################################### Event Handlers #########################################
app.add_event_handler("startup", s3_manager.create_bucket)
app.add_event_handler("startup", connect_mongodb)
app.add_event_handler("shutdown", shutdown_mongodb)
app.add_event_handler("startup",  connect_Redis_ratelimiter)
app.add_event_handler("shutdown", shutdown_redis_ratelimiter)
#################################### Admin Routers ################################################
app.include_router(admin_signup_router)
app.include_router(admin_login_router)
app.include_router(admin_trainer_router)
app.include_router(adminCourseRouter)
#################################### User Routers ################################################
app.include_router(user_signup_router)
app.include_router(user_login_router)
#################################### Trainer Panel Routers ################################################
app.include_router(Trainer_login_router)
app.include_router(Trainer_course_router)
app.include_router(Trainer_schedule_router)


if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=4522, reload=True)