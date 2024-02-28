from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.usermodel_response import User_Login_Response, User_SingUp_Response
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from ...core.config import settings


class UserService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("safeshooters")
        self.usersCollection = self.db.get_collection("users")

###############################################################################################################
    async def Singup_User(self, singup_data) -> User_SingUp_Response:
        if await self.usersCollection.find_one({"phone":singup_data.phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.usersCollection.find_one({"email":singup_data.email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        else:
            result = await self.usersCollection.insert_one(jsonable_encoder(singup_data))
            re1 = await self.usersCollection.find_one({"_id": result.inserted_id})
            data1 = {"sub":re1["phone"],"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"]}
            token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
            data1["token"] = token
            return User_SingUp_Response(**data1)
        
##################################################################################################################
    async def Login_User(self, login_data) -> User_Login_Response:
        re1 = await self.usersCollection.find_one({"email":login_data.email})
        if re1:
            if re1["password"]==login_data.password:
                data1 = {"sub":re1["phone"],"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"]}
                token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
                data1["token"] = token
                return User_Login_Response(**data1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Phone Number")
        
######################################################################################################################

    # async def find_user_by_phone(self, user_data:str) -> User_Singup_Model:
    #     result = await self.UserCollection.find_one({"Phone":user_data})
    #     if result:
    #         return User_Singup_Model(**result)
    #     else:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
######################################################################################################################