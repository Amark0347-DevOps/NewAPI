from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.admin.login_model import login_response_model, Admin_Login_Response, Admin_Login_Model
from ...model.admin.singup_model import Admin_SingUp_Response,signup_response_model, Admin_SingUp_Model
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from ...core.config import settings
from fastapi.responses import JSONResponse
from ...mongo.mongodb import mongodb
class AdminService:
    def __init__(self):
        self.adminCollection = mongodb.db.get_collection("Admin")
##########################################################################################################
    async def Singup_Admin(self, singup_data:Admin_SingUp_Model) -> Admin_SingUp_Response:
        '''SingUP ShopKeepar Logic'''
        # if await self.adminCollection.find_one({"Phone":singup_data.Phone}):
        if await self.adminCollection.count_documents({"Phone":singup_data.Phone}) == 1:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.adminCollection.count_documents({"Email":singup_data.Email}) == 1:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        result = await self.adminCollection.insert_one(dict(singup_data))
        re1 = await self.adminCollection.find_one({"_id": result.inserted_id})
        # data1 = {"sub":re1["Phone"],"FirstName": re1["FirstName"],"LastName": re1["LastName"],"Email": re1["Email"]}
        data1 = {"sub":singup_data.Phone,"FirstName": singup_data.FirstName,"LastName": singup_data.LastName,"Email": singup_data.Email}
        token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
        re1["Token"] = token
        return JSONResponse(content=jsonable_encoder(Admin_SingUp_Response(data=signup_response_model(**re1))), status_code=status.HTTP_200_OK)

############################################################################################################################
    async def Login_Admin(self, login_data) -> Admin_Login_Response:
        re1 = await self.adminCollection.find_one({"Email":login_data.Email})
        if re1:
            if re1["Password"]==login_data.Password:
                data1 = {"sub":re1["Phone"],"UserType":re1["UserType"], "FirstName": re1["FirstName"],"LastName": re1["LastName"],"Email": re1["Email"]}
                # data1 = {"sub":login_data.Phone,"FirstName": login_data.FirstName,"LastName": login_data.LastName,"Email": login_data.Email}
                token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
                re1["Token"] = token
                return JSONResponse(content=jsonable_encoder(Admin_Login_Response(data=login_response_model(**re1))))
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Not Exist")

###########################################################################################################