import logging

from loguru import logger

from config import settings

__version__ = settings.PROJECT_META["version"]


class PropagateHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logging.getLogger(record.name).handle(record)


logger.add(PropagateHandler(), format="{message}")
logger.add(settings.LOG_PATH / "critical.log", level="CRITICAL", rotation="10MB")
logger.add(settings.LOG_PATH / "error.log", level="ERROR", rotation="10MB")
logger.add(settings.LOG_PATH / "warning.log", level="WARNING", rotation="10MB")
logger.add(settings.LOG_PATH / "info.log", level="INFO", rotation="10MB")
logger.add(settings.LOG_PATH / "debug.log", level="DEBUG", rotation="10MB")
