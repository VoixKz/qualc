from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('USERNAME_DB')
DB_PASSWORD = os.getenv('PASSWORD_DB')
DB_HOST = os.getenv('HOST_DB')
DB_PORT = os.getenv('PORT_DB')
DB_NAME = os.getenv('NAME_DB')

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"