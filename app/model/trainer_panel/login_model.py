from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, List, Optional
import uuid
PyObjectId = Annotated[str, BeforeValidator(str)]

###################################### Teacher Login  Model ###############################################################
class Teacher_Login_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    Email:str = Field(...)
    Password:str= Field(...)
    class Config:
        alias_generator = lambda x: x
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "Email": "amarkila@gmail.com",
                "Password": "Amarjeet"
            }
        }
    # class Config:
    #     # Set alias_generator to convert camelCase to snake_case
    #     alias_generator = lambda x: x
    #     allow_population_by_field_name = True
    # model_config = ConfigDict(
    #     json_schema_extra={
    #         "example":{
    #             "email":"amarkila@gmail.com",
    #             "password":"Amarjeet"
    #         }
    #     }
    # )

    @field_validator("Email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value
    
###################################### Response  Model ###############################################################
class teacher_login_respose_model(BaseModel):
    Email:str  = Field(...)
    Phone:str  = Field(...)
    Password:str = Field(...)
    Experince:str = Field(...,min_length=1, max_length=2)
    UserType:str = Field(...)
    Token:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Trainer_Name":"Amarjeet",
                "Email":"amark0347@gmail.com",
                "Phone":"9056678462",
                "Password":"1234567",
                "Experince":"3",
                "UserType":"Trainer",
                "Token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiZmlyc3ROYW1lIjoiYmFibHUiLCJsYXN0TmFtZSI6IlVtcmlnYXIiLCJlbWFpbCI6ImJmdGRnZ2RAZ21haWwuY29tIiwicGhvbmUiOiIxZGRmZGRkZmY3OTA5NCJ9LCJleHAiOjE3MDg5MzIxNDN9.if5Zvi0Axaiee7UpnitBwOwjIHcGnFEYM0oh0j9b4SE"   
            }
        }
    )

###################################### Teacher Login Response  Model ###############################################################
class Teacher_Login_Response_Model(BaseModel):
    Message:str =Field(default="Login Success")
    Status:str =Field(default="Success")
    Status_Code:int =Field(default=200)
    data:teacher_login_respose_model
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Message": "Successfully User Register",
                "Status": "Success",
                "Status_Code": 200
            }
        }
    )

