import os
import json
import time
import requests
import asyncio

from loguru import logger
from fastapi import APIRouter, FastAPI, Response, Request, HTTPException

from core.models.service import ApiResponse
from v1.utils.database import get_info_from_db


api_router = APIRouter()

@api_router.get("/id/{id}", response_model=ApiResponse)
async def get_information_for_id(id: str):
    info = await get_info_from_db(id)

    if info:
        return ApiResponse.parse_obj({"info": info})
    else:
        raise HTTPException(status_code=204, detail=f"Not found any information for the requested ID")



