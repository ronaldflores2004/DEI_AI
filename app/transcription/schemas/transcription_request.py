from pydantic import BaseModel


class TranscriptionRequest(BaseModel):
    """
    Solicitud de transcripción.
    """

    audio_path: str