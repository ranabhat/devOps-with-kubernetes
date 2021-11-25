from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(title="TODO APP Backend",
    description="This is the backend for todo project app",
    version="0.0.1"
)
app.include_router(api_router)