from fastapi import APIRouter

from app.transcription.schemas.transcription_request import (
    TranscriptionRequest,
)

from app.transcription.schemas.transcription_response import (
    TranscriptionResponse,
)

from app.transcription.services.transcription_service import (
    TranscriptionService,
)


router = APIRouter(
    prefix="/transcription",
    tags=["Transcription"],
)


@router.post(
    "",
    response_model=TranscriptionResponse,
)
def transcribe(
    data: TranscriptionRequest,
):

    return (
        TranscriptionService.transcribe(
            data
        )
    )