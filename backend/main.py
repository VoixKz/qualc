from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
import uvicorn
from database import init_db
from config import settings

app = FastAPI()

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

@app.get("/api")
def read_root():
    return {"message": "API working"}

@app.get("/api/start_db")
async def on_startup(x_admin_token: str | None = Header(default=None)):
    if not settings.ENABLE_DB_INIT_ENDPOINT:
        raise HTTPException(status_code=404, detail="Not found")

    if settings.ADMIN_API_TOKEN and x_admin_token != settings.ADMIN_API_TOKEN:
        raise HTTPException(status_code=403, detail="Forbidden")

    await init_db()
    return {"message": "Database started"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)