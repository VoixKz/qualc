import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.auth import get_current_user
from app.auth import router as auth_router
from database import async_session_maker
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


app.include_router(auth_router, prefix="/auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck")
async def healthcheck():
    return {"message": "Бэк работает!"}

@app.get("/")
async def read_root():
    return {"message": "Qualc API is running!"}

@app.get("/protected")
async def protected_route(user: User = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
