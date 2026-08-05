from app.providers.analysis.ollama_analysis_provider import (
    OllamaAnalysisProvider,
)

from app.providers.transcription.faster_whisper_provider import (
    FasterWhisperProvider,
)


PROVIDER_REGISTRY = {

    "OLLAMA": OllamaAnalysisProvider,

    "FASTER_WHISPER": FasterWhisperProvider,

}