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