from pydantic import BaseModel, ConfigDict, field_validator, Field, EmailStr
from fastapi import HTTPException, status 
# class Add_Schedule(BaseModel):
#     Selected_Course:str = Field(...)
#     Day:str  = Field(...)
#     Start_Time:str  = Field(...)
#     End_Time:str = Field(...)
#     model_config = ConfigDict(
#         json_schema_extra={
#             "example":{
#                 "Selected_Course":"Python",
#                 "Day":"Monday",
#                 "Start_Time":"12 PM",
#                 "End_Time":"3 PM",
#             }
#         }
#     )


#     # @field_validator("course_name")
#     # def course_validate(cls, course_name):
#     #     if len(course_name) >= 10:
#     #         # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
#     #         raise ValueError("Invalid Course Name")
#     #     else:
#     #         return course_name
        

# class Add_Course_Model(BaseModel):
#     Course:str =Field(...)
#     Duration:str = Field(...)
#     Sdate:str = Field(...)
#     Edate:str = Field(...)
#     Cost:str = Field(...)
#     TrainerName:str = Field(...)
#     Discount:str = Field(...)
#     model_config = ConfigDict(
#          json_schema_extra={
#             "example":{
#                 "Course":"Python",
#                 "Duration":"1 month",
#                 "Sdate":"5 jan",
#                 "Edate":"9 may",
#                 "Cost":"5000",
#                 "TrainerName":"amarjeet",
#                 "Discount":"10"
#             }
#          }
#     )

#     # @field_validator("enter_course")
#     # def enter_course_validate(cls, enter_course):
#     #     if len(enter_course)>=10:
#     #         raise ValueError("crouse value error")
#     #     else:
#     #         return enter_course
        

# class Add_Trainer(BaseModel):
#     Trainer_Name:str = Field(...)
#     Email:str  = Field(...)
#     Phone:str  = Field(...)
#     Experince:str = Field(...)
#     model_config = ConfigDict(
#         json_schema_extra={
#             "example":{
#                 "Trainer_Name":"Amarjeet",
#                 "Email":"amark0347@gmail.com",
#                 "Phone":"9056678462",
#                 "Experince":"3 years"
#             }
#         }
#     )

class User_Login_Response(BaseModel):
    message:str =Field(default="Login Success")
    status:str =Field(default="Success")
    status_code:str =Field(default="200")
    firstName:str = Field(...)
    lastName:str = Field(...)
    phone:str = Field(...)
    email:str = Field(...)
    token:str=Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "message": "Successfully User Register",
                "status": "Success",
                "status_code": "200",
                "firstName":"rahul",
                "lastName":"kumar",
                "phone":"9056678462",
                "email":"rahul@gmail.com",
                "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiZmlyc3ROYW1lIjoiYmFibHUiLCJsYXN0TmFtZSI6IlVtcmlnYXIiLCJlbWFpbCI6ImJmdGRnZ2RAZ21haWwuY29tIiwicGhvbmUiOiIxZGRmZGRkZmY3OTA5NCJ9LCJleHAiOjE3MDg5MzIxNDN9.if5Zvi0Axaiee7UpnitBwOwjIHcGnFEYM0oh0j9b4SE"
            }
        }
    )

class User_SingUp_Response(BaseModel):
    message:str =Field(default="Successfully User Register")
    status:str =Field(default="Success")
    status_code:str =Field(default="200")
    firstName:str = Field(...)
    lastName:str = Field(...)
    phone:str = Field(...)
    email:str = Field(...)
    token:str=Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "message": "Successfully User Register",
                "status": "Success",
                "status_code": "200",
                "firstName":"rahul",
                "lastName":"kumar",
                "phone":"9056678462",
                "email":"rahul@gmail.com",
                "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiZmlyc3ROYW1lIjoiYmFibHUiLCJsYXN0TmFtZSI6IlVtcmlnYXIiLCJlbWFpbCI6ImJmdGRnZ2RAZ21haWwuY29tIiwicGhvbmUiOiIxZGRmZGRkZmY3OTA5NCJ9LCJleHAiOjE3MDg5MzIxNDN9.if5Zvi0Axaiee7UpnitBwOwjIHcGnFEYM0oh0j9b4SE"
            }
        }
    )