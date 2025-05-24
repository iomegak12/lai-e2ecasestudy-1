from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity}, store_id={self.store_id})"


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    location = Column(String, index=True)

    items = relationship(
        "Item", primaryjoin="Store.id == Item.store_id", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Store(id={self.id}, name={self.name}, description={self.description}, location={self.location})"
