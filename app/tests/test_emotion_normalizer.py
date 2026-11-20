import pytest

from app.shared.enums.emotion_enum import (
    EmotionEnum,
)

from app.shared.normalizers.emotion_normalizer import (
    EmotionNormalizer,
)


def test_normalize_tristeza():

    result = EmotionNormalizer.normalize(
        "tristeza"
    )

    assert result == EmotionEnum.TRISTEZA


def test_normalize_desanimo():

    result = EmotionNormalizer.normalize(
        "desánimo"
    )

    assert result == EmotionEnum.DESANIMO


def test_normalize_furia():

    result = EmotionNormalizer.normalize(
        "furia"
    )

    assert result == EmotionEnum.IRA


def test_unknown_emotion_returns_confusion():

    result = EmotionNormalizer.normalize(
        "cualquier cosa"
    )

    assert result == EmotionEnum.CONFUSION 

# Catálogo que guarda el backend (dei_backend/app/shared/emotions.py,
# lista EMOTIONS). Si esta prueba falla, los dos catálogos ya no
# coinciden: hay que cambiar ambos repositorios.
BACKEND_EMOTIONS = [
    "Alegría", "Tristeza", "Ansiedad", "Miedo", "Ira", "Asco",
    "Sorpresa", "Calma", "Estrés", "Desánimo", "Culpa", "Vergüenza",
    "Soledad", "Frustración", "Confusión", "Esperanza", "Confianza",
    "Gratitud", "Agotamiento", "Amor", "Preocupación", "Desesperanza",
]


def test_catalog_matches_backend():

    assert [emotion.label for emotion in EmotionEnum] == BACKEND_EMOTIONS


@pytest.mark.parametrize("label", BACKEND_EMOTIONS)
def test_backend_names_normalize_to_same_emotion(label):

    emotion = EmotionNormalizer.normalize(label)

    assert emotion.label == label
    assert EmotionNormalizer.normalize(emotion.value) == emotion


def test_desesperanza_is_not_desanimo():

    # La desesperanza es una señal de riesgo: no se mezcla
    # con el desánimo.
    assert EmotionNormalizer.normalize("desesperanza") == EmotionEnum.DESESPERANZA
    assert EmotionNormalizer.normalize("Desesperanza") == EmotionEnum.DESESPERANZA


@pytest.mark.parametrize("raw", ["preocupación", "PREOCUPACION", "inquietud", "preocupado"])
def test_preocupacion(raw):

    assert EmotionNormalizer.normalize(raw) == EmotionEnum.PREOCUPACION


def test_accents_and_case_are_ignored():

    assert EmotionNormalizer.normalize("  Estrés ") == EmotionEnum.ESTRES
    assert EmotionNormalizer.normalize("MELANCOLÍA") == EmotionEnum.TRISTEZA


def test_empty_emotion_returns_confusion():

    assert EmotionNormalizer.normalize("") == EmotionEnum.CONFUSION
