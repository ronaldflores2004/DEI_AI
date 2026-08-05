from pydantic import BaseModel

from app.analysis.schemas.analysis_data import (
    AnalysisData,
)

from app.shared.enums.emotion_enum import (
    EmotionEnum,
)

from app.shared.enums.intensity_enum import (
    IntensityEnum,
)

from app.shared.enums.provider_enum import (
    ProviderEnum,
)

from app.shared.enums.risk_level_enum import (
    RiskLevelEnum,
)


class AnalysisResponse(BaseModel):
    """
    Respuesta oficial del módulo
    de análisis emocional.
    """

    primary_emotion: EmotionEnum

    emotion_intensity: IntensityEnum

    risk_level: RiskLevelEnum

    provider: ProviderEnum

    model: str

    analysis_json: AnalysisData