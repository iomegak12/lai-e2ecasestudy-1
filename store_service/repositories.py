from sqlalchemy.orm import Session
from . import models, schemas


class ItemRepository:
    async def create(db: Session, item: schemas.ItemCreate) -> models.Item:
        db_item = models.Item(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return db_item

    async def fetch_by_id(db: Session, item_id: int) -> models.Item:
        return db \
            .query(models.Item) \
            .filter(models.Item.id == item_id) \
            .first()

    async def fetch_all(db: Session) -> list[models.Item]:
        return db \
            .query(models.Item) \
            .all()


class StoreRepository:
    async def create(db: Session, store: schemas.StoreCreate) -> models.Store:
        db_store = models.Store(**store.dict())
        db.add(db_store)
        db.commit()
        db.refresh(db_store)

        return db_store

    async def fetch_by_id(db: Session, store_id: int) -> models.Store:
        return db \
            .query(models.Store) \
            .filter(models.Store.id == store_id) \
            .first()

    async def fetch_all(db: Session) -> list[models.Store]:
        return db \
            .query(models.Store) \
            .all()
