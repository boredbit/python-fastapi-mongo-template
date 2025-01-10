from contextlib import asynccontextmanager
from contextlib import closing

from motor.motor_asyncio import AsyncIOMotorClient

from .settings import DATABASE_URL
from .settings import DEFAULT_DATABASE


@asynccontextmanager
async def create_database_connection():
    with closing(AsyncIOMotorClient(DATABASE_URL)) as client:
        db = client.get_database(DEFAULT_DATABASE)
        yield db
