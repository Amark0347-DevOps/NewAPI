from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv
load_dotenv()
class Settings(BaseSettings):
    jwt_secret_key:str = getenv("SECRECT_KEY")
    jwt_algorithem:str = getenv("ALGORITHEM")
    jwt_expire_time:str = getenv("TOKEN_EXPIRY_TIME_NEW")
    mongo_url:str = getenv("MONGO_URL")
    mongo_database:str = getenv("DATABASE")
    mongo_userCollection:str = getenv("USERCOLLECTION")
    mongo_adminCollection:str = getenv("ADMINCOLLECTION")
    redis_ratelimiting_url:str = getenv("REDIS_URL")
settings = Settings()

    