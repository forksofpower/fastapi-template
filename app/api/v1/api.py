from fastapi import APIRouter
from app.api.v1 import profiles, users, auth


router = APIRouter()
router.include_router(auth.router, tags=["auth"], prefix="/auth")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profile")
