from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

import config

engine = create_async_engine(url=config.pos_db, echo=False)


def create_session():
    return async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
