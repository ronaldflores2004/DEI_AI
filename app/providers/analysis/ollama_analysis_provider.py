from app.clients.ollama.ollama_client import (
    OllamaClient,
)

from app.providers.analysis.base import (
    BaseAnalysisProvider,
)

from app.analysis.pipeline.analysis_pipeline import (
    AnalysisPipeline,
)

from app.shared.utils.prompt_loader import (
    PromptLoader,
)

from app.shared.enums.provider_enum import (
    ProviderEnum,
)



class OllamaAnalysisProvider(
    BaseAnalysisProvider,
):
    """
    Implementación del proveedor
    de análisis emocional utilizando
    Ollama.
    """

    def __init__(self):

        self.client = OllamaClient()

    def analyze(
        self,
        text: str,
    ) -> dict:

        system_prompt = PromptLoader.load(
            "analysis",
            "system.txt",
        )

        user_prompt = self._build_user_prompt(
            text,
        )

        response = self.client.chat(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return AnalysisPipeline.process(
            response=response,
            provider=ProviderEnum.OLLAMA,
            model=self.client.model,
        )

    @staticmethod
    def _build_user_prompt(
        text: str,
    ) -> str:

        return (
            "Texto del paciente:\n\n"
            f"{text}"
        )