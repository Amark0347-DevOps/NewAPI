from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.trainer_panel.login_model import teacher_login_respose_model, Teacher_Login_Response_Model
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import timedelta
from ...core.config import settings
from fastapi.responses import JSONResponse
from ...mongo.mongodb import mongodb

class TrainerService:
    def __init__(self):
        self.teacherCollection = mongodb.db.get_collection("Trainers")

        
##################################################################################################################
    async def Trainer_Login_Function(self, login_data) -> Teacher_Login_Response_Model:
        re1 = await self.teacherCollection.find_one({"Email":login_data.Email})
        if re1:
            if re1["Password"]==login_data.Password:
                data1 = {"sub":re1["Phone"],"UserType":re1["UserType"], "Trainer_Name": re1["Trainer_Name"],"Email": re1["Email"], "Experince":re1["Experince"]}
                token = await create_access_token(data1,expires_delta=timedelta(minutes=int(settings.jwt_expire_time)))
                re1["Token"] = token
                return JSONResponse(content=jsonable_encoder(Teacher_Login_Response_Model(data=teacher_login_respose_model(**re1), status_code=status.HTTP_200_OK)))
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid User not Exist")
        