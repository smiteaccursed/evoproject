import logging
from fastapi import FastAPI, UploadFile
from typing import List, Annotated
from uuid import UUID
from . import config, crud
from .database import MongoDB, ComplaintStatusEnum
from .schemas import Complaint, ComplaintCreate
from fastapi.responses import JSONResponse


logger = logging.getLogger("telegram-service")
logging.basicConfig(level=logging.INFO, 
                    format="[%(levelname)s][%(name)s]")

cfg: config.Config = config.load_config(_env_file='.env')

logger.info("Service database loading...")
MongoDB(mongo_dsn=cfg.mongo_dsn.unicode_string())
logger.info("Service database loaded")

app = FastAPI(
    version='0.0.1',
    title='Complaint service'
)

@app.get("/complaints/by_status/{status}", summary='Возвращает список всех жалоб', response_model=List[Complaint])
async def get_complaints(status:ComplaintStatusEnum):
    return crud.get_complaints(status)

@app.get("/complaints/{CID}", summary='Возвращает жалобу по ID', response_model=Complaint)
async def get_complaint_by_id(CID:str):
    complaint =crud.get_complaint_ID(CID)
    if complaint is None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return complaint

@app.get("/complaints/user/{UID}", summary='Возвращает список жалоб на пользователя', response_model=List[Complaint])
async def get_complaint_by_user(UID: UUID):
    complaint=crud.get_complaint_by_user(UID)
    if complaint is None:
        return JSONResponse(status_code=404, content={"message": "Not found"})
    return complaint

@app.post("/complaints/",summary='Добавление новой жалобы', response_model=Complaint)
async def add_complaint(complaint:ComplaintCreate):
    return crud.create_complaint(complaint)

@app.put("/complaints/{CID}",summary='Обновление жалобы', response_model=Complaint)
async def update_complaint(CID:str, status:ComplaintStatusEnum ):
    return crud.update_complaint(CID, status)