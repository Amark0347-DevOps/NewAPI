from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
from typing import Annotated, Optional, List
import uuid
PyObjectId = Annotated[str, BeforeValidator(str)]

###################################### Add Trainer  Model ###############################################################
class Add_Trainer_Model(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    Trainer_Name:str = Field(...)
    Email:str  = Field(...)
    Phone:str  = Field(...)
    Password:str = Field(...)
    UserType:Optional[str] = Field(default="Trainer")
    Experince:str = Field(...,min_length=1, max_length=2)
    CoursesList:List[str] = Field(...)
    Permissions:List[str] = Field(...)
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Trainer_Name":"Amarjeet",
                "Email":"amark0347@gmail.com",
                "Phone":"9056678462",
                "Password":"1234567",
                "Experince":"3",
                "UserType":"Trainer",
                "CoursesList": ["Course1", "Course2"],  
                "Permissions": ["Read", "Write"]
            }
        }
    )

    @field_validator("Email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Only email addresses from example.com are allowed")
        return value
    
    @field_validator("Phone")
    def validate_phone(cls, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number format")
        return value
    
###################################### Add Trainer  Model ###############################################################
class Add_Trainer_Response_Model(BaseModel):
    Message:str =Field(default="Successfully Trainer Added")
    Status:str =Field(default="Success")
    Status_Code:int =Field(default=200)
    data:Add_Trainer_Model
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "Message": "Successfully User Register",
                "Status": "Success",
                "Status_Code": 200
            }
        }
    )
