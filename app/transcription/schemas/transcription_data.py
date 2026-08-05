from pydantic import BaseModel


class TranscriptionData(BaseModel):
    """
    Información obtenida durante la transcripción.
    """

    transcription: str

    language: str