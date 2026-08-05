from abc import (
    ABC,
    abstractmethod,
)


class BaseRecommendationProvider(ABC):
    """
    Contrato para generar
    recomendaciones.
    """

    @abstractmethod
    def generate(
        self,
        analysis: dict,
    ) -> dict:

        pass