from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    DATABASE_URL: str

    SECRET_KEY: str

    OPENAI_API_KEY: str = ""

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    OLLAMA_BASE_URL: str = "http://localhost:11434"

    OLLAMA_MODEL: str = "llama3.2:3b"

    OLLAMA_TIMEOUT: int = 120

    MAX_HISTORY_MESSAGES: int = 20

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()