from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.admin.trainer_model import Add_Trainer_Response_Model, Add_Trainer_Model
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ...mongo.mongodb import mongodb

class TrainerService:
    def __init__(self):
        self.trainersCollection = mongodb.db.get_collection("Trainers")

###########################################################################################################
    async def add_trainer(self, data)-> Add_Trainer_Response_Model:
        if await self.trainersCollection.find_one({"Phone":data.Phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Trainer Already Registered")
        elif await self.trainersCollection.find_one({"Email":data.Email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Trainer Already Registered")
        else:
            re = await self.trainersCollection.insert_one(jsonable_encoder(data))
            if re:
                re1 = await self.trainersCollection.find_one({"_id":re.inserted_id})
                return JSONResponse(content=jsonable_encoder(Add_Trainer_Response_Model(data=Add_Trainer_Model(**re1))), status_code=status.HTTP_200_OK)
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
###########################################################################################################
    async def update_trainer(self,trainer_phone, data):
        # if await self.coursesCollection.find_one({"Course":data.Course}):
        existing_item = await self.trainersCollection.find_one({"$and":[{"Phone": trainer_phone},{"Trainer_Name": data.Trainer_Name}]})
        if existing_item != None:
            if trainer_phone== data.Phone:
                updated_item = {**existing_item, **data.dict()}
                re = await self.trainersCollection.replace_one({"Phone": trainer_phone}, updated_item)
                return {"data": "Trainer Updated SuccessFully"}
            else:
                raise HTTPException(detail="Phone Number  Con't be Change ", status_code=status.HTTP_409_CONFLICT)

        else:
            raise HTTPException(detail="Trainer Not Exist", status_code=status.HTTP_409_CONFLICT)
        
###########################################################################################################
    async def delete_trainer(self, trainer_phone:str):
        result = await self.trainersCollection.delete_one({"Phone": trainer_phone})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Course Not Exist")
        return {"message": "Item deleted successfully"}
