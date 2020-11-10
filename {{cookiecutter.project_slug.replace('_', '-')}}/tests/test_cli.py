from _pytest.logging import LogCaptureFixture

from {{cookiecutter.project_slug}}.cli import Main, __version__
from {{cookiecutter.project_slug}}.config import settings


class TestMain:
    @staticmethod
    def test_project_name(caplog: LogCaptureFixture) -> None:
        main = Main()
        project_name = main.info()
        assert project_name in caplog.text
        assert project_name == "{{ cookiecutter.project_slug.replace('_', '-') }}"

    @staticmethod
    def test_version() -> None:
        assert __version__ == settings.PROJECT_META["version"]

    @staticmethod
    def test_option(caplog: LogCaptureFixture) -> None:
        Main(option="extra").info()
        assert "Hello, World!" in caplog.text
