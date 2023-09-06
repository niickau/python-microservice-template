from fastapi import APIRouter


system_router = APIRouter()

@system_router.get("/")
async def root():
    return {"status": "Application is running."}
