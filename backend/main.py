from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def read_root():
    return {"message": "API working"}

@app.get("/api/start_db")
async def on_startup():
    await init_db()
    return {"message": "Database started"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)