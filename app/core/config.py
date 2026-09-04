from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str
    environment: str

    # Database
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str
    database_url: str

    # API
    api_host: str
    api_port: int

    # Logging
    log_level: str

    secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()