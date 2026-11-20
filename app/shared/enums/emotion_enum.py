from enum import Enum


class EmotionEnum(str, Enum):
    """
    Catálogo canónico de emociones de DEI (22).

    Es el mismo catálogo que el backend guarda en
    app/shared/emotions.py (dei_backend). El valor
    viaja en mayúsculas y sin tildes; ``label`` es
    el nombre con tildes que el backend guarda y
    muestra. Si se agrega o quita una emoción, hay
    que cambiarla en los dos repositorios (las
    pruebas de contrato lo verifican).
    """

    ALEGRIA = "ALEGRIA"
    TRISTEZA = "TRISTEZA"
    ANSIEDAD = "ANSIEDAD"
    MIEDO = "MIEDO"
    IRA = "IRA"
    ASCO = "ASCO"
    SORPRESA = "SORPRESA"
    CALMA = "CALMA"
    ESTRES = "ESTRES"
    DESANIMO = "DESANIMO"
    CULPA = "CULPA"
    VERGUENZA = "VERGUENZA"
    SOLEDAD = "SOLEDAD"
    FRUSTRACION = "FRUSTRACION"
    CONFUSION = "CONFUSION"
    ESPERANZA = "ESPERANZA"
    CONFIANZA = "CONFIANZA"
    GRATITUD = "GRATITUD"
    AGOTAMIENTO = "AGOTAMIENTO"
    AMOR = "AMOR"
    PREOCUPACION = "PREOCUPACION"
    DESESPERANZA = "DESESPERANZA"

    @property
    def label(self) -> str:

        return _LABELS[self]


_LABELS = {
    EmotionEnum.ALEGRIA: "Alegría",
    EmotionEnum.TRISTEZA: "Tristeza",
    EmotionEnum.ANSIEDAD: "Ansiedad",
    EmotionEnum.MIEDO: "Miedo",
    EmotionEnum.IRA: "Ira",
    EmotionEnum.ASCO: "Asco",
    EmotionEnum.SORPRESA: "Sorpresa",
    EmotionEnum.CALMA: "Calma",
    EmotionEnum.ESTRES: "Estrés",
    EmotionEnum.DESANIMO: "Desánimo",
    EmotionEnum.CULPA: "Culpa",
    EmotionEnum.VERGUENZA: "Vergüenza",
    EmotionEnum.SOLEDAD: "Soledad",
    EmotionEnum.FRUSTRACION: "Frustración",
    EmotionEnum.CONFUSION: "Confusión",
    EmotionEnum.ESPERANZA: "Esperanza",
    EmotionEnum.CONFIANZA: "Confianza",
    EmotionEnum.GRATITUD: "Gratitud",
    EmotionEnum.AGOTAMIENTO: "Agotamiento",
    EmotionEnum.AMOR: "Amor",
    EmotionEnum.PREOCUPACION: "Preocupación",
    EmotionEnum.DESESPERANZA: "Desesperanza",
}
