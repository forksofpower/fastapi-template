from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.api.deps import SessionDep
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse


router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_user(
    session: SessionDep,
    user_in: UserCreate,  # pydantic model for user creation
):
    # TODO: check if user exists by email
    # user = await User.get_by_email(session, user_in.email)
    # if user:
    #     raise HTTPException(status_code=400, detail="Email already exists")
    query = select(User).where(User.email == user_in.email)
    result = await session.execute(query)
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already exists")

    return await User.create(session, user_in)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    session: SessionDep,
    user_id: str,
):
    user = await User.get(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[UserResponse])
async def get_users(
    session: SessionDep,
):
    users = await User.get_all(session)
    return users
