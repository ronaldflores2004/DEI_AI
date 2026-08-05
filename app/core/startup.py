import logging

from app.clients.whisper.whisper_client import (
    WhisperClient,
)
from app.core.config import settings

logger = logging.getLogger(__name__)


def startup():
    """
    Inicializa los recursos necesarios
    para la aplicación.
    """

    logger.info(
        "==================================="
    )

    logger.info(
        "Iniciando DEI AI..."
    )

    try:

        logger.info(
            "Inicializando Faster-Whisper..."
        )

        WhisperClient()

        logger.info(
            "Faster-Whisper listo."
        )

    except Exception:

        logger.exception(
            "No fue posible inicializar Faster-Whisper."
        )

        raise

    logger.info(
        "DEI AI iniciado correctamente."
    )

    logger.info(
        "==================================="
    )

    

logger.info("DEVICE = %s", settings.WHISPER_DEVICE)
logger.info("COMPUTE = %s", settings.WHISPER_COMPUTE_TYPE)