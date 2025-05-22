from __future__ import annotations

from sqlalchemy import ForeignKey, String, select
from app.models.base_class import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.models.mixins import CRUDMixin
from app.schemas.profiles import UserProfileCreate, UserProfileUpdate


class UserProfile(Base, CRUDMixin[UserProfileCreate, UserProfileUpdate]):
    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="userprofile")
    # email: Mapped[str] = mapped_column(String(255), index=True)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    biography: Mapped[str] = mapped_column(String, nullable=True)
    avatar: Mapped[str] = mapped_column(String, nullable=True)

    @classmethod
    async def get_by_user_id(
        cls,
        db: AsyncSession,
        user_id: str,
    ):
        query = select(UserProfile).where(UserProfile.user_id == user_id)

        try:
            result = await db.execute(query)
        except NoResultFound:
            return None
        return result
