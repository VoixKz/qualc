from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models.models import (
    User, 
    CallRecord, 
    Evaluation, 
    EvaluationCriteria, 
    EvaluationResult, 
    Recommendation, 
    CRMIntegration, 
    Alert,
)




load_dotenv()

DB_USER = os.getenv('USERNAME_DB')
DB_PASSWORD = os.getenv('PASSWORD_DB')
DB_HOST = os.getenv('HOST_DB')
DB_PORT = os.getenv('PORT_DB')
DB_NAME = os.getenv('NAME_DB')

if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    raise ValueError("Необходимо задать все переменные окружения для подключения к базе данных")

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)





async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)