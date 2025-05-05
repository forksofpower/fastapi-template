from typing import ClassVar
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __tablename__: ClassVar[str] = declared_attr(lambda cls: cls.__name__.lower())  # type: ignore[assignment]
