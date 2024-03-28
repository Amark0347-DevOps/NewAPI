from motor.motor_asyncio import AsyncIOMotorClient
from ...model.trainer_panel.trainer_schedule import Add_Schedule_Model_Response, schedule_response_model
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException
from ...mongo.mongodb import mongodb

class TrainerScheduleService:
    def __init__(self):
        ########################################################################################
        self.scheduleCollection = mongodb.db.get_collection("TrainerSchedule")

###########################################################################################################
    async def create_course_schedule(self, data, Token):
        if await self.scheduleCollection.count_documents({"$and":[{"Select_Course": data.Select_Course},{"Phone":Token["sub"]}]}) == 1:
            raise HTTPException(detail="Schedule Alredy Created", status_code=status.HTTP_409_CONFLICT)
        data.Phone = Token["sub"]
        re = await self.scheduleCollection.insert_one(jsonable_encoder(data))
        if re:
            re1 = await self.scheduleCollection.find_one({"_id":re.inserted_id})
            return JSONResponse(content=jsonable_encoder(Add_Schedule_Model_Response(data=schedule_response_model(**re1), status_code=status.HTTP_200_OK)))
        else:
            return HTTPException(detail="Having Some Problem Schedule Not Inserted in DB", status_code=status.HTTP_400_BAD_REQUEST)
###########################################################################################################
    async def get_all_created_schedule(self, Token):
        re = self.scheduleCollection.find({"Phone":Token["sub"]})
        if re:
            result_list = await re.to_list(length=None)
            return result_list
        else:
            return {"Data":"some Error"}
        
###########################################################################################################
    async def update_schedule(self,course_name:str, data, Token):
        # if await self.coursesCollection.find_one({"Course":data.Course}):
        existing_item = await self.scheduleCollection.find_one({"$and":[{"Phone": Token["Phone"]},{"Select_Course": course_name}]})
        if existing_item != None:
            if Token["Phone"] == data.Phone:
                updated_item = {**existing_item, **data.dict()}
                re = await self.scheduleCollection.replace_one({"Phone": data.Phone}, updated_item)
                return {"data": re}
            else:
                raise HTTPException(detail="Phone Number  Con't be Change ", status_code=status.HTTP_409_CONFLICT)

        else:
            raise HTTPException(detail="Trainer Not Exist", status_code=status.HTTP_409_CONFLICT)
        
###########################################################################################################
    async def delete_schedule(self, course_name:str, Token):
        result = await self.scheduleCollection.delete_one({"$and":[{"Select_Course": course_name},{"Phone":Token["Phone"] }]})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Course Not Exist")
        return {"message": "Item deleted successfully"}


