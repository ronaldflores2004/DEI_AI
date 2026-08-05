import logging

from app.shared.enums.risk_level_enum import (
    RiskLevelEnum,
)

logger = logging.getLogger(__name__)


class RiskLevelNormalizer:
    """
    Normaliza el nivel de riesgo
    clínico.
    """

    _RISK_MAP = {

        "low": RiskLevelEnum.LOW,
        "bajo": RiskLevelEnum.LOW,
        "leve": RiskLevelEnum.LOW,

        "medium": RiskLevelEnum.MEDIUM,
        "medio": RiskLevelEnum.MEDIUM,
        "moderado": RiskLevelEnum.MEDIUM,

        "high": RiskLevelEnum.HIGH,
        "alto": RiskLevelEnum.HIGH,
        "elevado": RiskLevelEnum.HIGH,

        "critical": RiskLevelEnum.CRITICAL,
        "crítico": RiskLevelEnum.CRITICAL,
        "critico": RiskLevelEnum.CRITICAL,
        "muy alto": RiskLevelEnum.CRITICAL,

    }

    @classmethod
    def normalize(
        cls,
        risk: str,
    ) -> RiskLevelEnum:

        normalized = risk.strip().lower()

        result = cls._RISK_MAP.get(
            normalized,
        )

        if result is None:

            logger.warning(
                "Nivel de riesgo no reconocido: '%s'. "
                "Se utilizará MEDIUM.",
                risk,
            )

            return RiskLevelEnum.MEDIUM

        return result