from fastapi import APIRouter
from app.schemas.users import UserCreate, UserRead
from app.core.auth import auth_backend
from app.core.user import fastapi_users


router = APIRouter()

# JWT Auth endpoint(s)
router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/jwt", tags=["auth"]
)

# User Registration endpoints(s)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)

# User Password Reset endpoint(s)
router.include_router(fastapi_users.get_reset_password_router(), tags=["auth"])

# Verify User endpoint(s)
router.include_router(fastapi_users.get_verify_router(UserRead), tags=["auth"])
