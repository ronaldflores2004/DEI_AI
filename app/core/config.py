from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    APP_NAME: str = "DEI AI"

    APP_VERSION: str = "1.0.0"

    HOST: str = "127.0.0.1"

    PORT: int = 8001

    LOG_LEVEL: str = "INFO"

    AI_PROVIDER: str = "OLLAMA"

    OLLAMA_URL: str = "http://localhost:11434"

    OLLAMA_MODEL: str = "llama3.1:8b"

    OLLAMA_TIMEOUT: int = 300

    OLLAMA_URL: str = "http://localhost:11434"

    OLLAMA_MODEL: str = "llama3.1:8b"

    OLLAMA_TIMEOUT: int = 300

    OLLAMA_TEMPERATURE: float = 0.2

    OLLAMA_NUM_PREDICT: int = 2048

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()