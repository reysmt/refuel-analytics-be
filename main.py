import time
from pathlib import Path

from fastapi import FastAPI
from app.core.configsql import connect_db, disconnect_db
from contextlib import asynccontextmanager

import logging

from app.core.custom_logging import CustomizeLogger
from app.services.data_service import get_all_rigs, get_rig_price_history, get_rig_pricehistory_all

logger = logging.getLogger(__name__)
config_path=Path(__file__).with_name("logging_config.json")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    print("Application is starting up...")
    connect_db()
    yield
    disconnect_db()
    print("Application is shutting down...")
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/analytics/rig/all")
async def get_all():
    return get_all_rigs()

@app.get("/analytics/rigprice/history/all")
async def get_all_price_history():
    return get_rig_pricehistory_all()

@app.get("/analytics/rigprice/history/{rig_id}")
async def get_history(rig_id: int):
    return get_rig_price_history(rig_id)

