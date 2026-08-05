from app.shared.enums.intensity_enum import (
    IntensityEnum,
)

from app.shared.normalizers.intensity_normalizer import (
    IntensityNormalizer,
)


def test_low():

    assert (
        IntensityNormalizer.normalize("LOW")
        == IntensityEnum.LOW
    )


def test_media():

    assert (
        IntensityNormalizer.normalize("media")
        == IntensityEnum.MEDIUM
    )


def test_alta():

    assert (
        IntensityNormalizer.normalize("alta")
        == IntensityEnum.HIGH
    )


def test_unknown_returns_medium():

    assert (
        IntensityNormalizer.normalize("xxxx")
        == IntensityEnum.MEDIUM
    )