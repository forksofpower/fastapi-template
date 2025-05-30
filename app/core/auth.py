from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from app.core.config import get_app_settings


def get_jwt_strategy() -> JWTStrategy:
    settings = get_app_settings()
    return JWTStrategy(
        secret=settings.jwt_secret_key,
        lifetime_seconds=(settings.jwt_token_expiration_minutes * 60),
    )


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
