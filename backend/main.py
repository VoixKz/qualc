import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from app.auth import get_current_user
from app.auth import router as auth_router
from database import async_session_maker, init_db
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.trustedhost import TrustedHostMiddleware
from config import settings

app = FastAPI()


app.include_router(auth_router, prefix="/auth")

allow_origins = settings.cors_origins
allow_credentials = "*" not in allow_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.allowed_hosts,
)

@app.get("/")
async def read_root():
    return {"message": "Qualc API is running!"}

@app.get("/healthcheck")
async def healthcheck():
    return {"message": "Бэк работает!"}

@app.get("/api")
async def read_root():
    return {"message": "API working"}

@app.get("/api/start_db")
async def on_startup(x_admin_token: str | None = Header(default=None)):
    if not settings.ENABLE_DB_INIT_ENDPOINT:
        raise HTTPException(status_code=404, detail="Not found")

    if settings.ADMIN_API_TOKEN and x_admin_token != settings.ADMIN_API_TOKEN:
        raise HTTPException(status_code=403, detail="Forbidden")

    await init_db()
    return {"message": "Database started"}

@app.get("/protected")
async def protected_route(user: User = Depends(get_current_user)):
    return {"message": f"Hello, {user.username}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
