from motor.motor_asyncio import AsyncIOMotorClient
from app.models import AuthModel

async def get_database_connection() -> AsyncIOMotorClient:
    return AsyncIOMotorClient("mongodb://krad:fakepassword@10.11.0.2/")

async def db_insert_one(obj:AuthModel) -> None:
    connection = await get_database_connection()
    db = connection.test
    return db.farm.insert_one(obj.dict())