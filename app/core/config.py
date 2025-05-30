from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.settings.app import AppSettings
from app.core.settings.base import AppEnvTypes, BaseAppSettings
from app.core.settings.development import DevAppSettings
from app.core.settings.production import ProdAppSettings
from app.core.settings.test import TestAppSettings


AppEnvType = DevAppSettings | TestAppSettings | ProdAppSettings

environments: dict[str, type[AppEnvType]] = {
    AppEnvTypes.development: DevAppSettings,
    AppEnvTypes.testing: TestAppSettings,
    AppEnvTypes.production: ProdAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    """
    Return application config
    """
    app_env = BaseAppSettings.app_env
    config = environments[app_env]
    return config()  # type: ignore


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Template"
    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432

    USER_RESET_PASSWORD_TOKEN_SECRET: str = "secret"
    USER_VERIFICATION_TOKEN_SECRET: str = "secret"
    USER_JWT_SECRET: str = "secret"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
