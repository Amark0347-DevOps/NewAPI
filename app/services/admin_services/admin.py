from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.adminmodel_response import Admin_Login_Response, Admin_SingUp_Response, Add_Trainer_Response,Add_Course_Response
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from ...core.config import settings

class AdminService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("safeshooters")
        self.adminCollection = self.db.get_collection("Admin")
        self.trainersCollection = self.db.get_collection("Trainers")
        self.coursesCollection = self.db.get_collection("Courses")
##########################################################################################################
    async def Singup_Admin(self, singup_data) -> Admin_SingUp_Response:
        '''SingUP ShopKeepar Logic'''
        if await self.adminCollection.find_one({"phone":singup_data.phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.adminCollection.find_one({"email":singup_data.email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        else:
            result = await self.adminCollection.insert_one(jsonable_encoder(singup_data))
            re1 = await self.adminCollection.find_one({"_id": result.inserted_id})
            data1 = {"sub":re1["phone"],"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"]}
            token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
            re1["token"] = token
            return Admin_SingUp_Response(**re1)

############################################################################################################################
    async def Login_Admin(self, login_data) -> Admin_Login_Response:
        re1 = await self.adminCollection.find_one({"email":login_data.email})
        if re1:
            if re1["password"]==login_data.password:
                data1 = {"sub":re1["phone"],"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"]}
                token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
                re1["token"] = token
                return Admin_Login_Response(**re1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dont have Permissions")

###########################################################################################################
    async def add_course(self, data)-> Add_Course_Response:
        if await self.coursesCollection.find_one({"Course":data.Course}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Course Already Registered")
        else:
            re = await self.coursesCollection.insert_one(jsonable_encoder(data))
            if re:
                re1 = await self.coursesCollection.find_one({"_id":re.inserted_id})
                return Add_Course_Response(**re1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tariner Not Added Some Issues ")
###########################################################################################################
    async def get_all_courses(self):
        l =[]
        cursor = self.coursesCollection.find()
        async for i in cursor:
            i["_id"]=str(i["_id"])
            l.append(i)
        return l


    # async def add_shop_keepar_details(self, data) -> Shop_Detailes_Model:
    #     ''' Add Shopkeepar Details Logic'''
    #     result = await self.ShopCollection.insert_one(jsonable_encoder(data))
    #     details = await self.ShopCollection.find_one({"_id":result.inserted_id})
    #     return Shop_Detailes_Model(**details)
    
###########################################################################################################
