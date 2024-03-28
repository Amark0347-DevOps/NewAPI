from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, Optional
import uuid
from fastapi import status 

PyObjectId = Annotated[str, BeforeValidator(str)]    
class Add_Course_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    CourseName:str =Field(...)
    Duration:str = Field(...)
    Sdate:str = Field(...)
    Edate:str = Field(...)
    Cost:int = Field(...)
    Discount:str = Field(...)
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "CourseName":"Python",
                "Duration":"1 month",
                "Sdate":"5 jan",
                "Edate":"9 may",
                "Cost":5000,
                "Discount":"10"
            }
         }
    )

class Add_Course_Response(BaseModel):
    Message:str =Field(default="Successfully Course Added")
    Status:str =Field(default="Success")
    Status_Code:int =Field(default=status.HTTP_200_OK)
    data:Add_Course_Model
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "Message": "Successfully Course Register",
                "Status": "Success",
                "Status_Code": status.HTTP_200_OK
            }
         }
    )

class Update_Course_Model(BaseModel):
    CourseName:str =Field(...)
    Duration:str = Field(...)
    Sdate:str = Field(...)
    Edate:str = Field(...)
    Cost:int = Field(...)
    Discount:str = Field(...)
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "CourseName":"Python",
                "Duration":"1 month",
                "Sdate":"5 jan",
                "Edate":"9 may",
                "Cost":5000,
                "Discount":"10"
            }
         }
    )

class Update_Course_Response(BaseModel):
    Message:str =Field(default="Successfully Course Updated")
    Status:str =Field(default="Updated Successfully")
    Status_Code:int =Field(default=status.HTTP_205_RESET_CONTENT)
    data:Update_Course_Model
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "Message": "Successfully Course Register",
                "Status": "Success",
                "Status_Code": status.HTTP_205_RESET_CONTENT
            }
         }
    )