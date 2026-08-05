from fastapi import FastAPI

from app.core.config import settings
from app.core.logging_config import configure_logging
from app.core.startup import startup

from app.analysis.api.analysis_router import (
    router as analysis_router,
)

configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.on_event("startup")
def on_startup():

    startup()


@app.get("/")
def root():

    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }

app.include_router(
    analysis_router
)