import logging
import time

from app.shared.enums.provider_enum import (
    ProviderEnum,
)

from app.shared.normalizers.emotion_normalizer import (
    EmotionNormalizer,
)

from app.shared.normalizers.intensity_normalizer import (
    IntensityNormalizer,
)

from app.shared.normalizers.risk_level_normalizer import (
    RiskLevelNormalizer,
)

from app.shared.parsers.json_response_parser import (
    JsonResponseParser,
)

from app.shared.validators.analysis_validator import (
    AnalysisValidator,
)

logger = logging.getLogger(__name__)

class AnalysisPipeline:
    """
    Pipeline encargado de transformar
    la respuesta cruda de la IA en
    una respuesta válida para DEI.
    """

    @staticmethod
    def process(
        response: str,
        provider: ProviderEnum,
        model: str,
    ) -> dict:

        start = time.perf_counter()

        parsed = JsonResponseParser.parse(
            response
        )

        AnalysisValidator.validate(
            parsed
        )

        parsed["primary_emotion"] = (
            EmotionNormalizer.normalize(
                parsed["primary_emotion"]
            ).value
        )

        parsed["emotion_intensity"] = (
            IntensityNormalizer.normalize(
                parsed["emotion_intensity"]
            ).value
        )

        parsed["risk_level"] = (
            RiskLevelNormalizer.normalize(
                parsed["risk_level"]
            ).value
        )

        parsed["provider"] = (
            provider.value
        )

        parsed["model"] = model

        elapsed = time.perf_counter() - start

        logger.info(
            "AnalysisPipeline ejecutado en %.4f segundos.",
            elapsed,
        )

        return parsed