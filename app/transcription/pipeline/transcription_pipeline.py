import time
import logging

from app.transcription.schemas.transcription_data import (
    TranscriptionData,
)

from app.transcription.schemas.transcription_response import (
    TranscriptionResponse,
)

from app.shared.enums.provider_enum import (
    ProviderEnum,
)


logger = logging.getLogger(__name__)


class TranscriptionPipeline:
    """
    Pipeline encargado de procesar
    la respuesta obtenida desde
    Faster-Whisper.
    """

    @staticmethod
    def execute(
        raw_data: dict,
    ) -> TranscriptionResponse:

        start = time.perf_counter()

        response = TranscriptionResponse(

            provider=ProviderEnum.WHISPER,

            model=raw_data["model"],

            transcription_data=TranscriptionData(

                transcription=raw_data["transcription"],

                language=raw_data["language"],

            )

        )

        elapsed = time.perf_counter() - start

        logger.info(
            "TranscriptionPipeline ejecutado en %.4f segundos.",
            elapsed,
        )

        return response