from pydantic import BaseModel, Field

from ..database.models import ComplaintStatusEnum
from bson import ObjectId
from uuid import UUID
from typing import Any

from typing import Optional, List, Any, Annotated
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
class ObjectIdPydanticAnnotation:
    @classmethod
    def validate_object_id(cls, v: Any, handler) -> str:
        if isinstance(v, ObjectId):
            return v

        s = handler(v)
        if ObjectId.is_valid(s):
            return str(s)
        else:
            raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, _handler) -> core_schema.CoreSchema:
        if not(source_type is str):
            raise ValueError("source_type is str")
        return core_schema.no_info_wrap_validator_function(
            cls.validate_object_id, 
            core_schema.str_schema(), 
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema, handler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())


class ComplaintBase(BaseModel):
    creator_id: UUID= Field(title="Creator ID")
    user_id: UUID = Field(title="Defendant ID")
    header:str = Field(title="Complaint header")
    text:str = Field(title="Complaint contents")
class ComplaintCreate(ComplaintBase):
    pass

class ComplaintUpdate(ComplaintBase):
    status:ComplaintStatusEnum = Field(title="Complaint status")

class Complaint(ComplaintBase):
    id: Annotated[str, ObjectIdPydanticAnnotation]
    status:ComplaintStatusEnum = Field(title="Complaint status")