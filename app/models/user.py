from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from app.models.base_class import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
