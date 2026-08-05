import logging

from app.shared.enums.intensity_enum import (
    IntensityEnum,
)

logger = logging.getLogger(__name__)


class IntensityNormalizer:
    """
    Normaliza la intensidad emocional
    hacia el estándar utilizado por DEI.
    """

    _INTENSITY_MAP = {

        "low": IntensityEnum.LOW,
        "baja": IntensityEnum.LOW,
        "leve": IntensityEnum.LOW,
        "mínima": IntensityEnum.LOW,
        "minima": IntensityEnum.LOW,

        "medium": IntensityEnum.MEDIUM,
        "media": IntensityEnum.MEDIUM,
        "moderada": IntensityEnum.MEDIUM,

        "high": IntensityEnum.HIGH,
        "alta": IntensityEnum.HIGH,
        "muy alta": IntensityEnum.HIGH,
        "intensa": IntensityEnum.HIGH,

    }

    @classmethod
    def normalize(
        cls,
        intensity: str,
    ) -> IntensityEnum:

        normalized = intensity.strip().lower()

        result = cls._INTENSITY_MAP.get(
            normalized,
        )

        if result is None:

            logger.warning(
                "Intensidad no reconocida: '%s'. "
                "Se utilizará MEDIUM.",
                intensity,
            )

            return IntensityEnum.MEDIUM

        return result