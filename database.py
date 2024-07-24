import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db_session() -> AsyncGenerator[AsyncSessionLocal, None]:
    async with AsyncSessionLocal() as session:
        yield session
