import os
from dotenv import load_dotenv
from typing import Optional
from urllib.parse import quote_plus

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    DB_HOST: str = Field(validation_alias=AliasChoices("DB_HOST", "HOST_DB"))
    DB_PORT: int = Field(validation_alias=AliasChoices("DB_PORT", "PORT_DB"))
    DB_NAME: str = Field(validation_alias=AliasChoices("DB_NAME", "NAME_DB"))
    DB_USER: str = Field(validation_alias=AliasChoices("DB_USER", "USERNAME_DB"))
    DB_PASSWORD: str = Field(validation_alias=AliasChoices("DB_PASSWORD", "PASSWORD_DB"))

    CORS_ORIGINS: str = os.environ.get("CORS_ORIGINS", "http://localhost:3000")
    ALLOWED_HOSTS: str = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1")
    SQL_ECHO: bool = os.environ.get("SQL_ECHO", "false").lower() == "true"
    ENABLE_DB_INIT_ENDPOINT: bool = os.environ.get("ENABLE_DB_INIT_ENDPOINT", "false").lower() == "true"
    ADMIN_API_TOKEN: Optional[str] = os.environ.get("ADMIN_API_TOKEN")

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]

    @property
    def allowed_hosts(self) -> list[str]:
        return [host.strip() for host in self.ALLOWED_HOSTS.split(",") if host.strip()]

settings = Settings()



def _build_db_url(driver: str) -> str:
    encoded_user = quote_plus(settings.DB_USER)
    encoded_password = quote_plus(settings.DB_PASSWORD)
    return (
        f"postgresql+{driver}://{encoded_user}:{encoded_password}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )


def get_db_url() -> str:
    return _build_db_url("psycopg2")


def get_async_db_url() -> str:
    return _build_db_url("asyncpg")