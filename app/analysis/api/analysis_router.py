from fastapi import APIRouter

from app.analysis.schemas.analysis_request import (
    AnalysisRequest,
)

from app.analysis.schemas.analysis_response import (
    AnalysisResponse,
)

from app.analysis.services.analysis_service import (
    AnalysisService,
)

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.post(
    "",
    response_model=AnalysisResponse,
)
def analyze(
    data: AnalysisRequest,
):

    return AnalysisService.analyze(
        data
    )