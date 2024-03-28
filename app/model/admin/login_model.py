from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, Optional
import uuid
PyObjectId = Annotated[str, BeforeValidator(str)]

###################################### Admin Login  Model ###############################################################
class Admin_Login_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    Email:str = Field(...)
    Password:str= Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Email":"amarkila@gmail.com",
                "Password":"Amarjeet"
            }
        }
    )

    @field_validator("Email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value
    

###################################### Response Model ###############################################################
class login_response_model(BaseModel):
    FirstName:str = Field(...)
    LastName:str = Field(...)
    Phone:str = Field(...)
    Email:str = Field(...)
    UserType:str = Field(...)
    Token:str=Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "FirstName":"rahul",
                "LastName":"kumar",
                "Phone":"9056678462",
                "Email":"rahul@gmail.com",
                "UserType":"Admin",
                "Token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiZmlyc3ROYW1lIjoiYmFibHUiLCJsYXN0TmFtZSI6IlVtcmlnYXIiLCJlbWFpbCI6ImJmdGRnZ2RAZ21haWwuY29tIiwicGhvbmUiOiIxZGRmZGRkZmY3OTA5NCJ9LCJleHAiOjE3MDg5MzIxNDN9.if5Zvi0Axaiee7UpnitBwOwjIHcGnFEYM0oh0j9b4SE"
            }
        }
    )

###################################### Admin Login  ResponsenModel ###############################################################
class Admin_Login_Response(BaseModel):
    Message:str =Field(default="Login Success")
    Status:str =Field(default="Success")
    Status_Code:int =Field(default=200)
    data:login_response_model
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Message": "Successfully User Register",
                "Status": "Success",
                "Status_Code": 200
            }
        }
    )