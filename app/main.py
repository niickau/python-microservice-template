from fastapi import FastAPI
from loguru import logger

from core.settings.logging import *
from core.logging.kafka_logger_handler import KafkaHandler
from v1.routes import api_router as v1_api_router
from core.system_routes.system import system_router
from core.settings.settings import tags_metadata


description = """
🚀 API Service

* [Swagger](http://test.api.com/docs)
* [ReDoc](http://test.api.com/redoc)
"""

app = FastAPI(
    title="API Service",
    description=description,
    version="1.0",
    openapi_url=f"/openapi.json",
    docs_url=f"/docs",
    redoc_url=f"/redoc",
    openapi_tags=tags_metadata
    )

app.include_router(
    v1_api_router,
    prefix=f"/v1",
    tags=["api"],
    responses={
        204: {"description": "Not found any information for the requested ID"},
        404: {"description": "Not found"}
    }
)

app.include_router(
    system_router,
    prefix=f"",
    tags=["system"],
    responses={
        404: {"description": "Not found!"}
    }
)

@app.on_event("startup")
async def app_startup():
    logger.remove(0)

    kafka_logger = KafkaHandler(brokers=LOGGING_KAFKA_BROKERS, topic=LOGGING_KAFKA_TOPIC, user=LOGGING_KAFKA_USER, password=LOGGING_KAFKA_PASSWORD)
    logger.add(kafka_logger, enqueue=True)

@app.on_event("shutdown")
async def app_shutdown():
    pass

