from abc import (
    ABC,
    abstractmethod,
)


class BaseInsightProvider(ABC):
    """
    Contrato para generar
    insights clínicos.
    """

    @abstractmethod
    def generate(
        self,
        history: list,
    ) -> dict:

        pass