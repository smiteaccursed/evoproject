from mongoengine import Document
from mongoengine import StringField, EnumField, UUIDField
from enum import IntEnum

class ComplaintStatusEnum(IntEnum):
    OPEN = 1
    APPROVED = 2
    REJECTED = 3

# Определение модели данных
class Complaint(Document):
    creator_id=UUIDField(UUIDField(binary=False, unique=True))
    user_id=UUIDField(UUIDField(binary=False, unique=True))
    status = EnumField(ComplaintStatusEnum)
    header=StringField(required=True,max_length=64)
    text= StringField(required=True,max_length=256)

