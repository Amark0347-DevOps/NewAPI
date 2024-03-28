from motor.motor_asyncio import AsyncIOMotorClient
from ...mongo.mongodb import mongodb
class TrainerCourseService:
    def __init__(self):
        ########################################################################################
        self.trainersCollection = mongodb.db.get_collection("Trainers")
        self.coursesCollection = mongodb.db.get_collection("Courses")

###########################################################################################################
    async def get_all_Assigin_courses(self, Token):
        re = await self.trainersCollection.find_one({"Phone":Token["sub"]})
        if re:
            re1 = self.coursesCollection.find({"CourseName": {"$in": re["CoursesList"]}})
            result_list = await re1.to_list(length=None)
            return result_list
        else:
            return {"Data":"some Error"}
###########################################################################################################


