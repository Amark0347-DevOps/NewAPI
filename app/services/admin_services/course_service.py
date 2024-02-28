from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.adminmodel_response import Add_Course_Response
from fastapi.encoders import jsonable_encoder


class CourseService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("safeshooters")
        self.coursesCollection = self.db.get_collection("Courses")


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
    
###########################################################################################################
    async def update_course(self,item_id: str, data):
        if await self.coursesCollection.find_one({"Course":data.Course}):
            raise HTTPException(detail="Course Already Exist", status_code=status.HTTP_409_CONFLICT)
        else:
            existing_item = await self.coursesCollection.find_one({"Course": item_id})
            if existing_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            else:
                # Update the existing item with the new values
                updated_item = {**existing_item, **data.dict()}
                await self.coursesCollection.replace_one({"Course": item_id}, updated_item)
                return {"message": "Item updated successfully"}
###########################################################################################################
    async def delete_course(self, item_id: str):
        result = await self.coursesCollection.delete_one({"Course": item_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Item deleted successfully"}


