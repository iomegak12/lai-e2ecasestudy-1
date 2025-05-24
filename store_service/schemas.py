from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    store_id: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class StoreBase(BaseModel):
    name: str
    description: str
    location: str


class StoreCreate(StoreBase):
    pass


class Store(StoreBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
