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
    aws_access_key:str= "AKIARWGZY7O43BFPMPO2"
    aws_secrect_key:str= "2P8IccNLgV1+5fRIsy8MuLtvI3lljOn76Jh8PtN6"
    aws_region:str = "ap-south-1"
    aws_s3_bucket:str = "safeshooter"
    # aws_access_key:str= getenv("AWS_ACCESS_KEY")
    # aws_secrect_key:str= getenv("AWS_SECRET_KEY")
    # aws_region:str = getenv("AWS_REGION")
    # aws_s3_bucket:str = getenv("AWS_S3_BUCKET")
    UserAdmin:str = getenv("ADMIN")
    UserTrainer:str = getenv("TRAINER")
    UserUser:str = getenv("USER")
settings = Settings()
####################################################################################################################

####################################################################################################################

    