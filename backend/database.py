from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declared_attr, sessionmaker
from config import get_async_db_url, settings
from sqlalchemy.ext.declarative import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs
DATABASE_URL = get_async_db_url()

engine = create_async_engine(DATABASE_URL, echo=settings.SQL_ECHO)
async_session_maker = sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
