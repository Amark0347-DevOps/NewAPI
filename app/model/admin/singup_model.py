from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, Optional
import uuid
PyObjectId = Annotated[str, BeforeValidator(str)]
###################################### Admin Signup Model ###############################################################
class Admin_SingUp_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    FirstName:str =Field(...,min_length=1, max_length=20)
    LastName:str =Field(...,min_length=1, max_length=20)
    Email:str =Field(...,min_length=1, max_length=50)
    Phone:str = Field(...)
    Password:str = Field(..., max_length=10)
    UserType:Optional[str] = Field(default="Admin")
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "FirstName": "bablu",
                "LastName": "Umrigar",
                "Email": "bablueet@gmail.com",
                "Phone": "11167",
                "Password":"12345678"
            }
        }
    )
    @field_validator("Phone")
    def validate_phone(cls, value):
        # Add your custom phone number validation logic here
        # For example, you might want to check the length or format
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number format")
        return value

    @field_validator("Email")
    def validate_email(cls, value):
        # Add your custom email validation logic here
        # For example, you might want to check for a specific domain
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value
    
###################################### Response  Model ###############################################################
class signup_response_model(BaseModel):
    FirstName:str =Field(...,min_length=1, max_length=20)
    LastName:str =Field(...,min_length=1, max_length=20)
    Email:str =Field(...,min_length=1, max_length=50)
    Phone:str = Field(...)
    UserType:str = Field(...)
    Token:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "FirstName": "bablu",
                "LastName": "Umrigar",
                "Email": "bablueet@gmail.com",
                "Phone": "9056678462",
                "UserType":"Admin",
                "Token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOnsiZmlyc3ROYW1lIjoiYmFibHUiLCJsYXN0TmFtZSI6IlVtcmlnYXIiLCJlbWFpbCI6ImJmdGRnZ2RAZ21haWwuY29tIiwicGhvbmUiOiIxZGRmZGRkZmY3OTA5NCJ9LCJleHAiOjE3MDg5MzIxNDN9.if5Zvi0Axaiee7UpnitBwOwjIHcGnFEYM0oh0j9b4SE"
            }
        }
    )

###################################### Admin Response Model ###############################################################
class Admin_SingUp_Response(BaseModel):
    Message:str =Field(default="Successfully User Register")
    Status:str =Field(default="Success")
    Status_Code:int=Field(default=200)
    data:signup_response_model
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Message": "Successfully User Register",
                "Status": "Success",
                "Status_Code": 200
            }
        }
    )