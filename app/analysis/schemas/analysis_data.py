from pydantic import BaseModel


class AnalysisData(BaseModel):
    """
    Información clínica obtenida
    durante el análisis emocional.
    """

    sentimientos: list[str]

    pensamientos: list[str]

    emociones: list[str]

    patrones_de_comportamiento: list[str]

    posibles_causas: list[str]

    resumen: str