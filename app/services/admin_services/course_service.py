from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...model.admin.course_model import Add_Course_Model, Add_Course_Response, Update_Course_Model, Update_Course_Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ..aws_service.s3_bucket import s3_manager
from ...mongo.mongodb import mongodb

class CourseService:
    def __init__(self):
        self.coursesCollection = mongodb.db.get_collection("Courses")

###########################################################################################################
    '''This Func is Used to Add The Courses by Admin'''
    async def AddCourseFunc(self, data:Add_Course_Model)-> Add_Course_Response:
        if await self.coursesCollection.count_documents({"CourseName":data.CourseName}) >=1:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Course Already Registered")
        
        checkInsertedUser = await self.coursesCollection.insert_one(jsonable_encoder(data))
        if checkInsertedUser.acknowledged:
            getInsertedDocument = await self.coursesCollection.find_one({"_id":checkInsertedUser.inserted_id})
            return JSONResponse(content=jsonable_encoder(Add_Course_Response(data=Add_Course_Model(**getInsertedDocument))), status_code=status.HTTP_200_OK)

##########################################################################################################
    ''' This Func is Used to Find All Courses by Admin'''
    async def GetAllCoursesFunc(self):

        if await self.coursesCollection.count_documents({}) < 1:
            raise HTTPException(detail="No Courses Exists in DataBase", status_code=status.HTTP_204_NO_CONTENT)
        
        getCoursesIntoDataBase = self.coursesCollection.find({})
        getAllCourses = [course async for course in getCoursesIntoDataBase]
        return getAllCourses
    
###########################################################################################################
    async def get_all_courses_with_teachers(self):
        if await self.coursesCollection.find_one({"TrainerName":"Sahil"}):
            # Aggregation pipeline
            pipeline = [
                {"$match": {"TrainerName": "Sahil"}},
                {
                    "$lookup": {
                        "from": "Trainers",
                        "localField": "TrainerName",
                        "foreignField": "Trainer_Name",
                        "as": "result"
                    }
                },
                {"$unwind": {"path":"$result"}}
            ]

            # Execute aggregation pipeline
            result = self.coursesCollection.aggregate(pipeline)
            result_list = await result.to_list(length=None)
            return result_list
        else:
            return {"data":"Error"}

    
###########################################################################################################
    '''This func Used to Update The Entire Admin Course'''
    async def UpdateCourseFunc(self, courseName: str, data:Update_Course_Model) -> Update_Course_Response: 
        if courseName != data.CourseName:
            raise HTTPException(detail="Course Name Can Not be Same in Body or Url Parameter", status_code=status.HTTP_400_BAD_REQUEST)
        
        updateDocument = await self.coursesCollection.find_one_and_update({"CourseName":courseName}, {"$set":dict(data)})
        return JSONResponse(content=jsonable_encoder(Update_Course_Response(data=Update_Course_Model(**updateDocument))), status_code=status.HTTP_205_RESET_CONTENT)

###########################################################################################################
    ''' This Func is Used to Delete The Courses by Admin'''
    async def DeleteCourseFunc(self, courseName: str):
        if await self.coursesCollection.count_documents({"CourseName":courseName}) < 1:
            raise HTTPException(detail="Course Not Exists", status_code=status.HTTP_204_NO_CONTENT)
        
        courseDeleted = await self.coursesCollection.delete_one({"CourseName":courseName})
        if courseDeleted.acknowledged:
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Course Deleted Successfully")

 
###########################################################################################################
    async def UploadCourseImage(self,file, fileName):
        fileContent = await file.read()
        re = await s3_manager.upload_to_s3(fileContent, fileName)
        if re:
            return {"data":"Image is Uploaded"}
        else:
            raise HTTPException(status_code=404, detail="Image is Not Uploadd in s3 bucket")


