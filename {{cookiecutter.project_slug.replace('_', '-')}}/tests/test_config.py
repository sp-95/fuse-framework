import pytest
from _pytest.logging import LogCaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from {{cookiecutter.project_slug}}.config import Config


@pytest.mark.parametrize("environment", ["development", "production"])
def test_env(
    monkeypatch: MonkeyPatch,
    caplog: LogCaptureFixture,
    environment: str,
) -> None:
    monkeypatch.setenv("ENV_FOR_DYNACONF", environment)
    settings = Config(environment=True)

    assert environment in caplog.text
    if environment != "production":
        assert settings.debug is True
        assert "Debug: ON" in caplog.text
    else:
        assert settings.debug is False
