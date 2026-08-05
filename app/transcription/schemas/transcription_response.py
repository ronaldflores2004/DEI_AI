from pydantic import BaseModel

from app.shared.enums.provider_enum import (
    ProviderEnum,
)

from app.transcription.schemas.transcription_data import (
    TranscriptionData,
)


class TranscriptionResponse(BaseModel):
    """
    Respuesta oficial del módulo
    de transcripción.
    """

    provider: ProviderEnum

    model: str

    transcription_data: TranscriptionData