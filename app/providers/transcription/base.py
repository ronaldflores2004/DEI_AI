from abc import ABC
from abc import abstractmethod


class BaseTranscriptionProvider(ABC):
    """
    Contrato para cualquier proveedor
    de transcripción.
    """

    @abstractmethod
    def transcribe(
        self,
        audio_path: str,
    ) -> dict:
        """
        Transcribe un archivo de audio.
        """
        pass