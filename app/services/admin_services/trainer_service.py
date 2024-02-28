from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.adminmodel_response import Admin_Login_Response, Admin_SingUp_Response, Add_Trainer_Response,Add_Course_Response
from ...core.security import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from ...core.config import settings

class TrainerService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("safeshooters")
        self.trainersCollection = self.db.get_collection("Trainers")

###########################################################################################################
    async def add_trainer(self, data)-> Add_Trainer_Response:
        if await self.trainersCollection.find_one({"Phone":data.Phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Trainer Already Registered")
        elif await self.trainersCollection.find_one({"Email":data.Email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Trainer Already Registered")
        else:
            re = await self.trainersCollection.insert_one(jsonable_encoder(data))
            if re:
                re1 = await self.trainersCollection.find_one({"_id":re.inserted_id})
                return Add_Trainer_Response(**re1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tariner Not Added Some Issues ")
###########################################################################################################
    async def get_all_trainer(self):
        l =[]
        cursor = self.trainersCollection.find()
        async for i in cursor:
            i["_id"]=str(i["_id"])
            l.append(i)
        return l
