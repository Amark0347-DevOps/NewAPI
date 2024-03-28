from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, Optional
import uuid
PyObjectId = Annotated[str, BeforeValidator(str)]
class Add_Schedule_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    Select_Course:str = Field(...)
    Day:str  = Field(...)
    STime:str  = Field(...)
    ETime:str = Field(...)
    Phone:Optional[str] = Field(default=None)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Select_Course":"Python",
                "Day":"Monday",
                "STime":"12 PM",
                "ETime":"3 PM"
            }
        }
    )


    @field_validator("Select_Course")
    def course_validate(cls, course_name):
        if len(course_name) >= 20:
            # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
            raise ValueError("Invalid Course Name")
        else:
            return course_name
     
class schedule_response_model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    Select_Course:str = Field(...)
    Day:str  = Field(...)
    STime:str  = Field(...)
    ETime:str = Field(...)
    Phone:str = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Select_Course":"Python",
                "Day":"Monday",
                "STime":"12 PM",
                "ETime":"3 PM",
                "Phone":"9056678462"
            }
        }
    )

class Add_Schedule_Model_Response(BaseModel):
    Message:str =Field(default="Successfully Trainer Added")
    Status:str =Field(default="Success")
    Status_code:int =Field(default=200)
    data:schedule_response_model
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Message": "Successfully User Register",
                "Status": "Success",
                "Status_code": 200
            }
        }
    )