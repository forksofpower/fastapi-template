from __future__ import annotations
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import relationship

from app.models.base_class import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    profile = relationship("UserProfile", back_populates="user")
