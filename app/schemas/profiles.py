from pydantic import BaseModel, ConfigDict, EmailStr


class UserProfileBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True


class UserProfileCreate(UserProfileBase):
    password: str


class UserProfileUpdate(UserProfileBase): ...


class UserProfileResponse(UserProfileBase):
    id: str

    model_config = ConfigDict(from_attributes=True)
