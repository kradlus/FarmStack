from motor.motor_asyncio import AsyncIOMotorClient
from app.models import AuthModel, FindOneModel

async def get_database_connection() -> AsyncIOMotorClient:
    return AsyncIOMotorClient("mongodb://krad:fakepassword@10.11.0.2/")

async def db_insert_one(obj:AuthModel) -> None:
    connection:AsyncIOMotorClient = await get_database_connection()
    db = connection.test
    return db.farm.insert_one(obj.dict())

async def db_find_one(obj:FindOneModel) -> AuthModel:
    connection:AsyncIOMotorClient = await get_database_connection()
    db = connection.test
    return await db.farm.find_one(obj.dict())
