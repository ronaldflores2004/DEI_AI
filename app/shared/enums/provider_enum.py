from enum import Enum


class ProviderEnum(str, Enum):

    OLLAMA = "OLLAMA"

    OPENAI = "OPENAI"

    GEMINI = "GEMINI"

    LMSTUDIO = "LMSTUDIO"

    VLLM = "VLLM"