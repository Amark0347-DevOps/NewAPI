from pydantic import BaseModel, ConfigDict, field_validator, Field, EmailStr,constr
from fastapi import HTTPException, status 
class Add_Schedule(BaseModel):
    Selected_Course:str = Field(...)
    Day:str  = Field(...)
    Start_Time:str  = Field(...)
    End_Time:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Selected_Course":"Python",
                "Day":"Monday",
                "Start_Time":"12 PM",
                "End_Time":"3 PM",
            }
        }
    )


    # @field_validator("course_name")
    # def course_validate(cls, course_name):
    #     if len(course_name) >= 10:
    #         # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
    #         raise ValueError("Invalid Course Name")
    #     else:
    #         return course_name
        

class Add_Course_Model(BaseModel):
    Course:str =Field(...)
    Duration:str = Field(...)
    Sdate:str = Field(...)
    Edate:str = Field(...)
    Cost:str = Field(...)
    TrainerName:str = Field(...)
    Discount:str = Field(...)
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "Course":"Python",
                "Duration":"1 month",
                "Sdate":"5 jan",
                "Edate":"9 may",
                "Cost":"5000",
                "TrainerName":"amarjeet",
                "Discount":"10"
            }
         }
    )

    # @field_validator("enter_course")
    # def enter_course_validate(cls, enter_course):
    #     if len(enter_course)>=10:
    #         raise ValueError("crouse value error")
    #     else:
    #         return enter_course
        

class Add_Trainer(BaseModel):
    Trainer_Name:str = Field(...)
    Email:str  = Field(...)
    Phone:str  = Field(...)
    Experince:str = Field(...,min_length=1, max_length=2)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Trainer_Name":"Amarjeet",
                "Email":"amark0347@gmail.com",
                "Phone":"9056678462",
                "Experince":"3"
            }
        }
    )

    @field_validator("Email")
    def validate_email(cls, value):
        # Add your custom email validation logic here
        # For example, you might want to check for a specific domain
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value

class Admin_Login(BaseModel):
    email:str = Field(...)
    password:str= Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "email":"amarkila@gmail.com",
                "password":"Amarjeet"
            }
        }
    )
    # @field_validator("phone")
    # def validate_phone(cls, value):
    #     # Add your custom phone number validation logic here
    #     # For example, you might want to check the length or format
    #     if len(value) != 10 or not value.isdigit():
    #         raise ValueError("Invalid phone number format")
    #     return value

    @field_validator("email")
    def validate_email(cls, value):
        # Add your custom email validation logic here
        # For example, you might want to check for a specific domain
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value

class Admin_SingUp(BaseModel):
    firstName:str =Field(...,min_length=1, max_length=20)
    lastName:str =Field(...,min_length=1, max_length=20)
    email:str =Field(...,min_length=1, max_length=50)
    phone:str = Field(...)
    password:str = Field(..., max_length=10)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "firstName": "bablu",
                "lastName": "Umrigar",
                "email": "bablueet@gmail.com",
                "phone": "11167",
                "password":"12345678"
            }
        }
    )
    @field_validator("phone")
    def validate_phone(cls, value):
        # Add your custom phone number validation logic here
        # For example, you might want to check the length or format
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number format")
        return value

    @field_validator("email")
    def validate_email(cls, value):
        # Add your custom email validation logic here
        # For example, you might want to check for a specific domain
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value
    