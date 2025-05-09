from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.models.profile import UserProfile
from app.schemas.profiles import UserProfileUpdate, UserProfileResponse


router = APIRouter()

# @router.post("/", response_model=UserResponse)
# async def create_user(
#     session: SessionDep,
#     user_in: UserProfileCreate,
# ):
#     # TODO: check if user exists by email
#     # user = await User.get_by_email(session, user_in.email)
#     # if user:
#     #     raise HTTPException(status_code=400, detail="Email already exists")
#     query = select(UserProfile).where(UserProfile.email == user_in.email)
#     result = await session.execute(query)
#     if result.scalars().first():
#         raise HTTPException(status_code=400, detail="Email already exists")

#     return await UserProfile.create(session, user_in)


@router.get("/{user_id}", response_model=UserProfileResponse)
async def get_user_profile(
    session: SessionDep,
    user_id: str,
):
    user = await UserProfile.get(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User Profile not found")

    return user


@router.get("/", response_model=list[UserProfileResponse])
async def get_user_profiles(
    session: SessionDep,
):
    return await UserProfile.get_all(session)


@router.post("/{user_id}", response_model=None)
async def update_user_profile(
    session: SessionDep, user_id: str, user_in: UserProfileUpdate
):
    user = await UserProfile.get(session, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User Profile not found")

    # TODO: handle update exception
    updated_user = await user.update(session, user_id, user_in)

    return updated_user
