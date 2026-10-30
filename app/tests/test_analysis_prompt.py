from app.shared.enums.emotion_enum import (
    EmotionEnum,
)

from app.shared.enums.risk_level_enum import (
    RiskLevelEnum,
)

from app.shared.normalizers.risk_level_normalizer import (
    RiskLevelNormalizer,
)

from app.shared.utils.prompt_loader import (
    PromptLoader,
)


def _prompt() -> str:

    return PromptLoader.load(
        "analysis",
        "system.txt",
    )


def test_prompt_does_not_ask_to_diagnose_or_guess():

    prompt = _prompt()

    assert "psicólogo clínico" not in prompt
    assert "mejor inferencia" not in prompt
    assert "no diagnosticas" in prompt


def test_prompt_defines_every_risk_level():

    prompt = _prompt()

    for level in RiskLevelEnum:
        assert f"{level.value}:" in prompt

    assert "elige el más alto" in prompt


def test_prompt_lists_every_emotion():

    prompt = _prompt()

    for emotion in EmotionEnum:
        assert emotion.value in prompt


def test_risk_synonyms():

    assert RiskLevelNormalizer.normalize("sin riesgo") == RiskLevelEnum.LOW
    assert RiskLevelNormalizer.normalize("Inminente") == RiskLevelEnum.CRITICAL
    # Lo desconocido no se trata como bajo riesgo.
    assert RiskLevelNormalizer.normalize("???") == RiskLevelEnum.MEDIUM
