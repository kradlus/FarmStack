from motor.motor_asyncio import AsyncIOMotorClient
from app.models import AuthModel, FindOneModel
from typing import Dict, Optional, Union, Sequence

class DBManager(AsyncIOMotorClient):
    def __init__(self, db_url:Union[str, Sequence], db_name:str = "test") -> None:
        super().__init__(self.__get_database_string(db_url))
        self.db = getattr(self, db_name)
    
    def __get_database_string(self, db_url:Union[str, Sequence]) -> str:
        if not isinstance(db_url, str):
            username, password, ip = db_url
            return f"mongodb://{username}:{password}@{ip}/"
        return db_url

    async def db_find_one(self, obj:FindOneModel) -> Optional[Dict]:
        return await self.db.farm.find_one(obj.dict())

    async def db_insert_one(self, obj:AuthModel) -> Dict:
        return self.db.insert_one(obj.dict())