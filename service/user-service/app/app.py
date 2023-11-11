import typing, logging
import json
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from . import database, config, users


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=20,
    format="%(levelname)-9s %(message)s"
)

logger.info("Configuration loading...")
cfg: config.Config = config.load_config(_env_file='.env')
logger.info(
    'Service configuration loaded:\n' +
    f'{cfg.model_dump_json(by_alias=True, indent=4)}'
)


app = FastAPI(
    version='0.0.1',
    title='User service'
)

users.configure_secrets(
    jwt_secret=cfg.jwt_secret.get_secret_value(),
    verification_token_secret=cfg.verification_token_secret.get_secret_value(),
    reset_password_token_secret=cfg.reset_password_token_secret.get_secret_value()
)
users.include_routers(app)


tag_name="group"

@app.post(
    "/groups", status_code=201, response_model=users.schemas.GroupRead,
    summary='Создает новую группу пользователей',tags=[tag_name]
)
async def add_group(
        group: users.schemas.GroupCreate,
        session: AsyncSession = Depends(database.get_async_session)
    ):

    return await users.crud.create_group(group, session)


@app.get(
    "/groups",
    summary='Возвращает список групп пользователей',
    response_model=list[users.schemas.GroupRead],tags=[tag_name]
)
async def get_group_list(
        session: AsyncSession = Depends(database.get_async_session),
        skip: int = 0,
        limit: int = 100
    ) -> typing.List[users.schemas.GroupRead]:

    return await users.crud.get_groups(session, skip, limit)


@app.get("/groups/{group_id}", summary='Возвращает информацию о группе пользователей',tags=[tag_name])
async def get_group_info(
        group_id: int, session: AsyncSession = Depends(database.get_async_session)
    ) -> users.schemas.GroupRead :
    
    group = await users.crud.get_group(session, group_id)
    if group != None:
        return group
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.put("/groups/{group_id}", summary='Обновляет информацию о группе пользователей',tags=[tag_name])
async def update_group(
        group_id: int, 
        group: users.schemas.GroupUpdate,
        session: AsyncSession = Depends(database.get_async_session)
    ) -> users.schemas.GroupRead:

    group = await users.crud.update_group(session, group_id, group)
    if group != None:
        return group
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.delete("/groups/{group_id}", summary='Удаляет информацию о группе пользователей',tags=[tag_name])
async def delete_device(
        group_id: int, 
        session: AsyncSession = Depends(database.get_async_session)
    ) -> users.schemas.GroupRead:


    if await users.crud.delete_group(session, group_id):
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.on_event("startup")
async def on_startup():
    await database.DB_INITIALIZER.init_db(
        cfg.PG_DSN.unicode_string()
    )

@app.on_event("startup")
async def on_startup():
    await database.DB_INITIALIZER.init_db(
        cfg.PG_DSN.unicode_string()
    )

    groups = []
    with open(cfg.default_groups_config_path) as f:
        groups = json.load(f)

    async for session in database.get_async_session():
        for group in groups:
            await users.crud.upsert_group(
                session, users.schemas.GroupUpsert(**group)
            )