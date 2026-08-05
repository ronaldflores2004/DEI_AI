from abc import (
    ABC,
    abstractmethod,
)


class BaseAnalysisProvider(ABC):
    """
    Contrato para cualquier proveedor
    encargado del análisis emocional.
    """

    @abstractmethod
    def analyze(
        self,
        text: str,
    ) -> dict:
        """
        Analiza un texto y devuelve
        el resultado estructurado.
        """
        pass