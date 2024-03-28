from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.user.login_model import login_respose_model, User_Login_Response_Model
from ...model.user.signup_model import User_SingUp_Response_Model, signup_respose_model
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from ...core.config import settings
from fastapi.responses import JSONResponse
from ...mongo.mongodb import mongodb


class UserService:
    def __init__(self):
        self.usersCollection = mongodb.db.get_collection("Users")

###############################################################################################################
    async def Singup_User(self, singup_data) -> User_SingUp_Response_Model:
        if await self.usersCollection.find_one({"Phone":singup_data.Phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.usersCollection.find_one({"Email":singup_data.Email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        else:
            result = await self.usersCollection.insert_one(jsonable_encoder(singup_data))
            re1 = await self.usersCollection.find_one({"_id": result.inserted_id})
            data1 = {"sub":singup_data.Phone,"FirstName": singup_data.FirstName,"LastName": singup_data.LastName,"Email": singup_data.Email, "UserType":singup_data.UserType}
            token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
            re1["Token"] = token
            return JSONResponse(content=jsonable_encoder(User_SingUp_Response_Model(data=signup_respose_model(**re1), status_code=status.HTTP_200_OK)))
        
##################################################################################################################
    async def Login_User(self, login_data) -> User_Login_Response_Model:
        re1 = await self.usersCollection.find_one({"email":login_data.email})
        if re1:
            if re1["password"]==login_data.password:
                data1 = {"sub":re1["phone"],"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"]}
                token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
                re1["token"] = token
                return JSONResponse(content=jsonable_encoder(User_Login_Response_Model(data=login_respose_model(**re1), status_code=status.HTTP_200_OK)))
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Phone Number")
        