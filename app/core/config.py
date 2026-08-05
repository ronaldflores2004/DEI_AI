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

    # OLLAMA CONFIGURATION

    OLLAMA_URL: str = "http://localhost:11434"

    OLLAMA_MODEL: str = "llama3.1:8b"

    OLLAMA_TIMEOUT: int = 300

    OLLAMA_TEMPERATURE: float = 0.2

    OLLAMA_NUM_PREDICT: int = 2048

    # WHISPER CONFIGURATION

    WHISPER_MODEL: str = "large-v3"

    WHISPER_DEVICE: str = "cpu"

    WHISPER_COMPUTE_TYPE: str = "int8"

    WHISPER_TIMEOUT: int = 600

    WHISPER_LANGUAGE: str = "es"

    WHISPER_CPU_THREADS: int = 4

    WHISPER_BEAM_SIZE: int = 5

    WHISPER_VAD_FILTER: bool = True

    WHISPER_WORD_TIMESTAMPS: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()