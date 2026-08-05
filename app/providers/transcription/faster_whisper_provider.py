from app.clients.whisper.whisper_client import (
    WhisperClient,
)

from app.providers.transcription.base import (
    BaseTranscriptionProvider,
)


class FasterWhisperProvider(
    BaseTranscriptionProvider
):
    """
    Provider que utiliza
    Faster-Whisper.
    """

    def __init__(self):

        self.client = WhisperClient()

    def transcribe(
        self,
        audio_path: str,
    ) -> dict:

        response = self.client.transcribe(
            audio_path
        )

        return response