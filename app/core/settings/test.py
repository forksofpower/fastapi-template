import logging

from pydantic import computed_field
from sqlalchemy import NullPool
from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """
    Application Settings for Test environment
    """

    debug: bool = True

    title: str = "[TEST] FastAPI Template"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env.test"

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict:
        return dict(
            url=self.sql_db_uri,
            echo=False,
            poolclass=NullPool,
            isolation_level="AUTOCOMMIT",
        )
