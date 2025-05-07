import contextlib
from typing import AsyncIterator

from fastapi import Depends

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base
from app.core.config import settings

DB_EXCEPTION = "DatabasSessionManager is not initialized"
engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    echo=False,  # Set True for debugging SQL queries
    future=True,
    pool_pre_ping=True,  # handles dropped connections
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False
)


# class DatabaseSessionManager:
#     _engine: AsyncEngine | None
#     _sessionmaker: async_sessionmaker | None

#     def __init__(self) -> None:
#         self._engine = None
#         self._sessionmaker = None

#     def init(self, host: str):
#         self._engine = create_async_engine(host)
#         self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

#     async def close(self):
#         if self._engine is None:
#             raise Exception(DB_EXCEPTION)
#         await self._engine.dispose()
#         self._engine = None
#         self._sessionmaker = None

#     @contextlib.asynccontextmanager
#     async def connect(self) -> AsyncIterator[AsyncConnection]:
#         if self._engine is None:
#             raise Exception(DB_EXCEPTION)
#         async with self._engine.begin() as connection:
#             try:
#                 yield connection
#             except Exception:
#                 await connection.rollback()
#                 raise

#     @contextlib.asynccontextmanager
#     async def session(self) -> AsyncIterator[AsyncSession]:
#         if self._sessionmaker is None:
#             raise Exception(DB_EXCEPTION)

#         session = self._sessionmaker()

#         try:
#             yield session
#         except Exception:
#             await session.rollback()
#             raise
#         finally:
#             await session.close()


# sessionmanager = DatabaseSessionManager()


# async def get_db():
#     async with sessionmanager.session() as session:
#         yield session
