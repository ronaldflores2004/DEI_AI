import logging
import unicodedata

from app.shared.enums.emotion_enum import (
    EmotionEnum,
)

logger = logging.getLogger(__name__)


def _key(
    emotion: str,
) -> str:
    """
    Minúsculas y sin tildes: "Estrés", "ESTRES"
    y "estres" dan la misma clave.
    """

    emotion = unicodedata.normalize(
        "NFKD",
        emotion.strip().lower(),
    )

    return "".join(
        char
        for char in emotion
        if not unicodedata.combining(char)
    )


# Sinónimos que el modelo suele devolver. Deben
# coincidir con EMOTION_ALIASES del backend
# (dei_backend/app/shared/emotions.py).
EMOTION_ALIASES = {
    "felicidad": EmotionEnum.ALEGRIA,
    "contento": EmotionEnum.ALEGRIA,
    "contenta": EmotionEnum.ALEGRIA,
    "optimismo": EmotionEnum.ALEGRIA,
    "melancolia": EmotionEnum.TRISTEZA,
    "ansioso": EmotionEnum.ANSIEDAD,
    "ansiosa": EmotionEnum.ANSIEDAD,
    "terror": EmotionEnum.MIEDO,
    "enojo": EmotionEnum.IRA,
    "furia": EmotionEnum.IRA,
    "rabia": EmotionEnum.IRA,
    "tranquilidad": EmotionEnum.CALMA,
    "abatimiento": EmotionEnum.DESANIMO,
    "culpabilidad": EmotionEnum.CULPA,
    "fatiga": EmotionEnum.AGOTAMIENTO,
    "cansancio": EmotionEnum.AGOTAMIENTO,
    "inquietud": EmotionEnum.PREOCUPACION,
    "preocupado": EmotionEnum.PREOCUPACION,
    "preocupada": EmotionEnum.PREOCUPACION,
}


class EmotionNormalizer:
    """
    Normaliza emociones detectadas
    por la IA hacia el catálogo
    canónico de DEI (EmotionEnum).
    """

    _EMOTION_MAP = {
        **{
            _key(emotion.value): emotion
            for emotion in EmotionEnum
        },
        **{
            _key(emotion.label): emotion
            for emotion in EmotionEnum
        },
        **EMOTION_ALIASES,
    }

    @classmethod
    def normalize(
        cls,
        emotion: str,
    ) -> EmotionEnum:

        result = cls._EMOTION_MAP.get(
            _key(emotion or ""),
        )

        if result is None:

            logger.warning(
                "Emoción no reconocida: '%s'. "
                "Se utilizará CONFUSION.",
                emotion,
            )

            return EmotionEnum.CONFUSION

        return result
