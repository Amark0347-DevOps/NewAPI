from fastapi import FastAPI
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from uvicorn import run

app = FastAPI()

# MongoDB connection
try:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.get_database("safeshooters")
    teachers_collection = db.get_collection("Teachers")
    courses_collection = db.get_collection("Courses")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise

@app.get("/all")
async def get_all_courses_with_teacher_details():
    # MongoDB aggregation pipeline to join Courses and Teachers collections
    pipeline = [
        {
            "$lookup": {
                "from": "Teachers",
                "localField": "TrainerName",
                "foreignField": "Trainer_Name",
                "as": "teacher_details"
            }
        },
        {
            "$unwind": "$teacher_details"
        },
        {
            "$project": {
                "_id": 0,
                "Course": 1,
                "Duration": 1,
                "Sdate": 1,
                "Edate": 1,
                "Cost": 1,
                "Discount": 1,
                "TrainerName": "$teacher_details.Trainer_Name",
                "TrainerEmail": "$teacher_details.Email",
                "TrainerPhone": "$teacher_details.Phone",
                "TrainerExperience": "$teacher_details.Experince"
            }
        }
    ]

    # Execute the aggregation pipeline
    try:
        result = await courses_collection.aggregate(pipeline).to_list(length=None)
    except Exception as e:
        print(f"Error during MongoDB aggregation: {e}")
        raise

    # Return the result as JSON response
    return JSONResponse(content=result)

if __name__ == "__main__":
    run("main:app", port=4522, reload=True, host="0.0.0.0")
