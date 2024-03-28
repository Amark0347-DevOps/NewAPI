from pydantic import BaseModel, ConfigDict, field_validator, Field, BeforeValidator
class Course_Image(BaseModel):
    Image_Name:str = Field(...)
    model_config = ConfigDict(
         json_schema_extra={
            "example":{
                "Image_Name":"Chauhan"
            }
         }
    )
