from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
import os 
# load_dotenv()
class Settings(BaseSettings):
    jwt_secret_key:str = os.getenv("SECRECT_KEY")
    jwt_algorithem:str = os.getenv("ALGORITHEM")
    jwt_expire_time:str = os.getenv("TOKEN_EXPIRY_TIME_NEW")
    mongo_url:str = os.getenv("MONGO_URL")
    mongo_database:str = os.getenv("DATABASE")
    mongo_userCollection:str = os.getenv("USERCOLLECTION")
    mongo_adminCollection:str = os.getenv("ADMINCOLLECTION")
    # redis_ratelimiting_url:str = os.getenv("REDIS_URL")
    # redis_ratelimiting_url:str = "redis://localhost"
    aws_access_key:str= "AKIARWGZY7O43BFPMPO2"
    aws_secrect_key:str= "2P8IccNLgV1+5fRIsy8MuLtvI3lljOn76Jh8PtN6"
    aws_region:str = "ap-south-1"
    aws_s3_bucket:str = "safeshooter"
    # aws_access_key:str= os.getenv("AWS_ACCESS_KEY")
    # aws_secrect_key:str= os.getenv("AWS_SECRET_KEY")
    # aws_region:str = os.getenv("AWS_REGION")
    # aws_s3_bucket:str = os.getenv("AWS_S3_BUCKET")
    UserAdmin:str = os.getenv("ADMIN")
    UserTrainer:str = os.getenv("TRAINER")
    UserUser:str = os.getenv("USER")
settings = Settings()
# ####################################################################################################################

# ####################################################################################################################

# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     jwt_secret_key: str
#     jwt_algorithm: str
#     jwt_expire_time: str
#     mongo_url: str
#     mongo_database: str
#     mongo_userCollection: str
#     mongo_adminCollection: str
#     redis_url: str
#     aws_access_key: str
#     aws_secret_key: str
#     aws_region: str
#     aws_s3_bucket: str
#     UserAdmin: str
#     UserTrainer: str
#     UserUser: str

#     class Config:
#         env_file_encoding = 'utf-8'
#         case_sensitive = True  # Ensure case sensitivity is handled

# settings = Settings()
