from app.providers.factory import (
    ProviderFactory,
)

from app.transcription.schemas.transcription_request import (
    TranscriptionRequest,
)

from app.transcription.pipeline.transcription_pipeline import (
    TranscriptionPipeline,
)

class TranscriptionService:
    """
    Servicio encargado de gestionar
    la transcripción de audio
    mediante IA.
    """

    @staticmethod
    def transcribe(
        data: TranscriptionRequest,
    ):

        provider = (
            ProviderFactory.create(
                "FASTER_WHISPER"
            )
        )

        raw_response = (
            provider.transcribe(
                data.audio_path
            )
        )

        return (
            TranscriptionPipeline.execute(
                raw_response
            )
        )