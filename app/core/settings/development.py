import logging

from pydantic import computed_field
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    """
    Application Settings for Development environment
    """

    debug: bool = True

    tile: str = "[DEV] FastAPI Template"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env.dev"

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(url=self.sql_db_uri, echo=True)
