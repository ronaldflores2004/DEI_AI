from pathlib import Path


class PromptLoader:
    """
    Carga prompts desde archivos.
    """

    BASE_PATH = (
        Path(__file__)
        .resolve()
        .parents[2]
        / "prompts"
    )

    @staticmethod
    def load(
        module: str,
        filename: str,
    ) -> str:

        path = (
            PromptLoader.BASE_PATH
            / module
            / filename
        )

        if not path.exists():

            raise FileNotFoundError(
                f"No existe el prompt: {path}"
            )

        return path.read_text(
            encoding="utf-8"
        )