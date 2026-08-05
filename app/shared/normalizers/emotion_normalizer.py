from app.shared.enums.emotion_enum import (
    EmotionEnum,
)

import logging

logger = logging.getLogger(__name__)


class EmotionNormalizer:
    """
    Normaliza emociones detectadas
    por la IA hacia el estándar
    clínico utilizado por DEI.
    """

    _EMOTION_MAP = {

        "alegría": EmotionEnum.ALEGRIA,
        "felicidad": EmotionEnum.ALEGRIA,
        "contento": EmotionEnum.ALEGRIA,
        "optimismo": EmotionEnum.ALEGRIA,

        "tristeza": EmotionEnum.TRISTEZA,
        "melancolía": EmotionEnum.TRISTEZA,

        "ansiedad": EmotionEnum.ANSIEDAD,
        "ansioso": EmotionEnum.ANSIEDAD,

        "miedo": EmotionEnum.MIEDO,
        "terror": EmotionEnum.MIEDO,

        "ira": EmotionEnum.IRA,
        "enojo": EmotionEnum.IRA,
        "furia": EmotionEnum.IRA,

        "asco": EmotionEnum.ASCO,

        "sorpresa": EmotionEnum.SORPRESA,

        "calma": EmotionEnum.CALMA,
        "tranquilidad": EmotionEnum.CALMA,

        "estrés": EmotionEnum.ESTRES,
        "estres": EmotionEnum.ESTRES,

        "desánimo": EmotionEnum.DESANIMO,
        "desanimo": EmotionEnum.DESANIMO,
        "desesperanza": EmotionEnum.DESANIMO,
        "abatimiento": EmotionEnum.DESANIMO,

        "culpa": EmotionEnum.CULPA,
        "culpabilidad": EmotionEnum.CULPA,

        "vergüenza": EmotionEnum.VERGUENZA,
        "verguenza": EmotionEnum.VERGUENZA,

        "soledad": EmotionEnum.SOLEDAD,

        "frustración": EmotionEnum.FRUSTRACION,
        "frustracion": EmotionEnum.FRUSTRACION,

        "confusión": EmotionEnum.CONFUSION,
        "confusion": EmotionEnum.CONFUSION,

        "esperanza": EmotionEnum.ESPERANZA,

        "confianza": EmotionEnum.CONFIANZA,

        "gratitud": EmotionEnum.GRATITUD,

        "agotamiento": EmotionEnum.AGOTAMIENTO,
        "fatiga": EmotionEnum.AGOTAMIENTO,
        "cansancio": EmotionEnum.AGOTAMIENTO,

        "amor": EmotionEnum.AMOR,
    }

    @classmethod
    def normalize(
        cls,
        emotion: str,
    ) -> EmotionEnum:

        normalized = emotion.strip().lower()

        result = cls._EMOTION_MAP.get(
            normalized,
        )

        if result is None:

            logger.warning(
                "Emoción no reconocida: '%s'. "
                "Se utilizará CONFUSION.",
                emotion,
            )

            return EmotionEnum.CONFUSION

        return result