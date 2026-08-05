from abc import (
    ABC,
    abstractmethod,
)


class BaseSummaryProvider(ABC):
    """
    Contrato para generar
    resúmenes.
    """

    @abstractmethod
    def summarize(
        self,
        entries: list,
    ) -> dict:

        pass