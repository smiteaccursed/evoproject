from .database import models
import typing
from uuid import UUID
from . import schemas, broker


def get_complaints( stat:models.ComplaintStatusEnum
    ) -> typing.List[models.Complaint]:
    return models.Complaint.objects  \
            .filter(status= stat) \
            .all()

def get_complaint_ID(
         cid: str
    ) -> models.Complaint:
    comp = models.Complaint.objects(id=cid).first()
    if comp is None: return None
    return comp

def create_complaint(
        complaint: schemas.ComplaintCreate, botq:broker.botqueue
    ) -> models.Complaint: 
    new_complaint=models.Complaint(**complaint.model_dump(),
                                   status=models.ComplaintStatusEnum.OPEN)
    botq.send_message(f"Новая жалоба c заголовком \"{complaint.header}\" создана. \n На пользователя: {complaint.user_id}")
    new_complaint.save()
    return new_complaint

def get_complaint_by_user( uid:UUID) -> typing.List[schemas.Complaint]:
    return models.Complaint.objects  \
            .filter(user_id= uid) \
            .all()

def update_complaint( cid: str, stat:models.ComplaintStatusEnum
    ) -> models.Complaint:
    comp = models.Complaint.objects(id=cid).first()
    if comp is None: return None
    comp.status=stat
    comp.save()
    return comp