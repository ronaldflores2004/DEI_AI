import logging
import time

from faster_whisper import (
    WhisperModel,
)

from app.core.config import settings

from app.shared.exceptions.transcription_exception import (
    TranscriptionException,
)

from app.shared.enums.provider_enum import (
    ProviderEnum,
)

logger = logging.getLogger(__name__)


class WhisperClient:
    """
    Cliente encargado de gestionar
    la comunicación con Faster-Whisper.

    El modelo se carga una única vez
    durante el ciclo de vida de la
    aplicación.
    """

    _model: WhisperModel | None = None

    def __init__(self):

        self.load_model()

    def load_model(
        self,
    ) -> None:
        """
        Carga el modelo de Faster-Whisper
        si todavía no fue inicializado.
        """

        if self.__class__._model is not None:

            return

        logger.info(
            "Cargando modelo Whisper '%s' | device=%s | compute_type=%s",
            settings.WHISPER_MODEL,
            settings.WHISPER_DEVICE,
            settings.WHISPER_COMPUTE_TYPE,
        )

        start = time.perf_counter()

        try:

            self.__class__._model = WhisperModel(

                model_size_or_path=settings.WHISPER_MODEL,

                device=settings.WHISPER_DEVICE,

                compute_type=settings.WHISPER_COMPUTE_TYPE,

                cpu_threads=settings.WHISPER_CPU_THREADS,
            )

            elapsed = time.perf_counter() - start

            logger.info(

                "Modelo Whisper cargado en %.2f segundos.| device=%s | compute_type=%s",

                elapsed,
                settings.WHISPER_DEVICE,
                settings.WHISPER_COMPUTE_TYPE,
            )

        except Exception as e:

            raise TranscriptionException(
                f"No fue posible cargar Faster-Whisper: {e}"
            ) from e

    def transcribe(
        self,
        audio_path: str,
    ) -> dict:
        """
        Transcribe un archivo de audio.
        """

        if self.__class__._model is None:

            raise TranscriptionException(
                "El modelo Whisper no está cargado."
            )

        start = time.perf_counter()

        try:

            logger.info(
            "Iniciando transcripción del audio: %s",
            audio_path,
            )

            segments, info = (
                self.__class__._model.transcribe(

                    audio_path,

                    language=settings.WHISPER_LANGUAGE,
                    beam_size=settings.WHISPER_BEAM_SIZE,
                    vad_filter=settings.WHISPER_VAD_FILTER,
                    word_timestamps=settings.WHISPER_WORD_TIMESTAMPS,
                )
            )

            logger.info(
                "Transcripción finalizada."
            )

            transcription = " ".join(

                segment.text.strip()

                for segment in segments
            )

            elapsed = time.perf_counter() - start

            logger.info(

                "Modelo '%s' transcribió el audio en %.2f segundos.",

                settings.WHISPER_MODEL,

                elapsed,
            )

            return {

                "provider": ProviderEnum.WHISPER,

                "model": settings.WHISPER_MODEL,

                "language": info.language,

                "transcription": transcription,

            }

        except Exception as e:

            raise TranscriptionException(
                f"Error durante la transcripción: {e}"
            ) from e