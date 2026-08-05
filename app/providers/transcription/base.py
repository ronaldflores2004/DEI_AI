from abc import (
    ABC,
    abstractmethod,
)


class BaseTranscriptionProvider(ABC):
    """
    Contrato para transcripción
    de audio.
    """

    @abstractmethod
    def transcribe(
        self,
        audio_path: str,
    ) -> str:

        pass