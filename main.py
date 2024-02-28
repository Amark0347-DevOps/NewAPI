from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from app.mongo.mongodb import connect_mongodb, shutdown_mongodb
from app.core.rate_limiting import connect_Redis_ratelimiter, shutdown_redis_ratelimiter
from app.api.v1.admin_endpoints.signup import admin_signup_router
from app.api.v1.admin_endpoints.login import admin_login_router
from app.api.v1.admin_endpoints.trainers import admin_trainer_router
from app.api.v1.admin_endpoints.courses import admin_course_router
from app.api.v1.users_endpoints.signup import user_signup_router
from app.api.v1.users_endpoints.login import user_login_router
app = FastAPI()
#################################### Cors Middleware #########################################
origins = ["http://localhost:5000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#################################### Event Handlers #########################################
app.add_event_handler("startup", connect_mongodb)
app.add_event_handler("startup", connect_Redis_ratelimiter)
app.add_event_handler("shutdown", shutdown_mongodb)
app.add_event_handler("shutdown", shutdown_redis_ratelimiter)
#################################### Admin Routers ################################################
app.include_router(admin_signup_router)
app.include_router(admin_login_router)
app.include_router(admin_trainer_router)
app.include_router(admin_course_router)
#################################### User Routers ################################################
app.include_router(user_signup_router)
app.include_router(user_login_router)


if __name__ == '__main__':
    run("main:app", reload=True, host="0.0.0.0", port=4522)