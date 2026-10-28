from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    DJANGO_SECRET_KEY: str
    ENVIRONMENT: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
