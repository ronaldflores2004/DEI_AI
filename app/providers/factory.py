from app.providers.registry import (
    PROVIDER_REGISTRY,
)

from app.shared.exceptions.ai_provider_exception import (
    AIProviderException,
)


class ProviderFactory:
    """
    Fábrica encargada de crear
    proveedores de IA.
    """

    @staticmethod
    def create(
        provider: str,
    ):

        provider_class = (
            PROVIDER_REGISTRY.get(
                provider.upper()
            )
        )

        if provider_class is None:

            raise AIProviderException(
                f"Proveedor '{provider}' no soportado."
            )

        return provider_class()