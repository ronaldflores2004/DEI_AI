from app.core.config import settings

from app.providers.factory import (
    ProviderFactory,
)

from app.analysis.schemas.analysis_request import (
    AnalysisRequest,
)


class AnalysisService:
    """
    Servicio encargado del análisis
    emocional mediante IA.
    """

    @staticmethod
    def analyze(
        data: AnalysisRequest,
    ) -> dict:

        provider = ProviderFactory.create(
            settings.AI_PROVIDER
        )

        return provider.analyze(
            data.text
        )