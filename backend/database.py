from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr
from config import settings

DATABASE_URL = (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
                f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
