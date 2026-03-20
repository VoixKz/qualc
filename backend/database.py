from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from config import get_async_db_url, settings
from models.models import Base

DATABASE_URL = get_async_db_url()

engine = create_async_engine(DATABASE_URL, echo=settings.SQL_ECHO)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)





async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)