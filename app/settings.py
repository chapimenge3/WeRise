import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_DIR : str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TELEGRAM_TOKEN: str
    BACKEND_URL: str
    WEBHOOK_ENDPOINT: str = '/telegram/webhook'
    VERIFY_ENDPOINT: str = '/telegram/verify/{token}'
    VERIFY_CALLBACK_ENDPOINT: str = '/telegram/verify/callback/{token}'

    # Database
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str


    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


settings = Settings()

