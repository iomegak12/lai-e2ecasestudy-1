from typing import Optional, List

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import time
import asyncio

from .schemas import Item, ItemCreate, Store, StoreCreate
from .db import get_db, engine, Base
from .repositories import ItemRepository, StoreRepository

app = FastAPI(title="Store Service API", version="1.0.0",
              description="API for managing stores and items",
              docs_url="/docs",
              redoc_url="/redoc",
              openapi_url="/openapi.json")

Base.metadata.create_all(bind=engine)


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    base_error_message = "An unexpected error occurred, {request.method} {request.url}"
    error_message = base_error_message.format(request=request)

    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error", "details": error_message},
    )


@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.post("/items/", response_model=Item, tags=["Item"], status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = await ItemRepository.create(db, item)

    return db_item


@app.get("/items/{item_id}", response_model=Item, tags=["Item"])
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = await ItemRepository.fetch_by_id(db, item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item


@app.get("/items/", response_model=List[Item], tags=["Item"])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_items = await ItemRepository.fetch_all(db)

    return db_items[skip: skip + limit]


@app.post("/stores/", response_model=Store, tags=["Store"], status_code=201)
async def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    db_store = await StoreRepository.create(db, store)

    return db_store


@app.get("/stores/{store_id}", response_model=Store, tags=["Store"])
async def read_store(store_id: int, db: Session = Depends(get_db)):
    db_store = await StoreRepository.fetch_by_id(db, store_id)

    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")

    return db_store


@app.get("/stores/", response_model=List[Store], tags=["Store"])
async def read_stores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_stores = await StoreRepository.fetch_all(db)

    return db_stores[skip: skip + limit]
