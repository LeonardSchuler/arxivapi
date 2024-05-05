import logging
import warnings
from typing import Annotated, Any, Self

from pydantic import AnyUrl, BeforeValidator, computed_field, model_validator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: Optional[str] = Field(..., env="NGINX_HOST")
    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = []
    LOG_LEVEL: int = logging.INFO

    ENVIRONMENT: str = ""
    VERSION: str = ""
    DEBUG: bool = True

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str = ""
    DB_POOL_SIZE: int = 83

    WEB_CONCURRENCY: int = 9
    MAX_OVERFLOW: int = 64

    @computed_field  # type: ignore[misc]
    @property
    def POSTGRES_URL(self) -> MultiHostUrl:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )

    @computed_field  # type: ignore[misc]
    @property
    def POOL_SIZE(self) -> int:
        return max(settings.DB_POOL_SIZE // settings.WEB_CONCURRENCY, 5)

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value in ["secret", "password", "changethis"]:
            message = (
                f"The value of {var_name} is considered insecure. "
                "For security, please change it."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("DB_PASSWORD", self.DB_PASSWORD)
        return self


settings = Settings()  # type: ignore
