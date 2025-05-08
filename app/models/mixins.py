from typing import Generic, Type, TypeVar, Any, Sequence
from uuid import uuid4
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# This Generic Type variable helps IDEs know that 'cls' returns an instance of the Model
CreateSchemaT = TypeVar("CreateSchemaT", bound=BaseModel)
ModelType = TypeVar("ModelType", bound="CRUDMixin")


class CRUDMixin(Generic[CreateSchemaT]):
    """
    A Mixin that adds convenience create/get/get_all methods.
    Assumes the model uses a String ID (UUID hex) as the primary key.
    """

    @classmethod
    async def create(
        cls: type[ModelType],
        db: AsyncSession,
        obj_in: CreateSchemaT,
        id: str | None = None,
    ) -> ModelType:
        """
        Generic create method.
        Expects a Pydantic model (obj_in) and automatically generates a UUID if id is missing.
        """
        if not id:
            id = uuid4().hex

        # exclude_unset=True prevents sending 'None' for optional fields
        # allowing the Database defaults (like is_active=True) to trigger.
        obj_data = obj_in.model_dump(exclude_unset=True)

        # 'cls' here is the actual model class (e.g. User)
        db_obj = cls(id=id, **obj_data)  # type: ignore

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @classmethod
    async def get(cls: type[ModelType], db: AsyncSession, id: str) -> ModelType | None:
        return await db.get(cls, id)

    @classmethod
    async def get_all(cls: type[ModelType], db: AsyncSession) -> Sequence[ModelType]:
        # Sequence is the correct return type for .all() results
        result = await db.execute(select(cls))
        return result.scalars().all()
