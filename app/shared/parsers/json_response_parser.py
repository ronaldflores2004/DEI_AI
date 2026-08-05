import json

from app.shared.exceptions.ai_provider_exception import (
    AIProviderException,
)


class JsonResponseParser:
    """
    Convierte la respuesta de un LLM
    en un diccionario Python.
    """

    @staticmethod
    def parse(
        response: str,
    ) -> dict:

        cleaned = (
            JsonResponseParser._clean(
                response
            )
        )

        try:

            return json.loads(
                cleaned
            )

        except json.JSONDecodeError as e:

            raise AIProviderException(
                "La IA devolvió un JSON inválido."
            ) from e

    @staticmethod
    def _clean(
        response: str,
    ) -> str:

        response = response.strip()

        if response.startswith(
            "```json"
        ):

            response = response.replace(
                "```json",
                "",
                1,
            )

        if response.startswith(
            "```"
        ):

            response = response.replace(
                "```",
                "",
                1,
            )

        if response.endswith(
            "```"
        ):

            response = response[:-3]

        return response.strip()