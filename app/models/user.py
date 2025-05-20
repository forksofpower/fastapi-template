from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, relationship

from app.models.base_class import Base
from app.models.profile import UserProfile


class User(SQLAlchemyBaseUserTableUUID, Base):
    profile: Mapped[UserProfile] = relationship(back_populates="user")
