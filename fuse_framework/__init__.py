from loguru import logger

from fuse_framework.config import settings

logger.add(settings.LOG_PATH / "critical.log", level="CRITICAL", rotation="10MB")
logger.add(settings.LOG_PATH / "error.log", level="ERROR", rotation="10MB")
logger.add(settings.LOG_PATH / "warning.log", level="WARNING", rotation="10MB")
logger.add(settings.LOG_PATH / "info.log", level="INFO", rotation="10MB")
logger.add(settings.LOG_PATH / "debug.log", level="DEBUG", rotation="10MB")
