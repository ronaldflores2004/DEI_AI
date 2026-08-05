import logging

import time

import httpx

from app.core.config import settings

from app.shared.exceptions.ai_provider_exception import (
    AIProviderException,
)


logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Cliente encargado de comunicarse
    con Ollama mediante su API Chat.

    Su única responsabilidad es
    enviar mensajes y devolver
    la respuesta generada.
    """

    def __init__(self):

        self.base_url = settings.OLLAMA_URL

        self.timeout = settings.OLLAMA_TIMEOUT

        self.model = settings.OLLAMA_MODEL

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        payload = self._build_payload(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        try:

            with httpx.Client(
                timeout=self.timeout,
            ) as client:

                start = time.perf_counter()

                response = client.post(
                    f"{self.base_url}/api/chat",
                    json=payload,
                )

                elapsed = time.perf_counter() - start

                logger.info(
                   "Modelo '%s' respondió en %.2f segundos." ,
                    self.model,
                    elapsed,
                )

                response.raise_for_status()

                data = response.json()

                return data["message"]["content"]

        except httpx.TimeoutException as e:

            raise AIProviderException(
                "Ollama excedió el tiempo de espera."
            ) from e

        except httpx.ConnectError as e:

            raise AIProviderException(
                "No fue posible conectar con Ollama."
            ) from e

        except httpx.HTTPStatusError as e:

            raise AIProviderException(
                f"Ollama respondió con error "
                f"{e.response.status_code}."
            ) from e

        except Exception as e:

            raise AIProviderException(
                str(e)
            ) from e

    def _build_payload(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:

        return {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            "stream": False,
        }