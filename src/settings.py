import logging
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # API
    API_PREFIX: str = "/api/v1"
    API_VERSION: str = "0.1.0"

    # APP
    DEBUG: str = False
    APP_NAME: str = "Sandbox Starkbank"
    APP_DESCRIPTION: str = "Integração Sandbox para gerenciamento de fatura."

    # DATABASE
    DB_URI: PostgresDsn

    # STARKBANK
    SB_API_URL: str

    # GERADOR BRASILEIRO
    GB_API_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


log = logging.getLogger("uvicorn")
log.info("Loading config settings from the environment...")
settings = Settings()
