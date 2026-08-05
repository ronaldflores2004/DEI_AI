from app.shared.exceptions.ai_provider_exception import (
    AIProviderException,
)


class AnalysisValidator:
    """
    Valida que la respuesta generada
    por la IA contenga todos los
    campos obligatorios.
    """

    REQUIRED_FIELDS = (

        "primary_emotion",

        "emotion_intensity",

        "risk_level",

        "analysis_json",

    )

    @classmethod
    def validate(
        cls,
        data: dict,
    ) -> None:

        for field in cls.REQUIRED_FIELDS:

            if field not in data:

                raise AIProviderException(
                    f"Campo obligatorio ausente: '{field}'."
                )

        if not isinstance(
            data["analysis_json"],
            dict,
        ):

            raise AIProviderException(
                "analysis_json debe ser un objeto."
            )