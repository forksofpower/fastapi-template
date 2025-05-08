from uuid import uuid4
from sqlalchemy import String, Boolean, select
from app.models.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.models.mixins import CRUDMixin
from app.schemas.user import UserCreate


class User(Base, CRUDMixin[UserCreate]):
    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), index=True)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    password: Mapped[str] = mapped_column(String(255))

    # @classmethod
    # async def create(
    #     cls,
    #     db: AsyncSession,
    #     user_in: UserCreate,
    #     id: str | None = None,
    # ):
    #     if not id:
    #         id = uuid4().hex  # generate a unique string ID if not provided

    #     user = cls(id=id, **user_in.model_dump())  # unpack model fields
    #     db.add(user)

    #     await db.commit()
    #     await db.refresh(user)

    #     return user

    # @classmethod
    # async def get(cls, db: AsyncSession, id: str):
    #     try:
    #         user = await db.get(cls, id)
    #     except NoResultFound:
    #         return None
    #     return user

    # @classmethod
    # async def get_all(cls, db: AsyncSession):
    #     return (await db.execute(select(cls))).scalars().all()


#     @classmethod
#     async def get_by_email(cls, db: AsyncSession, email: str):
#         try:
#             result = await db.execute(select(cls).where(cls.email == email))
#             user = result.scalar_one()
#         except NoResultFound:
#             return None
#         return user

#     @classmethod
#     async def delete(cls, db: AsyncSession, id: str):
#         transaction = await db.get(cls, id)
#         if transaction:
#             await db.delete(transaction)
#             await db.commit()
#             return transaction
#         return None

#     @classmethod
#     async def update(cls, db: AsyncSession, id: str, user_in: UserCreate):
#         transaction = await db.get(cls, id)
#         if transaction:
#             for field, value in user_in.model_dump(exclude_unset=True).items():
#                 setattr(transaction, field, value)
#             db.add(transaction)
#             await db.commit()
#             await db.refresh(transaction)
#             return transaction
#         return None
