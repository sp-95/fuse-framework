from typing import Optional

import fire
from loguru import logger

from config import settings
from {{cookiecutter.project_slug}} import __version__


class Main:
    def __init__(self, option: str = "info") -> None:
        self.option = option

    def info(self) -> Optional[str]:
        if self.option.lower() == "info":
            logger.info(f"{settings.name} {__version__}")
            return settings.name
        else:
            logger.info("Hello, World!")
            return None


def main() -> None:
    fire.Fire(Main)


if __name__ == "__main__":
    main()
